category_list={'Cloths':['Tshirt','pants'],
           'Shoes':['Nike','jordan'],
           'Kitchen':['RiceCooker','pan']
           }

def Add_items(category,item):
    if category in category_list.keys():
        category_list[category].append(item)
    else:
        category_list[category]=[item]
  
def Show_Products(category_list):
    print("The list of category with items are:")
    for i,j in category_list.items():
        print(f'{i}:{j}')

if __name__=="__main__":
    print("---------------------------------")
    print("-----------Menu------------------")
    print("---------------------------------")
    print("1:Add Items")
    print("2:Display items")
    print("3:Exit")
    print("---------------------------------")
    
    while(True):
        choice=int(input("Enter your choice"))
        if(choice==1):
            category=input("Enter the category")
            item=input("Enter the item ot add on category")
            Add_items(category,item)
        elif(choice==2):
            Show_Products(category_list)
        elif(choice==3):
            exit()
        else:
            print("Wrong choice")

    
    