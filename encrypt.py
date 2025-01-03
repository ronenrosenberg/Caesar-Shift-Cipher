#this program uses the simple caesar cipher (kinda) to encrypt and decrypt messages

#this list assigns each different letter (plus space) a different value. !!!IMPORTANT!!! Using any values out of this list in your message will result in an error
encList = {
        "A" : 1, "a" : 28,
        "B" : 2, "b" : 29,
        "C" : 3, "c" : 30,
        "D" : 4, "d" : 31,
        "E" : 5, "e" : 32,
        "F" : 6, "f" : 33,
        "G" : 7, "g" : 34,
        "H" : 8, "h" : 35,
        "I" : 9, "i" : 36,
        "J" : 10, "j" : 37,
        "K" : 11, "k" : 38,
        "L" : 12, "l" : 39,
        "M" : 13, "m" : 40,
        "N" : 14, "n" : 41,
        "O" : 15, "o" : 42,
        "P" : 16, "p" : 43,
        "Q" : 17, "q" : 44,
        "R" : 18, "r" : 45,
        "S" : 19, "s" : 46,
        "T" : 20, "t" : 47,
        "U" : 21, "u" : 48,
        "V" : 22, "v" : 49,
        "W" : 23, "w" : 50,
        "X" : 24, "x" : 51,
        "Y" : 25, "y" : 52,
        "Z" : 26, "z" : 53,
        " " : 27
        }

#the key decides how many times the letters should be rotated (neg back, pos forward)
encKey = input("What is your encrytion key?(" + str(-(len(encList))) + " --- " + str(len(encList)) + ") ")
encKey = int(encKey)

#this just asks if the user is encrypting or decryting their, if they are decryting the program just does the inverse operation used to encrypt
deORen = input("Would you like to encrypt or decrypt a message(e/d)?")

#the plaintext or encoded message goes here
message = input("what is your message?")

if deORen == "encrypt" or deORen == "e":
    #where the final nanswer is stored
    encAnswer = ("")
    for letters in message:

        #creates the encryted value(but is still in numerical form)
        modVal = (encList[letters] + encKey)

        #used to make sure value can't go above len(encKey) or below 0. Basically if it goes above/below those values this part wraps their value back around to one/highest value of dict
        if modVal > len(encList):
            modVal = modVal - len(encList) # actives if value greater or equal to 1 more that highest value in dict
        elif modVal <= 0:
            modVal = modVal + len(encList) # actives if 0 or below
        
        # ^^^ if no wrap-around is needed this code is ignored
        
        #this is the part that turns each number back into a character
        for k, v in encList.items():
            if v == modVal:
                encAnswer += k
    
    #prints final answer
    print("your message encrypted is:" + (encAnswer))

elif deORen == "decrypt" or deORen == "d":
    #stores unrotated values
    deMessage = []
    
    #stores rotated values
    rotatedDe = []
    
    #container used for rotation protection
    almostDone = []
    #final decoded message
    finalDe = ""
    
    #this code converts the letters back into numbers, but they have not been rotated yet
    for letters in message:
        for k, v in encList.items():
            if k == letters:
                deMessage.append(v)
    
    #rotates values
    for things in deMessage:
        rotatedDe.append(things - encKey)
    
    for numbers in rotatedDe:
        #used to make sure value can't go above len(rotatedDe) or below 0. Basically if it goes above/below those values this part wraps their value back around to one/highest value of dict
        if numbers > len(encList):
            almostDone.append(numbers - len(encList)) # actives if value greater or equal to 1 more that highest value in dict
        elif numbers < 1:
            almostDone.append(numbers + len(encList)) # actives if 0 or below
        else:
            almostDone.append(numbers)
    
    for things in almostDone:
        for k, v in encList.items():
            if v == things:
                finalDe += k
    print(("Your message decryped is:") + finalDe)
else:
    print("error")

#ver 1.0 is done!