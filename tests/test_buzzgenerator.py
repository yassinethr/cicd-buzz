import unittest
from buzz.buzzgenerator import BuzzGenerator


class TestBuzzGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.buzzgenerator = BuzzGenerator()

    def test_sample(self):
        test_values = ('foo', 'bar', 'foobar')
        generated_word = self.buzzgenerator.sample(test_values)
        self.assertIn(generated_word, test_values,
                      'Generated word not in test values')

    def test_sample_multiple(self):
        test_values = ('foo', 'bar', 'foobar', 'foofoobarbar')
        generated_words = self.buzzgenerator.sample(test_values, n=2)
        self.assertIn(generated_words[0], test_values,
                      'Generated word not in test values')
        self.assertIn(generated_words[1], test_values,
                      'Generated word not in test values')

    def test_generate_buzz(self):
        phrase = self.buzzgenerator.generate_buzz()
        self.assertGreaterEqual(len(phrase.split()), 5,
                                'Sentence not long enough')


if __name__ == '__main__':
    unittest.main()
