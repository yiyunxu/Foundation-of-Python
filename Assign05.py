'''
Title: Assignment 05
Dev: Elaine Xu
Date: Oct 31, 2018
ChangeLog: N/A
'''
#Step 1 read from a text file into dictionary
obj = open("Todo.txt","r")
lst = []
for line in obj:
    line = line.strip() #to remove "\n"
    (key, val) = line.split(',')
    dicRow = {key:val}
    #dic[key] = val
    lst.append(dicRow) #add dict row into a list
print(lst)

#Step 2 display a menu of choice
while True:
    print("Menu of Options")
    print("Choose 1 to Show current data")
    print("Choose 2 to Add a new item")
    print("Choose 3 to Remove an existing item")
    print("Choose 4 to Save date to file")
    print("Choose 5 to Exit Program")
    strChoice = input("Enter your choice: ")

    #Step 3 show the current items in the table
    if strChoice.strip() == "1":
        print(lst)

    #Step 4 add a new item to the list/table
    elif strChoice.strip() == "2":
        task = input("Add a task: ")
        priority = input("Its priority level: ")
        newRow = {task:priority}
        lst.append(newRow)

    #Step 5 remove a new item to the list/table
    elif strChoice.strip() == "3":
        print(lst)
        x = int(input("Enter the index number of the item you want to remove (1 to n): "))
        del lst[x-1]
        print("Item has been removed:")
        print(lst)

    #Step 6 save tasks to the text file
    elif strChoice.strip() == "4":
        obj = open("Todo.txt", "w")
        for line in lst:
            for key, val in line.items():
                obj.write(key + "," + val + "\n")
        obj.close()
        print("Data have been saved.")

    #Step 7 exit program
    elif strChoice.strip() == "5": break
    else: print("Invalid input, try again.")