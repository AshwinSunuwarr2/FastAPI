from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default = None)
    title : str = Field(default = None)
    content : str = Field(default = None)
    class Config:
        schema_extra = {
            "post demo" : {
                "title": "Some title about animals",
                "content": "Some details about animal"
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user demo" : {
                "fullname" : "George Hill",
                "email" : "abc@gmail.com",
                "password" : "abc"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user demo" : {
                "email" : "abc@gmail.com",
                "password" : "abc"
            }
        }