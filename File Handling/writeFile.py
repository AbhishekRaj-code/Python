#Using try-except block to handle potential file errors
#Using 'with' statement to open a file in append text mode
try:
    with open('output.txt', 'at') as file:
        file.write(input("Enter text to write to the file: ") + '\n')
        print("Data successfully written to the file.")

        #Appending additional content to the file
        while True:
            content = input("Give additional text to append to the file (or Press ENTER to stop): ")
            if content == '':
                break
            else:
                file.write(content + '\n')
                print("Data successfully appended to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    #Reading and displaying the final content of the file
    print("Final Content of the file")
    with open('output.txt', 'rt') as file:
        lines = file.readlines()
    
        for line in lines:
            print(line)    # Printing each line from the file