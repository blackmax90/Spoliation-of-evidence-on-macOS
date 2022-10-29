from Modules.TEFT_Define import *

def run_tool():
    os.system('cls')
    f = Figlet(font='big')
    print(colored(f.renderText('< TEFT >\n             - MS OFFICE'), 'magenta'))
    print(colored("Trace Evidence Forensics Tool\n\n", 'blue'))

def select_input():
    while True:
        print("|################## I.N.P.U.T #################|")
        print("|   1. Live System                             |")
        print("|   2. Disk Image                              |")
        print("|   3. Directory (or for test)                 |")
        print("|##############################################|")
        print()
        inputType = input("Select Input: ")
        if int(inputType) == 1 or int(inputType) == 3:
            return inputType
        elif int(inputType) == 2:
            print()
            print("> In development...")
            print("> Please select another input type\n")
        else:
            print()
            print("> Please type correct number (1~3)\n")

def type_source_path():
    while True:
        print("|################## P.A.T.H ###################|")
        print("|    ex) /Users/[Account]/Desktop/source       |")
        print("|    ex) D:/source                             |")
        print("|    ex) For test, type 'SampleDataSet'        |")
        print("|##############################################|")
        print()
        inputType = input("Please type the source folder (Absolute Path): ")
        if os.path.isdir(inputType) == True:
            return inputType
        else:
            print()
            print("> Please type correct path\n")

def type_user_name(sourceFolder):
    while True:
        print("|################## U.S.E.R ###################|")
        print("|    ex) max                                   |")
        print("|    ex) david                                 |")
        print("|    ex) x (if you don't know the user name)   |")
        print("|##############################################|")
        print()
        UserName = input("Please type the user name: ")
        if os.path.isdir(sourceFolder+'/Users/'+UserName) == True:
            return UserName
        elif UserName == 'x':
            return UserName
        else:
            print()
            print("> Please type correct user name or type 'x'\n")