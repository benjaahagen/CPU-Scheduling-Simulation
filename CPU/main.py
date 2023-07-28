#!/usr/bin/python
import openpyxl
# from Process import Process
from FCFS import FCFS
from SJF import SJF
from Priority import Priority
from RoundRobin import RoundRobin
import sys
words = []
processes = list()
processesSJF = list()

wb = openpyxl.load_workbook(filename = 'cpu-scheduling.xlsx')
ws = wb.active
words = [list(row) for row in ws.iter_rows(max_col=4, values_only=True)][1:]
def menu():
    print("\nWhat algorithm you want to launch?")
    print('1. FCFS')
    print('2. SJF')
    print('3. Priority')
    print('4. Round Robin')
    print('5. End')
    z = int(input('(1-4):'))
    if z == 1:
        fcfs = FCFS(words)
        fcfs.run()
    elif z == 2:
        sjf = SJF(words)
        sjf.run()
    elif z == 3:
        pr = Priority(words)
        pr.run()
    elif z == 4:
        rr = RoundRobin(words)
        rr.run()
    elif z == 5:
        sys.exit()
    else:
        print("Wrong input")
        menu()

while(True):
    menu()