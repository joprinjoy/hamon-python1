#function to check the string is Palindrome or not

def palindrome(s):
    revs = s[::-1]      #reversing the string

    if revs==s:         #checking whether the user input string and reversed string are same
         print(s," is PALINDROME")
    else:
         print(s," is NOT PALINDROME")


if __name__=="__main__":
     s=input("enter the string:")
     palindrome(s)