#x is the number youre checking for perfect  square.


def sqr():
    n = 0
    x =  input()
    x = int(x)
    
    if x >= 0:                      
        while n*n < x:              
            n = n +1
            print(n,'-',n*n)
            
        if n * n != x:
            print(x, "is not a Perfect Square.")
            sqr()
        else:
            print(x,"is a Perfect Square.")
            sqr()
            
    else:
        print("not a positive number")
        sqr()
        
sqr()

BO = n
