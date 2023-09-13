# This file adds a new file and is setup with the base requirements

# Creates the file
def create():
    # Prints the purpose of the code
    print("\n \n \nThis file adds a new file and is setup with the base requirements")


    # Base text for the file
# Name: <your name goes here – first and last minimum>
# <ProgramName>.py
#
# Problem: <Brief, one or two sentence description of the
# problem that this program solves, in your own
# words.>
# Certification of Authenticity:
# <include one of the following>
# I certify that this lab is entirely my own work.
# I certify that this lab is my own work, but I
# discussed it with: <Name(s)>


    # Asks for the programs name
    print("\nWhat is the name of the file (.py will be added)?")
    fileName = input("Name of program = ")

    # Asks for the users name
    print("\nWhat is your first and last name?")
    userName = input("Name = ")

    # Asks for the programs purpose
    print("\nWhat is the purpose of this program?\n(Start with: This program or similar)")
    purpose = input("Purpose = ")

    # Asks for the certification of the program
    print("\nYes or no. Did you discuss the code with others?")
    certi = input("Code discussed = ")
    certi.lower
    discussed = False

    # If the user did discuss with people then who
    if (certi == "yes"):
        discussed = True
        print("\nWho were the people you discussed with (separate names with a comma and space)?")
        peopleTalkedTo = input("\nNames = ")




    # Instantiates the new file
    newFile = None

    while (newFile == None):
        try: newFile = open(f"{fileName}.py", "x")
        except: "This file already exists"

    # Writes the base to the new file
    baseTextToWrite = ["## Imports:\n\n\n", f"# Name: {userName}\n#\n", f"# {fileName}.py\n#\n", f"# Problem: {purpose}\n#\n", f"# Certification of Authenticity:\n"]
    newFile.writelines(baseTextToWrite)
    
    # Sets the certification
    if (discussed == True):
        discussedText = [f"# I certify that this lab is my own work, but I\n", f"# discussed it with: {peopleTalkedTo}\n"]
        newFile.writelines(discussedText)
    else:
        newFile.write("# I certify that this lab is entirely my own work.\n")

    newFile.writelines(["\n\ndef main():\n",f"print({purpose})" "\t#(Write your cool code here)\n\n", "\t# This can be deleted\n", "\treturn\n", "\nmain()"])

    newFile.close


    

create()