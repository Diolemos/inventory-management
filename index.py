products = [{"name":"water bottle",
 "manufacturer": "Tupperware", "code": 1 },{"name":"Accustic guitar",
 "manufacturer": "Yamaha", "code": 2}, {"name":"Piano",
 "manufacturer": "Yamaha", "code": 3 },{"name":"pendrive",
 "manufacturer": "sandisk", "code": 4 }]

codeCounter = 5 #counter for tracking the product codes


def registerProduct(code):
     name = input("What's the product name?")  #whats the product's name?
   
     manufacturer = input("What's the manufacturer?")#what's its manufacturer?
     #what's its cost ? 
     #save it to a dictionary 
     newProduct = {"name":name,"manufacturer": manufacturer,"code": code}  
     codeCounter += 1
     list.append(newProduct)


def consultProduct():
    #sub menu : consult all products
                #consult by code
                #consult by manufacturer
                #back to main manu
                


def removeProduct():
             #ask for the product's code


while True:
    print("Welcom the Pedro Diogenes' stock managment system")
    print("What would you like to do?")
    print("1 - Register new product")
    print("2 - consult product")
    print("3 . remove product")
    print("4 - Exit program")
    #implement try to catch value errors
    choice = int(input(""))
    
    if choice == 1:
        print("You chose 1- Register new product")
        registerProduct(codeCounter)
        continue
    elif choice == 2:
        print("You chose 2- Consult product")
        consultProduct()
        continue
    elif choice == 3:
        print("You chose 3- remove a product")
        removeProduct()
        continue
    elif choice == 4:
        print("You chose- 4, exeting...")
        break    
    else:
        print("Error. invelid option")
        continue        
        
    
                             