import datetime;
menu = int(input("ORDER PLEASE \n 1.Pasta  \n 2.Rice \n 3.Cake \n \n  Select Yours: "))

if menu == 1:
    print("\nPasta with 340 BDT ")
    
    date_entry = input('Enter You date of birth in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    pyear=datetime.datetime.now().year
    pmonth=datetime.datetime.now().month
    pday=datetime.datetime.now().day
    quantity=int(input('Quantity: '))
    age=pyear-year;
    if(month==pmonth and day==pday):
        print('Congratulation Today is Your Birthday ! Enjoy Our offer!')
        if(age>=0 and age<=25):
          pasta=340
          discount=(pasta*quantity)*35/100;
          total_bill=pasta*quantity-discount;
          print('Today You been ' ,age,'Years Old')
          print("Happy Birthday! You Got the discount 15% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        elif(age>=60):
          pasta=340
          discount=(pasta*quantity)*50/100;
          total_bill=pasta*quantity-discount;
          print("Happy Birthday! You Got the discount 30% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        else:
          pasta=340
          discount=(pasta*quantity)*25/100;
          total_bill=pasta*quantity-discount;
          print("Happy Birthday! You Got the discount 5% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
    else:
        pasta=340
        print('Today is not Your Birthday')
        print('Your Total Bill is ',pasta*quantity)
        print('Thank you so Much for Ordering!!😍')

    conform =int(input("\n confirm to press one :"))

    if conform ==1:
        print("\n Order confirmed!! ")
    else:
        print("Select correct option")

elif menu == 2:
    print("\n Rice with 150 BDT")
    date_entry = input('Enter You date of birth in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    pyear=datetime.datetime.now().year
    pmonth=datetime.datetime.now().month
    pday=datetime.datetime.now().day
    quantity=int(input('Quantity: '))
    age=pyear-year;
    if(month==pmonth and day==pday):
        print('Congratulation Today is Your Birthday ! Enjoy Our offer!')
        if(age>=0 and age<=25):
          Rice=150
          discount=(Rice*quantity)*15/100;
          total_bill=Rice*quantity-discount;
          print('Today You been ' ,age,'Years Old')
          print("Happy Birthday! You Got the discount 15% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        elif(age>=60):
          Rice=150
          discount=(Rice*quantity)*30/100;
          total_bill=Rice*quantity-discount;
          print("Happy Birthday! You Got the discount 30% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        else:
          Rice=150
          discount=(Rice*quantity)*5/100;
          total_bill=Rice*quantity-discount;
          print("Happy Birthday! You Got the discount 5% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
    else:
        Rice=150
        print('Today is not Your Birthday')
        print('Your Total Bill is ',Rice*quantity)
        print('Thank you so Much for Ordering!!😍')

    confirm = int(input("\nconform to press one"))

    if confirm == 1:
        print("\n Order confirmed")
    else:
        print("chose correct option")

elif menu == 3:
    print("\n  Cake with  250 BDT")
    date_entry = input('Enter You date of birth in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    pyear=datetime.datetime.now().year
    pmonth=datetime.datetime.now().month
    pday=datetime.datetime.now().day
    quantity=int(input('Quantity: '))
    age=pyear-year;
    if(month==pmonth and day==pday):
        print('Congratulation Today is Your Birthday ! Enjoy Our offer!')
        if(age>=0 and age<=25):
          Cake=250
          discount=(Cake*quantity)*15/100;
          total_bill=Cake*quantity-discount;
          print('Today You been ' ,age,'Years Old')
          print("Happy Birthday! You Got the discount 15% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        elif(age>=60):
          Cake=250
          discount=(Cake*quantity)*30/100;
          total_bill=Cake*quantity-discount;
          print("Happy Birthday! You Got the discount 30% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
        else:
          Cake=250
          discount=(Cake*quantity)*5/100;
          total_bill=Cake*quantity-discount;
          print("Happy Birthday! You Got the discount 5% ")
          print("After discount Total bill is: ",total_bill,'BDT')
          print('Thank you so Much for Ordering!!😍')
    else:
        Cake=250
        print('Today is not Your Birthday')
        print('Your Total Bill is ',Cake*quantity)
        print('Thank you so Much for Ordering!!😍')

    conform = int(input("\n conform to press one"))

    if conform == 1:
        print("\n Order confirmed")
    else:
        print("chose correct option")

else:
    print("\n WRONG SELECTION")