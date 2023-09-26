# This file adds a new file and is setup with the base requirements

# Creates the file
def create():
    # Prints the purpose of the code
    print("\n \n \nThis file adds a new file and is setup with the base requirements")


    """Base text for the file
Name: <your name goes here – first and last minimum>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the
problem that this program solves, in your own
words.>
Certification of Authenticity:
<include one of the following>
I certify that this lab is entirely my own work.
I certify that this lab is my own work, but I
discussed it with: <Name(s)>"""


    # Asks for the programs name
    fileName = input("\nWhat is the name of the file (.py will be added)? \nName of program = ")

    # Asks for the users name
    userName = input("\nWhat is your first and last name? \nName = ")

    # Asks for the programs purpose
    purpose = input("\nWhat is the purpose of this program?\n(Start with: This program or similar) \nPurpose = ")

    # Asks for the certification of the program
    certi = input("\nYes or no. Did you discuss the code with others? \nCode discussed = ")
    certi.lower
    discussed = False

    # If the user did discuss with people then who
    if (certi == "yes"):
        discussed = True
        peopleTalkedTo = input("\nWho were the people you discussed with (separate names with a comma and space)?\nNames = ")

    # Asks if user wants to import anything
    pickingImports = True

    addImports = input("\nDo you wish to import libraries? (yes or no) \nImport = ")
    addImports.lower

    imports = []

    # If user does want to import things user puts what to import
    if (addImports == "yes"):
        while (pickingImports == True):
            try: importType = int(input("\nType 1 to do (import NAME)\nType 2 to do (import NAME as NEWNAME)\nType 3 to do (from NAME import *)\nType 4 to END"))
            except: print("\nThat's not a valid import type")

            if (importType == 1):
                name = str(input("What is the name of the library?\nName = "))
                imports.append(f"import {name}\n")

            elif (importType == 2):
                name = str(input("What is the name of the library?\nName = "))
                newName = str(input("What is the new name for the library?\nName = "))
                imports.append(f"import {name} as {newName}\n")

            elif (importType == 3):
                name = str(input("What is the name of the library?\nName = "))
                imports.append(f"from {name} import *\n")

            elif (importType == 4):
                pickingImports = False


            

    # Instantiates the new file
    newFile = None

    while (newFile == None):

        # Opens a new file if it doesnt already exist
        #try: newFile = open(f"{fileName}.py", "x")
        #except: "This file already exists"

        # Opens a possible new file but can also overwrite an already existing file
        newFile = open(f"{fileName}.py", "w")
    

    # Writes the base to the new file
    importTextToWrite = ["## Imports\n"]
    importTextToWrite.extend(imports)
    importTextToWrite.append("\n\n\n")
    newFile.writelines(importTextToWrite)

    baseTextToWrite = [f"'''\nName: {userName}\n\n", f"{fileName}.py\n\n", f"Problem: {purpose}\n\n", f"Certification of Authenticity:\n"]
    newFile.writelines(baseTextToWrite)
    
    # Sets the certification
    if (discussed == True):
        discussedText = [f"I certify that this lab is my own work, but I\n", f"discussed it with: {peopleTalkedTo}\n"]
        newFile.writelines(discussedText)
    else:
        newFile.write("I certify that this lab is entirely my own work.\n")

    newFile.write("'''\n")

    newFile.writelines(["\n\ndef main():\n", "\t# Prints the purpose of the code\n", f"\tprint('{purpose}')\n\n", "\t#(Write your cool code here)\n\n", "\t# This can be deleted\n", "\treturn\n", "\nmain()"])

    newFile.close


    

create()