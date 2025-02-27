import re

'''
Task 1: String Reversal
Create a Python function that takes a string as input and returns the reverse of that string. For example, if the input is "hello", the function should return "olleh".
'''
def str_reverse(word):
    return word[::-1]

'''
Task 2: Temperature Conversion
Create a Python program that converts temperatures between Celsius and Fahrenheit. Prompt the user to enter a temperature value and the unit of measurement, and then display the converted temperature.
'''
def celsi_to_fahren(temp):
    return (temp*9/5)+32

def fahren_to_celsi(temp):
    return (temp-32)*5/9

'''
Task 3: Email Validator
Develop a Python function that validates whether a given string is a valid email address. Implement checks for the format, including the presence of an "@" symbol and a domain name
'''
def email_isvalid(email):
    return True if re.search("@+[a-z]+.com",email) else False    

'''
Task 4: Calculator Program
Create a Python program that acts as a basic calculator. It should prompt the user to enter two numbers and an operator (+, -, *, /, %), and then display the result of the operation.
'''
def calculate(num1,num2,sym):
    res = 0
    if sym=='+':
        res = num1+num2
    elif sym=='-':
        res = num1-num2
    elif sym=='*':
        res = num1*num2
    elif sym=='/':
        res = num1/num2
    elif sym=='%':
        res = num1%num2
    if res!=0:
        print("\n-> {} {} {} = {}".format(num1, sym, num2, res))
    else:
        print("Invalid Operator - {}".format(sym))

'''
Task 5: Palindrome Checker
Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward (e.g., "madam" or "racecar").
'''
def ispalin(text):
    if str_reverse(text)==text:
        return True
    else:
        return False


if __name__=="__main__":
    print("\n\t\tWelcome \nThis is Cognifyz Internship Task - 1")
    while 1:
        print('''
            1 - String Reversal
            2 - Temperature Conversion
            3 - Email Validator
            4 - Calculator Program
            5 - Palindrome Checker
            0 - Exit
    ''')
        x=int(input("Enter the number for process: "))
        if x==1:
            txt=input("Enter a word to reverse: ")
            print("The Reversed word is:",str_reverse(txt))

        elif x==2:
            t=int(input("Enter the Temperature: "))
            s=input("Enter the Unit (C - celsius, F - Fahrenheit): ").upper()
            if s=="C":
                print("The {}°C is {}°F".format(t,celsi_to_fahren(t)))
            elif s=="F":
                print("The {}°F is {}°C".format(t,fahren_to_celsi(t)))

        elif x==3:
            e=input("Enter the gmail id for validation: ")
            if email_isvalid(e):
                print("'{}' is valid".format(e))
            else:
                print("'{}' is not valid".format(e))

        elif x==4:
            a=int(input("Enter a Number1: "))
            b=int(input("Enter a Number2: "))
            s=input("Enter an Operator(+, -, *, /, %): ")
            calculate(a,b,s)

        elif x==5:
            txt=input("Enter a word to check palindrome: ")
            if ispalin(txt.lower()):
                print("'{}' is a Palindrome String".format(txt.title()))
            else:
                print("'{}' is not a Palindrome String".format(txt.title()))

        else:
            print("\n\t\tThank you")
            break
