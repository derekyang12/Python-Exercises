counter = 99
while (counter > 1):
    print ("%d bottles of beer on the wall, %d bottles of beer." % (counter, counter))
    print ("Take one down and pass it around, %d bottles of beer on the wall." % (counter - 1))
    counter  = counter - 1
if (counter == 1):
    print ("%d bottle of beer on the wall, 1 bottle of beer." % counter)
    print ("Take one down and pass it around, no more bottles of beer on the wall.")
    print ("No more bottles of beer on the wall, no more bottles of beer. ")
    print ("Go to the store and buy some more, 99 bottles of beer on the wall.")


print (userInput())
input("")
