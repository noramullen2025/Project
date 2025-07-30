import pygame


from calcmath import calculate, calc


pygame.init()



screen_width=800
screen_height=500
clock = pygame.time.Clock()
screen=pygame.display.set_mode((screen_width, screen_height))



GREY=(50,50,50) #grey
BLACK=(0,0,0) #black
WHITE=(255,255,255) #white
buttons={1:(270,200,75,75),2:(350,200,75,75),3:(430,200,75,75),4: (270,280,75,75),5: (350,280,75,75),6:(430,280,75,75),7:(270,360,75,75),8:(350,360,75,75),9:(430,360,75,75),"+":(510,200,75,75),"-":(510,280,75,75),"*":(510,360,75,75),"/":(510,440,75,75),0:(350,440,75,75),"AC":(430,440,75,75),"=":(270,440,75,75)}


display = ""


myfont = pygame.font.SysFont("monospace", 30)



RECT1=pygame.draw.rect(screen, GREY, (230,0, 320, 500))
running=True
while running:
    clock.tick(1)
    screen.fill((225,225,225))
    pygame.draw.rect(screen, GREY, (257,0, 338, 500))
    DISPLAY=pygame.draw.rect(screen, WHITE, (280,30,290,130))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.KEYDOWN == event.type and pygame.K_1 == event.key:
            print (1)
        elif pygame.MOUSEBUTTONDOWN == event.type:
            cur_x, cur_y = event.pos
            for button in buttons:
                pos = buttons[button]
                left = pos [0]
                right = pos[2] + left
                top = pos [1]
                bottom = pos[3] + top
                if cur_x>=left and cur_x <= right and cur_y >= top and cur_y <= bottom:
                    if button == "=":
                        display = str(calc(display))
                    elif button == "AC":
                        display = ""
                    elif len(display) < 15:
                        if display == "Invalid input":
                            display = ""
                        display = display + str(button)
    label = myfont.render(display, 1, (0,0,0))
    screen.blit(label, (280,100))
    
    
    
    for button in buttons:
        pygame.draw.rect(screen, BLACK, buttons[button])
        btn_label=myfont.render(str(button), True, (255,255,255))
        btn_x, btn_y, btn_w, btn_h = buttons[button]
        text_rect = btn_label.get_rect(center=(btn_x + btn_w // 2, btn_y + btn_h // 2))
        screen.blit(btn_label, text_rect)
    btn_x, btn_y, btn_w, btn_h = buttons[1]
    btn_label = myfont.render("1", True, (255,255,255))
    text_rect = btn_label.get_rect(center=(btn_x + btn_w // 2, btn_y + btn_h // 2))
    screen.blit(btn_label, text_rect)
    pygame.display.flip()