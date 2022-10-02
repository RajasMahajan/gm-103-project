import random
# del list
openit = open('dataone.txt', 'a+')

Well = True
while Well:
    thatone = ['He will win who knows when to fight and when not to fight.','Appear weak when you are strong, and strong when you are weak.','if you know enemy and your self you are ready to fight 1000 battles.','You have to believe in yourself.','All the rules are form Art of war']
    talkto_me = input('Type gm: ')
    if(talkto_me == 'gm'):
        print(thatone[random.randint(0,4)])
else:
    print("Bye")
    Well = False
    
