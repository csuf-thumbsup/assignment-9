def run_parser(parsing_table, cfg_table, input_str):
    str_list = list(input_str)

    stack = ['0'] # init stack to 0

    i = 0 # index for str_list
    read_char = str_list[0] # init read_char to first char

    while(True):

        # pop the stack on every iteration and store into popped_char
        popped_char = stack.pop()

        # find [popped_char, read_char] in our parsing_table
        temp_parsed_value = parsing_table[popped_char][read_char]

        # our checks and balances
        # if our value is S#
        if temp_parsed_value[0] == 'S':
            # append our 3 values to the stack
            stack.extend([popped_char, read_char, temp_parsed_value[1:]]) # temp_parsed_value[1:] accounts for digits like 14 (use of string slicing)

            # printing our matches for every instance of a read/accepted char
            print('match: ' + popped_char + '\tstack: ' + stack.__str__())

            i += 1 # increment our index for str_list
            read_char = str_list[i] # update read_char

        # if our value is R#
        elif temp_parsed_value[0] == 'R':
            # first we append our popped_char
            stack.append(popped_char)

            # get the rule defined by its index (temp_parsed_value[1]) e.g R8 => Rule #8 in CFG
            rule_dict = cfg_table[ int(temp_parsed_value[1])-1 ] # convert to int and subtract by 1 to account for 0-indexing

            # pop the stack amount of 2*Length of the RHS
            for x in range(0, 2*rule_dict['length']):
                stack.pop()

            # update read_char to the LHS of our rule
            read_char = rule_dict['lhs']

        elif temp_parsed_value == 'undef':
            print('Your string is NOT valid for the given language!:', input_str)
            return
        elif temp_parsed_value == 'ACCEPT':
            print('Your string IS valid for the given language!:', input_str)
            return

        # else our value is a number
        else:
            # append our 3 values to the stack
            stack.extend([popped_char, read_char, temp_parsed_value])

            # update read_char to the current char
            read_char = str_list[i]

if __name__ == '__main__':
    # Data for Problem #1

    parsing_table = {
        '0': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': '1',
              'T': '2',
              'F': '3'
              },
        '1': {'i': 'undef',
              '+': 'S6',
              '-': 'S7',
              '*': 'undef',
              '/': 'undef',
              '(': 'undef',
              ')': 'undef',
              '$': 'ACCEPT',
              'E': 'undef',
              'T': 'undef',
              'F': 'undef'
              },
        '2': {'i': 'undef',
              '+': 'R3',
              '-': 'R3',
              '*': 'S8',
              '/': 'S9',
              '(': 'undef',
              ')': 'R3',
              '$': 'R3',
              'E': 'R3',
              'T': 'undef',
              'F': 'undef'
              },
        '3': {'i': 'undef',
              '+': 'R6',
              '-': 'R6',
              '*': 'R6',
              '/': 'R6',
              '(': 'undef',
              ')': 'R6',
              '$': 'R6',
              'E': 'undef',
              'T': 'undef',
              'F': 'undef'
              },
        '4': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': '10',
              'T': '2',
              'F': '3'
              },
        '5': {'i': 'undef',
              '+': 'R8',
              '-': 'R8',
              '*': 'R8',
              '/': 'R8',
              '(': 'undef',
              ')': 'R8',
              '$': 'R8',
              'E': 'undef',
              'T': 'undef',
              'F': 'undef'
              },
        '6': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': 'undef',
              'T': '11',
              'F': '3'
              },
        '7': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': 'undef',
              'T': '12',
              'F': '3'
              },
        '8': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': 'undef',
              'T': 'undef',
              'F': '13'
              },
        '9': {'i': 'S5',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'S4',
              ')': 'undef',
              '$': 'undef',
              'E': 'undef',
              'T': 'undef',
              'F': '14'
              },
        '10': {'i': 'undef',
              '+': 'S6',
              '-': 'S7',
              '*': 'undef',
              '/': 'undef',
              '(': 'undef',
              ')': 'S15',
              '$': 'undef',
              'E': 'undef',
              'T': 'undef',
              'F': 'undef'
              },
        '11': {'i': 'undef',
              '+': 'R1',
              '-': 'R1',
              '*': 'S8',
              '/': 'S9',
              '(': 'undef',
              ')': 'R1',
              '$': 'R1',
              'E': 'undef',
              'T': 'undef',
              'F': 'undef'
              },
        '12': {'i': 'undef',
               '+': 'R2',
               '-': 'R2',
               '*': 'S8',
               '/': 'S9',
               '(': 'undef',
               ')': 'R2',
               '$': 'R2',
               'E': 'undef',
               'T': 'undef',
               'F': 'undef'
               },
        '13': {'i': 'undef',
               '+': 'R4',
               '-': 'R4',
               '*': 'S4',
               '/': 'S4',
               '(': 'undef',
               ')': 'R4',
               '$': 'R4',
               'E': 'undef',
               'T': 'undef',
               'F': 'undef'
               },
        '14': {'i': 'undef',
               '+': 'R5',
               '-': 'R5',
               '*': 'R5',
               '/': 'R5',
               '(': 'undef',
               ')': 'R5',
               '$': 'R5',
               'E': 'undef',
               'T': 'undef',
               'F': 'undef'
               },
        '15': {'i': 'undef',
               '+': 'R7',
               '-': 'R7',
               '*': 'R7',
               '/': 'R7',
               '(': 'undef',
               ')': 'R7',
               '$': 'R7',
               'E': 'undef',
               'T': 'undef',
               'F': 'undef'
               },
    }

    cfg_table = [
        {'lhs': 'E', 'length': 3}, # 1) E -> E+T
        {'lhs': 'E', 'length': 3}, # 2) E -> E-T
        {'lhs': 'E', 'length': 1}, # 3) E -> T
        {'lhs': 'T', 'length': 3}, # 4) T -> T*F
        {'lhs': 'T', 'length': 3}, # 5) T -> T/F
        {'lhs': 'T', 'length': 1}, # 6) T -> F
        {'lhs': 'F', 'length': 3}, # 7) F -> (E)
        {'lhs': 'F', 'length': 1}, # 8) F -> i
    ]


    input_str_1 = '(i+i)*i$'
    input_str_2 = '(i*)$'

    print('Parsing String #1: ', input_str_1)
    run_parser(parsing_table, cfg_table, input_str_1)

    print('\nParsing String #2: ', input_str_2)
    run_parser(parsing_table, cfg_table, input_str_2)

'''
Sample Output:

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
'''