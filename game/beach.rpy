define ezeriaPresent = True
define hutPresent = True

#Home positions
transform homeMiddle:
    yalign 0.8
    xcenter 0.35
    zoom 0.5

transform talkHome:
    yalign 1
    xcenter 0.2
    zoom 1

transform midleft:
    yalign 0.8
    xcenter 0.25
    zoom 0.5


image beach=("images/beach/bg.png")
image hut=("images/beach/hut.png")

label homeBeach:
    hide screen overworld_buttons
    scene black
    window hide
    show beach
    if hutPresent == True:
        show hut
    show screen people
    show screen ui_bar
    $ renpy.pause()
    jump homeBeach


screen people:
    if ezeriaPresent == True:
            fixed:
                imagebutton:
                    idle ezeria.getImage("happy") at homeMiddle
                    action [Jump("ezeriaTalk")]