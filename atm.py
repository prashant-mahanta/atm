import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3

import demo
import getpass
import os
import time
#the use of this function is to take sleep for 4.5 sec and the restart the program
def time_taken():
    time.sleep(4.5)
#starting of the atm process or home page
def start():
    demo.welcome()
    demo.yes_bank()
    p=process()
    if(p==0):
        #print("YOUR ACCOUNT DOESNOT EXIST PLEASE CONTACT OUR NEAREST BRANCH")
        start_time = time.time()
        time_taken()
        t0 = time.clock()
        #time_taken()
        os.system("cls")
        start()
    else:
        start_time = time.time()
        time_taken()
        t0 = time.clock()
        #time_taken()
        os.system("cls")
        start()
#use of this function to take the atm pin
def pin_code(count):
    try:
        pin=int(getpass.getpass("\n\n      PLEASE ENTER YOUR PIN:      "))
        if(count==0):
            print("\n\nYOU ENTERED 3 INCORRECT ENTRIES YOUR CARD IS BLOCKED PLEASE CONTACT THE NEAREST YES BANK BRANCH\n\n")
            return 0
        return (pin,count)
    except ValueError:
        print("\n\n     ENTER YOUR  PIN AGAIN:      ")
        pin_code(count-1)




#copy contents of file dummy to file original
def copyFiles():
    open("original.txt","w").close()
    f=open("dummy.txt","r")
    fp1=open("original.txt","a")
    for c in f:
        fp1.write(c)
    fp1.close()
    f.close()
    #while c!='':
    #    pk1.write(c)
    #    c=pk.readline()
    #pk.close()
    #pk1.close()


#check existance of account of the user
def check_account(card_no):
    fp=open("original.txt","r+")
    fp1=open("dummy.txt","w+")
    account_holder=fp.readline()
    details=[]
    while account_holder!="":
        check=account_holder.split()
        if int(check[0])==card_no:
            details=check
        else:
            check=" ".join(check)
            fp1.write(check)
            fp1.write("\n")
        account_holder=fp.readline()
    fp.close()#closing of original file
    fp1.close()#closing of dummy file
    if(len(details)!=0):
        return details      #account exist send details to the process function
    else:
        #print("YOUR ACCOUNT DOESNOT EXIST PLEASE CONTACT OUR NEAREST BRANCH")
        demo.account_not_exist()
        return 0

#if the destination account exsists or not
def accountExists(t_account):
    p=open("original.txt","r")
    c=p.readline()
    ac_d=[]
    while c!='':
        cd=c.split()
        if int(cd[0]) == t_account:
            ac_d=cd
        c=p.readline()
    p.close()
    if(len(ac_d)!=0):
        return ac_d
    else:
        demo.account_not_exist()
        return 0

#this the process of atm
def process():
    count_time=3
    try:
        card_no=int(input("\n\n      PLEASE ENTER YOUR CARD NO:     "))
    except ValueError:
        print("\n\n     PLEASE ENTER YOUR CARD NUMBER:      ")
    if_=check_account(card_no)
    if if_==0:
        return 0
    PIN,count_time=pin_code(count_time)
    if(PIN==0):
        return 0
    if int(if_[1])!=PIN:
        print("\n\n--------------------INVALID PIN-----------------------------\n")
        PIN,count_time=pin_code(count_time)
        if PIN==0:
            return 0
        elif int(if_[1])==PIN:
            next_process(if_)
    else:
        next_process(if_)

#done for option 1,2 and 3
def done(details,option):
    if option < 4:
        f=open("dummy.txt","a")
        c=' '.join(details)
        #print(c)
        f.write(c)
        f.close()
        copyFiles()
