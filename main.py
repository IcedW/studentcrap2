import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.toilet = 0
        self.alive = True
        self.hunger = 30
        self.loudness = 30

    def to_go_to_the_toilet(self):
        print("pissing")
        self.toilet =- 5
        self.happiness -= 3

    def to_sleep(self):
        print("sleep")
        self.happiness += 3
        self.hunger =+ 1

    def to_chill(self):
        print("do useless stuff for long time")
        self.toilet += 2
        self.happiness += 5
        self.hunger += 1

    def to_eat(self):
        print("i hungah must eat")
        self.toilet += 2
        self.hunger -= 1
        self.happiness -= 2
    def to_loud(self):
        self.happiness += 5
        self.loudness += 5

    def is_alive(self):
        if self.toilet >= 20:
            print("you crapped yourself")
            self.alive = False
        elif self.happiness <= 0:
            print("u has depression now")
            self.alive = False
        elif self.hunger > 60:
            print("u has ate too much.")
            self.alive = False
        elif self.hunger < 0:
            print("u has not eaten so you ded.")
            self.alive = False
        elif self.loudness > 60:
            print("Bad cat stop being a bad cat now go think about ur life outside.")
            self.alive = False



    def end_of_the_day(self):
        print(f"Happiness = {self.happiness}")
        print(f"Toilet = {round(self.toilet)} needing to pee level.")
        print(f"Hunger = {round(self.hunger)} needing to eat level")
        print(f"Owner`s temper {self.loudness}")

    def days_of_life(self, day):
        day = "Day " + str(day) + "of" + self.name + "live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_go_to_the_toilet()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_loud()
        elif live_cube == 5:
            self.to_sleep()
        self.end_of_the_day()
        self.is_alive()



cat = Cat(name = "cat")
for day in range (366):
    if cat.alive == False:
        break
    cat.days_of_life(day)
