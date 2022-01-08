def Get(text, error = "Invalid input"):
    while True:
        returnValue = input(text)
        if(len(returnValue) > 0):
            return returnValue
        print(error)