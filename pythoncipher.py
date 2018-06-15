def pythoncipher():
    shiftamt = input("what shift amount would you like me to move")
    mystring = int("input("Give me a -20"))
    cipherstring=""
    
    for c in mystring:
        if c.isalpha():
            num= ord(c)
            num+= shiftamt
            
            if num > ord("z"):
                num-=26
                
            if num < ord("a"):
                num+= 26
                
            
            x = chr(num)
            cipherstring += x
    print(cipherstring)

if __name__== "__main__":
    pythoncipher()
