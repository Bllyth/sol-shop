import binascii
import os

import shopify
from fastapi import FastAPI

# from app.db import database
# from app.api import api_router
from starlette.responses import RedirectResponse

from backend.app.config import settings

app = FastAPI()

state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
shopify.Session.setup(api_key=settings.SHOPIFY_API_KEY, secret=settings.SHOPIFY_API_SECRET)

"""
shopify.Session.setup(api_key=API_KEY, secret=API_SECRET)


shop_url = "SHOP_NAME.myshopify.com"
api_version = '2020-10'
state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
redirect_uri = "http://myapp.com/auth/shopify/callback"
scopes = ['read_products', 'read_orders']

newSession = shopify.Session(shop_url, api_version)
auth_url = newSession.create_permission_url(scopes, redirect_uri, state)
# redirect to auth_url
"""


@app.get("/install")
def read_root():
    redirect_uri = RedirectResponse(url='/callback')
    new_session = shopify.Session(settings.SHOP_URL, settings.SHOPIFY_API_VERSION)
    auth_url = new_session.create_permission_url(settings.SCOPES, redirect_uri, state)
    return auth_url


@app.get("/redirect")
async def redirect():
    response = RedirectResponse(url='/redirected')
    return response


@app.get("/callback")
async def redirected():
    # logger.debug("debug message")
    session = shopify.Session(settings.SHOP_URL, settings.SHOPIFY_API_VERSION)
    # access_token = session.request_token(request_params)
    return {"message": "This is callback"}

# @app.on_event("startup")
# async def startup() -> None:

# if not database.is_connected:
#     await database.connect()
# # create a dummy entry
# await User.objects.get_or_create(email="test@test.com")


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     if database.is_connected:
#         await database.disconnect()
#
#
# app.include_router(api_router)
