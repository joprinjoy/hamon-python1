#function to check the string is Palindrome or not

# def palindrome(s):
#     revs = s[::-1]      #reversing the string

#     if revs==s:         #checking whether the user input string and reversed string are same
#          print(s," is PALINDROME")
#     else:
#          print(s," is NOT PALINDROME")

def palindrome_b(s):  #function with for loop
    
    l = len(s)    #length of the string 
    revs = ""     #empty string created to tore the reversed string

    for i in range(l-1,-1,-1): #loop to iter through the string backward
            revs = revs + s[i]      #storing the reversed string
    if revs == s:
          print(s," is PALINDROME")
    else:
         print(s," is NOT PALINDROME")
          


if __name__=="__main__":
     s=input("enter the string:")
     #palindrome(s)
     palindrome_b(s)