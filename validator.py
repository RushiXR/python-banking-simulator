from pydantic import BaseModel,EmailStr,model_validator

class Validate(BaseModel):

    username :str
    email : EmailStr
    password : str
    confirm_password : str

    @model_validator(mode='after')
    def passwordCheck(self):
        if self.confirm_password != self.password:
            raise ValueError("PASSWORD INCORRECT")
        else:
            return self

    



        