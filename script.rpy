

define you = Character("You")
define Gus= Character("Gus")
define Host= Character("Casino Host")
define Security= Character("Security")

#characters and background images
image Gus neutral= "Gus_neutral.png"
image Gus angry= "Gus_angry.png"
image Casino Host = "casino_host.png"
image Casino Host upset = "casino_host_upset.png"
image Casino Host angry = "casino_host_angry.png"
image security= "security.png"
image bg skyline= "images/city_sky.jpg"
image bg hospital="images/hospital_bed.jpg"
image bg casino ad= "images/casino_ad.jpg"
image bg casino = "images/casino.jpg"
image bg slots = "images/slots.jpg"
image bg outside casino= "images/outside_casino.jpg"
image bg roulette= "images/roulette.jpg"
image bg hallway= "images/hallway.jpg"

# The game starts here.

label start:
    show bg skyline
    with fade
    "It's not fair."
    "Why do some people have everything?"


    "They've never had to work for anything, it's all been handed to them."

    "They will never know struggle."
    "Why do they have everything..."
    show bg hospital
    with fade
    "And you have nothing?"

    #first images of rich/wealthy areas, then in a hospital room we see the T.V
    #show commercial for new casino
    show bg casino ad
    with fade
    "Why is it that you and your loved ones are expected to suffer in silence, barely being able to pay for life-saving procedures, while others get to carelessly throw away their money at any chance they see?"
    you "Something's gotta change."
    you "After tomorrow, we shouldn't need to worry about stupid hospital bills ever again."

    #again show commercial boasting of all the money you could win


label thePlan:
    show bg outside casino
    with fade
    show Gus neutral at character_sizing
    
    Gus "So here's the plan:"
    #as he's talking include background of the casino/ puzzles
    show bg casino
    with fade
    Gus "Like any casino, it's going to be heavily guarded so you have to remain as inconspicuous as possible."
    
    Gus "Now your main objective is to crack into the casino's vault and get the money"
    show bg outside casino
    with fade
    Gus "But remember: I was the one who was able to pull strings to give you this opportunity in the first place so we're splitting 50/50."
    Gus "Anything else you win is just extra for you to keep."
    hide Gus neutral 
    you "Yeah, yeah. I understand."
    show Gus neutral at character_sizing
    Gus "Ok, before you go in, I need to tell you some things."
    hide Gus neutral
    you "Go for it."
    show Gus angry at character_sizing
    Gus "I was getting there if you gave me a moment."
    show Gus neutral at character_sizing
    Gus "Anyways"
    show bg slots
    with fade
    Gus "Throughout the casino there's going to be hints, so pay attention to your surroundings and what you hear because that's going to ultiamtely help you."
    Gus "With games like the slot machines and even roulette you might be able to win by using what you observed in the actual casino."
    Gus "... So feel free to try your hand in those, if you feel like the money in the safe wouldn't be enough for you."
    
    hide Gus neutral
    you "The more I can get the better.."
    show Gus angry at character_sizing
    Gus "Wellm let's not get hasty. If you raise suspicion at any of these games, a Casino Host will call security on you- completely ruining your chances of getting ANY money."
    show Gus neutral at character_sizing
    Gus "I'm just telling you this because... well I guess I feel like being a good person today."
    "You know he knows about your financial problems- I mean, you've known him almost your whole life, of course he knows. And he wants to help... Even if it means splitting profit."
    "Despite his rough appearance, you can't say that Gus doesn't care about others."
    hide Gus neutral
    you "After all this time, you still manage to find a way to surprise me-"
    show Gus angry at character_sizing
    Gus "Alright, don't be a wise ass."
    show Gus neutral
    Gus "I'm just saying that anything else you win is gonna be extra for you to keep."
    Gus "Also, I gave you some decoy chips so that if you did want to play some of those games you could."
    hide Gus neutral
    you "Thank you, I really appreciate-"
    show Gus angry at character_sizing
    Gus "Don't thank me just yet."
    show Gus neutral at character_sizing
    Gus "The decoy chips won't raise suspician only if you win. So if you get caught, security will find you and kick you out promptly."
    Gus "Anyways..."
    Gus "The signal is there is going to be spotty, so there's going to be times where you won't be able to contact me."
    Gus "Good luck in there, kid."
    hide Gus neutral
    you "Aye aye, captain. I hear you loud and clear. "

