from render import *
import pygame
from math import cos, sin, pi

if __name__ == '__main__':

    txts = {
        '1': pygame.image.load('./textures/brick.jpg'),
        '2': pygame.image.load('./textures/clear.jpg'),
        '3': pygame.image.load('./textures/dark.jpg'),
        '4': pygame.image.load('./textures/stone.jpg'),
        '5': pygame.image.load('./textures/white.jpg')
    }

    enemies = [{"x": 80,
                "y": 300,
                "texture": pygame.image.load('./sprites/zombie.png')},

               {"x": 270,
                "y": 280,
                "texture": pygame.image.load('./sprites/crepper.png')},

               {"x": 420,
                "y": 420,
                "texture": pygame.image.load('./sprites/herobrine.png')}
               ]

    pygame.init()
    disp = pygame.display.set_mode((1000, 500), pygame.DOUBLEBUF | pygame.HWACCEL)
    disp.set_alpha(None)
    tkei = pygame.time.Clock()
    ltr = pygame.font.Font("./fonts/Raleway-Medium.ttf", 30)
    pygame.mixer.music.load("./music/MinecraftMusicMenu.mp3")
    pygame.mixer.music.play(-1)


    def incF():
        fs = str(int(tkei.get_fps()))
        fs = ltr.render(fs, 1, pygame.Color("white"))
        return fs


    cast = MyRender(disp, txts, enemies)

    button = pygame.image.load("./UIElements/MinecraftButton.png")
    mysound = pygame.mixer.Sound("./music/MinecraftMenuButtonSoundEffect.wav")

    tabIndex = -1
    buttonPressed = False

    isPrincipalMenu = True
    isPaused = True

    flag = True


    def createButton(buttonInfo):
        disp.blit(button, (buttonInfo['x'], buttonInfo['y']))
        disp.blit(ltr.render(buttonInfo['text'], 1, pygame.Color("white")), (
            int(buttonInfo['x'] + (button.get_width() / 2) - (ltr.size(buttonInfo['text'])[0] / 2)),
            int(buttonInfo['y'] + (button.get_height() / 2) - (ltr.size(buttonInfo['text'])[1] / 2))))


    menubuttons = [
        {
            "x": int((cast.width / 2) - (button.get_width() / 2)),
            "y": 120,
            "text": "Nivel 1",
            "tabIndex": 0
        },
        {
            "x": int((cast.width / 2) - (button.get_width() / 2)),
            "y": 200,
            "text": "Nivel 2",
            "tabIndex": 1
        },
        {
            "x": int((cast.width / 2) - (button.get_width() / 2)),
            "y": 280,
            "text": "Nivel 3",
            "tabIndex": 2
        },
        {
            "x": int((cast.width / 2) - (button.get_width() / 2)),
            "y": 360,
            "text": "Salir",
            "tabIndex": 3
        },
    ]

    while flag:
        mpos = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                flag = False

            if isPrincipalMenu or isPaused:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    for but in menubuttons:
                        if but['x'] < mpos[0] < but['x'] + button.get_width() and but['y'] < mpos[1] < but[
                            'y'] + button.get_height():
                            mysound.play()
                            tabIndex = but['tabIndex']
                            buttonPressed = True

            if ev.type == pygame.KEYDOWN:
                if isPaused:
                    if ev.key == pygame.K_TAB:
                        tabIndex = (tabIndex + 1) % 4
                    elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                        if tabIndex != -1:
                            mysound.play()
                            buttonPressed = True
                    elif ev.key == pygame.K_ESCAPE:
                        isPaused = False
                else:
                    nX = cast.x
                    nY = cast.y
                    if ev.key == pygame.K_ESCAPE:
                        isPaused = True
                    elif ev.key == pygame.K_w:
                        nX += cos(cast.ag * pi / 180) * cast.stpsize
                        nY += sin(cast.ag * pi / 180) * cast.stpsize
                    elif ev.key == pygame.K_s:
                        nX -= cos(cast.ag * pi / 180) * cast.stpsize
                        nY -= sin(cast.ag * pi / 180) * cast.stpsize
                    elif ev.key == pygame.K_a:
                        nX -= cos((cast.ag + 90) * pi / 180) * cast.stpsize
                        nY -= sin((cast.ag + 90) * pi / 180) * cast.stpsize
                    elif ev.key == pygame.K_d:
                        nX += cos((cast.ag + 90) * pi / 180) * cast.stpsize
                        nY += sin((cast.ag + 90) * pi / 180) * cast.stpsize
                    elif ev.key == pygame.K_LEFT:
                        cast.ag -= 5
                    elif ev.key == pygame.K_RIGHT:
                        cast.ag += 5

                    a = int(nX / cast.bksize)
                    b = int(nY / cast.bksize)

                    if cast.chzu[b][a] == ' ':
                        cast.x = nX
                        cast.y = nY

        if isPrincipalMenu:
            if buttonPressed:
                if tabIndex == 0:
                    isPrincipalMenu = False
                    isPaused = False
                    pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                    pygame.mixer.music.play(-1)
                    cast.glload_map('./maps/chzu.txt')
                elif tabIndex == 1:
                    isPrincipalMenu = False
                    isPaused = False
                    pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                    pygame.mixer.music.play(-1)
                    cast.glload_map('./maps/chzu2.txt')
                elif tabIndex == 2:
                    isPrincipalMenu = False
                    isPaused = False
                    pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                    pygame.mixer.music.play(-1)
                    cast.glload_map('./maps/chzu3.txt')
                elif tabIndex == 3:
                    flag = False
                buttonPressed = False

            disp.blit(pygame.image.load("./backgrounds/minecraftbg.png"), (0, 0))

            title = pygame.image.load("./UIElements/MinecraftTitle.png")
            disp.blit(title, (int((cast.width / 2) - (title.get_width() / 2)), 30))

            for but in menubuttons:
                if (but['x'] < mpos[0] < but['x'] + button.get_width() and but['y'] < mpos[1] < but[
                    'y'] + button.get_height()) or tabIndex == but['tabIndex']:
                    disp.fill(pygame.Color("yellow"), (
                        int(but['x'] - 3), int(but['y'] - 3), int(button.get_width() + 6),
                        int(button.get_height() + 6)))
                    createButton(but)
                    if but['x'] < mpos[0] < but['x'] + button.get_width() and but['y'] < mpos[1] < but[
                        'y'] + button.get_height():
                        tabIndex = -1
                else:
                    createButton(but)
        else:
            disp.blit(pygame.image.load("./backgrounds/grass.png"), (0, 0))

            disp.blit(pygame.image.load("./backgrounds/sky.png"), (int(cast.width / 2), 0))

            disp.blit(pygame.image.load("./backgrounds/grassfloor.png"), (int(cast.width / 2), int(cast.height / 2)))

            cast.glrender()

            disp.fill(pygame.Color("black"), (0, 0, 30, 30))

            disp.blit(incF(), (0, 0))
            tkei.tick(30)

            if isPaused:
                s = pygame.Surface((cast.width, cast.height))
                s.set_alpha(192)
                s.fill((0, 0, 0))
                disp.blit(s, (0, 0))

                if buttonPressed:
                    if tabIndex == 0:
                        isPaused = False
                        pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                        pygame.mixer.music.play(-1)
                        cast.glload_map('./maps/chzu.txt')
                        cast.glrender()
                    elif tabIndex == 1:
                        isPaused = False
                        pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                        pygame.mixer.music.play(-1)
                        cast.glload_map('./maps/chzu2.txt')
                        cast.glrender()
                    elif tabIndex == 2:
                        isPaused = False
                        pygame.mixer.music.load("./music/MinecraftBackgroundMusic.mp3")
                        pygame.mixer.music.play(-1)
                        cast.glload_map('./maps/chzu3.txt')
                        cast.glrender()
                    elif tabIndex == 3:
                        isPrincipalMenu = True
                    buttonPressed = False

                for but in menubuttons:
                    if (but['x'] < mpos[0] < but['x'] + button.get_width() and but['y'] < mpos[1] < but['y'] + button.get_height()) or tabIndex == but['tabIndex']:
                        disp.fill(pygame.Color("yellow"), (
                            int(but['x'] - 3), int(but['y'] - 3), int(button.get_width() + 6),
                            int(button.get_height() + 6)))
                        createButton(but)
                        if but['x'] < mpos[0] < but['x'] + button.get_width() and but['y'] < mpos[1] < but['y'] + button.get_height():
                            tabIndex = -1
                    else:
                        createButton(but)

        pygame.display.update()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
