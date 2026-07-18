image overworld=("overworld/overworld.png")
image homeBeach_idle=im.Scale("overworld/homeBeach.png", 100, 100)
image homeBeach_hover=im.Scale("overworld/homeBeach_hover.png", 100, 100)

define unlocked = [""]
define available = ["homeBeach"]

label overworld:
    hide screen people
    scene black
    window hide
    show overworld
    show screen overworld_buttons
    $ renpy.pause()
    jump overworld


screen overworld_buttons:
    modal False
    fixed:
        imagebutton auto 'homeBeach_%s' yalign 0.45 xcenter 0.275:
            action Jump("homeBeach")