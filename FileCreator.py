runTime = int(input("How many files would you like to create?: "))



def CreateFiles(NumFiles):
    NameFile = input("What is the name you want the file to have?: ")
    WriteFile = input("What would you like to write in the file?: ")
    
    with open(NameFile, "a") as Create:
        Create.write(WriteFile)
    for i in range(NumFiles):    
        NameFile = input("Input Name of File again[E to exit]: ")
        if NameFile in ("e", "E"):
            print("Now Exiting...")
            exit()
        with open(NameFile, "a") as NewCreate:
            NewCreate.write(WriteFile)

CreateFiles(runTime)
