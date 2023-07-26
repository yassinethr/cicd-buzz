from __future__ import print_function
import random


class Generator:

    def __init__(self):

        self.adverbs = ('remarkably', 'enormously', 'substantially',
                        'significantly', 'seriously')
        self.adjectives = ('complete', 'modern', 'self-service',
                           'integrated', 'end-to-end')
        self.verbs = ('accelerates', 'improves', 'enhances',
                      'revamps', 'boosts')

    def sample(self, list, n=1):
        result = random.sample(list, n)
        if n == 1:
            return result[0]
        return result
