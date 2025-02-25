# 🏗️ Asynchronous Programming in Python 🚀  

## **📌 Overview**
This repository contains a series of **asynchronous programming projects in Python**, structured by increasing complexity. Each project is designed to help master concepts such as `asyncio`, `await`, `asyncio.Queue()`, `aiohttp`, and more.

---

## **📂 Project List & Progress**  

| # | **Project Name** | **Concepts Covered** | **Status** |  
|---|------------------|----------------------|-----------|  
| 1️⃣ | **Simulated Task Runner** | `async def`, `await`, `asyncio.run()` | ✅ Completed |  
| 2️⃣ | **Parallel API Requests Simulator** | `asyncio.gather()`, `aiohttp` | ✅ Completed |  
| 3️⃣ | **Asynchronous Web Scraper with Timeouts** | `asyncio.wait_for()`, `asyncio.Semaphore()` | ✅ Completed |  
| 4️⃣ | **Async Task Queue (Order Processing)** | `asyncio.Queue()`, Multiple Workers | ✅ Completed |  
| 5️⃣ | **Async Chat Server (Networking)** | `asyncio.start_server()`, Sockets | ❌ **Undone** |  
| 6️⃣ | **Asynchronous Web Crawler with Database Storage** | `asyncpg`, `asyncio.Semaphore()`, Efficient Async DB Writes | ❌ **Undone** |  

---

## **📌 Completed Projects**
### **1️⃣ Simulated Task Runner** ✅  
🔹 **Goal:** Simulate a system where tasks run asynchronously instead of sequentially.  
🔹 **Concepts Covered:**  
- `async def`, `await`  
- `asyncio.run()`  

🔹 **Key Learning:** Tasks should run in **parallel**, not one after another.

---

### **2️⃣ Parallel API Requests Simulator** ✅  
🔹 **Goal:** Fetch data from multiple URLs **concurrently** instead of sequentially.  
🔹 **Concepts Covered:**  
- `asyncio.gather()` (run multiple async tasks together)  
- `aiohttp` for **async HTTP requests**  
- Handling responses asynchronously  

🔹 **Key Learning:** Using `asyncio.gather()` **reduces API response time dramatically**.

---

### **3️⃣ Asynchronous Web Scraper with Timeouts** ✅  
🔹 **Goal:** Fetch multiple web pages **concurrently** while handling **slow responses** and **timeouts**.  
🔹 **Concepts Covered:**  
- `asyncio.wait_for()` to **cancel slow tasks**  
- `asyncio.Semaphore()` for **rate-limiting**  
- `aiohttp` for **efficient async HTTP requests**  

🔹 **Key Learning:** **Timeouts and error handling** are crucial for building **reliable async programs**.

---

### **4️⃣ Async Task Queue (Order Processing System)** ✅  
🔹 **Goal:** Implement an **async queue-based system** where multiple workers process tasks concurrently.  
🔹 **Concepts Covered:**  
- `asyncio.Queue()` (buffered task queue)  
- Multiple workers (`async def worker()`)  
- Graceful shutdown (`asyncio.gather()`, `task_done()`)  

🔹 **Key Learning:** **Queues** prevent bottlenecks and **ensure smooth parallel processing**.

---

## **📌 Pending Projects**
### **5️⃣ Async Chat Server (Networking)** ❌ **Undone**  
🔹 **Goal:** Build a **real-time chat server** where multiple users send & receive messages asynchronously.  
🔹 **Concepts to Implement:**  
- `asyncio.start_server()` (handle multiple clients)  
- `asyncio.StreamReader` & `asyncio.StreamWriter` for **reading/writing messages**  
- Broadcasting messages to **all connected clients**  

🔹 **Status:** **Pending Implementation**  

---

### **6️⃣ Asynchronous Web Crawler with Database Storage** ❌ **Undone**  
🔹 **Goal:** Build a **large-scale web crawler** that stores scraped data into a database.  
🔹 **Concepts to Implement:**  
- `asyncpg` or `aiomysql` for **async database writes**  
- **Task concurrency control** using `asyncio.Semaphore()`  
- **Error handling & retries** for failed requests  

🔹 **Status:** **Pending Implementation**  

---

## **📌 Running the Projects**
### **Prerequisites**
Ensure you have Python **3.8+** installed. Install required dependencies:
```bash
pip install aiohttp
```

---

## **📌 Next Steps**
✅ **Continue working on the remaining projects**  
✅ **Push updates to GitHub**  
✅ **Improve error handling & efficiency in completed projects**  
✅ **Optimize code for performance improvements**  

---

## **👨‍💻 Author**
Built by **[SCCSMARTCODE](https://github.com/sccsmartcode)** as part of mastering **Python Asynchronous Programming** 🚀.