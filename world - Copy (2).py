age = 16
day = "Sriday"


if age <= 6:
    message = "Free entry"
elif age <= 15 and day[0] == "S":
    message = "Half price"
else:
    message = "Full price"

alpha = False;
beta = True;
gamma = True;

if (alpha or (beta and gamma)):
    print("Trueee")
else:
        print("nah mate")

if (alpha or beta) and (alpha or gamma):
    print("T")
else:
    print("F")

people = 10
if people < 5:
    pizzas = people
elif people < 10:
    pizzas = 3 * people // 4
elif people < 15:
    pizzas = 2 * people // 3
else:
    pizzas = people // 2
print(pizzas)
