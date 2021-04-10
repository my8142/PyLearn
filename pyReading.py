
# READING FILES WITH OPEN

File1 = open("/resources/data/Example2.txt","r")   # use "r" to read ; "w" to write (overwrites all the existing data in the file) ; "a" to append.
File1.name      # displays the name
File1.mode      # displays the mode
File1.close()   # to close the object

exmp2 = '/resources/data/Example2.txt'
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


with open("Example1.txt","r") as File1:            # using with open allows to immediately close the file out of the brackets
    file_stuff = File1.read()
    print(file_stuff)

print(File1.closed)                                 
print(file_stuff)


with open("Example1.txt","r") as File1:
    file_stuff = File1.readlines()                 # readlines() : read the lines separated by \n
    print(file_stuff)


with open("Example1.txt","r") as File1:
    file_stuff = File1.readline()                  # readline() : read the first line
    print(file_stuff)
    file_stuff = File1.readline()                  # readline() : read the second line and so on
    print(file_stuff)


with open("Example1.txt","r") as File1:
    for line in File1:                             # uese a loop to print every line
        print(line)


with open("Example1.txt","r") as File1:
    file_stuff = File1.readlines(4)                # read the first 4 characters of the first line
    print(file_stuff)




# Writing files with Open

File1 = open("/resources/data/Example2.txt","w")   # use "w" to write ; "r" to read ; "a" to append

with open("Example1.txt","w") as File1:
    File1.write("This is line A")


Lines = ["This is line A\n","This is line B\n","This is line C\n"]      # Write each element in a list to a file with a for loop
with open("/resources/data/Example2.txt","w") as File1:
    for line in Lines:
        File1.write(line)

with open("File1.txt","r") as listWriteFile:                # verify the file is written
    print(listWriteFile.read())


with open("/resources/data/Example2.txt","a") as File1:     # append a new line
    File1.write("this is a new line)



# It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines. Luckily we can access the file in the following modes:

#   r+ : Reading and writing. Cannot truncate the file.
#   w+ : Writing and reading. Truncates the file.
#   a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.


#Opening the file in **w** is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows.
#Whereas opening the file in **a** is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text. <br>
#It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -

#-   <code>.tell()</code> - returns the current position in bytes
#-   <code>.seek(offset,from)</code> - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


#Finally, a note on the difference between **w+** and **r+**. Both of these modes allow access to read and write methods, However opening a file in **w+** overwrites it and deletes all existing data. <br>
#To work with a file on existing data, use **r+** and **a+**. While using **r+**, it can be useful to add a <code>.truncate()</code> method at the end of your data. This will reduce the file to your data and delete everything that follows. <br>
#In the following code block, Run the code as it is first and then run it with the <code>.truncate()</code>.

with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())


# Copy a file to a new one

with open("Example1.txt","r") as readfile:
    with open("Example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)
            
with open('Example3.txt','r') as testwritefile:             # Verify if the copy is successfully executed
    print(testwritefile.read())
