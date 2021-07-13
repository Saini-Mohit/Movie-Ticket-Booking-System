def viewDetails():                                         #Function creation
         print("____________________________________________")
         print("Movie : ",movie)
         print("Screen : ",screen)
         print("The name of the customer is: ", allotteeName)
         print("The customer contact number is : ", allotteeNumber)
         print("Number of seats reserved by the customer: ", validate)
         print("____________________________________________")
         print("")

print("____________________________WELCOME TO MOVIE TICKET BOOKING SYSTEM_____________________________________")    #Intro
print("")
listName=list()                                         #Decleration
movie = "Avengers Endgame"                              #Static value      
screen = 1                                              #Static value
price = 16.99                                           #Static value
orderedSeats = []
validate=0
allotteeName = []
allotteeNumber = []

for list1 in range(1,101):                              #Decleration
    listName.append(list1)
    firstNameStore=list()
for list2 in range(1,101):                              #Decleration
    firstNameStore.append(list2)
    lastNameStore=list()
for list3 in range(1,101):                              #Decleration
    lastNameStore.append(list3)
    contactNumberStore=list()

for list1 in range(1,101):                              
    contactNumberStore.append(list1)
    r=1
while r !=0:                                            #Loop for menu starts here
     print("***************************************************************************")  
     print("If you want to want to book a ticket then select :-  1)         Book ticket")
     print("If you want to see seat avalibility then select  :-  2)  Check availibiltiy")
     print("If you want to see total booking select          :-  3)       Total booking")
     print("If you want to see exit,select                   :-  4)                Exit")
     print("***************************************************************************") 
         
     choice = int(input("Enter your option: "))                         #To store the choice
     print("")
     if choice==1:                                                      #To book tickets
         firstName=str(input("Please Enter your First Name: "))
         lastName=str(input("Please Enter your Last Name: "))
         contactNumber=int(input("Please Enter your Phone Number: "))
         allotteeName.append(firstName)
         allotteeNumber.append(contactNumber)
         seatInput = int(input("Enter the desired seat you want to book: "))       
         validate = validate + seatInput
         if (seatInput<=0):                                             #If users enters zero numbers of seat(s)
            print("Sorry, please enter valid number.")
            print("")
         elif(seatInput>100):                                           #If users enters more than 100 numbers of seat(s)
            print("Sorry, you cannot buy more than 100 seats")
            print("")
         else:
             for x in range(1,seatInput+1):
                 bookingSaver=int(input("Enter th seat no: "))          #Booking happens here
                 if  listName[bookingSaver-1]==bookingSaver:            #If user enters the valid seat number         
                     listName.pop(bookingSaver-1)
                     firstNameStore.pop(bookingSaver-1)
                     lastNameStore.pop(bookingSaver-1)
                     contactNumberStore.pop(bookingSaver-1)
                     listName.insert(bookingSaver-1,"This seat is Booked.")     #Pop-up message after the seat is booked 
                     firstNameStore.insert(bookingSaver-1,firstName)
                     lastNameStore.insert(bookingSaver-1,lastName)
                     contactNumberStore.insert(bookingSaver-1,contactNumber)
                     orderedSeats.append(bookingSaver)
                     totalprice = price * seatInput                             #Seat total
                     federaltax = (totalprice * 3) / 100                        #Tax 
                     provincetax = (totalprice * 8.54) / 100                    #Tax 
                     grandTotal = (totalprice + federaltax + provincetax)       #Amount to be paid
                     print("---------------------------------------------------")
                     print("Seat(s) Booked successfully.")
                 else:                                                    #If user enters duplicate value while booking seat(s)
                     print("---------------------------------------------------")
                     print("Sorry! This seat(s) is already been booked by another costumer, please try other seat.")
                     print("The seat is: ",bookingSaver)
                     print("Customer Name is :",firstNameStore[bookingSaver-1].title(),"",lastNameStore[bookingSaver-1].title(),
                           "and Number is : ",contactNumberStore[bookingSaver-1])
             print("---------------------------------------------------")
             print("Your ",seatInput," ticket(s) are booked.")        #Prebooking report       
             print("The customer name is: ",firstNameStore[bookingSaver-1].title(),'',lastNameStore[bookingSaver-1].title())
             print("The customer contact number is: ",contactNumberStore[bookingSaver-1])
             print("Seat(s) booked are: ",orderedSeats)
             print("The total price of ticket(s) are: ",totalprice)
             print("Final amount after adding tax for " , seatInput , " tickets are: " , grandTotal)        
             print("____________________________________________")
             print("")
             orderedSeats = []                                         # To reset 
            
     elif choice==2:                                                   #Check ticket availbality 
         print("____________________________________________")
         seatReference=int(input('Enter seat no: '))
         seatReference=seatReference-1
         if firstNameStore[seatReference]==seatReference+1:             #If ticket is booked
             print("---------------------------------------------------")
             print('This seat is not booked.')
             print("---------------------------------------------------")
         else:                                                          #If ticket is not book
             print("---------------------------------------------------")
             print("Movie : ",movie)
             print("Screen : ",screen)
             print('Customer Name is :',firstNameStore[seatReference].title(),'',lastNameStore[seatReference].title(),
                   'and Number is : ',contactNumberStore[seatReference])
             print("The seat chosen by customer is: ",seatReference)             
             print("---------------------------------------------------")
             print("")

     elif choice==3:                                                    #View total booking of one invidual
        viewDetails()                                                   #Function calling
     elif choice==4:                                                    #Exit loop on valid command only
        print("")
        print("---------------------------------------------------")
        print("Thank you for choosing our platfrom,Enjoy your movie",movie,"Have a nice day")
        print("---------------------------------------------------")
        print("")
        break
     else:
        print("---------------------------------------------------")
        print("!!!!!!!!!!!!Please select correct option!!!!!!!!!!!")
        print("---------------------------------------------------")
        print("")
