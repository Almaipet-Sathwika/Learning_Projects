import csv
import os


def authenticate(user_name, password):
        
        try: 
    
            with open("data/users.csv", "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row or len(row) < 2:
                        continue

                    if(row[0]==user_name):
                        if(row[1]==password):
                            return True
                        else:
                            raise ValueError("Wrong password")
                        
                raise ValueError("User name not found")
        except ValueError as e:
             print(e)
        
                    
def create_user(user_name, password):
    try:

        exists = False
        
        with open("data\\users.csv", "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    if not row or len(row) < 2:
                        continue
                    if(row[0]== user_name):
                        exists = True
                        break
        
        if exists:
                raise ValueError("User already exists")
        else:
            with open("data\\users.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([user_name, password])
            
            path = os.path.join("data", f"{user_name}_expense.csv")
            #path = "data\\"+user_name+"_expenses.csv"
            file = open(path, "a")
            print("Successfully created user name")

    except ValueError as e:
         print(e)        

     

                
            
            

            


       
