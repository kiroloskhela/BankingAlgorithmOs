# BankingAlgorithmOs

 Banker Algorithm
==================

    This is a program that implements the Banker's algorithm for resource allocation.

    Usage
    -----
    1. Enter the number of processes.
    2. Enter the names of the processes.
    3. Enter the number of resources.
    4. Enter the names of the resources.
    5. Enter the allocated values for each process and resource.
    6. Enter the maximum needed values for each process and resource.
    7. Enter the available resources.
    8. Click the Submit button to execute the algorithm.

    Requirements
    ------------
    - Python 3.x
    - tkinter library

    How it works
    ------------
    1. The program takes user input for the number of processes, names of processes, number of resources, and names of resources.
    2. The program then takes user input for the allocated values and maximum needed values for each process and resource.
    3. The program calculates the needed values based on the allocated and maximum values.
    4. The program checks for a safe sequence using the Banker's algorithm.
    5. If a safe sequence is found, the program executes the processes in the safe sequence.
    6. The program simulates the execution of each process by printing messages and releasing resources.
    7. After executing all processes, the program displays the new available resources.
    
    example of inputs
    -----------------
    Enter The Number Of The Process : 3
    Enter The Name Of The Process : A B C (You must write them sebartly)
    Enter The Number of resourc : 2
    Enter The name of resource : X Y (You must write them sebartly)
    
    For process  a =>
    0 1 0
    For process  b =>
    2 0 0
    For process  c =>
    3 0 2
    Enter the Maximum needed value by the process
    For process  a =>
    7 5 3
    For process  b =>
    3 2 2
    For process  c =>
    9 0 2
    -------------------------------------------------------------------
    Enter the available resource
    3 3 2
    There is no Safe sequence  
    c a  Process can't be executed

  

    """
