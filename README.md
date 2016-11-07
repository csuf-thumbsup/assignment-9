# assignment-9
Given the following CFG and the LR Parsing table. Write a program to trace the following input strings:

  1) (i+i)*i$
  
  2) (i*)$
  
# Results from Main.py 
    Parsing String #1:  (i+i)*i$
    match: 0	stack: ['0', '(', '4']
    match: 4	stack: ['0', '(', '4', 'i', '5']
    match: 10	stack: ['0', '(', '4', 'E', '10', '+', '6']
    match: 6	stack: ['0', '(', '4', 'E', '10', '+', '6', 'i', '5']
    match: 10	stack: ['0', '(', '4', 'E', '10', ')', '15']
    match: 2	stack: ['0', 'T', '2', '*', '8']
    match: 8	stack: ['0', 'T', '2', '*', '8', 'i', '5']
    Your string IS valid for the given language!: (i+i)*i$

    Parsing String #2:  (i*)$
    match: 0	stack: ['0', '(', '4']
    match: 4	stack: ['0', '(', '4', 'i', '5']
    match: 2	stack: ['0', '(', '4', 'T', '2', '*', '8']
    Your string is NOT valid for the given language!: (i*)$
