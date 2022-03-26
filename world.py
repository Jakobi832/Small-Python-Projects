from time import sleep


burger = (""" Number 15: Burger king foot lettuce.
The last thing you'd want in your Burger King burger is someone's foot fungus.
But as it turns out, that might be what you get.
A 4channer uploaded a photo anonymously to the site showcasing his feet
in a plastic bin of lettuce. With the statement:
"This is the lettuce you eat at Burger King." Admittedly, he had shoes on.
But that's even worse.  Bamboozled!!!
""")
value = 0

burger.split()
for loop in range(len(burger)-1):
    value += 1
    print(burger[value], sep='', end='', flush=True); sleep(0.1)
    
