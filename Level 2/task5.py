# Task 5: File Manipulation - Write a Python program that reads a text file and counts the occurrences of each word in the file. Display the results in alphabetical order along with their respective counts.

f = open("Level 2/file.txt",'r')

text = f.read().lower()

words = text.split()

word_dict={}

for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


for word in sorted(word_dict):
    print(word,"-",word_dict[word])
