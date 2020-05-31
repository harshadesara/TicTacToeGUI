import pygame

q = pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
blue = (0, 0, 255)
pygame.display.set_caption('Tic Tac Toe')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.mixer.music.load('Jazz_In_Paris.mp3')
pygame.mixer.music.play(-1)
FPS = 5
smallfont = pygame.font.SysFont('comicsansms', 25)
mediumfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 75)


def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen('Controls', green, -100, 'large')
        message_to_screen('Click on the square on which you want to place your mark!', black, -30)
        message_to_screen('Player\'s turn is mentioned by the green indicator!', black, 10)
        button('Play', 150, 500, 100, 50, green, light_green, action='play')
        button('Main', 350, 500, 100, 50, yellow, light_yellow, action='main')
        button('Quit', 550, 500, 100, 50, red, light_red, action='quit')
        pygame.display.update()
        clock.tick(FPS)


def game_over(msg):
    message_to_screen(msg, green, -200, 'large')
    button('Play Again', 150, 500, 150, 50, green, light_green, action='play')
    button('Controls', 375, 500, 100, 50, yellow, light_yellow, action='controls')
    button('Quit', 550, 500, 100, 50, red, light_red, action='quit')


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen('Welcome to TicTacToe', green, -100, 'large')
        message_to_screen('This is a 2 player game!', black, -30)
        message_to_screen('Have fun!', black, 10)
        button('Play', 150, 500, 100, 50, green, light_green, action='play')
        button('Controls', 350, 500, 100, 50, yellow, light_yellow, action='controls')
        button('Quit', 550, 500, 100, 50, red, light_red, action='quit')
        pygame.display.update()
        clock.tick(FPS)


def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    if size == 'medium':
        textSurface = mediumfont.render(text, True, color)
    if size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size='small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + (buttonwidth / 2)), (buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def possibilities(lst2, value):
    if lst2[0] == value and lst2[1] == value and lst2[2] == value:
        pygame.draw.line(gameDisplay, green, (250, 200), (550, 200), 5)
        return value, 1
    elif lst2[3] == value and lst2[4] == value and lst2[5] == value:
        pygame.draw.line(gameDisplay, green, (250, 300), (550, 300), 5)
        return value, 1
    elif lst2[6] == value and lst2[7] == value and lst2[8] == value:
        pygame.draw.line(gameDisplay, green, (250, 400), (550, 400), 5)
        return value, 1
    elif lst2[0] == value and lst2[3] == value and lst2[6] == value:
        pygame.draw.line(gameDisplay, green, (300, 150), (300, 450), 5)
        return value, 1
    elif lst2[1] == value and lst2[4] == value and lst2[7] == value:
        pygame.draw.line(gameDisplay, green, (400, 150), (400, 450), 5)
        return value, 1
    elif lst2[2] == value and lst2[5] == value and lst2[8] == value:
        pygame.draw.line(gameDisplay, green, (500, 150), (500, 450), 5)
        return value, 1
    elif lst2[0] == value and lst2[4] == value and lst2[8] == value:
        pygame.draw.line(gameDisplay, green, (250, 150), (550, 450), 5)
        return value, 1
    elif lst2[2] == value and lst2[4] == value and lst2[6] == value:
        pygame.draw.line(gameDisplay, green, (550, 150), (250, 450), 5)
        return value, 1
    else:
        return value, 0


def condition(lst, symbol):
    sym, done = possibilities(lst, symbol)
    if done == 1:
        if sym == 'O':
            return True, 1
        elif sym == 'X':
            return True, 2
    return False, 0


def scenarios(symbol, x, y, lst, index):
    if symbol == 'X':
        text_to_button(symbol, blue, x, y, 100, 100, size='large')
    elif symbol == 'O':
        text_to_button(symbol, red, x, y, 100, 100, size='large')
    lst[index] = symbol


def gameLoop():
    gameDisplay.fill(white)
    first = pygame.draw.rect(gameDisplay, white, (250, 150, 100, 100))
    second = pygame.draw.rect(gameDisplay, white, (350, 150, 100, 100))
    third = pygame.draw.rect(gameDisplay, white, (450, 150, 100, 100))
    fourth = pygame.draw.rect(gameDisplay, white, (250, 250, 100, 100))
    fifth = pygame.draw.rect(gameDisplay, white, (350, 250, 100, 100))
    sixth = pygame.draw.rect(gameDisplay, white, (450, 250, 100, 100))
    seventh = pygame.draw.rect(gameDisplay, white, (250, 350, 100, 100))
    eighth = pygame.draw.rect(gameDisplay, white, (350, 350, 100, 100))
    ninth = pygame.draw.rect(gameDisplay, white, (450, 350, 100, 100))
    pygame.draw.line(gameDisplay, black, (350, 150), (350, 450), 5)
    pygame.draw.line(gameDisplay, black, (450, 150), (450, 450), 5)
    pygame.draw.line(gameDisplay, black, (250, 250), (550, 250), 5)
    pygame.draw.line(gameDisplay, black, (250, 350), (550, 350), 5)
    text_to_button('Player 1\'s Turn', red, 50, 250, 100, 100, size='small')
    text_to_button('Player 2\'s Turn', blue, 650, 250, 100, 100, size='small')
    tex1 = smallfont.render("Player 1\'s Symbol: O", True, red)
    gameDisplay.blit(tex1, [10, 0])
    text2 = smallfont.render("Player 2\'s Symbol: X", True, blue)
    gameDisplay.blit(text2, [550, 0])
    gameExit = False
    c = 0
    symbol = ''
    flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = 0
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    bol = False
    player = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        click = pygame.mouse.get_pressed()
        if c % 2 == 1:
            symbol = 'X'
            pygame.draw.rect(gameDisplay, white, (75, 225, 50, 50))
            pygame.draw.rect(gameDisplay, green, (675, 225, 50, 50))
        elif c % 2 == 0:
            symbol = 'O'
            pygame.draw.rect(gameDisplay, white, (675, 225, 50, 50))
            pygame.draw.rect(gameDisplay, green, (75, 225, 50, 50))
        mouse_pos = pygame.mouse.get_pos()
        if flag1 == 0:
            if first.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 250, 150, lst, 0)
                    flag1 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag2 == 0:
            if second.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 350, 150, lst, 1)
                    flag2 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag3 == 0:
            if third.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 450, 150, lst, 2)
                    flag3 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag4 == 0:
            if fourth.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 250, 250, lst, 3)
                    flag4 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag5 == 0:
            if fifth.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 350, 250, lst, 4)
                    flag5 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag6 == 0:
            if sixth.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 450, 250, lst, 5)
                    flag6 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag7 == 0:
            if seventh.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 250, 350, lst, 6)
                    flag7 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag8 == 0:
            if eighth.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 350, 350, lst, 7)
                    flag8 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if flag9 == 0:
            if ninth.collidepoint(mouse_pos):
                if click[0] == 1:
                    scenarios(symbol, 450, 350, lst, 8)
                    flag9 = 1
                    c += 1
                    bol, player = condition(lst, symbol)
        if c >= 9 and not bol:
            game_over('It\'s a draw!')
        if bol:
            if player == 1:
                game_over('Player 1 won!')
            elif player == 2:
                game_over('Player 2 won!')
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'controls':
                game_controls()
            if action == 'play':
                gameLoop()
            if action == 'main':
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)


game_intro()
gameLoop()
