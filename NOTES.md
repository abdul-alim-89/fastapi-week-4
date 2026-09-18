#Day 1

Think About It: What's the practical difference between ASGI and WSGI, and why does that matter for how many requests FastAPI can serve at once?

Answer : WSGI is designed around synchronous request handling, while ASGI supports asynchronous and concurrent I/O. FastAPI uses ASGI, so when an async request is waiting for I/O, the event loop can work on other requests instead of blocking on that wait, allowing better concurrency for I/O-bound applications.

A single async worker can theoretically handle thousands of idle or waiting connections, up to the available memory limits. However, the actual throughput (the number of requests successfully processed per second) depends on how quickly downstream services, such as databases and external APIs, respond, as well as how many CPU cores and workers are available.

Think About It: If you remove the : int type hint from item_id, what changes in how FastAPI treats a request to /items/abc?

Answer: When we remove type hints, we can pass any type of value as a parameter, such as a string, special character, or abc, and Python will accept it.FastAPI will no longer validate or convert item_id as an integer.

#day2

Think About It: What happens if a client sends an extra field your Pydantic model doesn't define — is it kept, dropped, or rejected? Test it and note what you observed.

Answer: I noticed that passing an extra field "sales_price": 50 in the 'create product' endpoint didn't trigger a validation error and the API succeeded. To resolve this, I set extra="forbid" inside Pydantic's ConfigDict.
After that we observed that extra inputs are not permitted

Think About It: Why would you ever want response_model to be a DIFFERENT model than the one used for the request body?

Answer: It depends on the use case. Since our current endpoint required identical request and response formats, a separate response model wasn't necessary. In production applications, however, incoming data often includes sensitive fields like passwords. In those cases, we define a dedicated response schema excluding those fields so that calling the GET API with that response_model prevents sensitive data leakage.

#day3

Think About It: Why do large FastAPI apps avoid keeping every route in one main.py? What specifically goes wrong as the app grows?

Answer: Large FastAPI applications avoid keeping all routes in main.py because a single file quickly becomes bloated and unmaintainable, creating severe readability and navigation issues. Splitting routes into modular files (routers/users.py, routers/products.py) enables multiple developers to work simultaneously without Git merge conflicts, simplifies unit testing, prevents Python circular import errors, and keeps the overall architecture scalable and clean.

Think About It: What's the difference between PUT and PATCH in practice — if you only update one field, which should you use, and why?

Answer: Both PUT and PATCH are HTTP methods used to update data. PUT is used for a full replacement of a resource, meaning you must send all fields in the payload. PATCH, on the other hand, is used for partial updates, modifying only the specified fields without affecting the rest. If I only need to update a single field, I should use PATCH because it allows partial updates without requiring or overwriting all the other fields.