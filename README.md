# assignment-9
Given the following CFG and the LR Parsing table. Write a program to trace the following input strings:

  1) (i+i)*i$
  
  2) (i*)$
  
# Results from Main.py 
      Parsing String #1:  (i+i)*i$
      Match!	popped_char: 0	read_char: (	stack: ['0', '(', '4']
      Match!	popped_char: 4	read_char: i	stack: ['0', '(', '4', 'i', '5']
      Match!	popped_char: 10	read_char: +	stack: ['0', '(', '4', 'E', '10', '+', '6']
      Match!	popped_char: 6	read_char: i	stack: ['0', '(', '4', 'E', '10', '+', '6', 'i', '5']
      Match!	popped_char: 10	read_char: )	stack: ['0', '(', '4', 'E', '10', ')', '15']
      Match!	popped_char: 2	read_char: *	stack: ['0', 'T', '2', '*', '8']
      Match!	popped_char: 8	read_char: i	stack: ['0', 'T', '2', '*', '8', 'i', '5']
      Your string IS valid for the given language!: (i+i)*i$

      Parsing String #2:  (i*)$
      Match!	popped_char: 0	read_char: (	stack: ['0', '(', '4']
      Match!	popped_char: 4	read_char: i	stack: ['0', '(', '4', 'i', '5']
      Match!	popped_char: 2	read_char: *	stack: ['0', '(', '4', 'T', '2', '*', '8']
      Fail!	popped_char: 8	read_char: )	stack: ['0', '(', '4', 'T', '2', '*']
      Your string is NOT valid for the given language!: (i*)$
