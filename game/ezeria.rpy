image ezeriaIntro=("images/ezeria/Intro1.png")

label introEzeria:
    scene black
    "Hey"
    "Hey, you!"
    show ezeriaIntro
    with dissolve
    ## Ezerria standing over the player on ah beach
    "Wake up!"
    mc "Wha.. where am I?"
    "How the hell should I know?!"
    mc "Who are you?"
    e "[e.name], I was aboard the same ship as you."

    scene beach
    show ezeria sad at homeMiddle
    mc "Wait, why... we shouldn't even be awake."
    e "What's your name?"
    mc "I'm... [mcName]"
    mc "Last I remember I got stuffed in an old cryo pod and promised a journey to the Auzlar Ring."
    e "Same here, but I don't think this is it..."
    e "..."
    mc "You saved me?"

    show ezeria neutral at homeMiddle
    e "Well, yeah I woke up on the ground and after a few meters of stumbling I found you."
    e "I dragged you here, because of the smoke."
    mc "How long have I been out?"
    e "Half a day, maybe, since I found you atleast."
    mc "...fuck, well thanks..."
    e "..."
    mc "Are you ok?"
    e "Yeah, somehow I managed to get through the crash with just minor bruises"
    e "I suspect my AI core did some autonomous quick reactions while i was out, but it's no longer responding..."
    mc "Maybe fried itself trying to save you?"
    
    show ezeria sad at homeMiddle
    e "Yeah, might be"
    mc "..."
    mc "Any guesses on where we are?"
    e "Im guessing some sort of artifical world..."

    show ezeria neutral at homeMiddle
    e "The sky looks way to clean and artificial to be real"
    mc "Yeah, I figured the same. The air is... just perfect in every way. The water is too clear."
    mc "Hm, seen anything living? Like besides the trees and stuff."
    e "Mmh, I think I saw some fish or something in the water, but nothing on land."
    mc "So a fake world, with a fake jungle and a semi-fake ocean?"
    e "Something like that yes."
    mc "What now..."

    menu optional_name:
        "What now..."
        "Suggest going back to the crash site.":
            jump goBack
        "Suggest getting water.":
            jump getWater
        "Suggest rest":
            jump rest
        
label goBack: # PLACEHOLDER
    mc "Maybe we should go back to the crash site. To see if anyone else survived or if there's a emergency kit."
    e "Sure, I'm up for it"
    scene crashSite
    e "This is where i found you."
    jump homeBeach 

label getWater: # PLACEHOLDER
    mc "If we expect to spend any more time here we need water."
    e "And eventually something to eat."
    mc "Exactly, lets go."
    jump homeBeach

label rest: # PLACEHOLDER
    mc "I need to lay down."
    e "Oh, yeah sure. I'll look around some while you rest."
    "test - "
    jump homeBeach


# example
label ezeriaTalk:
    hide screen people
    show image ezeria.getImage("happy") at talkHome
    "Hi"
    menu state:
        "normal":
            $ ezeria.removeModifier("n")
            $ ezeria.removeModifier("p")
        "nerdy":
            $ ezeria.addModifier("n")
        "preppy":
            $ ezeria.addModifier("p")
    jump homeBeach
