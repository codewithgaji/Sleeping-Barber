# Sleeping Barber Problem - School Project  

This project is an implementation of the **Sleeping Barber Problem**, a classic synchronization problem in operating systems. I solved this problem using **semaphores** and **threading** in Python.  

## What I Learned  

1. **Enforcing FIFO with Queues:**  
   - Initially, I noticed that customers were not being served in a strict **First-In, First-Out (FIFO)** order.  
   - I learned how to use the `Queue` module to properly enforce FIFO, ensuring fairness in serving customers.  

2. **Understanding Global Interlock in Multi-threading:**  
   - At first, I thought Python supported true multi-threading, but I later realized that due to the **Global Interpreter Lock (GIL)**, Python does not run threads simultaneously.  
   - Instead, it switches execution between threads during idle times, making it appear as if multiple threads are running at once.  

3. **Working with Semaphores and Threading:**  
   - Using **semaphores**, I managed access to the waiting room chairs and the barber’s chair.  
   - I also learned to use **thread synchronization techniques**, such as the `Event` object, to signal when a customer arrives.  

## How the Code Works  

- Customers arrive at the barbershop and check for an available waiting seat.  
- If a seat is available, they take a seat and wait for the barber. Otherwise, they leave.  
- The barber either sleeps (when no customers are waiting) or serves customers one by one.  
- The barber chair and waiting room seats are controlled using **semaphores**, ensuring proper synchronization.  

## Test the Code [Here](https://colab.research.google.com/drive/19jn10l2xzTtZGDBZepiy7HlMYs3WTNsN?usp=sharing) 
---

