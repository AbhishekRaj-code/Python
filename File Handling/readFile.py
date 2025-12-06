
# Using try-except block to handle potential file not found error
# Using 'with' statement to open a file in read text mode
try:
    with open('sample.txt', 'rt') as file:
        content = file.readlines()
        #Each line from the file is stored in the 'content' list
        
except FileNotFoundError:
    print("The file was not found.")
else:

# Printing each line from the file
    for line in content:
        print(line)
