class Quete:
    def __init__(self, titre, description, objets_requis):
        self.titre = titre
        self.description = description
        self.objets_requis = objets_requis
        self.completee = False
        self.quete_accomplit = []



    def proposer_quete(self,joueur,Npc):
        if self.quete_actuelle == None:
            if NPC.name == "Godefroy" :
                self.quete_actuelle = quete1
                   
            if NPC.name == "Guenièvre":
                self.quete_actuelle= quete2
                       
            if NPC.name == "Merlin":
                self.quete_actuelle= quete3
                      
            if NPC.name == "Morgane":
                self.quete_actuelle= quete4
                    
            if NPC.name == "Arthur":
                self.quete_actuelle= quete5
                       
            if NPC.name == "Élaine":
                self.quete_actuelle= quete6
                          
            if NPC.name == "Galahad":
                self.quete_actuelle= quete7
        
            if NPC.name == "Lancelot":
                self.quete_actuelle= quete8
                
            if NPC.name == "Tristan":
                self.quete_actuelle= quete9 
            
   
    
    
    
    
    
    
   
    
      

    def verifier_completion(self, joueur):
        for objet in self.objets_requis:
            if not joueur.possede_objet(objet):
                print(f"{joueur.nom} n'a pas encore tous les objets nécessaires pour compléter la quête '{self.titre}'.")
                return False
        self.completee = True
        quete_accomplit.append(self.quete_actuelle
        print(f"{joueur.nom} a complété la quête '{self.titre}'!")
        self.inventaire.pop
        self.quete_actuelle.pop
        return True

    def __str__(self):
        return f"Quête: {self.titre}\nDescription: {self.description}\nObjets requis: {', '.join(self.objets_requis)}"

# Création des quêtes : 
quete1 = Quete("La quête du chevalier", "Trouver l'épée et le bouclier.", ["Épée", "Bouclier"])
quete2 = Quete("La quête de l'archer", "Trouver l'arc et les flèches.", ["Arc", "Flèches"])
quete3 = Quete("La quête du mage", "Trouver le grimoire et l'amulette.", ["Grimoire", "Amulette"])
quete4 = Quete("La quête du guérisseur", "Trouver les herbes médicinales et la potion de soin.", ["Herbes médicinales", "Potion de soin"])
quete5 = Quete("La quête de l'aventurier", "Trouver la tunique et le heaume.", ["Tunique", "Heaume"])
quete6 = Quete("La quête du voleur", "Trouver les gants et la lanterne.", ["Gants", "Lanterne"])
quete7 = Quete("La quête de l'explorateur", "Trouver la sacoche et le parchemin.", ["Sacoche", "Parchemin"])
quete8 = Quete("La quête du gardien", "Trouver la clef et le trophée.", ["Clef", "Trophée"])
quete9 = Quete("La quête du cuisinier", "Trouver le pain et le fromage.", ["Pain", "Fromage"])

# Création des perso : 
npc1 = NPC("Godefroy", 5, quete1)
npc2 = NPC("Guenièvre", 5, quete2)
npc3 = NPC("Merlin", 5, quete3)
npc4 = NPC("Morgane", 5, quete4)
npc5 = NPC("Arthur", 5, quete5)
npc6 = NPC("Élaine", 5, quete6)
npc7 = NPC("Galahad", 5, quete7)
npc8 = NPC("lancelot",5,quete8)
npc9 = NPC("Tristan",5,quete9)



# Dictionnaire des quêtes disponibles
quetes_disponibles = {
    "quete1": quete1,
    "quete2": quete2,
    "quete3": quete3,
    "quete4": quete4,
    "quete5": quete5,
    "quete6": quete6,
    "quete7": quete7,
    "quete8": quete8,
    "quete9": quete9 }



512 205028
# A ajouter dans la classe joueur : self.

# Faire 
 L'objet qu'on cherche sera toujours un coffre