#next process
def next_process(details):
    #demo.welcome_user()
    #print("*****")
    restart='Y'
    i=2
    name=""
    while i<len(details)-2:
        name=name+details[i]
        name=name+" "
        i+=1
    name=name.upper()
    print("\n")
    print("             ********************************\n            HELLO  "+name+"\n              ****************************************\n")
    demo.option()
    while restart not in ('n','NO','no','N'):

        try:
            option = int(input('\nWHAT WOULD YOU LIKE TO CHOOSE:      '))
        except ValueError:
            print("ENTER A VALID OPTION\n\n")
            continue
        #option 1 to check balance
        if option==1:
            print('\n\n\nYOUR BALANCE IS  Rs:',details[-2],'\n\n\n')
            restart = input('WOULD YOU LIKE TO GO  BACK: ')
            if restart in ('n','NO','no','N'):
                #print('Thank You')
                #done(details,option)
                demo.thank_you()
                break
        #option 2 to withdraw cash
        elif option == 2:
            op=option2(details)# = ('y')
            done(details,option)
            if op==0:
                demo.thank_you()
                break

        #option 3 to deposit cash
        elif option == 3:
            while 1:
                try:
                    Pay_in =  int(input('\n\nHOW MUCH WOULD YOU LIKE TO DEPOSIT:      '))
                except ValueError:
                     print("\n-------------PLEASE ENTER THE CORRECT AMOUNT IN THE MULTIPLE OF 100-----------------\n")
                if type(Pay_in)== int:
                    break
            balance=int(details[-2])
            balance = balance + Pay_in
            #print ('\n\nYOUR BALANCE IS:   ',balance)
            details[-2]=str(balance)
            restart = input('\n\nWOULD YOU LIKE TO GO BACK:     ')
            if restart in ('n','NO','no','N'):
                #print('Thank You')

                demo.thank_you()
                break
            done(details,option)
            copyFiles()
        elif option == 4:
            op_=option4(details)
            if op_==0:
                demo.thank_you()
                break
            copyFiles()
        elif option == 5:
            c=0
            while 1:
                pi=int(getpass.getpass("\n\nENTER YOUR PIN:          "))
                if pi==int(details[1]):
                    try:
                        ph=int(input("\n\nENTER YOUR NEW PHONE NUMBER:        "))
                    except ValueError:
                        print("\n\n-----------PLEASE ENTER YOUR PHONE NUMBER------------\n\n")
                    if len(str(ph))==10:
                        details[-1]=int(ph)
                        break
                    else:
                        print("\n\n---------------------NOT A VALID PHONE NUMBER-----------------\n\n")
                        continue

                c+=1
                if c == 3:
                    print("\n\n----------MORE NUMBER OF WRONG ATTEMPTS, CONTACT TO OUR NEAREST BRANCH-----------\n\n")
                    demo.thank_you()
                    break
            done(details,option)
            copyFiles()

        else:
            print("\n\n-----------------INVALID OPTION----------------\n")
            demo.thank_you()
            break




#option 4 for transfer of CASH
def option4(details):
    while 1:
        try:
            t_account=int(input("\n\nENTER THE TO ACCOUNT NUMBER:    "))
        except ValueError:
            print("\n\n-------PLEASE ENTER A PROPER ACCOUNT NUMBER---------------\n")
        if type(t_account) == int:
            break
    ac_d=accountExists(t_account)
    if ac_d==0:
        print("\n\n----------ACCOUNT DOESNOT EXIST---------\n\n----------PLEASE ENTER THE ACCOUNT NUMBER AGAIN----------\n")
        option4(details)
    else:
        #print("\n\n--PLEASE ENTER YOUR ACCOUNT NUMBER:    ")
        while 1:
            you=int(input("\n\nENTER YOUR ACCOUNT NUMBER:          "))
            if you != int(details[0]):
                continue

            you_p=int(getpass.getpass("\n\nPLEASE ENTER YOUR PIN AGAIN:         "))
            if you_p != int(details[1]):
                print("\n\nINVALID PIN :      ")
                continue
            break
        checkAmount(details,ac_d)
        writeAmount(ac_d,details)



#writing he final details to the original file
def writeAmount(ac_d,details):
    p=open("original.txt","r+")
    p1=open("dummy.txt","w+")
    ch=p.readline()
    while ch!='':
        d=ch.split()
        if int(d[0])!=int(details[0])  and int(d[0])!=int(ac_d[0]):
            p1.write(ch)
            #print(d[0],details[0],ac_d[0])
            #p1.write("\n")
        ch=p.readline()
    p.close()
    p1.close()
    p=open("dummy.txt","a")
    dd=' '.join(details)
    p.write(dd)
    p.write("\n")
    ac=' '.join(ac_d)
    p.write(ac)
    p.write("\n")
    p.close()

#this function is a part of option 4 to check whether the ammount entered is valid or not
def checkAmount(details,ac_d):
    amount_t=int(input("\n\nENTER AMOUNT TO TRANSFER:      "))
    if int(details[-2]) < amount_t:
        print("\n\nINSUFFICIENT FUNDS ")
        checkAmount(details,ac_d)
    else:
        ac_d[-2]=str(int(ac_d[-2]) + amount_t)
        details[-2]=str(int(details[-2])-amount_t)



#option 2 CASH WITHDRAWAL
def option2(details):
    try:
        withdrawl = int(input('\n\nHOW MUCH WOULD YOU LIKE TO WITHDRAW:     '))
    except ValueError:
        print("\n\nPLEASE ENTER CORRECT AMOUNT\n\n")
        option2(details)

    if withdrawl%100!=0:
        print('\n\n-------INVALID AMOUNT, PLEASE ENTER AMOUNT IN THE MULTIPLE OF 100---------\n')
        option2(details)
    elif  withdrawl > int(details[-2]):
        print("\n\n-------INSUFFICIENT FUNDS, PLEASE RE-ENTER YOUR AMOUNT------\n")
    elif withdrawl % 100==0 or withdrawl%1000==0:
        details[-2] = str(int(details[-2]) - withdrawl)
        #print ('\nYour Balance is now ',balance)
        restart = input('\n\nWOULD YOU LIKE TO GO BACK:    ')
        if restart in ('n','NO','no','N'):
            #print('Thank You')
            #demo.thank_you()
            return 0

    elif withdrawl == 0:
        option2(details)

start()
