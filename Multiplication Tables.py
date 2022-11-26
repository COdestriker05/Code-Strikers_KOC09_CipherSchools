#This is the Python Mini-project done by : Shivam Singh(12221831) [Roll No.= 39]

#Aim of project: Create a multiplication table application where user will enter a sentinel value n and the application will display the mathematical multiplication
#                tables till given sentinel value n.

#Code of project using Class Concepts:
class tables: 
    def tables (self ,n_value): 
        self.n_value = n_value
        for x in range(2, n_value + 1):
            print("TABLE OF",x,':-')
            print("-"*14)
            
            for y in range(1, 11): 
                print(x," x", y,"=",x*y)
            print("-"*14)
            
#Taking a sentinel value as input from user.           
n_value=int(input("Enter a sentinel value till that tables execute :- "))
f=tables() 
f.tables(n_value)