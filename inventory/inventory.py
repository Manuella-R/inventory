import fileinput  # Importing fileinput module to allow in-place editing of files

def mainmenu():
    # Display the main menu for inventory management
    print("************************")
    print(" INVEN MANAGEMENT MENU  ")
    print("************************")
    print("(1) Add new item to inventory")
    print("(2) Remove item from inventory")
    print("(3) Update inventory")
    print("(4) Search item in inventory")
    print("(5) Print inventory report")
    print("(0) Quit")
    
    # Get user input for menu option
    Op = int(input("Enter Option: "))
    selectitems(Op)  # Call function to handle the selected option

def selectitems(Op):
    # Call the appropriate function based on user input
    if Op == 1:
        addinvent()  # Add new item
    elif Op == 2:
        removeinvent()  # Remove an existing item
    elif Op == 3:
        updateinvent()  # Update item details
    elif Op == 4:
        searchinvent()  # Search for an item
    elif Op == 5:
        printinvent()  # Print all inventory items
    elif Op == 0:
        exit()  # Exit the program
    else:
        print("INVALID!!!!!!")

def addinvent():
    # Add a new item to the inventory
    with open('Inventory.txt', 'a') as InFile:
        # Open file in append mode
        print("Adding Inventory")
        print("****************")
        item_desc = input("Enter name of item: ")  # Get item name from user
        item_qty = input("Enter the quantity of the item: ")  # Get item quantity from user
        InFile.write(item_desc + '\n')  # Write item name to file
        InFile.write(item_qty + '\n')  # Write item quantity to file

    # Prompt user to continue or exit
    Op = int(input('Enter 1 to continue or 0 to exit: '))
    if Op == 1:
        mainmenu()  # Show main menu again
    else:
        exit()  # Exit the program

def removeinvent():
    # Remove an item from the inventory
    print("Removing Inventory")
    print("****************")
    item_desc = input("Enter item name to remove it from inventory: ")  # Get item name to remove

    lines = []
    with open('Inventory.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    with open('Inventory.txt', 'w') as file:
        # Open file in write mode
        skip = False
        for line in lines:
            if item_desc in line:
                # If item description is found, set skip to True
                skip = True
            elif skip:
                # If skip is True, skip the next line (item quantity) and reset skip
                skip = False
            else:
                file.write(line)  # Write the line back to the file if not skipped

    # Prompt user to continue or exit
    Op = int(input('Enter 1 to continue or 0 to exit: '))
    if Op == 1:
        mainmenu()  # Show main menu again
    else:
        exit()  # Exit the program

def updateinvent():
    # Update the quantity of an existing item
    print("Updating Inventory")
    print("*******************")
    item_desc = input("Enter name of item to update: ")  # Get item name to update
    item_qty = input("Enter the updated quantity of the item: ")  # Get new quantity from user
    
    lines = []
    with open('Inventory.txt', 'r') as f:
        # Read all lines from the file
        lines = f.readlines()
    
    with open('Inventory.txt', 'w') as f:
        # Open file in write mode
        for i, line in enumerate(lines):
            if item_desc in line:
                # If item description is found, update its quantity
                next_line = lines[i+1].strip() if i+1 < len(lines) else ""
                f.write(item_desc + '\n')  # Write item name back to file
                f.write(item_qty + '\n')  # Write updated quantity to file
            else:
                f.write(line)  # Write unchanged lines back to file
    
    # Prompt user to continue or exit
    Op = int(input('Enter 1 to continue or 0 to exit: '))
    if Op == 1:
        mainmenu()  # Show main menu again
    else:
        exit()  # Exit the program

def searchinvent():
    # Search for an item in the inventory
    print("Searching Inventory")
    print("*******************")
    item_desc = input("Enter name of item: ")  # Get item name to search
    
    with open('Inventory.txt', 'r') as f:
        # Read all lines from the file
        search = f.readlines()
    
    found = False
    for i, line in enumerate(search):
        if item_desc in line:
            # If item description is found, print the item and its quantity
            print('Item:    ', line.strip())
            if i+1 < len(search):
                print('Quantity: ', search[i+1].strip())
                found = True
            print('**************')

    if not found:
        # If item was not found in the file
        print("Item not found.")
    
    # Prompt user to continue or exit
    Op = int(input('Enter 1 to continue or 0 to exit: '))
    if Op == 1:
        mainmenu()  # Show main menu again
    else:
        exit()  # Exit the program

def printinvent():
    # Print all items in the inventory
    print('Current Inventory')
    print('*****************')

    with open('Inventory.txt', 'r') as InFile:
        # Open file in read mode
        while True:
            item_desc = InFile.readline()  # Read item description
            if not item_desc:
                break  # Exit loop if end of file is reached
            item_qty = InFile.readline()  # Read item quantity
            print('Item:     ', item_desc.strip())  # Print item description
            print('Quantity: ', item_qty.strip())  # Print item quantity

    # Prompt user to continue or exit
    Op = int(input('Enter 1 to continue or 0 to exit: '))
    if Op == 1:
        mainmenu()  # Show main menu again
    else:
        exit()  # Exit the program

if __name__ == "__main__":
    mainmenu()  # Start the program by showing the main menu
