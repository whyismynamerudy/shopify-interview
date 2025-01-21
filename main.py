# shopify interview
"""
Each year, leads at Shopify organize a holiday gift exchange for their teammates and their partners. 
Previously, the draw was done manually by using pieces of paper. As your team grows, the process becomes 
more error prone and lengthy; you've thus decided to write a program to automate it as much as possible.


If you get matched with youself, everything starts again.
"""

# we want to want to represent this as a class.

# reppresent teammates with idx
# represent relationships in a dictionary
# represent everybody reminaing in a list
# represent people chosen so far in a set - maybe

# one way thing

class GiftExchange:
    def __init__(self, n: int, relationship: dict): # n is number of people in the team
        self.n = n
        self.teammates = list(range(n)) # people remaining

        self.relationship = {}
        for k, v in relationship.items():
            self.relationship[k] = v
            self.relationship[v] = k

        self.matched = {}

    def match(self):
        # for each person in 0 to n-1 idx:
        # if person is matched:
        #     continue
        # else:
        #     match person with a random person from teammates
        #     remove person from teammates

        for i in range(self.n):
            # if i in self.matched.values():
            #     # person i has been matched to someone else prior
            #     continue
            # else:
                # get a random idx in self.teammates
            import random
            j = random.choice(self.teammates)
            while j == i or (i in self.relationship and j == self.relationship[i]):
                j = random.choice(self.teammates)

            self.matched[i] = j
            self.teammates.remove(j)

        return self.matched
    

# test
# my_test = GiftExchange(4, {})
# print(my_test.match())
# {0: 1, 1: 3, 2: 0, 3: 2}

# my_test = GiftExchange(4, {0: 2})
# print(my_test.match())
# {0: 1, 1: 2, 2: 3, 3: 0}

my_test = GiftExchange(5, {0: 2})
print(my_test.match())
# {0: 4, 1: 2, 3: 0}


        