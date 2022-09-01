products = [{"name":"water bottle",
 "manufacturer": "Tupperware", "code": 1375 },{"name":"Accustic guitar",
 "manufacturer": "Yamaha", "code": 1387 }, {"name":"Piano",
 "manufacturer": "Yamaha", "code": 1388 },{"name":"pendrive",
 "manufacturer": "sandisk", "code": 1466 }]




def registerProduct():
     print("test")
     #whats the product's name?
     #what's its manufacturer?
     #what's its cost ? 
     #save it to a dictionary 


def consultProduct():
    #sub menu : consult all products
                #consult by code
                #consult by manufacturer
                #back to main manu
                


def removeProduct():
             #ask for the product's code

while True:
    print("Welcom the stock managment system")
    print("What would you like to do?")
    print("1 - Register new product")
    print("2 - consult product")
    print("3 . remove product")
    print("4 - Exit program")
    #implement try to catch value errors
    choice = int(input(""))
    
    if choice == 1:
        registerProduct()
        continue
    elif choice == 2:
        consultProduct()
        continue
    elif choice == 3:
        removeProduct()
        continue
    elif choice == 4:
        print("exeting...")
        break    
    else:
        print("Error. invelid option")
        continue        
        
    
                             