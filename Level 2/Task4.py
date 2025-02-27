# Task 4: Fibonacci Sequence - Write a Python function that generates the Fibonacci sequence up to a given number of terms. The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.

n=int(input("enter the term: "))

res=[0,1]

for i in range(2,n):

    res.append(res[-1]+res[-2])

print(res)
