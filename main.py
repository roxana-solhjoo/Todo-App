# encoding=utf8
import sys
import os


def UsageInfo():
      print ("$ todo" "\n"
           "Command Line Todo application" "\n"
           "=============================" "\n"
           "                             " "\n"
           "Command line arguments:" "\n"
           "   -l   Lists all the tasks" "\n"
           "   -a   Adds a new task" "\n"
           "   -r   Removes an task" "\n"
           "   -c   Completes an task""\n"
            )

def ToDoList():
    if sys.argv[1] == "-l":
        count = 1
        tasks= open('List_tasks.txt', 'r').readlines()
        filesize = os.path.getsize("List_tasks.txt")
        if filesize == 0:
         print("No todos for today! :)")
        else:
            print("$ todo -l" "\n")
            check = "√"
            for task in tasks:
                if check in task:
                    task = task.replace(check, "")
                    print(str(count) + " _ " + "[X] " + task)
                    count += 1
                else:
                    print(str(count) + " _ " + "[ ] " + task)
                    count += 1
    else:
        MissingIndex()

def MissingIndex():
    if sys.argv[1] == "-a":
         print("Unable to add: no task provided")
    elif  sys.argv[1] == "-c":
        print("Unable to check: no index provided")
    elif  sys.argv[1] == "-r":
        print("Unable to remove: no index provided")
    else:
        print("Unsupported argument")
        UsageInfo()

def addToList():
        value = str (sys.argv[2])
        contents = open('List_tasks.txt', 'r').readlines()
        filesize = os.path.getsize("List_tasks.txt")
        if filesize == 0:
            contents.append(value)
            AddTask = open("List_tasks.txt", "w")
            contents = "".join(contents)
            AddTask.write(contents)
            AddTask.close()
        else:
         contents.append("\n" + value)
         AddTask = open("List_tasks.txt", "w")
         contents = "".join(contents)
         AddTask.write(contents)
         AddTask.close()

def removeTask():
 try:
     index = int(sys.argv[2]) - 1
     text_file = open("List_tasks.txt", "r")
     lines = text_file.readlines()
     try:
      del lines[index]
     except:
       print("Unable to remove: index is out of bound")
     text_file = open("List_tasks.txt", "w")
     for line in lines:
          text_file.write(line)
     text_file.close()
 except:
    print("Unable to remove: index is not a number")


def showError():
     print("Unsupported argument")
     UsageInfo()


def completed():
 try:
     index = int(sys.argv[2]) - 1
     tasks = open("List_tasks.txt", "r").readlines()
     LenText = len(tasks)
     if index > LenText:
         print("Unable to check: index is out of bound ")
     else:
      for task in range(LenText):
           if task == index:
                 tasks[index] = "√" +  tasks[index]
                 text_file = open("List_tasks.txt", "w")
                 text_file.writelines(tasks)
                 text_file.close()
 except:
    print("Unable to check: index is not a number")

