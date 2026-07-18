image intro intro1 = "images/intro/intro1.png"
image intro intro2 = "images/intro/intro2.png"
image intro intro3 = "images/intro/intro3.png"
image intro intro4 = "images/intro/intro4.png"
image intro intro5 = "images/intro/intro5.png"
image intro intro6 = "images/intro/intro6.png"

image intro spaceshipInterior = "images/intro/spaceshipinterior_placeholder.jpg"
image intro crashSite=("images/intro/crashsite.png")

label intro:
    scene black
    ""
    scene intro intro1
    ## a compelling backstory to the universe
    "A standard universe is vast, in both space and time."
    "Almost impossibly vast, in fact. The sort of vastness that makes the human mind do peculiar things, like give up entirely and demand a nice cup of tea."
    "The common setup also allows for the formation of matter."
    "This is generally considered a good thing, though it does lead to a lot of complaining about paperwork in the long run."
    "In such cases as matter is allowed to form, structures take shape."
    "Planets, stars, the occasional rogue asteroid with delusions of grandeur—all the usual furniture of reality."
    "Structures leads to small rebellious instances of order, and by the inexplicable forces of nature, intelligence appears."
    "Which, frankly, was probably a mistake. But mistakes, like tea stains, are remarkably difficult to remove from the fabric of existence."

    scene intro intro2
    "Intelligence takes many forms, which is to say it takes far more forms than is strictly sensible, and most of them are absolutely certain they're right about everything."
    "Most often collectives of smaller entities acting on each other to create something bigger than the sum of the parts."
    "Bacteria become organisms. Organisms become civilizations. Civilizations become bureaucracies. The trajectory is depressingly predictable."
    "During the lifetime of a universe, different types of collectives emerge—civilizations, hives, gestalt consciousnesses, and various other arrangements of matter that have learned to be insufferably annoyed with existence."
    "Some achieve remarkable heights. Others achieve remarkable depths. A few manage both simultaneously, which is typically quite painful for everyone involved."
    
    scene intro intro3
    "Some may even reach the power to control a whole galaxy, known by those who would care to classify these types of things as a Type 3 civilization."
    "Though honestly, the classification system was devised by a committee, so it's rather dubious to begin with."
    "These collectives are capable of the most awesome and monumental undertakings: terraforming planets wholesale, moving stars about like chess pieces, breaking the laws of physics with the casual assurance of someone who's read all the small print and found it rather unconvincing."
    "They build things. Massive things. Incomprehensibly expensive things. The sort of things that make you wonder what they were possibly thinking, though they probably weren't, which explains quite a lot."
    "Yet..."

    scene intro intro4
    "...the candle that burns twice as bright burns for half as long."
    "Or in this case, considerably less. Because civilizations, no matter how magnificently advanced, have a fatal flaw: they're run by intelligent beings."
    "And intelligent beings, for all their cleverness, are remarkably good at making catastrophically poor decisions."
    
    scene intro intro5
    "Eventually, even these titans of creation succumb to the inevitability of chaos and entropy—the universe's way of reminding everyone that it was here first and will be here last, laughing at the lot of you."
    "But before they collapse entirely, before the lights go out for the final time, they leave behind artifacts."
    "Artifacts: monuments to hubris, repositories of forgotten knowledge, and occasionally useful things like coffee makers, though you'd have to ask the aliens about that."
    "Artifacts that, at the far end of history, might seem fantastical to those who witness them—and probably completely inexplicable to anyone who tries to use them without the instruction manual."

    scene intro intro6
    "One such creation is a 'dome world'—a small artificial sphere of controlled reality, created by those most powerful civilizations for reasons that made perfect sense at the time but are now utterly mysterious."
    "Tiny, by planetary measures. Retreats for those individuals who wished to control their entire existence and everyone living inside."
    "Personalized pocket universes, essentially. Which is either a brilliant solution to personal autonomy or a monument to supreme narcissism, depending on your point of view."
    "Though since long abandoned by their previous masters—who either transcended, self-destructed, or went off to find something more interesting to do—a dome world might orbit a planet."
    "...dormant"
    "...waiting"
    "...waiting for its master to return."
    "Which, statistically speaking, is unlikely."
    "And yet there are always exceptions to probability."
    "Exceptions are what keep the universe interesting."
    "Unfortunately, this is exactly such a place where your spacecraft is now crashing towards, while you and everyone else onboard lay motionless in your stasis pods, completely unaware of the spectacular misfortune about to befall you."

    scene black

    $ mcName = renpy.input("What's your name, travler?")

    $ player_name = mcName.strip()

    if mcName == "":
        "Travler it is..."
        $ mcName="Travler"

    "Wake up, [mcName]!"

    # interior of the ship, stasis pod, lights blinking red, alarms blaring, smoke everywhere

    scene intro spaceshipInterior    
    pai "Warning: Vital signs critical. Evacuate area."
    mc "What the fuck!"
    mc "My eyes are all blurry..."
    pai "Evacuate area."
    mc ""


# code for the spaceship interior where the player must choose one of several stasis pods to rescue one other passanger
    mc "I cant leave them behind..."
    menu:
        "What pod should I open?"
        "Pod 1":
            $ pod1 = True
            jump pod1
        "Pod 2":
            $ pod2 = True
            jump pod2
        "Pod 3":
            $ pod3 = True
            jump pod3
        "Drone Pod":
            $ pod4 = True
            jump pod4


# pod1 - The young beautiful passanger Ezeria, who is a bit of a nerd and has a hesitant personality.
    label pod1:
        mc "I guess I should start with the first pod."
        mc "I hope she's ok..."
        scene intro podCrash1
        mc "Wake up, wake up!"
        e "huh..."
        mc "Quickly, we need to get out of here!"
        e "Wuah...?"
        "The girl faints and falls back into the pod."
        mc "No, no, no!"
        shipPa "Warning: Toxic gas detected."
        mc "We need to hurry!"
        "You lift the girl out of the pod and carry her on your back."
        "You wont be able to carry her for long, but you need to get out of here."
        jump crashSite

# pod2 - The middle aged woman passanger who is motherly and strong willed.
    label pod2:
        mc "I guess I should start with the second pod."
        mc "I hope she's ok..."
        scene intro podCrash2
        mc "Wake up, wake up!"
        a "What the..."
        mc "Quickly, we need to get out of here!"
        a "Who are you?"
        mc "I'm [mcName], we need to hurry!"
        shipPa "Warning: Toxic gas detected."
        "The woman takes your outstretched hand and you pull her out of the pod."
        a "Let's go!"
        mc "What about the others?"
        a "They'll be alright inside of the pods for now, we need to get out of here!"

    


label crashSite:
    scene intro crashSite
    pai "Danger zone evacuated."
    mc "fuck..."
    pai "Major lacerations detected."
    mc "The ship crashed?!"
    pai "Minor fracture detected."
    mc "Where the fuck am I?"
    pai "Blood loss detected."
    pai "Seek medical attention."
    mc "I... I'm not..."

    show black
    with dissolve
    
    jump introEzeria