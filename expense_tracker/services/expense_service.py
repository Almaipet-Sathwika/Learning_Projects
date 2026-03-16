import csv
import os


def add(user_name, category, amount):
    if(amount<=0):
        raise ValueError("Invalid amount")
    
    file = os.path.join("data", f"{user_name}_expense.csv")
    #file = "data\\"+user_name+"_expense.csv"
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([category, amount])


def fetch(user_name, category):
    file = os.path.join("data", f"{user_name}_expense.csv")
    #file = "data\\"+user_name+"_expense.csv"
    if(os.path.getsize(file)==0):
        return ("No expenses found")
    sum =0
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            
            if(len(row)>=2 and row[0]==category):
                sum += float(row[1])
    return sum



def view(user_name):
    file = os.path.join("data", f"{user_name}_expense.csv")
    #file = "data/"+user_name+"_expense.csv"
    if(os.path.getsize(file)==0):
        return ("No expenses found")
    data = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


    

def total(user_name):
    file = os.path.join("data", f"{user_name}_expense.csv")
    #file = "data\\"+user_name+"_expense.csv"
    tot = 0
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            tot += float(row[1])
    return(tot)
    