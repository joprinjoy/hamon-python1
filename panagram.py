def panagram(s):                    #function to check panagram
    chk="abcdefghijklmnopqrstuvwxyz"   #predefined alphabets
    s=s.lower()
    for i in chk:                   #itering through alphabets
        if i not in s:                  #comparing alphabet with string entered
            print("not panagram")
            break                          #exiting if any alphabet not found
    else:
        print("panagram")



if __name__=="__main__":
     s=str(input("enter the string:"))
     panagram(s)