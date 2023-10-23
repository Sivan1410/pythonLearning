
# Open a text file in write mode
file_name = "my_text_file.txt"

# You can use 'w' for writing (will overwrite the file if it already exists)
# or 'a' for appending (will create the file if it doesn't exist or append to an existing file)
with open(file_name, 'w') as file:
    # Write some text to the file
    file.write("Hello, this is a text file.\n")
    file.write("This is another line in the file.\n")

