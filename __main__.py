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

import os, shutil
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
    try:
        value = int(input(label))
    except (KeyboardInterrupt, SystemExit):
        print(LANGUAGE.GAME_CLOSE)
        exit()
    except:
        return False
    return value

def header():
    clear()
    print("\n")
    tab = int((WIDTH - len(LANGUAGE.LOGO[0][0])) / 2)
    for col in range(2):
        for lin in range(5):
            print(" " * tab, LANGUAGE.LOGO[col][lin])
        tab = int((WIDTH - len(LANGUAGE.LOGO[1][0])) / 2)
        print("\n")
    print("\n")

def body(table):
    col = 0
    lin = 0
    tab = int((WIDTH - len(_[0]) * 3)/2)
    result = str(" " * tab)
    jp = '\n' + ' ' * tab
    vb = '|'
    hb = '-' * 3 * len(_[0])
    while(lin < 3):
        while(col < 3):
            aux = 0
            while(aux < 5):
                for add in range(3):
                    if(table[col][lin + add] == 'x'):
                        result += X[aux] + (vb if 0 <= add < 2 else '')
                    elif(table[col][lin + add] == 'o'):
                        result += O[aux] + (vb if 0 <= add < 2 else '')
                    else:
                        result += _[0] + (vb if 0 <= add < 2 else '')
                result += jp if aux < 4 else ''
                aux += 1
            result += jp + (hb if 0 <= col < 2 else '' + jp)
            col += 1
            result += jp
        lin += 1
    print(result)

def check(table):
    for aux in range(3):
        col = (table[aux][0] == table[aux][1] and table[aux][0] == table[aux][2]) and table[aux][0] != ' '
        lin = (table[0][aux] == table[1][aux] and table[0][aux] == table[2][aux]) and table[0][aux] != ' '
        ver = (table[0][0] == table[1][1] == table[2][2] or table[0][2] == table[1][1] == table[2][0]) and table[1][1] != ' '
        if(col or lin or ver):
            return True
        else:
            return False

def run():
    endgame = False
    count = 1
    msg = str()
    while(count <= 10):
        header()
        body(TABLE)

        if(count % 2 == 0):
             print(LANGUAGE.PLAYING_X)
        else:
             print(LANGUAGE.PLAYING_O)
             
        print(msg)
        msg = str()

        if(endgame):
            exit()

        if(count < 10):
            lin = validIntInput(LANGUAGE.LABEL_INPUT_ROW) - 1
            col = validIntInput(LANGUAGE.LABEL_INPUT_COL) - 1
              
            if (lin >= 0 and lin < 3 and col >= 0 and col < 3):
                if(TABLE[lin][col] == ' '):
                    if(count % 2 == 0):
                        TABLE[lin][col] = 'x'
                    else:
                        TABLE[lin][col] = 'o'

                    if(check(TABLE)):
                        if(count % 2 == 0):
                             msg = LANGUAGE.WINNER_X
                        else:
                             msg = LANGUAGE.WINNER_O
                        endgame = True
                    count += 1
                else:
                    msg = LANGUAGE.OVERWRITE
            else:
                msg = LANGUAGE.INVALID_POSITION
        else:
            msg = LANGUAGE.GAME_OVER
            endgame = True

run()

