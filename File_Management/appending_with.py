with open("File_Management\output.txt","a") as file:
    file.write("\nLearning best practices")

# The with statement automatically closes the file after the block of code is executed, even if an error occurs.
# This is a best practice for file handling in Python, as it ensures that resources are properly managed and prevents potential memory leaks or file corruption