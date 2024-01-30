

def lcm(num1,num2):
    if num1 > num2:
        greater=num1
    else:
        greater=num2

    while True:
        if greater%num1==0 and greater%num2==0:
            lcm=greater
            return lcm
            break
        greater=greater+1  

def gcd(num1,num2): 
    gcd_value = (num1*num2) /lcm(num1,num2)
    print(gcd_value)

gcd(20,15)


