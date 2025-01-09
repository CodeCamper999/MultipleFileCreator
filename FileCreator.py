import random
runTime = int(input("How many files would you like to create?: "))

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "I", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

CustomizableFile = input("Would you like to add your custom edits to the file as in directory, name, etc...[Y/N]: ")

    
def CreateFiles(NumFiles):

    if CustomizableFile in ("y", "Y"):
        NameFile = input("Where would you like the file to be please add name aswell: ")
        WriteFile = input("What would you like to write in the file?: ")
        
        with open(NameFile, "a") as Create:
            Create.write(WriteFile)
            
        for i in range(NumFiles):    
            NameFile = input("Input Name of File again[E to exit]: ")
            print(i)
            
        if NameFile in ("e", "E"):
            print("Now Exiting...")
            exit()
       
    elif CustomizableFile in ("N", "n"):
        Original = input("What is a file name(don't put .txt or list the directory)")
        for i in range(runTime):
            getLetter = random.choice(Alphabet[0:])
            print(getLetter)
            
            with open(Original + getLetter + ".txt", "a") as Create:
                Create.write("this is our new file")
                
            
            
            
            

CreateFiles(runTime)
