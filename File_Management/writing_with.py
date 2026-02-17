with open("File_Management\output.txt","w") as file:
    file.write("Hello Python\n")
    file.write("Using with statement")

# The with statement automatically closes the file after the block of code is executed, even if an error occurs.
# This is a best practice for file handling in Python, as it ensures that resources are properly managed and prevents potential memory leaks or file corruption.