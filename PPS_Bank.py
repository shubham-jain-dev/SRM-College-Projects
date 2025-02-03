#PROGRAM TO RUN AN ATM MACHINE OF A BANK
print("Welcome to SRM BANK")
p = int(input("Enter your 4 digit PIN number: "))
m = 25000
if(p == 1234):
	print("1-Withdraw Money")
	print("2-Balance Enquiry")
	print("3-Fast Cash")
	c = int(input("Please Choose Transactions: "))
	if c == 1:
    	w = int(input("Enter Amount to Withdraw: "))
    	if (w < m ):
        	print("Please take your Amount:", w)
        	print("Balance Left:",m-w)
    	else:
        	print("Insufficient Balance")
	elif(c==2):
    	print("Your Available Balance is : ",m)
	elif (c == 3):
    	print("1->5,000")
    	print("2->10,000")
    	print("3->15,000")
    	print("4->20,000")
    	f = int(input("Enter Fast Cash Option: "))
    	if (f =   	= 1 and 5000 < m):
        	print("Please take Cash 5000")
        	print("Balance Left",m - 5000)
    	elif (f == 2 and 10000 < m):
        	print("Please take Cash 10000")
        	print("Balance Left",m - 10000)
    	elif (f == 3 and 15000 < m):
        	print("Please take Cash 15000")
        	print("Balance Left",m - 15000)
    	elif (f == 4 and 20000 < m):
        	print("Please take Cash 20000")
        	print("Balance Left",m - 20000)
    	else:
        	print("Invalid Fast Cash option")
	else:
        	print("Invalid Choice")
else:
	print("Wrong PIN Number")
