#nokte: in mashin hesab faghat ta 2 adad suport mikonad
def hesab():
    l=input('''
khob hala mikhay che amaliaty angam bedy??
baray jam bezan '+'
baray tafrigh bezan '-'
baray zarb bezan '*'
baray taghsim bezan '/'
== ''')
    number1=float(input('Enter Number ='))
    number2=float(input('Enter Number ='))
    if l=='+':
        print(number1+number2)
    elif l=='-':
        print(number1-number2)
    elif l=='*':
        print(number1*number2)
    elif l=='/':
        print(number1/number2)
    else:
        print('''
lotfan az gozine ha entekhab kon
gozineha:
zarb:*
taghsim:/
jam:+
tafrigh:-''')
        
    again()
        
def again():
    m=input('''
aya dost darid baz hesab konid
age are bezan 'Y'
age na bezan 'N'
== ''')
    if m.upper()=='Y':
        hesab()
    elif m.upper()=='N':
        print('mamnoon az entekhabeton va khodangahdar')
    else:
        again()
hesab()