label firstGlance:
    show bg casino
    with fade
    you "Wow, this place is extravogant. Remind me of one of those classic ones from the 19th century..."
    show Casino Host at character_sizing
    Host "Hi!"
    Host "Welcome to Tempest Casino! Our casino was establish March 12, 1846, making this our 177th anniversary. Isn't that just so exciting?!"
    menu:
        "Wow, that's so interesting!":
            Host "I'm glad you agree! Have a good visit and good luck out there!"
            hide Casino Host 
        "Yeah, ok, I've got somewhere to be, I don't really have time for this.":
            show Casino Host upset at character_sizing
            Host "Ohh... Well, ok..."
            show Casino Host angry at character_sizing
            Host "SECURITY!!"
            Host "Get'em out of here!"
            hide Casino Host angry 
            show security at character_sizing
            hide security
            show bg skyline
            with fade
            "Really? You couldn't just be nice to her?."
            "You failed."
            return


label slotsPuzzle:
    show bg slots
    with fade
    you "Hmm... These seem to be the slot machines Gus was talking about."
    you "I wonder if I should even bother trying to win one of these."
    menu:
        "Might as well, let's see if I can get lucky.":
            "You look closer at the machines."
            you "I remember Gus saying that there's one or two of them that are so old, I might just win regardless of my spin."
            you "But the question now is: Which is the lucky one I should try?"
            menu:
                "Machine #1":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #2":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #3":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #4":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #5":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #6":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "LOST"
                    you "Uh oh... I guess this means that security is going to-"
                    show security at character_sizing
                    Security "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Machine #7":
                    "You pull the lever..."
                    "You're waiting..."
                    "You're waiting..."
                    "CONGRATULATIONS! YOU WON"
                    you "Oh, thank God."
                    "You collect your earnings and continue on your way throughout the casino, trying to find where the vault may be."
        "No, I have too much on the line here.":
            "You leave the machines and continue on your way throughout the casino, trying to find where the vault may be."

label roulette:        
    show bg roulette
    with fade
    you "Ahh, here's the roulette table that Gus was mentioning."
    you "I'm just not sure if I want to try my luck with this..."
    menu:
        "Go for it: It's a 50/50 chance!":
            you "There's a 50% chance I bet correctly. Now what should that bet be? What color seems to be the most related to Tempest Casino?"
            menu:
                "Red":
                    "The game starts."
                    "You're waiting..."
                    "You're waiting..."
                    "And..."
                    "It landed on red!"
                    you "Yes!"
                    "You collect your earnings and leave promptly, still trying to figure out how to get to that vault."
                "Green":
                    "The game starts."
                    "You're waiting..."
                    "You're waiting..."
                    "And..."
                    "It landed on red."
                    you "Oh no... I should run-"
                    show security at character_sizing
                    Secrity "Where do you think you're going?"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
        "No, I should really start looking for that safe.":
            "You leave the table and promptly leave, still trying to figure out how to get to that vault."

label search:
    show bg casino
    with fade
    "You feel as though you've been searching forever, constantly looking preoccupied as not to raise suspicion."
    "Suddenly, you hear static in your concealed ear piece: Gus."
    show Gus neutral at character_sizing
    Gus "Hey, I'm glad to see you're still hanging in there, kid."
    Gus "Now listen, I've got a guy on the inside who told me how to access the room where the vault is stored and you only need to remember three directions."
    hide Gus neutral
    you "Only three? So much for high-security casino..."
    show Gus angry at character_sizing
    Gus "You better not be complaining! I had to give away a pretty penny for that information."
    show Gus neutral at character_sizing
    Gus "Anyways, all you need to remember is left, right, straight. And remember, on your way back, the order of directions will be ba-"
    "He suddenly cuts off."
    hide Gus neutral
    you "Okay... Here goes nothing..."
    "You continue to aimlessly look for some sort of room or hallway that could lead you to this vault."

