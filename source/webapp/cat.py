from random import random, randint


class Cat:
    name = None
    age = randint(1, 13)
    fullness = 50
    happiness = 50
    activity = 50

    @classmethod
    def action(cls, action):
        if action:
            if action == 'play':
                cls.play()
            elif action == 'eat':
                cls.eat()
            else:
                cls.sleep()

    @classmethod
    def play(cls):
        if random() < 0.3:
            cls.happiness = 0
        else:
            cls.happiness += 15
            cls.fullness -= 10

    @classmethod
    def eat(cls):
        if cls.fullness >= 100:
            pass
        else:
            cls.fullness += 15
            cls.happiness += 5

    @classmethod
    def sleep(cls):
        cls.activity += 15
