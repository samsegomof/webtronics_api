import re
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator


class UserBaseReadSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserAuthRegisterSchema(BaseModel):
    name: str
    surname: Optional[str] = None
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)

    @validator('password')
    def validate_password(cls, password: str) -> str:
        pattern = r'^(?=.*[\d])(?=.*[!@#$%^&*-])[\w!@#$%^&*-]{8,24}$'
        if not re.match(pattern, password):
            raise ValueError('Password must contain at least one small letter '
                             'one capital letter, '
                             'digit or '
                             'special character')

        return password

    @validator('email')
    def validate_email(cls, email: str) -> str:
        pattern = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        if not re.match(pattern, email):
            raise ValueError('Email format should be correctly')

        return email

    class Config:
        schema_extra = {
            'example': {
                'name': 'Ivan',
                'surname': 'Ivanov',
                'email': 'vanyaivan@gmail.com',
                'password': 'superSecurepass!09',
            }
        }


class UserAuthLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'vanyaivan@gmail.com',
                'password': 'superSecurepass!09',
            }
        }


class UserAccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True
