#This program opens file using read funtion
#initializing variable using file I/O read
with open('examplefile.txt', 'r') as file:
    content = file.read()
print(f"Here was your file{content.strip()}")

#another method to read the file breaks in three category
#read whole, read whole by list, read line by line

#read whole txt 
with open('examplefile.txt', 'r') as file:
    content = file.read()

#read by list
with open('examplefile.txt', 'r') as file:
    lines = file.readlines()

#read line by line
with open('examplefile.txt', 'r') as file:
    for lines in file:
        print(lines)

