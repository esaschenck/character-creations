#this is the main code yayyy

print("Welcome to the cartoon character creator program originator -- or C3PO!")

print()
print("We're going to be taking a quiz today to create YOUR unique original character.")
print("Are you ready??")

def askReady():
 ready = (input("(Y/N) to begin:")).upper()
 
 if ready == 'Y':
     print("Great! Let's get started...")
 elif ready == 'N':
    print("Well, take your time...")
    print("...")
    print("How about now?")
    askReady()
 else:
    print("I didn't quite get that -- let's try again!")
    ready = askReady()

askReady()

