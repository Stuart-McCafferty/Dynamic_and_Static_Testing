import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Spades", 5)
        self.card3 = Card("Spades", 7)
        self.card8 = Card("Spades", 9)
        self.cards = [self.card1, self.card2, self.card3]

    def test_card_has_suit(self):
        self.assertEqual("Spades", self.card1.suit)
    
    def test_card_has_value(self):
        self.assertEqual(1, self.card1.value)
    
    def test_check_for_ace_true(self):
        result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, result)
    
    def test_check_for_ace_false(self):
        result = CardGame.check_for_ace(self, self.card2)
        self.assertEqual(False, result)
    
    def test_highest_card_first(self):
        result = CardGame.highest_card(self, self.card2, self.card1)
        self.assertEqual(self.card2, result)
    
    def test_highest_card_second(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, result)
    
    def test_card_total(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 13", result)