label passage:
    show bg hallway
    with fade
    "You've been searching for a passage all while keeping a low profile when you find yourselves in a network of dark hallways."
    you "This must be the hallways that lead to the vault."
    you "Now what was the order that Gus said I had to go in?"
    menu:
        "Right":
            "You take a right."
            "The only think accompanying you on your walk is the sound of your footsteps."
            "When suddenly..."
            show security at character_sizing
            Security "HEY!"
            hide security
            show bg skyline
            with fade
            "You failed."
            return

        "Straight":
            "You go straight."
            "The only think accompanying you on your walk is the sound of your footsteps."
            "When suddenly..."
            show security at character_sizing
            Security "HEY!"
            hide security
            show bg skyline
            with fade
            "You failed."
            return

        "Left":
            "You take a left."
            you "Now what?"
            menu:
                "Right":
                    "You take a right."
                    you "What next?"
                    menu:
                        "Right":
                            "You take a right."
                            "The only think accompanying you on your walk is the sound of your footsteps."
                            "When suddenly..."
                            show security at character_sizing
                            Security "HEY!"
                            hide security
                            show bg skyline
                            with fade
                            "You failed."
                            return
               
                        "Straight":
                            "You go straight."
                            "You keep walking down the hallway, growing more scared as the sound of your footsteps echo in your head."
                            "Suddenly, you come across a room with a massive vault."
                        "Left":
                            "You take a left."
                            "The only think accompanying you on your walk is the sound of your footsteps."
                            "When suddenly..."
                            show security at character_sizing
                            Security "HEY!"
                            hide security
                            show bg skyline
                            with fade
                            "You failed."
                            return
                "Straight":
                    "You go straight."
                    "The only think accompanying you on your walk is the sound of your footsteps."
                    "When suddenly..."
                    show security at character_sizing
                    Security "HEY!"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return
                "Left":
                    "You take a left."
                    "The only think accompanying you on your walk is the sound of your footsteps."
                    "When suddenly..."
                    show security at character_sizing
                    Security "HEY!"
                    hide security
                    show bg skyline
                    with fade
                    "You failed."
                    return


init python:
    import math
    def dial_events(event, x, y, st):
        global dial_rotate
        global old_mousepos
        global old_degrees
        global degrees
        global dial_start_rotate
        global dial_text
        global dial_number
        global previous_dial_text
        global dial_changed
        global combination_check
        global combination_length
        global completed_combination_numbers
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dial_start_rotate:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] + dial_offset and dial_sprite.y <= y <= dial_sprite.y + dial_size[1] + dial_offset:
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] - dial_offset / 2) - y, (dial_sprite.x + dial_size[0] - dial_offset / 2) - x)
                        old_degrees = math.degrees(angle_radians) % 360
                else:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] and dial_sprite.y <= y <= dial_sprite.y + dial_size[1]:
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] / 2) - y, (dial_sprite.x + dial_size[0] / 2) - x)
                        old_degrees = math.degrees(angle_radians) % 360
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                dial_rotate = False
                safe = "safe_{}".format(current_safe)
                if dial_changed:
                  
                    if combination_length < 4:
                        dial_changed = False
                        combination_check = None
                        if len(completed_combination_numbers) == 0:
                            completed_combination_numbers[safe] = []
                            completed_combination_numbers[safe].append(dial_text)
                        else:
                            completed_combination_numbers[safe].append(dial_text)
                        combination_length += 1
                    if combination_length == 4:
                        if completed_combination_numbers[safe] == combinations[safe]:
                            dial_changed = False
                            combination_length = 0
                            completed_combination_numbers = {}
                            combination_check = "correct"
                            renpy.play("audio/success.ogg", "sound")
                        else:
                            dial_changed = False
                            combination_length = 0
                            completed_combination_numbers = {}
                            combination_check = "wrong"
                            renpy.play("audio/error.ogg", "sound")
                renpy.restart_interaction()
        elif event.type == renpy.pygame_sdl2.MOUSEMOTION:
            if dial_rotate:
                angle_radians = math.atan2((dial_sprite.y + dial_size[1] / 2) - y, (dial_sprite.x + dial_size[0] / 2) - x)
                degrees = math.degrees(angle_radians) % 360
                rotate_amount = math.hypot(x - old_mousepos[0], y - old_mousepos[1]) / 5
                if degrees > old_degrees:
                    dial_sprite.rotate_amount += rotate_amount
                elif degrees < old_degrees:
                    dial_sprite.rotate_amount -= rotate_amount

                t = Transform(child = dial_image, zoom = 0.5)
                t.rotate = 3.6 * round(dial_sprite.rotate_amount / 3.6)
                if int(t.rotate / 3.6) % 100 == 0 and int(t.rotate / 3.6) != 0:
                    dial_number = 0
                    dial_sprite.rotate_amount = 0.0
                else:
                    dial_number = int(t.rotate / 3.6)

                
                if dial_number > 0:
                    
                    dial_text = 100 - dial_number
                elif dial_number < 0:
                    dial_text = abs(dial_number)
                else:
                    dial_text = dial_number

                
                if dial_text != previous_dial_text:
                    dial_changed = True
                    renpy.music.play("audio/dial.ogg", "sound", relative_volume = 0.3)

                previous_dial_text = dial_text

                t.subpixel = True
                dial_start_rotate = True
                dial_sprite.set_child(t)
                dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2 - dial_offset
                dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2 - dial_offset
                old_degrees = math.degrees(angle_radians) % 360
                old_mousepos = (x, y)
                dial_sprite_manager.redraw(0)
                renpy.restart_interaction()

    def reset_safe():
        global dial_number
        global dial_text
        global completed_combination_numbers
        global combination_length
        global combination_check
        global dial_start_rotate

        dial_number = 0
        dial_text = 0
        dial_sprite.rotate_amount = 0
        completed_combination_numbers = {}
        combination_length = 0
        combination_check = None
        dial_start_rotate = False

        t = Transform(child = dial_image, zoom = 0.5)
        dial_sprite.set_child(t)
        dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2
        dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2
        dial_sprite_manager.redraw(0)

