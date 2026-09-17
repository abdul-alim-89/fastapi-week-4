#Day 1

Think About It: What's the practical difference between ASGI and WSGI, and why does that matter for how many requests FastAPI can serve at once?

Answer : WSGI is designed around synchronous request handling, while ASGI supports asynchronous and concurrent I/O. FastAPI uses ASGI, so when an async request is waiting for I/O, the event loop can work on other requests instead of blocking on that wait, allowing better concurrency for I/O-bound applications.

A single async worker can theoretically handle thousands of idle or waiting connections, up to the available memory limits. However, the actual throughput (the number of requests successfully processed per second) depends on how quickly downstream services, such as databases and external APIs, respond, as well as how many CPU cores and workers are available.

Think About It: If you remove the : int type hint from item_id, what changes in how FastAPI treats a request to /items/abc?

Answer: When we remove type hints, we can pass any type of value as a parameter, such as a string, special character, or abc, and Python will accept it.FastAPI will no longer validate or convert item_id as an integer.