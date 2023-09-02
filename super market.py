from datetime import datetime

name=input("enter your name :")
list="""
rice  Rs 30/kg
sugar Rs 20/kg
salt  Rs 10/kg
oil   Rs 250/kg
garlic Rs 45/kg
ginger Rs 90/kg
shampoo Rs 100/kg
paste Rs 80/kg
brush Rs 30/kg

------------------------
"""
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items= {
"rice":30,   
"sugar": 20,
"salt" : 10,
"oil"   :250,
"garlic" :45,
"ginger" :90,
"shampoo ":100,
"paste" :80,
"brush" :30
}
options=int(input("\n enter 1 to see the menu or 2 to exit:"))
if options==1:
  print(list)
for i in range(len(items)):
  inp1=int(input("\nif you want buy enter 1 or enter 2 to exit"))
  if inp1==2:
    print("thanks for visit.")
    break
  elif inp1==1:
    item=input("\n enter your items")
    quantity=int(input("enter quantity in Kg's :"))
    if item in items.keys():
        price=quantity*(items[item])
        pricelist.append((item,quantity,items,price))     
        ilist.append(item)
        qlist.append(quantity)
        totalprice+=price
        plist.append(price)
        gst=totalprice*0.10
        finalamount=totalprice+gst
    else:
      print("your entered wrong item")
    inp=input("\n you want bill the list enter yes or no :")
    if inp.lower()=="yes":
      pass
      if finalamount!=0:
         print(30*"^","python super market",30*"^")
         print(30*"^", "hanmakonda",30*"^")
         print(name,60*" ","date",datetime.now())
         for j in range(len(ilist)):
           print(j,3*"\t",ilist[j],4*"\t",qlist[j],3*"\t",plist[j])
           print(100*"-")
           print(9*"\t","total amount: ",totalprice)
           print(9*"\t","gst :",2*"\t",gst)
           print(100*"-")
           print(9*"\t","finalamount :",finalamount)
           print(100*"-")
           print(40*" ","Thanks for shopping")
           print(100*"-")
           print()
      elif inp.lower=="no":
         pass
    else:
        print("you have entered wrong input") 
  else:   
        print ("your entered wrong item") 
else:
  print("Thanks for your time")
  pass