screen scene_1:
    image "images/scene-1-background.png" at half_size
    imagebutton auto "images/scene-1-safe-door-%s.png" focus_mask True action [Show("safe_puzzle", Fade(1, 1, 1)), Hide("scene_1")] at half_size

screen safe_opened:
    on "show" action Hide("safe_puzzle")
    image "safe-opened-background.png" at half_size
    imagebutton auto "images/back-button-%s.png" action [Show("scene_1", Fade(1, 1, 1)), Hide("safe_opened")] align(0.95, 0.95) at half_size
    if current_safe == 1:
        image "images/money_pile.webp" at money_sizing

screen safe_puzzle:
    on "show" action Function(reset_safe)
    image "images/safe-closeup-background.png" at half_size
    if combination_check == "wrong":
        imagebutton auto "images/safe-handle-ind-red-%s.png" focus_mask True action Play(file = "audio/locked-door.ogg", channel = "sound") at half_size
        
    elif combination_check == "correct":
        imagebutton auto "images/safe-handle-ind-green-%s.png" focus_mask True action [Play(file = "audio/open-door.ogg", channel = "sound"), Show("safe_opened", transition = Fade(1, 1, 1))] at half_size
    elif combination_check == None:
        imagebutton auto "images/safe-handle-ind-normal-%s.png" focus_mask True action Play(file = "audio/locked-door.ogg", channel = "sound") at half_size
    image "images/dial-shadow.png" align(0.48, 0.5) alpha 0.3 at half_size
    image "images/dial-backing.png" align(0.5, 0.5) at half_size
    add dial_sprite_manager
    imagebutton auto "images/dial-reset-button-%s.png" align(0.5, 0.5) focus_mask True action Function(reset_safe) at half_size
    image "images/dial-text-background.png" align(0.5, 0.17) at half_size
    imagebutton auto "images/back-button-%s.png" align(0.95, 0.95) action [Show("scene_1", Fade(1, 1, 1)), Hide("safe_puzzle")] at half_size
    text "[dial_text]" color "#000000" align(0.505, 0.18) text_align 0.5

transform half_size:
    zoom 0.5
transform money_sizing:
    zoom 0.4
    align (0.5,1.0)
transform character_sizing:
    zoom 0.5
    align (0.01, 0.5)
label safe:
    # Dial variables
    $dial_image = "images/dial.png"
    $dial_size = (660 / 2, 660 / 2)
    $t = Transform(child = dial_image, zoom = 0.5)
    $dial_sprite_manager = SpriteManager(event = dial_events)
    $dial_sprite = dial_sprite_manager.create(t)
    $dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2
    $dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2
    $dial_rotate = False
    $dial_sprite.rotate_amount = 0
    $dial_offset = 68.2
    $dial_start_rotate = False
    $dial_number = 0
    $dial_text = 0
    $previous_dial_text = 0
    $dial_changed = False

    # Other variables
    $old_mousepos = (0.0, 0.0)
    $degrees = 0
    $old_degrees = 0
    $combinations = {"safe_1" : [3, 12, 18, 46], "safe_2" : [23, 5, 75, 44]}
    #correct combo is 3-12-18-46 (March 12, 1846. The date the casino was established.)
    $completed_combination_numbers = {}
    $combination_check = None
    $current_safe = 1
    $combination_length = 0
    call screen scene_1
    return


label end:
    "You retrace your steps and make your way out of the casino, running straight to the hospital."
    show bg hospital
    with fade
    "You sit at the side of the hospital bed with a smile on your face."
    "You warmly look down at your younger sister who has been sick for almost all of her life."
    you "We did it, Lily."
    "A tear begins to fall down your cheek."
    you "Things are going to get much better for us."