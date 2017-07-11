import random


class GuessNumber:

    def __init__(self):
        self.reset()

    def reset(self):
        self.target = random.randint(1, 100)
        self.min = 1
        self.max = 100
        self.count = 0
        self.finish = False

    def guess(self, number):
        self.count += 1
        if self.target == number:
            self.finish = True
            return {
                'finish': self.finish,
                'target': self.target,
                'count': self.count
            }
        else:
            if number > self.target:
                self.max = number - 1
            else:
                self.min = number + 1
            return {
                'finish': self.finish,
                'count': self.count,
                'min': self.min,
                'max': self.max
            }

    def report(self):
        return {
            'min': self.min,
            'max': self.max,
            'count': self.count,
            'finish': self.finish
        }
