# Defining main function
def main():
    
    
    terms = int(input("Enter terms : "))

    #first two terms
    f1=0
    f2=1
    index = 0
    test_str = ''
    
    print("\n")
    print('First n Fibonacci numbers:')
    while index < terms:
            if(len(test_str) == 0):
             test_str = str(f1)
             
            else:
             test_str = test_str + ',' + str(f1)
             
            nxt = f1 + f2
            f1 = f2
            f2 = nxt
            index = index+1
        
    print(test_str)
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()