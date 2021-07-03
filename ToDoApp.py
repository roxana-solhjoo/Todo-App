# encoding=utf8
from main import *

if len(sys.argv) == 1:
     UsageInfo()

elif len(sys.argv) == 2:
      check = "√"
      ToDoList()


if    len(sys.argv)== 3 and sys.argv[1] == "-a":
       addToList()

if    len(sys.argv)== 3 and sys.argv[1] == "-r":
       removeTask()

if len(sys.argv) == 3 and sys.argv[1] == "-c":
    completed()
