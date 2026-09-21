from fastapi import FastAPI
from routers.products import router as product_router
from routers.items import router as item_router
from routers.db import router as db_router

app = FastAPI()

app.include_router(product_router)
app.include_router(item_router)
app.include_router(db_router)

