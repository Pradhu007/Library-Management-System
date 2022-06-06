import datetime
import random
import random

availabebooks = ["John Peterson's Murder","Markwille's Grand Cresent","Willy"]
borrowedbooks = []
quotes = ["The purpose of our lives is to be happy","Get busy living or get busy dying","You only live once, but if you do it right, once is enough"]

def randomquote():
    quote = random.choice(quotes)

    return quote














def listborrowedbooks(borrowedbooks:list):

    for i,borrowedbooksnames in enumerate(borrowedbooks,start=1):

        print(i,borrowedbooksnames)









def add_book(nameofbook:str,availablebooks:list):

    isAdded = False
    availabebooks.append(nameofbook)
    isAdded = True


    if isAdded == True:
        print("The book {} has been succesfully added at {}".format(nameofbook,datetime.datetime.now()))











def borrow(books:list):

    listbooks(availabebooks)

    found = False
    borrow = int(input("Please enter the number corresponding to the  book you would you like to borrow?"))

    for i,name in enumerate(books,start=1):
        if i == borrow:

            s = name
            borrowedbooks.append(name)
            books.remove(name)
            found = True



    if found == True:
           print("The book {} has been successfully borrowed  at {} ".format(s,datetime.datetime.now()))

    else:
        print("Not found")



















def returnbook(borrowedbooks:list):

    listborrowedbooks(borrowedbooks)

    isReturn = False



    returnbookinput = int(input("What book would you like to return"))

    for s,returnbookname in enumerate(borrowedbooks,start=1):


     if s == returnbookinput:
        borrowedbooks.remove(returnbookname)

        availabebooks.append(returnbookname)
        isReturn = True

    if isReturn == True:
        print("Succesfully returned  {} at {} ".format(returnbookname,datetime.datetime.now()))














def listbooks(books:list):

    print("--------------------------------")
    print("---------Available Books!----- ")
    print("--------------------------------")
    for i, name in enumerate(books,start=1):
        print(i,name)











def menu():
    print("--------------------------")
    print("---------------------------")
    print("---------------------------")
    print("--------Library System-----")
    print("---------by Pradhu007-------")
    print("----------------------------")

    getrandomquote = randomquote()
    print("Quote of the day:" + getrandomquote)

    print("1. List Available Books")
    print("2. Borrow a  book "     )
    print("3. Return a book  "     )
    print("4. Add a  book     "    )
    print("5. List borrowed books" )





    while 1:






       choice = int(input("What would you like to do today ?"))








       if choice == 1:
           listbooks(availabebooks)


       elif choice == 2:
           borrow(availabebooks)


       elif choice == 3:
           returnbook(borrowedbooks)


       elif choice == 4:
           nameofbook = input("Please enter the  name of book?")
           add_book(nameofbook,availabebooks)


       elif choice == 5:
           listborrowedbooks(borrowedbooks)


menu()








































