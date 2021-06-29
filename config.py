import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_URL: str = Field(..., env='DATABASE_URL')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    ALGORITHM: str = Field(..., env='ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(..., env='ACCESS_TOKEN_EXPIRE_MINUTES')

    SHOPIFY_API_KEY = 'a3d1a601bfbbd9e8423eebb58281a479'
    SHOPIFY_API_SECRET = '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'
    SHOPIFY_API_VERSION = '2021-01'
    SHOP_URL = "sol-o-vino.myshopify.com"
    SCOPES = ['read_products', 'write_products', 'read_script_tags', 'write_script_tags', 'read_shipping',
              'write_shipping']


settings = Settings()
