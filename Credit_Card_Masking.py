CardNo = input("Enter Your Credit Card Number::")

def Maskify(CardNo):
    newCard = ''
    if (len(CardNo) > 4):
        newCard += '#' * (len(CardNo) - 4) + CardNo[-4:]
    else:
        return CardNo
    return newCard


print(Maskify(CardNo))
