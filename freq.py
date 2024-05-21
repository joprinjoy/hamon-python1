mydict={}  #empty dictionary for storing the incoming

def freq(string):       #function  string recieved from user
    for x in string:    #itering through the string to take it as key
        if x != " ":      #ignoring whitespaces
            count = 0
            for z in string:    #itering for the count of charecters
                if z == x:      
                    count += 1
            mydict[x] = count
    print(mydict)



if __name__=="__main__":
    s=input("Enter the string")
    s=s.lower()     #converting all characters to lowercase
    freq(s)

