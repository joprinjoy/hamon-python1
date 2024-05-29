from sys import argv
script,filename = argv
#ARI = 0
def ari():
    #opening and reading file
    target = open(filename,'r')
    indata = target.read()

    #saving the no of words, characters(.split split string into substrings)
    word_count = len(indata.split())
    char_count = len(indata)

    #Saving the no of sentences
    #fullstop count
    fulstop = indata.count(".")
    #count of ?
    qm = indata.count("?")
    #count of !
    excl = indata.count("!")
    #adding all 
    sent_count = fulstop+qm+excl

    #Calculating with Formula
    ARI = (4.71*(char_count / word_count)) + (0.5*(word_count/sent_count))-21.43
    print(f"Automated Readability Index for {filename} : {ARI}")
    
    #formating a string for printing result
    suit="Suitable for {}"

    #Checking the grade
    if ARI <2:
         print(suit.format("Kindergarten"))
    elif ARI < 3 :
         print(suit.format("GRADE 1"))
    elif ARI < 4 :
         print(suit.format("GRADE 2"))
    elif ARI < 5 :
         print(suit.format("GRADE 3"))
    elif ARI < 6 :
         print(suit.format("GRADE 4"))
    elif ARI < 7 :
         print(suit.format(" GRADE 5"))
    elif ARI < 8 :    
         print(suit.format("GRADE 6"))
    elif ARI < 9 :
         print(suit.format("GRADE 7"))
    elif ARI < 10 :
         print(suit.format("GRADE 8"))
    elif ARI < 11 :
         print(suit.format("GRADE 9"))
    elif ARI < 12 :
         print(suit.format("GRADE 10"))
    elif ARI < 13 :
         print(suit.format("GRADE 11"))
    elif ARI < 14 :
         print(suit.format("GRADE 12"))
    elif ARI > 14 :
         print(suit.format("COLLEGE STUDENTS"))
    else:
         print("Invalid")


if __name__=="__main__":
     ari()
