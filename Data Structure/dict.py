#Defining a dictionary to store student names and their corresponding scores
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "Derick": 88
}

#Printing all student names
for student in students:
    print(f"{student}")

#Taking input from the user for a student's name
name = input("Enter the student's name: ")
#Retrieving and printing the score for the given student name
score = students.get(name, "Student not found")
print(f"{name}'s score: {score}")   

