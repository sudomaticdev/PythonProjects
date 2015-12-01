import random
from champions import *

user_input = raw_input("WELCOME TO THE RANDOM CHAMP PICKER \n Please type TOP, MID, JUNGLE, ADC, or SUPPORT : ")

if user_input.lower() == "top":
    print random.choice(lol_top)
elif user_input.lower() == "mid":
    print random.choice(lol_mid)
elif user_input.lower() == "jungle":
    print random.choice(lol_jungle)
elif user_input.lower() == "adc":
    print random.choice(lol_adc)
elif user_input.lower() == "support":
    print random.choice(lol_support)
else:
    print "Please re-launch and try again."