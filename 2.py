Product_list={
            'Tshirt':1000,
           'Nike':5000,
           'Acer':100000,
           'RiceCooker':3000
            }
My_cart={}
def Add_to_Cart(item):
    if item in Product_list.keys():
        My_cart[item]=Product_list[item]
    else:
        print("Item not in Product list")
    
    
def Show_Products(lists):
    print("-------------------------------")
    print("Name          |           Price")
    print("-------------------------------")
    for Name,price in lists.items():
        print(Name+"                RS:"+ str(price))

if __name__=="__main__":
    print("---------------------------------")
    print("-----------Menu------------------")
    print("---------------------------------")
    print("1:Add Tocart")
    print("2:Display cart")
    print("3:Exit")
    print("---------------------------------")
    print("Items in Product_List")
    Show_Products(Product_list)
    while(True):
        choice=int(input("Enter your choice: "))
        if(choice==1):
            item=input("Enter the Item to add: ")
            Add_to_Cart(item)
        elif(choice==2):
            Show_Products(My_cart)
        elif(choice==3):
            exit()
        else:
            print("Wrong choice")

    
    