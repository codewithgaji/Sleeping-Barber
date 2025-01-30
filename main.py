import threading
import time
from queue import Queue

# Number of chairs in the waiting room
num_chairs = int(input("How many waiting seats do you want the barber to have?"))
waiting_room = threading.Semaphore(num_chairs)

# Semaphore for the barber's chair and event to signal when the barber is ready
barber_chair = threading.Semaphore(1)
barber_ready = threading.Event()

# Customer queue to store customers waiting
customer_q = Queue()

# Shared variables to track the number of served customers
total_customers = int(input("How many customers do you want? "))
total_customers_served = 0

# Lock to prevent race conditions when updating shared variables
customer_lock = threading.Lock()


# Customer function
def customer(id):
    global total_customers_served

    print(f"Customer {id} is arriving...")
    time.sleep(3)  # Simulate time for customer arrival

    # Try to acquire a seat in the waiting room
    if waiting_room.acquire(blocking=False):
        print(f"\nCustomer {id} sits in the waiting room.")
        time.sleep(0.7)
        customer_q.put(id)  # Customer waits in the queue
        barber_ready.set()  # Notify barber that there's a customer waiting
    else:
        print(f"\nCustomer {id} finds no seat and leaves.")
        with customer_lock:
            total_customers_served += 1  # Count the customer that leaves


# Barber function
def barber():
    global total_customers_served

    while total_customers_served < total_customers:  # Stop when all customers are served
        if not customer_q.empty():
            # Get the next customer in line
            customer_id = customer_q.get()
            time.sleep(1.5)
            print(f"\nBarber is serving customer {customer_id}...")

            # Customer gets the barber's chair
            barber_chair.acquire()

            # Free up a seat in the waiting room
            waiting_room.release()

            # Simulate serving time
            time.sleep(3)  # Time for serving a customer
            print(f"Barber finished with customer {customer_id}\n")

            # Release the barber's chair after serving
            barber_chair.release()

            with customer_lock:
                total_customers_served += 1  # Update number of customers served
        else:
            # No customers are waiting, barber is sleeping
            print("\nBarber is sleeping...")
            barber_ready.wait()  # Wait for a customer to arrive
            barber_ready.clear()  # Clear the event to wait for the next customer

    print("All customers have been served. Barber is going home.")


# Create and start the barber thread
barber_thread = threading.Thread(target=barber)
barber_thread.start()

# Create and start customer threads
for customer_id in range(total_customers):
    threading.Thread(target=customer, args=(customer_id,)).start()
    time.sleep(0.5)  # Simulate small delay between customer arrivals

# Wait for the barber thread to finish
barber_thread.join()




