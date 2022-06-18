import datetime

class Library():
    def __init__(self,Name,Author,Quantity,Price):
        self.Name = Name
        self.Author = Author
        self.Quantity = Quantity
        self.Price = Price
        
        
    def display1(self):
        Books = [self.Name,self.Author,self.Quantity,self.Price]
        file = open("Books.txt","a")
        content = ",".join(Books)        
        file.writelines(content)
        file.writelines("\n")
        file.close()

    def display11(self):    
        Books = [self.Name,self.Author,self.Quantity,self.Price]
        content = ",".join(Books)
        print(content)
            
        
    def display2(self,user,phn1,date1,time1):
        self.user = user
        self.phn1 = phn1
        self.date1 = date1
        self.time1 = time1
        userlend = 'Name of the user is: '+self.user
        phonelend = 'Phone Number of the user is: '+self.phn1
        datelend = 'The date of the book borrowed is: '+self.date1
        timelend = 'The time of the book borrowed is: '+self.time1
        total = 0
        quantity = 0
        for i in range(N):
            bookks = input("Enter the name of the Book you want to borrow: ")
            booknames = 'Name of the book borrowed is: '+bookks
            bookname = str(booknames)
            if bookks == Chirayu1.Name:
                if int(Chirayu1.Quantity) >= 1:
                    print("Book is Available")
                    total = total + int(Chirayu1.Price)
                    Chirayu1.Quantity = int(Chirayu1.Quantity) -1
                    Chirayu1.Quantity = str(Chirayu1.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data0 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data0)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                    
                    
                else:
                    print("Book is out of Stock")
                    
            elif bookks == Chirayu2.Name:
                if int(Chirayu2.Quantity) >= 1:
                    print("Book is Available")
                    total = total + int(Chirayu2.Price)
                    Chirayu2.Quantity = int(Chirayu2.Quantity) -1
                    Chirayu2.Quantity = str(Chirayu2.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data1 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data1)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                else:
                    print("Book is out of Stock")
                    
                
            elif bookks == Chirayu3.Name:
                if int(Chirayu3.Quantity) >=1:
                    print("Book is Available")
                    total = total + int(Chirayu3.Price)
                    Chirayu3.Quantity = int(Chirayu3.Quantity) -1
                    Chirayu3.Quantity = str(Chirayu3.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data2 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data2)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                else:
                    print("Book is out of Stock")

            elif bookks == Chirayu4.Name:
                if int(Chirayu4.Quantity) >=1:
                    print("Book is Available")
                    total = total + int(Chirayu4.Price)
                    Chirayu4.Quantity = int(Chirayu4.Quantity) -1
                    Chirayu4.Quantity = str(Chirayu4.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data3 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data3)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                else:
                    print("Book is out of Stock")

            elif bookks == Chirayu5.Name:
                if int(Chirayu5.Quantity) >=1:
                    print("Book is Available")
                    total = total + int(Chirayu5.Price)
                    Chirayu5.Quantity = int(Chirayu5.Quantity) -1
                    Chirayu5.Quantity = str(Chirayu5.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data4 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data4)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                else:
                    print("Book is out of Stock")

            elif bookks == Chirayu6.Name:
                if int(Chirayu6.Quantity) >=1:
                    print("Book is Available")
                    total = total + int(Chirayu6.Price)
                    Chirayu6.Quantity = int(Chirayu6.Quantity) -1
                    Chirayu6.Quantity = str(Chirayu6.Quantity)
                    print("Price for the total book is Rs",total)
                    print("Data Added")
                    print("You can take book now")
                    amount = "Amount for the book given is: "+str(total)
                    amount = str(amount)
                    data5 = [bookname,"\n",userlend,"\n",phonelend,"\n",datelend,"\n",timelend,"\n",amount]
                    file = open(self.user + ".txt","a")
                    file.writelines("\n")
                    file.writelines(data5)
                    file.close()
                    print("_____________________Borrow Information_____________________")
                    data00 = [bookname]
                    contentt = ",".join(data00)
                    print(contentt)
                    data01 = [userlend]
                    contentt1 = ",".join(data01)
                    print(contentt1)
                    data02 = [phonelend]
                    contentt2 = ",".join(data02)
                    print(contentt2)
                    data03 = [datelend]
                    contentt3 = ",".join(data03)
                    print(contentt3)
                    data04 = [timelend]
                    contentt4 = ",".join(data04)
                    print(contentt4)
                    data05 = [amount]
                    contentt5 = ",".join(data05)
                    print(contentt5)
                    print("____________________________________________________________")
                else:
                    print("Book is out of Stock")
                    
                                
            else:
                print("Book you are searching for is not Available at this time")


def borrowerfun1():
    flag = True
    file = open(userborrowed + ".txt", "r")
    file1 = file.readlines()
    file2 = file1[2]
    file2 = str(file2)
    file.close()
    return file2

def borrowerfun2():
    file = open(userborrowed + ".txt", "r")
    file1 = file.readlines()
    file2 = file1[1: -1]
    file2 = str(file2)
    file.close()
    return file2
   
Chirayu1 = Library("Harry Potter","JK Rowling","30","100")
Chirayu2 = Library("Start With Why","Simon Sinek","10","120")
Chirayu3 = Library("Programming With Python","John Smith","20","150")
Chirayu4 = Library("The Testaments","Margaret Atwood","10","90")
Chirayu5 = Library("The Overstory","Richard Powers","15","100")
Chirayu6 = Library("My Journey","Dr. A.P.J. Abdul Kalam","10","110")




