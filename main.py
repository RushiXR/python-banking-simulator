import Login,operations



while True:
    Login.Loginportal.show_options()
    try:
        choice = int(input("ENTER YOUR CHOICE:"))
    except:
        print("PLEASE ENTER A VALID ENTERY")
    if choice == 1:
        Login.Loginportal.register()

    elif choice == 2:
        user_username,Login_status = Login.Loginportal.login()
        if Login_status == True and user_username is not None:
            user = operations.BankAccount(name=user_username)
            while True:
                user.show_methods()
                a = int(input("\nCHOOSE ONE OF THE OPTION:"))

                if a == 1:

                    user.deposit()
                    user.display_balance()

                elif a == 2:
                    
                    user.withdraw()
                    user.display_balance()

                elif a == 3:
                    user.display_balance()

                elif a == 4:
                    user.display_details()

                elif a == 5:
                    break

                else:
                    print("\nENTER A VALID INPUT")
                
    elif choice == 3:
        break