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

    License: GPL
    Version: 1.0.0
    Status: Production
    Author: Júlio César
    Copyright: Copyright 2018, Júlio César
    Email: jccb2@cin.ufpe.br
"""

import os, shutil, time
from en_us import EN_US
from pt_br import PT_BR

LANGUAGE = EN_US()
#LANGUAGE = PT_BR()

IMGX, IMGO, IMG_ = LANGUAGE.X, LANGUAGE.O, LANGUAGE._     
WIDTH, HEIGHT = shutil.get_terminal_size()
BOARD = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

def clearTerminal():
    '''
        Method: clearTerminal
        Description: clears the characters in the terminal
        Param: @void
        Return: @void
    '''
    os.system("cls" if os.name=='nt' else 'clear')

def inputValidInt(label):
    '''
        Method: inputValidInt
        Description: captures entries of valid integers
        Param: @string
        Return: @void
    '''
    verticalMargin = int((WIDTH - len(IMG_[0]) * 3)/2)
    try:
        result = int(input(' ' * verticalMargin + label))
    except (KeyboardInterrupt, SystemExit):
        print(LANGUAGE.GAME_CLOSE)
        menu()
    except:
        return False
    return result

def printTextCenter(text):
    '''
        Method: printTextCenter
        Description: Prints received text as parameter horizontally centered
        Param: @string
        Return: @void
    '''
    print(' ' * int((WIDTH - len(text))/2) + text)

def printHeader():
    '''
        Method: printHeader
        Description: Prints header with logo horizontally centered
        Param: @void
        Return: @void
    '''
    clearTerminal()
    horizontalMargin = int((HEIGHT - 39)/2)
    verticalMargin = int((WIDTH - len(LANGUAGE.LOGO[0][0])) / 2)
    print("\n" * horizontalMargin)
    for col in range(2):
        for row in range(5):
            print(" " * verticalMargin, LANGUAGE.LOGO[col][row])
        verticalMargin = int((WIDTH - len(LANGUAGE.LOGO[1][0])) / 2)
        print("\n")

def printBoard(board):
    '''
        Method: printBoard
        Description: Prints board centered 
        Param: @list
        Return: @void
    '''
    verticalMargin = int((WIDTH - len(IMG_[0]) * 3)/2)
    result = str(" " * verticalMargin)
    jumpLine = '\n' + ' ' * verticalMargin
    verticalGrid = '|'
    horizontalGrid = '-' * 3 * len(IMG_[0])

    col = 0
    row = 0
    while(row < 3):
        while(col < 3):
            aux = 0
            while(aux < 5):
                for add in range(3):
                    if(board[col][row + add] == 'x'):
                        result += IMGX[aux] + (verticalGrid if 0 <= add < 2 else '')
                    elif(board[col][row + add] == 'o'):
                        result += IMGO[aux] + (verticalGrid if 0 <= add < 2 else '')
                    else:
                        result += IMG_[0] + (verticalGrid if 0 <= add < 2 else '')
                result += jumpLine if aux < 4 else ''
                aux += 1
            result += jumpLine + (horizontalGrid if 0 <= col < 2 else '' + jumpLine)
            col += 1
            result += jumpLine
        row += 1
    print(result)

def checkWinner(board):
    '''
        Method: checkWinner
        Description: Checks if any of the players won and returns boolean equivalent
        Param: @list
        Return: @void
    '''
    for aux in range(3):
        col = (board[aux][0] == board[aux][1] == board[aux][2]) and board[aux][0] != ' '
        row = (board[0][aux] == board[1][aux] == board[2][aux]) and board[0][aux] != ' '
        ver = (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != ' '
        if(col or row or ver):
            return True
        else:
            return False

def startGame():
    '''
        Method: startGame
        Description: Initialize a new game and routines involved
        Param: @void
        Return: @void
    '''
    BOARD = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    endgame = False
    count = 1
    message = str()
    while(count <= 10):
        printHeader()
        printBoard(BOARD)

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
                row = inputValidInt(LANGUAGE.LABEL_INPUT_ROW) - 1
                col = inputValidInt(LANGUAGE.LABEL_INPUT_COL) - 1
                
                if(row >= 0 and row < 3 and col >= 0 and col < 3):
                    if(BOARD[row][col] == ' '):
                        if(count % 2 == 0):
                            BOARD[row][col] = 'x'
                        else:
                            BOARD[row][col] = 'o'
                        count += 1
                    else:
                        message = LANGUAGE.OVERWRITE
                else:
                    message = LANGUAGE.INVALID_POSITION
            else:
                message = LANGUAGE.GAME_OVER
                endgame = True

            if(checkWinner(BOARD)):
                if((count - 1) % 2 == 0):
                    message = LANGUAGE.WINNER_X
                else:
                    message = LANGUAGE.WINNER_O
                endgame = True

def menu(message = ''):
    '''
        Method: menu
        Description: Display the main menu
        Param: @string
        Return: @void
    '''
    printHeader()
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

    choose = inputValidInt(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 1):
        startGame()
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
    '''
        Method: settings
        Description: Display the settings menu
        Param: @string
        Return: @void
    '''
    global LANGUAGE
    printHeader()
    print('\n' * 3)
    printTextCenter(LANGUAGE.MENU_SETTINGS.upper())
    print('\n' * 1)
    printTextCenter('1 - ' + LANGUAGE.SETTINGS_LANGUAGE + ': ' + LANGUAGE.SETTINGS_LANGUAGE_DEFAULT)
    print('\n' * 7)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 3)
    printTextCenter(message)

    choose = inputValidInt(LANGUAGE.LABEL_INPUT_MENU)

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
    '''
        Method: about
        Description: Display the about menu
        Param: @string
        Return: @void
    '''
    printHeader()
    print('\n' * 3)
    printTextCenter(LANGUAGE.MENU_ABOUT.upper())
    print('\n' * 1)
    count = 0
    while count < len(LANGUAGE.ABOUT):
        printTextCenter(LANGUAGE.ABOUT[count])
        count += 1
    print('\n' * 1)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 2)
    printTextCenter(message)

    choose = inputValidInt(LANGUAGE.LABEL_INPUT_MENU)

    if(choose == 5):
        menu()
    else:
        about(LANGUAGE.INVALID_COMMAND)

def instruction(message = ''):
    '''
        Method: settings
        Description: Display the instruction menu
        Param: @string
        Return: @void
    '''
    clearTerminal()
    printHeader()
    print('\n' * 3)
    printTextCenter(LANGUAGE.MENU_INSTRUCTIONS.upper())
    print('\n' * 3)
    count = 0
    while count < len(LANGUAGE.INSTRUCTIONS):
        printTextCenter(LANGUAGE.INSTRUCTIONS[count])
        count += 1
    print('\n' * 2)
    printTextCenter('5 - ' + LANGUAGE.SETTINGS_RETURN)
    print('\n' * 3)
    printTextCenter(message)

    choose = inputValidInt(LANGUAGE.LABEL_INPUT_MENU)
    
    if(choose == 5):
        menu()
    else:
        instruction(LANGUAGE.INVALID_COMMAND)

#Start method
menu()

