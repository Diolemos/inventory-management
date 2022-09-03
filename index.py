print("Welcom the Pedro Diogenes' stock managment system")
productList = [{"name":"water bottle",
 "manufacturer": "Tupperware","cost":70, "code": 1 },{"name":"Accustic guitar",
 "manufacturer": "Yamaha","cost":1850, "code": 2}, {"name":"Piano",
 "manufacturer": "Yamaha","cost":2300, "code": 3 },{"name":"pendrive",
 "manufacturer": "sandisk","cost":40, "code": 4 }]

codeCounter = 5 #counter for tracking the product codes


def registerProduct(code):
     name = input("What's the product name?")  #whats the product's name?
   
     manufacturer = input("What's the manufacturer?")#what's its manufacturer?
     cost = float(input("What's the product's cost?"))#what's its cost ? 
     
     newProduct = {"name":name,"manufacturer": manufacturer,"cost":cost,"code": code}  #creates the object to be apended to the list
     #myList = list()
     productList.append(newProduct.copy()) #save it to a dictionary 


def consultProduct():
    print("\n Would you like to:")#sub menu : consult all products
    print("1- See all products")
    print("2- consult by code")#consult by code
    print("3- consult by manufacturer")#consult by manufacturer
    print("4- go back to main manu") #back to main manu
    option = int(input(""))
    if option == 1:
        for product in productList:
            print("--------\n")
            for key, value in product.items():
                print("{} : {}".format(key,value))
    elif option == 2:
        usersInput = int(input("Please, insert the code:"))
        for product in productList:
            if product["code"] == usersInput:
              for key, value in product.items():
                  print("{}: {}".format(key,value))
    
        
    elif option == 3:
        usersInput = input("Please, type the manufacturer name:")
        for product in productList:
            if product["manufacturer"] == usersInput:
              print("-----------------\n")
              for key, value in product.items():
                  print("{}: {}".format(key,value))
            
        
            
    elif option == 4:
        print("4: Back to main manu...")
        return 
    else:
        print("Invalid option")
        return            
                
            
               
                


def removeProduct():
        usersInput = int(input("What's the code of the product you would like to remove?")) #still need to implement try and execpt
        for product in productList:
            if product["code"] == usersInput:
                print("Deleting Product: ", product["name"])
                productList.remove(product) #I still need to implement a submition for the user's confirmation. Asking if he really wants to delete the selected file


while True:
    
    print("\nWhat would you like to do?")
    print("1 - Register new product")
    print("2 - consult product")
    print("3 . remove product")
    print("4 - Exit program")
    #implement try to catch value errors
    choice = int(input(""))
    
    if choice == 1:
        print("You chose 1- Register new product")
        registerProduct(codeCounter)
        codeCounter += 1 #adds a number to the counter, so next products can have different codes
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
        print("Error. invalid option")
        continue        
        
    
                             