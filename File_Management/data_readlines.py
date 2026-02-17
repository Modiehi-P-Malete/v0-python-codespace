file =open("File_Management\data.txt","r")
lines = file.readlines()
print(lines)
file.close()

#Output will be a list of all the lines in the file...each line will be an element in the list.