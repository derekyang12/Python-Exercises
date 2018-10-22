
def breakRule():
    firstSide = input("Enter one side: ")
    secondSide = input("Enter the other side:")
    thirdSide = input("Enter last side: ")

    if (firstSide > secondSide) and (firstSide > thirdSide):
        hypotenuse = firstSide
        oneSide = thirdSide
        twoSide = secondSide
    elif(secondSide > thirdSide) and (secondSide > firstSide):
        hypotenuse = secondSide
        oneSide = firstSide
        twoSide = thirdSide
    elif (thirdSide > secondSide) and (thirdSide > firstSide):
        hypotenuse = thirdSide
        oneSide = firstSide
        twoSide = secondSide
    oneSide = int(oneSide)
    twoSide = int(twoSide)
    hypotenuse = int(hypotenuse)
    if ((oneSide * oneSide) + (twoSide * twoSide) == (hypotenuse * hypotenuse)):
        print ("It is a pythagorean triple")
    else:
        print ("It is not a pythagorean triple")
breakRule()

again = input("Do you want to check again? (N/Y)")
while again == "Y":
    breakRule()
    again = input("Do you want to check again? (N/Y)")
