print('===============')
print('The Enchanted Starfall')
print('===============')

# ~~~~~~~~~~~~~~~ Introduction ~~~~~~~~~~~~~~~

print('Introduction')
print('You are the Captain of the starship Lunaquest, part of a crew of curious explorers who have ventured deep into an unknown galaxy.')
print('Your mission is to explore uncharted planets, gather knowledge, and ensure the safety of your crew.')
print('But as you traverse through the cosmos, you stumble upon a mysterious planet that seems to radiate magical energy.')
print('Little do you know, this planet is home to both fairies and monsters, each with their own secrets and challenges.')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Chapter 1: The Starfall')
print('Your starship, Lunaquest, detects an unusual energy signature from a nearby planet.')
print('As you approach, you witness a spectacular phenomenon—a massive star shower, with one particularly large star fragment crashing into the planets surface.')
print('The planets atmosphere shimmers with an ethereal glow.')

print('You have two options. Choode wisely')
print('1.Investigate the Starfall: You decide to land near the crash site of the large star fragment, curious to see what secrets it holds.')
print('2.Explore the Shimmering Forest:the planets surface is covered in a vast, glowing forest. You choose to land the ship near the edge of the forest and explore its mysteries.')

answear1 = int(input('Enter answer (1-2): '))

# ~~~~~~~~~~~~~~~ Question 2A ~~~~~~~~~~~~~~~
if answear1 == 1:
    print('Chapter 2A: The Fallen Star')
    print('As you step onto the planets surface, you notice that the star fragment pulses with magical energy.')
    print('Suddenly, a group of fairies emerges from the fragment, their wings glowing brightly.')
    print('They greet you with caution, warning that the starfall has awakened a powerful monster beneath the planets surface.')

    print('You have two options. Choose wisely')
    print('1.Seek the Fairies Help: You ask the fairies to assist you in calming the monster, hoping they have the knowledge to control the situation.')
    print('2.Investigate the Monster Alone: You choose to delve deeper into the planets core, determined to face the monster on your own.')

    answear2a = int(input('Enter answer (1-2): '))

    if answear2a == 1:
        print('Peaceful Resolution: If you spared the monster or calmed it down, the fairies bless you with safe passage through the galaxy, and your crew leaves the planet in harmony.')
    elif answear2a == 2:
        print('Chapter 3A: The Monsters Awakening')
        print('You make your way to the planets core, where you find the awakened monster—a colossal beast with scales that shimmer like the stars.')
        print('As it roars, the ground trembles beneath your feet.')
        print('The monster seems unstoppable, but you notice that it hesitates whenever you get close to the star fragment you brought with you.')

        print('You have two options. Choose wisely')
        print('1.Use the Star Fragment: You attempt to use the star fragments energy to weaken the monster.')
        print('2.You decide to engage the monster in combat, relying on your weapons and skills.')

        answear3a = int(input('Enter answer (1-2): '))

        if answear3a == 1:
            # ~~~~~~~~~~~~~~~ Question 4A ~~~~~~~~~~~~~~~
            print('Chapter 4: The Final Confrontation')
            print('Path A: The Weakened Monster')
            print('The star fragments energy (or the magic from the pool) significantly weakens the monster, and you engage in a final battle. ')
            print('With your new power, you can either:')

            print('You have two options. Choode wisely')
            print('1.Destroy the Monster: You decide to end the threat once and for all, using the full extent of your power.')
            print('2.Spare the Monster:You realize that the monster is not evil, only confused and scared. You use your power to calm it and return it to its slumber.')

            answear4a = int(input('Enter answer (1-2): '))

            if answear4a == 1:
                print('Triumphant Victory: If you destroyed the monster, the planet begins to heal, and the fairies thank you for saving their world, but there is a lingering sadness for what was lost.')
            elif answear4a == 2:
                print('Peaceful Resolution: If you spared the monster or calmed it down, the fairies bless you with safe passage through the galaxy, and your crew leaves the planet in harmony.')

        elif answear3a == 2:
            print('Chapter 4: The Final Confrontation')
            print('Path B: The Mighty Beast')
            print('The battle is fierce, with the monster overpowering you at every turn.')
            print('You must rely on your crew and all your resources to survive. You can:')

            print('You have two options. Choode wisely')
            print('1.Call for Backup: You send a distress signal to your ship, asking your crew for additional firepower.')
            print('2.Fight to the Last Breath: You refuse to retreat, determined to defeat the monster even if it means risking your life.')

            answear4b = int(input('Enter answer (1-2): '))

            if answear4b == 1:
                print('Peaceful Resolution: If you spared the monster or calmed it down, the fairies bless you with safe passage through the galaxy, and your crew leaves the planet in harmony.')
            elif answear4b == 2:
                print('Narrow Escape: If you barely survived the battle, your ship is damaged but functional, and you leave the planet with a hard-earned lesson about the dangers of the unknown.')

elif answear1 == 2:
    print('Chapter 2B: The Shimmering Forest')
    print('The forest is teeming with life, its flora glowing with an otherworldly light.')
    print(' As you navigate through the dense foliage, you encounter a fairy elder who tells you of an ancient monster that has been awakened by the recent starfall.')
    print('The elder offers to guide you to a mystical pool that can grant you the power needed to defeat the monster.')

    print('You have two options. Choode wisely')
    print('1.Follow the Fairy Elder: You decide to trust the fairy elder and follow them to the mystical pool, hoping to gain the power needed to confront the monster.')
    print('2.Ignore the Elders Advice: You decide to continue exploring the forest, believing that you can find a way to defeat the monster without magical assistance.')

    answear2b = int(input('Enter answer (1-2): '))

    if answear2b == 1:
        print('Chapter 3B: The Mystical Pool')
        print('The fairy elder leads you to a hidden pool deep within the forest. ')
        print(' The water sparkles with a soft blue light, and the elder tells you that by immersing yourself in the pool, you can harness the ancient magic of the fairies.')
        print('However, the magic is dangerous and may have unforeseen consequences.')

        print('You have two options. Choode wisely')
        print('1.Immerse Yourself in the Pool: You decide to take the risk and immerse yourself in the pool, hoping to gain the power needed to face the monster.')
        print('2.Decline the Magic: You choose not to risk the unknown magic and instead rely on your wits and the fairy elders guidance to defeat the monster.')

        answear3b = int(input('Enter answer (1-2): '))

        if answear3b == 1:
            print('Triumphant Victory: If you destroyed the monster, the planet begins to heal, and the fairies thank you for saving their world, but there is a lingering sadness for what was lost.')
        elif answear3b == 2:
            print('Peaceful Resolution: If you spared the monster or calmed it down, the fairies bless you with safe passage through the galaxy, and your crew leaves the planet in harmony.')
    
    elif answear2b == 2:
        print('Narrow Escape: If you barely survived the battle, your ship is damaged but functional, and you leave the planet with a hard-earned lesson about the dangers of the unknown.')










