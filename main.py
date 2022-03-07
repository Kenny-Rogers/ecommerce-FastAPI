from fastapi import FastAPI
from ecommerce.user import router as user_router

# create a fast API defining meta data about the API
app = FastAPI(title='EcommerceApp',
              version='0.0.1')

app.include_router(user_router.router)
