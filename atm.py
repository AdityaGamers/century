class Atm(object):
    def __init__(self,card , pin) :
        self.cardnumber=card
        self.pin=pin
    def cashwithdrawal(self):
        print("CASH HAS BEEN WITHDRAWEN")
    def checkbalance(self):
        print("balance is 400000")
ATM=Atm(1223433,4444)
ATM.cashwithdrawal()
ATM.checkbalance()

        