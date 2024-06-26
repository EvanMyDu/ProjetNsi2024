import pygame
from classes.Joueur import *
from Constantes.constante_partie import *
pygame.init()



class boite_dialogue:
  X_POSITION = 60
  Y_POSITION = 470


  def __init__(self):
    pygame.init()
    self.box = pygame.image.load('Graphisme\Objet\dialog_box.png')
    self.box = pygame.transform.scale(self.box, (850, 100))
    self.texts = ["Bonjour Neuille"]
    self.text_index = 0
    self.font = pygame.font.Font("Graphisme\Objet\dialog_font.ttf", 24)
    self.etat = False

  def info(self, screen, info):
    lines = info
    lines = lines.splitlines()
    i = 0
    for line in lines:
      text = self.font.render(line ,False,(255, 255, 255))
      screen.blit(text,(screen_width//2 - 200 - 135* i,screen_height-200 + 40*i))
      i += 1

  def execute(self):
    if self.etat:
      self.prochain_text()
    else:
      self.etat = True
      self.text_index = 0

  def render(self, screen):
    if self.etat:
      screen.blit(self.box,(self.X_POSITION,self.Y_POSITION))
      text = self.font.render(self.texts[self.text_index],False,(0, 0, 0))
      screen.blit(text,(self.X_POSITION + 60,self.Y_POSITION + 30))



  def prochain_text(self):
    self.text_index += 1
    if self.text_index >= len(self.texts) :
      self.etat = False




