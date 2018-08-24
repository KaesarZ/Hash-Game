"""
     __  __     ______     ______     __  __    
    /\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \    
    \ \  __ \  \ \  __ \  \ \___  \  \ \  __ \   
     \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  
      \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/  
     ______     ______     __    __     ______   
    /\  ___\   /\  __ \   /\ \"-./  \   /\  ___\ 
    \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\  
     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\
      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/

    __license__ = "GPL"
    __version__ = "1.0.0"
    __status__ = "Production"
    __author__ = "Júlio César"
    __copyright__ = "Copyright 2018, Júlio César"
    __email__ = jccb2@cin.ufpe.br
"""

import os, shutil, time
from en_us import EN_US
from pt_br import PT_BR

LANGUAGE = EN_US()
#LANGUAGE = PT_BR()

X, O, _ = LANGUAGE.X, LANGUAGE.O, LANGUAGE._     
WIDTH, HEIGHT = shutil.get_terminal_size()
TABLE = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

def clear():
     os.system("cls" if os.name=='nt' else 'clear')

def validIntInput(label):
    verticalMargin = int((WIDTH - len(_[0]) * 3)/2)
    try:
        result = int(input(' ' * verticalMargin + label))
    except (KeyboardInterrupt, SystemExit):
        print(LANGUAGE.GAME_CLOSE)
        menu()
    except:
        return False
    return result

def printTextCenter(text):
    print(' ' * int((WIDTH - len(text))/2) + text)

def header():
    clear()
    horizontalMargin = int((HEIGHT - 39)/2)
    verticalMargin = int((WIDTH - len(LANGUAGE.LOGO[0][0])) / 2)
    print("\n" * horizontalMargin)
    for col in range(2):
        for row in range(5):
            print(" " * verticalMargin, LANGUAGE.LOGO[col][row])
        verticalMargin = int((WIDTH - len(LANGUAGE.LOGO[1][0])) / 2)
        print("\n")

def body(table):
    verticalMargin = int((WIDTH - len(_[0]) * 3)/2)
    result = str(" " * verticalMargin)
    jumpLine = '\n' + ' ' * verticalMargin
    verticalGrid = '|'
    horizontalGrid = '-' * 3 * len(_[0])

    col = 0
    row = 0
    while(row < 3):
        while(col < 3):
            aux = 0
            while(aux < 5):
                for add in range(3):
                    if(table[col][row + add] == 'x'):
                        result += X[aux] + (verticalGrid if 0 <= add < 2 else '')
                    elif(table[col][row + add] == 'o'):
                        result += O[aux] + (verticalGrid if 0 <= add < 2 else '')
                    else:
                        result += _[0] + (verticalGrid if 0 <= add < 2 else '')
                result += jumpLine if aux < 4 else ''
                aux += 1
            result += jumpLine + (horizontalGrid if 0 <= col < 2 else '' + jumpLine)
            col += 1
            result += jumpLine
        row += 1
    print(result)

def check(table):
    for aux in range(3):
        col = (table[aux][0] == table[aux][1] == table[aux][2]) and table[aux][0] != ' '
        row = (table[0][aux] == table[1][aux] == table[2][aux]) and table[0][aux] != ' '
        ver = (table[0][0] == table[1][1] == table[2][2] or table[0][2] == table[1][1] == table[2][0]) and table[1][1] != ' '
        if(col or row or ver):
            return True
        else:
            return False

def start():
    TABLE = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    endgame = False
    count = 1
    message = str()
    while(count <= 10):
        header()
        body(TABLE)

        if(count % 2 == 0):
             printTextCenter(LANGUAGE.PLAYING_X)
        else:
             printTextCenter(LANGUAGE.PLAYING_O)
             
        printTextCenter(message)
        message = str()

        if(endgame):
            time.sleep(5)
            menu()
        else:
            if(count < 10):
                row = validIntInput(LANGUAGE.LABEL_INPUT_ROW) - 1
                col = validIntInput(LANGUAGE.LABEL_INPUT_COL) - 1
                
                if (row >= 0 and row < 3 and col >= 0 and col < 3):
                    if(TABLE[row][col] == ' '):
                        if(count % 2 == 0):
                            TABLE[row][col] = 'x'
                        else:
                            TABLE[row][col] = 'o'
                        count += 1
                    else:
                        message = LANGUAGE.OVERWRITE
                else:
                    message = LANGUAGE.INVALID_POSITION
            else:
                message = LANGUAGE.GAME_OVER
                endgame = True

            if(check(TABLE)):
                if((count - 1) % 2 == 0):
                    message = LANGUAGE.WINNER_X
                else:
                    message = LANGUAGE.WINNER_O
                endgame = True

def menu(message = ''):
    header()
    print('\n' * 3)
    printTextCenter(' 1 - ' + LANGUAGE.MENU_GAME_START)
    print('\n' * 1)
    printTextCenter(' 2 - ' + LANGUAGE.MENU_INSTRUCTIONS)
    print('\n' * 1)
    printTextCenter(' 3 - ' + LANGUAGE.MENU_SETTINGS)
    print('\n' * 1)
    printTextCenter(' 4 - ' + LANGUAGE.MENU_ABOUT)
    print('\n' * 1)
    printTextCenter(' 5 - ' + LANGUAGE.MENU_EXIT)
    print('\n' * 3)
    printTextCenter(message)

    choose = validIntInput(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 1):
        start()
    elif(choose == 2):
        instruction()
    elif(choose == 3):
        settings()
    elif(choose == 4):
        about()
    elif(choose == 5):
        exit()
    else:
        menu(LANGUAGE.INVALID_COMMAND)
    
def settings(message = ''):
    global LANGUAGE
    header()
    print('\n' * 3)
    printTextCenter('1 - ' + LANGUAGE.SETTINGS_LANGUAGE + ': ' + LANGUAGE.SETTINGS_LANGUAGE_DEFAULT)
    print('\n' * 10)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 3)
    printTextCenter(message)

    choose = validIntInput(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 1):
        if(LANGUAGE.SETTINGS_LANGUAGE_DEFAULT != 'EN-US'):
            LANGUAGE = EN_US()
        else:
            LANGUAGE = PT_BR()
        settings()
    elif(choose == 5):
        menu()
    else:
        settings(LANGUAGE.INVALID_COMMAND)

def about(message = ''):
    header()
    print('\n' * 3)
    printTextCenter('ABOUT')
    print('\n' * 10)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 3)
    printTextCenter(message)

    choose = validIntInput(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 5):
        menu()
    else:
        about(LANGUAGE.INVALID_COMMAND)

def instruction(message = ''):
    header()
    print('\n' * 3)
    printTextCenter('INSTRUCTION')
    print('\n' * 10)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 3)
    printTextCenter(message)

    choose = validIntInput(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 5):
        menu()
    else:
        instruction(LANGUAGE.INVALID_COMMAND)

menu()
#start()

