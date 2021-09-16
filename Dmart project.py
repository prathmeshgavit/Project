
import mysql.connector
import sys
import time
from functools import reduce
import pickle
print("Please Enter your personal details and register. \n")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="storemart"
)

mycursor=mydb.cursor()
def cust():
    id1=1
    name=input("enter your name: ")
    mobile=int(input("enter mob number: "))
    email=input("enter your email id: ")
    address=input("enter your address: ")
    data=(id1,name,mobile,email,address)
    insert_stmt=("insert into customer (cust_id ,cust_name,cust_mob, cust_email,cust_address) values (%s, %s, %s, %s, %s)")

    mycursor.execute(insert_stmt,data)
    mydb.commit()

cust()





print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
print("                         WELCOME TO 'THE PLAZA STORE'   \n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
print('''<<<  Select a number for the action that you would like to do:

         1. Welcome
         2. Select the items from grocery list
         3. select items from cosmetics
         4. select items from snacks
         5. select items from Dairy
         6. select items from Household
         7. Show the final list with price
         8. exit
         ''')

print("Select items that are available in store")

Grocery   = {'oil':150,'sugar':200,'flour':400,'Jaggery':350,'salt':50,
              'Turmeric powder':45,'Basmati_rice':700,'Wheat_flour':480,
             'Besan_flour':540,'Rava':300,'Toor_dal':250,'urad_dal':300,
             'moong_dal':220,'red_chili':180}
Cosmetics = {'soap':300,'hairshampoo':260,'conditioner':450,'body_lotion':600,
             'hair_oil':300,'face_cream':450,'lipcosmetics':230,'facewash':390}
snacks    = {'lays':75,'biscuits':120,'chocolates':250,'muffins':225,'cookie':170,
             'pancake':250,'popcorn':40,'bananachips':300}
Dairy     = {'milk':60,'butter':225,'cheese':350,'yoghurt':80,'paneer':280,
             'cream':125}      
Household = {'pan':2500,'wall_watch':1000,'cooker':5000,'mixer':6500,'tiffin':200,'cup':70,
             'glass':150,'plates':225,'lamp':525,'bulb':170,'bags':850}


def main():
    List_Items=[]
    g_price=[]
    while True:
        print("\n"*2)
        select=int(input("  // make your selection: "))

        print("\n")

        if select==1:
            time.sleep(2)
            print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n")
            print(" ----Up to your standard----\n     ----Save more with us----\n         ----20% Discount(if amount >5000rps)----\n")
            print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n")

        elif select==2:
            print("Grocery section: \n",Grocery)            
            need_items=True
            while need_items==True:
                enter=input("\n* Enter the items in grocery list(/lit or /kg): ").split(",")    
                quant=int(input("* Enter quantity of item: "))    
                for items in enter:
                    List_Items.extend(enter)
                    if items not in Grocery:
                        List_Items.remove(items)
                        print("some groceries are not available.\nPlease select the items which are available in shop list")
        
                    if items in Grocery.keys():
                        G_total=Grocery[items]*quant
                        print("Price:",G_total)
                        g_price.extend([G_total])
                        
                ans=input("\nDo you want Add another item(y/n)?")
                if ans=="y":
                    need_items==True
                else:
                    need_items=False

            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
        elif select==3:
            print("Cosmetics products are: \n",Cosmetics)
            need_items=True

            while need_items==True:
                enter3=input("\n* Enter the product of cosmetics items(1 set): ").split(",")        
                quant=int(input("* Enter quantity of item: "))
                for items in enter3:
                    List_Items.extend(enter3)
                    if items not in Cosmetics:
                        List_Items.remove(items)
                        print("some groceries are not available")
        
                    if items in Cosmetics.keys():
                        C_total=Cosmetics[items]*quant
                        print("Price:",C_total)
                        g_price.extend([C_total])
                
                ans=input("\nDo you want Add another item(y/n)?")
                if ans=="y":
                    need_items==True
                else:
                    need_items=False

            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif select==4:
            print("Snacks : \n",snacks)
            need_items=True

            while need_items==True:
                enter=input("\n* Enter the items(1 packet) : ").split(",")            
                quant=int(input("* Enter quantity of item: "))
                for items in enter:
                    List_Items.extend(enter)
                    if items not in snacks:
                        List_Items.remove(items)
                        print("some groceries are not available")
        
                    if items in snacks.keys():
                        S_total=snacks[items]*quant
                        if quant%2==0:
                            total=S_total/1.5
                            print("""""""""""""""""""""""""""""")
                            print("X-X-X-X  ( Buy 1 Get 1 FREE* )  X-X-X-X")
                            print("Price:",total)
                            g_price.extend([total])
                        else:
                            print("Price:",S_total)
                
                ans=input("\nDo you want Add another item(y/n)?")
                if ans=="y":
                    need_items==True
                else:
                    need_items=False

            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        elif select==5:    
            print("Dairy items are: ",Dairy)
            need_items=True

            while need_items==True:
                enter=input("\n* Enter the items in dairy section : ").split(",")
                quant=int(input("* Enter quantity of item: "))
                for items in enter:
                    List_Items.extend(enter)
                    if items not in Dairy:
                        List_Items.remove(items)
                        print("some groceries are not available")
        
                    if items in Dairy.keys():
                        D_total=Dairy[items]*quant
                        print("Price:",D_total)
                        g_price.extend([D_total])
                
                ans=input("\nDo you want Add another item(y/n)?")
                if ans=="y":
                    need_items==True
                else:
                    need_items=False

            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif select==6: 
            print("Household products: \n",Household)
            need_items=True

            while need_items==True:
                enter=input("\n* Enter the items: ").split(",")
                quant=int(input("* Enter quantity of item: "))
                for items in enter:
                    List_Items.extend(enter)
                    if items not in Household:
                        List_Items.remove(items)
                        print("some groceries are not available")
        
                    if items in Household.keys():
                        H_total=Household[items]*quant
                        print("Price:",H_total)
                        g_price.extend([H_total])
                
                ans=input("\nDo you want Add another item(y/n)?")
                if ans=="y":
                    need_items==True
                else:
                    need_items=False

            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif select==7:
            f=open("liststored.txt","wb")
            print("Items in your list: ")
            a=zip(List_Items,g_price)
            for i in a:
                print(i)
            pickle.dump(a,f)
            f.close()
            def remove():
                try:
                    print("\n iF yOu don'T waNt To RemovE iTem tHen skip It.\n")
                    removeitem=input("Enter the item that you want to remove from list: ")
                    price=int(input("enter correct  price of that item : "))
                    List_Items.remove(removeitem)
                    g_price.remove(price)
                    print("\n * Your final list are: \n",List_Items)
                except:
                    print("All items that you are selected are: \n",List_Items)
                    
            remove()

            def sum1():
                final_price = reduce(lambda x,y:x+y, g_price)               
                if final_price>=10000:
                    offer_price=final_price-final_price*(20/100)
                    print("\n ////  20% Discount  //// ")
                    print("Total Amount: ",offer_price)
                else:
                    print("Total Amount: ",final_price)

            sum1()
            print("\n"*2)
            def final():
                click=input("select the button for the payment procedure(pay(*)/cashonDelivery(:)/cancel(-)): ")
                if click=="*":
                    print("Your payment has been done .....!\n")
                    time.sleep(10)
                    print(" <<<<<<<   WE WILL BRING IT OUT TO YOU IN 30 mins   >>>>>>>>")
                    print("\n   ****************************************************\n")
                if click==":":
                    print("Cash on delivery")
                    print("\n <<<<<<<   WE WILL BRING IT OUT TO YOU IN 30 mins   >>>>>>>>")
                    print("\n   ****************************************************\n")
                    
                else:
                    print("Your payment has been cancelled")
                    print("  !!!!!!!!!!!!  visit for the next time  !!!!!!!!!!!!!!  ")
     
            final()

        else:
            print("On behalf of 'THE PLAZA STORE', we wanted to say thank you for your purchase.")
            sys.exit()
            
main()
mydb.close()
