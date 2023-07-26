from buzz.generator import Generator


class BuzzGenerator(Generator):

    def __init__(self):
        super().__init__()
        self.buzz = ('new value', 'continuous testing',
                     'continuous integration',
                     'continuous deployment', 'continuous improvement',
                     'devops')

    def generate_buzz(self):
        buzz_terms = super().sample(self.buzz, 2)
        phrase = ' '.join([super().sample(self.adjectives), buzz_terms[0],
                           super().sample(self.adverbs),
                           super().sample(self.verbs), buzz_terms[1]])
        return phrase.title()
