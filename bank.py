import sys


def get_balance():
    with open('vault.txt','r') as f:
        data = f.readline()
        return int(data)

def deposit(amount):
    balance = get_balance()
    with open('vault.txt','w') as f:
        new_balance = balance+amount
        f.write(str(new_balance))
        print("Deposited amount "+str(amount)+"$"+" succesfully")
    

def withdraw(amount):
    balance = get_balance()
    
    with open('vault.txt','w') as f:
        if balance < amount:
            f.write(str(balance))
            #print("Insufficient balance")
            return False, 'Withdraw failed, Insufficient balance'

        else:
            new_balance = balance-amount
            f.write(str(new_balance))
            return True
            #print("withdrawn amount "+str(amount)+"$"+" succesfully")


try: 

    if sys.argv[1]== "-balance":
        print("Your account balance is "+ str(get_balance())+"$")

    if sys.argv[1]== "-deposit":
        amount = sys.argv[2].split('$')[0]
        amount = int(amount)
        deposit(amount)
        print("Your account balance is "+ str(get_balance())+"$")
        
    if sys.argv[1]== "-withdraw":
        amount = sys.argv[2].split('$')[0]
        amount = int(amount)
        result = withdraw(amount)
        if result[0]== False:
            print(result[1])

        print("Your account balance is "+ str(get_balance())+"$")

except:
    msg = '''
        Usage:
        bank -[balance | deposit | withdraw]

'''
    print(msg)


