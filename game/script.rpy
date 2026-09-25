# Define the logo image
image logo = "logo.jpg"

label splashscreen:
    scene black with fade
    $ renpy.pause(0.5)
    show logo with dissolve
    $ renpy.pause(4.0)
    scene black with dissolve
    $ renpy.pause(2.5)

label start:
    $ m_mouth = "smile"
    $ m_brow = "happy"
    scene mov_back with fade
    show maihi casual sneakers at fullbody_pos
    s "Welcome to my personal project! In this game, I want you to enjoy the game and read the story carefully, pick options that suit you!"
    show maihi notice at fullbody_pos
    $ m_brow = "suspicious"
    s "Now tell me, what is the name of your character?"
    
    $ mc_name = renpy.input("What is your name?")
    $ mc_name = mc_name.strip() or "MC"
        
    show maihi None at fullbody_pos
    $ m_brow = "happy"
    s "Nice to meet you, [mc_name]!"
    s "Let's get this show going, [mc_name]!"
    
    scene backstreet with fade
    play music tweetybirds fadein 1.0
    "You, [mc_name], are dropped off at the exit of Kaerdence National Airport with only your luggage and dreams.. What dreams? Up to you, bud."
    "You're walking across the airport, the rustle of the bag on your back faint against the loud noises of people walking and talking as you head to find some food."
    "Along the way, you come across a convenience store, no name on it but it does have two vending machines on each side of the door, pretty convenient."
    
    menu:
        "Do you enter?"
        "Yes.":
            jump convenience_store
        "No.":
            jump busstop

label convenience_store:
    scene convenience_store with fade
    stop music
    "You enter the convenience store, and are greeted by shelves of food, and aisles of snacks along the flooring and a few things catch your eye."
    "You come to realize that.. there's no one else in here. No customers, no cashiers.. In fact, there's no image at all!"
    show maihi exclaim casual sneakers at fullbody_pos
    $ m_mouth = "o"
    s "Oh, hey! Uhhh.. there's no image here right now!"
    show maihi question casual sneakers at fullbody_pos
    $ m_brow = "sad"
    $ m_mouth = "biggrin"
    s "Oops.. not sure what happened here.. {w=1.5}{nw}"
    show maihi exclaim casual sneakers at fullbody_pos
    extend "Why not come back at a later update to see if I've an image to show, hm?"
    hide maihi exclaim casual sneakers
    jump busstop

label busstop:
    scene busstop with fade
    stop music
    "After having decided you wouldn't enter the convenience. Along the way, you spy a nearby bus stop and after a while, you decided 'Why not?' and decide to go and wait for the next bus."
    scene busstop2 with fade
    play music rain fadein 1.0
    
    "After waiting for seemed as hours, rain started to pour, drenching the street and bus stop with the salted waters."
    "It had been useless to wait so long, so you just decided walk home."
    scene black with fade
    $ renpy.pause(hard=True)
