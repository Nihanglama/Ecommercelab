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

def Checkout(lists):
    print("Your Items to Checkout ")
    print("-------------------------------")
    print("Name          |           Price")
    print("-------------------------------")
    for Name,price in lists.items():
        print(Name+"                RS:"+ str(price))
    print("--------------------------------")
    print(f"Total Item:                  {len(list(lists.keys()))}")
    print("--------------------------------")
    print(f'Total Amount                  Rs:{sum(lists.values())}\n\n')


def Show_Mycart(lists):
    print("Items in Product_List")
    print("-------------------------------")
    print("Name          |           Price")
    print("-------------------------------")
    for Name,price in lists.items():
        print(Name+"                RS:"+ str(price))
    print("--------------------------------\n\n")

if __name__=="__main__":
    print("Your Items in Cart \n")
    print("---------------------------------")
    print("-----------Menu------------------")
    print("---------------------------------")
    print("1:Add Tocart")
    print("2:Display cart")
    print("3:Checkout")
    print("4:Exit")
    print("---------------------------------\n\n")

    Show_Mycart(Product_list)
    while(True):
        choice=int(input("Enter your choice: "))
        if(choice==1):
            item=input("Enter the Item to add: ")
            Add_to_Cart(item)
        elif(choice==2):
            Show_Mycart(My_cart)
        elif(choice==3):
            Checkout(My_cart)
        elif(choice==4):
            exit()
        else:
            print("Wrong choice")

    
    