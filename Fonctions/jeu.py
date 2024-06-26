import pygame, os, sys
from pytmx.util_pygame import load_pygame
from Constantes import constante_partie as cp
from classes.Bouton import Button
from classes.Joueur import Player
from classes.Game import Game


pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()


def fenetre(menuoujeu, nom_fenetre):
    pygame.display.set_caption(nom_fenetre) #Met le nom du jeu dans le fenêtre en haut à gauche
    pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
    if menuoujeu == 'Menu':
        cp.NomEcran = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE) #Chargement du menu selon les résolutions de l'ordinateur du joueur


def musiquemenu():
    pygame.mixer.init()
    pygame.mixer.music.load(cp.SonMenu) #Lancement de la musique du jeu
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.04) #Initialisation du volume de la musique par défaut

def menu():
    QuitterN = Button(cp.screen_width / 2, cp.screen_height / 2, pygame.image.load('Graphisme\Boutons\Bouton_Quitter_Noir-removebg-preview.png'), 1)  #Bouton Quitter
    OptionN = Button(cp.screen_width / 2, cp.screen_height / 2 - 150, pygame.image.load('Graphisme\Boutons\Bouton_Options_Noir-removebg-preview.png'),1)  #Bouton Option
    Icone = Button(cp.screen_width - 100, cp.screen_height / 100, pygame.image.load('Graphisme\Boutons\icone.png'),1)  #Bouton pour mettre en fullscreen
    PlayN = Button(cp.screen_width / 2, cp.screen_height / 2-300, pygame.image.load('Graphisme\Boutons\Bouton_Jouer_Noir-removebg-preview.png'),1)  #Bouton pour Jouer
    QuitterO = Button(cp.screen_width / 2, cp.screen_height / 2 - 25, pygame.image.load('Graphisme\Boutons\Bouton_Quitter_Orange-removebg-preview.png'), 1) #Boutton Quitter Orange
    OptionO = Button(cp.screen_width / 2, cp.screen_height / 2-175, pygame.image.load('Graphisme\Boutons\Bouton_Options_Orange-removebg-preview.png'), 1) #Bouton Options Orange
    PlayO = Button(cp.screen_width / 2, cp.screen_height / 2-325, pygame.image.load('Graphisme\Boutons\Bouton_Jouer_Orange-removebg-preview.png'), 1) #Bouton Jouer Orange
    MusiqueOn = Button(cp.screen_width - cp.screen_width + 210, cp.screen_height /100 , pygame.image.load('Graphisme\Boutons\Anote_Musique_On.png'), 0.15) #Bouton Musique On
    MusiqueOff = Button(cp.screen_width - cp.screen_width + 350, cp.screen_height / 100, pygame.image.load('Graphisme\Boutons\Anote_Musique_Off.png'), 0.15) #Bouton Musique Off

    Quitter = (QuitterN,QuitterO)
    Jouer = (PlayN,PlayO)
    Option = (OptionN,OptionO)
    Musique = (MusiqueOn, MusiqueOff)
    musiquemenu()
    while True:
        # Arrière Plan
        cp.timer.tick(cp.fps)
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
        cp.NomEcran.blit(pygame.image.load('Graphisme\Background\Bg1.jpg'), (0, 0)) #Chargement de l'arrière plan
        # Dessiner les boutons
        Jouer[0].draw(cp.NomEcran)
        Icone.draw(cp.NomEcran)
        Option[0].draw(cp.NomEcran)
        Quitter[0].draw(cp.NomEcran)
        Jouer[1].draw(cp.NomEcran)
        Icone.draw(cp.NomEcran)
        Option[1].draw(cp.NomEcran)
        Quitter[1].draw(cp.NomEcran)
        if cp.music_enabled:
            Musique[0].draw(cp.NomEcran)
        else:
            Musique[1].draw(cp.NomEcran)
        for event in pygame.event.get():  # Récupère les actions du joueur
            if event.type == pygame.QUIT:  # Si le joueur veut quitter la fenêtre
                pygame.quit() #Quitte la fenêtre
                sys.exit()
            if Jouer[0].est_dans(): #Si le curseur est dans le bouton noir
                Jouer[0].rect.topleft = (-500,Jouer[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
                Jouer[1].rect.topleft = (Jouer[1].coordonnee[0] - Jouer[1].width/2,Jouer[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
            if Jouer[1].clique(cp.NomEcran): #Si on clique gauche dans la zone du bouton
                pygame.quit()
                game1 = Game("world", 'Numeric Project v1.0')
                if cp.music_enabled == True:
                    musiquemenu()
                    game1.run()
                else:
                    game1.run()

            if Jouer[0].est_dans() == False and Jouer[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
                Jouer[0].rect.topleft = (Jouer[0].coordonnee[0] - Jouer[0].width/2,Jouer[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
                Jouer[1].rect.topleft = (-800 ,Jouer[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
            if Option[0].est_dans(): #Si le curseur est dans le bouton noir
                Option[0].rect.topleft = (-500,Option[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
                Option[1].rect.topleft = (Option[1].coordonnee[0] - Option[1].width/2,Option[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
            if Option[1].clique(cp.NomEcran): #Si on clique gauche dans la zone du bouton
                pygame.quit()
            if Option[0].est_dans() == False and Option[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
                Option[0].rect.topleft = (Option[0].coordonnee[0] - Option[0].width/2,Option[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
                Option[1].rect.topleft = (-800 ,Option[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
            if Quitter[0].est_dans(): #Si le curseur est dans le bouton noir
                Quitter[0].rect.topleft = (-500,Quitter[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
                Quitter[1].rect.topleft = (Quitter[1].coordonnee[0] - Quitter[1].width/2,Quitter[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
            if Quitter[1].clique(cp.NomEcran): #Si on clique gauche dans la zone du bouton
                pygame.quit() #Quitte la fenêtre
                sys.exit()
            if Quitter[0].est_dans() == False and Quitter[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
                Quitter[0].rect.topleft = (Quitter[0].coordonnee[0] - Quitter[0].width/2,Quitter[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
                Quitter[1].rect.topleft = (-800 ,Quitter[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
            if Icone.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:  # Si un clic de souris est détecté
                if event.button == 1:
                    pygame.display.toggle_fullscreen() #Met le jeu en plein écran selon les résolutions de l'ordinateur du joueur
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Musique[0].est_dans() and Musique[0].clique(cp.NomEcran):
                    pygame.mixer.music.pause() # Si le bouton musique "On" a été cliqué, le menu se réactualise en mettant le bouton musique "Off"
                    cp.music_enabled = False #Coupe la musique
                    Musique[0].rect.topleft = (-2000, Musique[0].coordonnee[1]) #Localisation du  bouton musique
                    Musique[1].rect.topleft = (Musique[1].coordonnee[0] - Musique[1].width / 2-67, Musique[1].coordonnee[1])
                elif Musique[1].est_dans() and Musique[1].clique(cp.NomEcran):
                    pygame.mixer.music.unpause()
                    cp.music_enabled = True
                    Musique[1].rect.topleft = (-2000, Musique[1].coordonnee[1]) #Localisation du  bouton musique
                    Musique[0].rect.topleft = (Musique[0].coordonnee[0] - Musique[0].width / 2, Musique[0].coordonnee[1])


        pygame.display.update()






