import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from random_profile import RandomProfile

# random_profile==0.2.3 required
rp = RandomProfile()
app = FastAPI()

@app.get("/")
def index():
    return {"message": "the api is working"}

@app.get('/api/v1/random_profile')
async def single_profile():
    """ Get single profile with all details """
    profile = rp.full_profile()
    return {'profile': profile}

@app.get('/api/v1/random_profile/<int:num>')
async def multiple_profile(num):
    """ Get multiple profile with all details
    
    args:
        num (int): number of profiles to generate
    
    """
    num = int(num)
    num = num if num <= 100 else 100
    
    profile = rp.full_profile(num)
    return {'profile': profile}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Random Profile Generator API",
        version="0.2.3",
        description="Python Module To Generate Random Profile Data",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi