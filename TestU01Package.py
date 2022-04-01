from genericpath import exists
import subprocess

def main():
    choice = 0
    exitCondition = ["q", "Q"]
    batteryName = ""
    print("Welcome to the TestU01 package")
    print("------------------------------")
    while (choice not in exitCondition):
        print("Enter 1 for SmallCrush test battery")
        print("Enter 2 for Crush test battery")
        print("Enter 3 for BigCrush test battery")
        print("Enter 4 for Rabbit test battery")
        print("Enter 5 for Alphabit test battery")
        print("Enter 6 for BlockAlphabit test battery")
        print("Enter 7 for pseudoDIEHARD test battery")
        print("Enter 8 for NIST test battery")
        print("Enter Q to quit")
        
        choice = input()
        
        if choice == "1":
            batteryName = "SmallCrushFile.c"
        if choice == "2":
            batteryName = "CrushFile.c"
        if choice == "3":
            batteryName = "BigCrushFile.c"
        if choice == "4":
            batteryName = "RabbitFile.c"
        if choice == "5":
            batteryName = "AlphabitFile.c"
        if choice == "6":
            batteryName = "BlockAlphabitFile.c"
        if choice == "7":
            batteryName = "pseudoDIEHARDFile.c"
        if choice == "8":
            batteryName = "NISTFile.c"
        if choice == "Q":
            break
        if choice == "q":
            break
        
        if batteryName != "":
            print("Please type the file name including full file path and extension (if the file is in the same directory as 'TestU01Package.py', you only need to enter the file name and extension)")
            fileName = input()
            if exists(fileName):
                print("---------Start---------")
                subprocess.call(["gcc", batteryName, "-ltestu01", "-lprobdist", "-lmylib", "-lm"])
                subprocess.call(["./a.out",  fileName])
                print("----------End----------")
                print()
                batteryName = ""
                fileName = ""
            else:
                print("Invalid file name")

if __name__ == "__main__":
    main()
