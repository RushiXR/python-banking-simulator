import validator 
from pydantic import ValidationError

class Loginportal:
    userdetails = []
    # userdetails = [{"username":"Rushikesh","password":"pass1"},{"username":"Vedant","password":"pass2"},{"username":"manash","password":"pass3"},{"username":"Rudra","password":"pass4"}]

    @classmethod
    def show_options(cls):
        print("\n1.) Register")
        print("2.) Login")
        print("3.) Exit\n")

        
    @classmethod
    def register(cls):                                  #Register method for user registration
        while True:
            user_username   = input("ENTER USERNAME:")              #taking user data
            user_email      = input("ENTER YOUR EMAIL:")
            user_password   = input("ENTER YOUR PASSWORD:")
            user_conf_pass  = input("CONFIRM PASSWORD:")

            try:
                userinfo = validator.Validate(
                                            username=user_username,               #sending user data to pydantic to validate data via making object or pydantic model
                                            email=user_email, 
                                            password=user_password,
                                            confirm_password=user_conf_pass
                                            )

                user_dict = userinfo.model_dump(exclude={"confirm_password"})           #converting succesfully validated model ito dictionary + excluding unneccery field

                cls.userdetails.append(user_dict)                                   #saving that converted dict to our database/list
                print("REGISTRATION SUCCESSFUL!\n")
                # print(cls.userdetails)                                              #test to see if it working or not
                break                                       
                
            except ValidationError as e:                                            #if data has validation error,this handles it
                 print("\n--- REGISTRATION ERROR ---")
                 for error in e.errors():                                        # Grabs just the clean message (e.g., "value is not a valid email address")
                    print(f"Error: {error['msg']}")
                    print("Please try entering your details again.\n")


    @classmethod
    def login(cls):
        user_username   = input("ENTER USERNAME:")
        user_password   = input("ENTER YOUR PASSWORD:")

        user_found = False
        Login_status = False

        for users in cls.userdetails:

            if user_username == users["username"]:
                user_found = True

                if user_password == users["password"]:

                    print("LOGGED IN SUCCESSFULLY!!!!")
                    Login_status = True
                    return user_username,Login_status

                else:

                    print("INCORRECT PASSWORD!!!")
                    return user_username,Login_status
                
        if user_found == False:
            print("USERNAME NOT FOUND/INCORRECT!!!")

        return None, Login_status