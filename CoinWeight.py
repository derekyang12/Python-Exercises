penny = 2.5
dime = 2.268
nickel = 5
quater = 5.67
fiftyCents = 11.34
dollar = 8
def findCoin():
    print("Enter the following in weights: ")
    pennyQ = float(input("Penny: "))
    nickelQ = float(input("Nickel: "))
    dimeQ = float(input("Dime: "))
    quaterQ = float(input("Quarter: "))
    fiftyQ = float(input("Fifty Cents: "))
    dollarQ = float(input("Dollar: "))
    amountPenny = pennyQ / penny
    amountNickel = nickelQ / nickel
    amountDime = dimeQ / dime
    amountQuarter = quaterQ / quater
    amountFifty = fiftyQ / fiftyCents
    amountDollar = dollarQ / dollar
    return int(amountPenny), int(amountNickel), int(amountDime), int(amountQuarter), int(amountFifty), int(amountDollar)
def calculateCoin():
    print(findCoin())


calculateCoin()
again = input("")
