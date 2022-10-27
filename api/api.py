import uvicorn
from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi

from pydantic import create_model
from random_profile import RandomProfile

# random_profile==0.2.3 required
rp = RandomProfile()
app = FastAPI()

query_model = create_model("num", num=(int, ...))
api_version = "0.2.3"


@app.get("/")
def index():
    return {"status": "200",
            "message": "Welcome to Random Profile Generator API",
            "version": api_version}


@app.get('/api/v1/random_profile/full_profile')
async def multiple_profile(params: query_model = Depends()):
    """ Get multiple profile with all details

    args:
        num (int): number of profiles to generate
    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > 100:
        return {"status": "400",
                "message": "Number of profiles should be less than 100",
                "version": api_version}

    num = params_as_dict['num']
    profile = rp.full_profile(num)
    return profile


@app.get('/api/v1/random_profile/first_name')
async def multiple_first_name(params: query_model = Depends()):
    """ Get multiple first names

    args:
        num (int): number of first names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > 100:
        return {"status": "400",
                "message": "Number of profiles should be less than 100",
                "version": api_version}

    num = params_as_dict['num']
    first_names = rp.first_name(num)
    return first_names


@app.get('/api/v1/random_profile/last_name')
async def multiple_last_name(params: query_model = Depends()):
    """ Get multiple last names

    args:
        num (int): number of last names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > 100:
        return {"status": "400",
                "message": "Number of profiles should be less than 100",
                "version": api_version}

    num = params_as_dict['num']
    last_names = rp.last_name(num)
    return last_names


@app.get('/api/v1/random_profile/full_name')
async def multiple_full_name(params: query_model = Depends()):
    """ Get multiple full names

    args:
        num (int): number of full names to generate

    """
    params_as_dict = params.dict()
    if params_as_dict['num'] > 100:
        return {"status": "400",
                "message": "Number of profiles should be less than 100",
                "version": api_version}

    num = params_as_dict['num']

    full_names = rp.full_name(num)
    return full_names


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Random Profile Generator API",
        version=api_version,
        description="Python Module To Generate Random Profile Data",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
