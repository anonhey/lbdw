init python:
    def getCharImage(name, mood, modifiers):
        imagePath = name + "/" + "character" + "/" + mood        
        if "n" in modifiers:
            imagePath += "_" + "n"
        if "p" in modifiers:
            imagePath += "_" + "p"
        imagePath += ".png"
        return imagePath

    class GameCharacter:
        def __init__(self, character):
            self.character = character
            self.mood = "neutral"
            self.bodyModifiers = []

        def getImage(self, newMood = None):
            if newMood is not None:
                self.mood = newMood
            return getCharImage(self.character.name, self.mood, self.bodyModifiers)

        def addModifier(self, bodyModifier):
            if bodyModifier not in self.bodyModifiers:
                self.bodyModifiers.append(bodyModifier)

        def removeModifier(self, bodyModifier):
            if bodyModifier in self.bodyModifiers:
                self.bodyModifiers.remove(bodyModifier)

#Menu
image menu_map_idle=im.Scale("icons/menu_map.png", 100, 100)
image menu_map_hover=im.Scale("icons/menu_map_hover.png", 100, 100)
image menu_stats_idle=im.Scale("icons/menu_stats.png", 100, 100)
image menu_stats_hover=im.Scale("icons/menu_stats_hover.png", 100, 100)
image menu_world_idle=im.Scale("icons/menu_world.png", 100, 100)
image menu_world_hover=im.Scale("icons/menu_world_hover.png", 100, 100)
screen ui_bar():
    #add "gui/ui_main.png"
    fixed:
        imagebutton auto 'menu_map_%s' yalign 1 xcenter 0.7:
            action [Jump("overworld")]
        imagebutton auto 'menu_stats_%s' yalign 1 xcenter 0.8:
            action [Jump("overworld")]
        imagebutton auto 'menu_world_%s' yalign 1 xcenter 0.9:
            action [Jump("overworld")]



define mc = Character("[mcName]")
define pai = Character("[mcName]-internal-AI")
define shipPa = Character("Ship PA")

#Body modifiers
define validBodyModifiers = ["n","p"]

#Ezeria
define e = Character("Ezeria", color = "#FFA4AF", image="ezeria")
define aLivedAge = 20
define eRealAge = 34
define ezeria = GameCharacter(e)
image ezeria neutral = ezeria.getImage("neutral")
image ezeria happy = ezeria.getImage("happy")
image ezeria sad = ezeria.getImage("sad")
image ezeria = ezeria.getImage(None)