while(True):
    print("\n")
    print("_______________________WELCOME TO CHIRAYU LIBRARY_______________________")
    print("                      Enter your Choice to continue                     ")
    print("1. Display Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    choice = input("Enter your Choice: ")
    if choice not in ["1","2","3","4"]:
        print("Enter valid option")
        continue
        
    else:
        choice = int(choice)

    if choice == 1:
        Chirayu1.display1()
        Chirayu2.display1()
        Chirayu3.display1()
        Chirayu4.display1()
        Chirayu5.display1()
        Chirayu6.display1()
        print("Books are shown in books file")
        print("Press s if you want to show Books here and Press c if you want to continue")
        show = ""
        while(show != "s" and show != "c"):
            show = input().lower()
            if show == "s":
                print("_________________________Book Information_________________________")
                print("\n")
                Chirayu1.display11()
                Chirayu2.display11()
                Chirayu3.display11()
                Chirayu4.display11()
                Chirayu5.display11()
                Chirayu6.display11()
                print("__________________________________________________________________")
                print("Press c to Continue")
                cc = ""
                while(cc != "c"):
                    cc = input().lower()
                    if cc == "c":
                        continue
                    
            elif show == "c":
                continue
        
    elif choice == 2:
        print("_________________________Borrow Section_________________________")
        print("_________Book Names_________")
        print("Harry Potter")
        print("Start With Why")
        print("Programming With Python")
        print("The Testaments")
        print("The Overstory")
        print("My Journey")
        print("____________________________")
        try:
            N = int(input("How many books you want to borrow ?: "))
        except ValueError:
            print("Enter numerical value")
            continue
        if N > 3:
            print("You cannot Borrow more than 3 books")
        else:
            user = input("Enter your Name: ")
            phn1 = input("Enter your Phone Number: ")
            date = datetime.datetime.today().date()
            date1 = str(date)
            print("Date you have borrowed book is ",date1)
            time1 = input("Enter the Time you have borrow book: ")
            data = Library(user,phn1,date1,time1)
            data.display2(user,phn1,date1,time1)
        print("Press q to quit and c to continue")
        choice2 = ""
        while(choice2!="c" and choice2!="q"):
            choice2 = input().lower()
            if choice2 == "q":
                exit()
            elif choice2 == "c":
                continue


    elif choice == 3:
        
        print("_________________________Return Section_________________________")
        userborrowed = input("Enter your Name: ")
        try:
            if userborrowed in borrowerfun1():
                print("You have borrowed some Book")
                bookborrow = input("Enter the Name of the book you have borrowed: ")
                if bookborrow in borrowerfun2():
                    print("Yes, you have borrowed this book")
                    if bookborrow == Chirayu1.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu1.Quantity == "30":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu1.Quantity = int(Chirayu1.Quantity) + 1
                            Chirayu1.Quantity = str(Chirayu1.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")

                    elif bookborrow == Chirayu2.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu2.Quantity == "10":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu2.Quantity = int(Chirayu2.Quantity) + 1
                            Chirayu2.Quantity = str(Chirayu2.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")

                    elif bookborrow == Chirayu3.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu3.Quantity == "20":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu3.Quantity = int(Chirayu3.Quantity) + 1
                            Chirayu3.Quantity = str(Chirayu3.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")

                    elif bookborrow == Chirayu4.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu4.Quantity == "10":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu4.Quantity = int(Chirayu4.Quantity) + 1
                            Chirayu4.Quantity = str(Chirayu4.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")

                    elif bookborrow == Chirayu5.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu5.Quantity == "15":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu5.Quantity = int(Chirayu5.Quantity) + 1
                            Chirayu5.Quantity = str(Chirayu5.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")

                    elif bookborrow == Chirayu6.Name:
                        try:
                            days = int(input("Enter the days you have taken book: "))
                        except ValueError:
                            print("Enter numerical value")
                        if days > 10:
                            print("Fine for the late submission of book is Rs 200.")
                        else:
                            print("No fine taken")
                        if Chirayu6.Quantity == "10":
                            print("No borrowed books, Book has already been returned")
                        else:
                            Chirayu6.Quantity = int(Chirayu6.Quantity) + 1
                            Chirayu6.Quantity = str(Chirayu6.Quantity)
                            print("Book returned")
                            days = str(days)
                            borrowerr = "Name of the borrower is "+userborrowed
                            booknames = "Name of the borrowed book is "+bookborrow
                            dayy = "User had taken book for "+days+" days."
                            borrowerr = str(borrowerr)
                            booknames = str(booknames)
                            dayy = str(dayy)
                            returndata = [borrowerr,"\n",booknames,"\n",dayy]
                            file = open("Returndata.txt","a")
                            file.writelines("\n")
                            file.writelines(returndata)
                            file.writelines("\n______________________________________")
                            file.close()
                            print("_____________________Return Information_____________________")
                            print(borrowerr)
                            print(booknames)
                            print(dayy)
                            print("____________________________________________________________")
                else:
                    print("Enter valid book name")

        except FileNotFoundError:
            print("No Borrower Data found")
        
        

    else:
        exit()
        



        
        
        

        
        
        
    
        
    
    
    
