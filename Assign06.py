'''
Title: Assignment 06
Dev: Elaine Xu
Date: Nov 07, 2018
ChangeLog: N/A
'''

#-----Data-----
strChoice = None #user choice input
obj = None #file handler
line = None #reads line by line
dicRow = None #a row of dictionary
lst = [] #list of all data

#-----Processing-----
class DataOperation(object):
    @staticmethod
    def openfile():
        '''Step 1 read from a text file into dictionary'''
        obj = open("Todo.txt","r")
        for line in obj:
            line = line.strip() #to remove "\n"
            (key, val) = line.split(',')
            dicRow = {key:val}
            #dic[key] = val
            lst.append(dicRow) #add dict row into a list

    @staticmethod
    def menu():
        '''Step 2 display a menu of choice'''
        print("Menu of Options")
        print("Choose 1 to Show current data")
        print("Choose 2 to Add a new item")
        print("Choose 3 to Remove an existing item")
        print("Choose 4 to Save date to file")
        print("Choose 5 to Exit Program")

    @staticmethod
    def showdata():
        '''Step 3 show the current items in the table'''
        print(lst)

    @staticmethod
    def additem():
        '''Step 4 add a new item to the list/table'''
        task = input("Add a task: ")
        priority = input("Its priority level: ")
        newRow = {task:priority}
        lst.append(newRow)
        print(lst)

    @staticmethod
    def removeitem():
        '''Step 5 remove a new item to the list/table'''
        print(lst)
        x = int(input("Enter the index number of the item you want to remove (1 to n): "))
        del lst[x-1]
        print("Item has been removed:")
        print(lst)

    @staticmethod
    def savedata():
        '''Step 6 save tasks to the text file'''
        obj = open("Todo.txt", "w")
        for line in lst:
            for key, val in line.items():
                obj.write(key + "," + val + "\n")
        obj.close()
        print("Data have been saved.")

#-----Presentation------
DataOperation.openfile()
print(lst)
while True:
    DataOperation.menu()
    strChoice = input("Enter your choice: ")
    if strChoice.strip() == "1":
        DataOperation.showdata()
    elif strChoice.strip() == "2":
        DataOperation.additem()
    elif strChoice.strip() == "3":
        DataOperation.removeitem()
    elif strChoice.strip() == "4":
        DataOperation.savedata()
    # Step 7 exit program
    elif strChoice.strip() == "5": break
    else: print("Invalid input, try again.")