def fizzbizz(n):
        print("hello")
            
        for i in range(1,n+1):
            if(i%3==0 or i%5==0):
                if(i%5==0):
                    if(i%15==0):
                         print("fizzbizz")
                    else:
                        print("bizz")
                else:
                    print("fizz")
            else:
                print(i)

if __name__=="__main__":
     n=int(input("enter the number:"))
     fizzbizz(n)