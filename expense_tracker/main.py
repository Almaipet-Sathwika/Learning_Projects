from services import auth_service, expense_service


print("WELCOME TO EXPENSE TRACKER")
print("1. login     2. create acc   3. exit")


while(True):
    
    print("1. login     2. create acc   3. exit")
    opt = int(input("Choose your option: "))
    match opt:
        case 1:
            user_name = input("Enter user name: ")
            password = input("Enter your password")
            
            if auth_service.authenticate(user_name, password):
                while(True):
                    print("1.Add     2. fetch    3. view     4. Total    5. logout")
                    opt2 = int(input("Choice: "))
                    match opt2:
                        case 1:
                            category = input("Entercategory: ")
                            amount = int(input("enter amount: "))
                            expense_service.add(user_name, category, amount)

                        case 2:
                            category = input("Enter category: ")
                            expense_service.fetch(user_name, category)

                        case 3:
                            expense_service.view(user_name)

                        case 4:
                            expense_service.total(user_name)

                        case 5:
                            print("logged out successfully")
                            break


        case 2:
            
                user_name = input("Enter user name: ")
                password = input("enter password: ")
                auth_service.create_user(user_name, password)
            

                


        case 3:
            print("Thank you!")
            break