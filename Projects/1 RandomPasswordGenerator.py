import string
import random
def id_generator_six(size = 6 , chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator_twelve(size = 12 , chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

user_input = raw_input("Receive your randomized I.D. number here. Would you like a 6 or 12 charactar password? :  ")

if user_input.lower() == "6":
    print "Your new I.D. number will be generated below, please write it down for future use..."
    print id_generator_six()
elif user_input.lower() == "12":
    print "Your new I.D. number will be generated below, please write it down for future use..."
    print id_generator_twelve()
else:
    print "Please enter a correct command."
//

    
    
