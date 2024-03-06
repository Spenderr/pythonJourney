import random
import os

word_list = [
    "Elephant", "Sunshine", "Butterfly", "Symphony", "Chocolate",
    "Adventure", "Dragonfly", "Happiness", "Universe", "Firework",
    "Whisper", "Mystery", "Rainbow", "Harmony", "Journey",
    "Serenade", "Bamboo", "Giraffe", "Moonlight", "Cascade",
    "Velvet", "Enchantment", "Tranquility", "Blossom", "Celestial",
    "Lighthouse", "Thunderstorm", "Eclipse", "Sapphire", "Caramel",
    "Galaxy", "Lullaby", "Penguin", "Aurora", "Radiance",
    "Ephemeral", "Reflection", "Marvelous", "Puzzle", "Wanderlust",
    "Majestic", "Infinity", "Ethereal", "Serendipity", "Rhapsody",
    "Zephyr", "Cascade", "Pumpkin", "Cinnamon", "Serene",
    "Tangerine", "Ethereal", "Crimson", "Starlight", "Breeze",
    "Charm", "Glisten", "Vivid", "Cerulean", "Ballet",
    "Auburn", "Lagoon", "Chrysalis", "Quasar", "Cappuccino",
    "Tranquil", "Meadow", "Mystique", "Vibrant", "Galactic",
    "Mango", "Lavender", "Radiant", "Bliss", "Mellifluous",
    "Plethora", "Solitude", "Ineffable", "Whimsical", "Effervescent",
    "Luminescent", "Incandescent", "Resplendent", "Dazzling", "Mystical",
    "Gossamer", "Quintessential", "Bucolic", "Ebullient", "Piquant",
    "Zephyr", "Lustrous", "Halcyon", "Ethereal", "Aureate",
    "Breathtaking", "Intrigue", "Serendipity", "Nostalgia", "Melancholy",
    "Ephemeral", "Enrapture", "Epiphany", "Spectacle", "Ethereal",
    "Efflorescent", "Phantasmagoria", "Enigmatic", "Cacophony", "Umbrella",
    "Mellifluous", "Quixotic", "Cynosure", "Juxtapose", "Nebula",
    "Surreptitious", "Quintessence", "Obfuscate", "Labyrinthine", "Rendezvous",
    "Penumbra", "Seraphic", "Halcyon", "Coruscate", "Pulchritude",
    "Ebullient", "Incognito", "Evanescent", "Languorous", "Susurrus",
    "Peripatetic", "Sagacious", "Quotidian", "Recumbent", "Ephemeral"
]

startPop = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

'''

six = '''
 +---+
  |   |
      |
      |
      |
      |
=========
'''
five = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
four = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
three = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
two = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
one = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

zero = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
imgArr = [zero,one,two,three,four,five,six]


print(startPop)



hangman = word_list[random.randint(0,100)]
hangList = ['_']*len(hangman)
print(hangList,"\n")






lives = 6
victory = 0

while lives>=0:
    letter = input("Enter Your guess :")
    
    found = False

    for x in range(0,len(hangman)):
        
        let = hangman[x]
        if letter.lower() == let.lower():
            
            hangList[x] = letter
            victory+=1
            found = True
    # Clearing the Screen
    os.system('clear')
  
    if victory == len(hangList):
        break
    
    
    if not found:
        lives-=1
    print(imgArr[lives])
    print(hangList,"\n")
    #print(hangList)

if lives<0:
    print("GAMEOVER :))))))")
else:
    
    print(hangList+"\nCongratulations You won :p")
    

        









