import time
class BalanceExceptionError(Exception):
    pass
class AttemptExceptionError(Exception):
    pass

attempts = 1
def withdraw():
    global attempts
    save_pin = 8877
    balance = 10000
    pin = int(input("enter your pin = "))
    if pin == save_pin:
        try:
            amt = float(input("enter your amt = "))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceExceptionError("insufficient balance ")
            balance = balance - amt
            print("remind balance is ", balance)
        except Exception as object:
            print(object)
    else:
        ans = input("wrong pin, do you want to contiune again (y/n) ")
        if ans.lower()=="y":
            attempts += 1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("too many attempts your account is blocked for an hour ")
            except Exception as object:
                print(object)
                time.sleep(120)
            else:
                withdraw()
        else:
            print("thank you ")
            return
withdraw()
