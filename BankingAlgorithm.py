from tkinter import *
from functools import partial
import threading, time, random
import time
from tkinter import messagebox
import os

# window
tkWindow = Tk()
tkWindow.geometry('2000x2000')
tkWindow.title('Banker Algorithm')

# label
NumberOfTheProcess = Label(tkWindow, text="Enter The Number Of The Process")
# entry for user input
NameOfTheProcess = Label(tkWindow, text="Enter The Name Of The Process")
NumberOfResource = Label(tkWindow, text="Enter The Number of resource")
NameOfResource = Label(tkWindow, text="Enter The name of resource")
AllocatedValue = Label(tkWindow, text="Enter the allocated value")
# MaximumNeeded = Label(tkWindow, text="Enter the Maximum needed value by the process")
# AvailableResource = Label(tkWindow, text="Enter the allocated value")

class color:
    # This is decoration class
    Greeen = '\033[92m'
    Reed = '\033[91m'
    Bolld = '\033[1m'
    Ennd = '\033[0m'


my_mutex = threading.Lock()


class thread_one(threading.Thread):  # Thread creation class
    def run(self):
        global my_mutex
        print(color.Bolld + color.Greeen + "The  thread is now sleeping\n" + color.Ennd)
        time.sleep(3)
        print(color.Bolld + color.Reed + "Thread is finished" + color.Ennd)
        my_mutex.release()


abe = Entry(tkWindow)

b = Entry(tkWindow)
c = Entry(tkWindow)
d = Entry(tkWindow)
e = Entry(tkWindow)
# f = Entry(tkWindow)
# g = Entry(tkWindow)
# h = Entry(tkWindow)
NumberOfTheProcess.grid(row=0, column=0)
abe.grid(row=0, column=1)

NameOfTheProcess.grid(row=2, column=0)
b.grid(row=2, column=1)

NumberOfResource.grid(row=4, column=0)
c.grid(row=4, column=1)

NameOfResource.grid(row=6, column=0)
d.grid(row=6, column=1)

# AllocatedValue.grid(row=0,column=2)
# e.grid(row=0,column=3)
#
# MaximumNeeded.grid(row=1,column=2)
# f.grid(row=1,column=3)
#
# AvailableResource.grid(row=2,column=2)
# g.grid(row=2,column=3)



def submit_button():
    m = int(abe.get())
    Processes = b.get().strip().split()
    n = int(c.get())
    Resources = d.get().strip().split()
    print(m, Processes, n, Resources)
    messagebox.showinfo("Continue in terminal ")
    Allocated_Value = []  # The array will store the allocated value
    MaxValue = []  # The array will store the MAximum value
    Need_Value = []  # The array will store the Needed value


    for i in range(m):
        print("For process ", Processes[i], "=>")
        Allocated_Value.append(list(map(int, input().strip().split())))


    print("Enter the Maximum needed value by the process")
    for j in range(m):
        print("For process ", Processes[j], "=>")
        MaxValue.append(list(map(int, input().strip().split())))
    print("-------------------------------------------------------------------")

    print("Enter the available resource")
    AvailableValue = list(map(int, input().strip().split()))
    AvailableCopy = AvailableValue[:]

    for j in range(m):
        print("For process ", Processes[j], "=>")
        MaxValue.append(list(map(int, input().strip().split())))
    print("-------------------------------------------------------------------")

    print("Enter the available resource")
    AvailableValue = list(map(int, input().strip().split()))
    AvailableCopy = AvailableValue[:]

    for i in range(m):
        a = []
        for j in range(n):
            a.append(MaxValue[i][j] - Allocated_Value[i][j])
        Need_Value.append(a)

    NeedCopy = Need_Value[:]


    def Executed():  # This will check for the checking of safe class

        Unable = []
        Out = 1
        for i in range(n):
            Inspect_Value = 0
            for j in range(m):
                Inspect_Value += Allocated_Value[j][i]
            Inspect_Value += AvailableValue[i]
            CheckPoint = 1
            for k in range(m):
                if (MaxValue[k][i] > Inspect_Value):
                    CheckPoint = 0
                    Unable.append(Processes[k])
                    break
            if (CheckPoint == 0):
                Out = 0
        if Out:
            return Unable, 1
        else:
            return Unable, 0


    Unable, Inspect_Value = Executed()
    if (Inspect_Value == 0):
        print("There is no Safe sequence  ")
        print(*Unable, " Process can't be executed")
    else:
        Safe_Sequence = []
        while (Inspect_Value and len(Safe_Sequence) < m):
            for i in range(len(Need_Value)):
                if Processes[i] not in Safe_Sequence:
                    CheckPoint = 1
                    for z in range(n):
                        if (Need_Value[i][z] > AvailableValue[z]):
                            CheckPoint = 0
                    if CheckPoint:

                        for z in range(n):
                            AvailableValue[z] += Allocated_Value[i][z]
                        Safe_Sequence.append(Processes[i])
        print("Safe sequence is =>")
        messagebox.showinfo(*Safe_Sequence)
        print(*Safe_Sequence, sep=" ")
        print("\n\n")

    NewAvailable = AvailableCopy
    if Inspect_Value == 1:

        for i in range(len(Safe_Sequence)):  # after the safe sequence is done this will execute process using mutex lock
            my_mutex.acquire()

            t1 = thread_one()
            t1.start()
            AllocatedCopy = Allocated_Value[i]

            print("\nProcess", Safe_Sequence[i], ":")
            j = Processes.index(Safe_Sequence[i])
            print("    Allocated     =>", Allocated_Value[i])
            print("    Available     =>", NewAvailable)
            print("    Need          =>", NeedCopy[j])
            time.sleep(1)
            print("    Resource Allocated!  ")
            time.sleep(1)
            print("    Process Code Running..")
            time.sleep(1)
            print("    Process Code Completed...\n    Process Releasing Resource...\n ")
            time.sleep(1)
            print("    Resource Released!")
            for i in range(len(Resources)):
                NewAvailable[i] = AllocatedCopy[i] + NewAvailable[i]
            time.sleep(1)
            print("    New Available =>", NewAvailable)
            print("\n\n")
            time.sleep(2)

    # main loop
# ButtonA= Button(tkWindow, text="Submit")
# ButtonA.grid(row=20, column=4)
submitButton = Button(tkWindow, text="Submit", command=submit_button)
submitButton.grid(row=20, column=1)
# place label, entry, and button in grid


tkWindow.mainloop()

