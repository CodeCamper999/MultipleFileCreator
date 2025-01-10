import random # importing the random module 
runTime = int(input("How many files would you like to create?: "))

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "I", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# Making a list of the Alphabet 
CustomizableFile = input("Would you like to add your custom edits to the file as in directory, name, etc...[Y/N]: ")
# Allowing user to pick if they was to make a custom file or let it automate 
    
def CreateFiles(NumFiles):

    if CustomizableFile in ("y", "Y"): # If the user inputs y or Y then run this program
        NameFile = input("Where would you like the file to be please add name aswell: ")
        WriteFile = input("What would you like to write in the file?: ")
        
        with open(NameFile, "a") as Create: # opening a new file and writing the name of the file the user wanted to create 
            Create.write(WriteFile)
            # wrote what the user wanted me to write in that file 
            
        for i in range(NumFiles):    
            # we will loop through this however many times the user would like 
            NameFile = input("Input Name of File again[E to exit]: ")
            print(i)
            
        if NameFile in ("e", "E"):
            print("Now Exiting...")
            exit()
       
    elif CustomizableFile in ("N", "n"):
        Original = input("What is a file name(don't put .txt or list the directory): ")
        directory = input("Custom Directory(\"C\")[C/D]? please press \"D\" to use default file save: ")
        GetDirectory = input("put in directory(DO NOT use / at the end): ")
        for i in range(runTime):
            getLetter = random.choice(Alphabet[0:])
            # we used random to choose a random letter to put at the end of the file
            
            if directory in ("C", "c"):
                
                with open(GetDirectory + "/" + Original + getLetter + ".txt", "a") as originalfile:
                    originalfile.write("New File in" + directory)
            elif directory in ("D", "d"):
                
                with open(Original + getLetter + ".txt", "a") as Create:
                    Create.write("this is our new file")
            # we concat the file name the user choose, the random letter, and the .txt inorder to make it a text file 
            
            print(i)
                
            
            
            
            

CreateFiles(runTime)
