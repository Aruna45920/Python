def power_of(a,b):
    c=a**b
    print(c)


def get_quotient(numerator,denominator):
    
    '''This function calculates the quotient of numerator divided by denominator'''
    quotient=numerator/denominator
    print(quotient)
    
if __name__ == "__main__":
    power_of(2,5)
    get_quotient(100,2)

    # why i am writing this __name__ condition is it will check wheather it is executed as  a script file or imported as module if it
    # is executed as a script file only it will execute other wise it won't

    def main():
        power_of(2,5)
        get_quotient(100,2)
if __name__ == "__main__":
    main()

    
       
