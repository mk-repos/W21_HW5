#########################################
##### Name:     Moeki Kurita        #####
##### Uniqname: mkurita             #####
#########################################

import unittest
import hw5_cards_ec1


class TestHand(unittest.TestCase):

    def test_initialize_Hand(self):
        """Test that a hand is initialized properly
        """
        d = hw5_cards_ec1.Deck()
        init_cards = d.deal_hand(5)
        h = hw5_cards_ec1.Hand(init_cards)

        # number of cards in the hand
        self.assertEqual(len(h.cards), 5)
        # resulted in the same list as the initializer
        self.assertEqual(h.cards, init_cards)
        # instance of each card
        for c in h.cards:
            self.assertIsInstance(c, hw5_cards_ec1.Card)

    def testAddAndRemove(self):
        """Test add_card() and remove_card() work properly
        Compare the number of cards before/after the method
        """
        # starts with 5 cards in the hand
        init_cards = [hw5_cards_ec1.Card(suit=0, rank=1),
                      hw5_cards_ec1.Card(suit=1, rank=3),
                      hw5_cards_ec1.Card(suit=2, rank=5),
                      hw5_cards_ec1.Card(suit=3, rank=7),
                      hw5_cards_ec1.Card(suit=0, rank=13)]
        h = hw5_cards_ec1.Hand(init_cards)

        # check add_card()
        # doesn't increase if already exist
        num_before = len(h.cards)
        h.add_card(hw5_cards_ec1.Card(suit=0, rank=1))
        num_after = len(h.cards)
        self.assertEqual(num_before, num_after, 5)
        # increase if not exist
        num_before = len(h.cards)
        h.add_card(hw5_cards_ec1.Card(suit=1, rank=1))
        num_after = len(h.cards)
        self.assertEqual(num_before + 1, num_after, 6)

        # check remove_card()
        # decrease if already exist
        num_before = len(h.cards)
        h.remove_card(hw5_cards_ec1.Card(suit=1, rank=1))
        num_after = len(h.cards)
        self.assertEqual(num_before - 1, num_after, 5)
        # doesn't decrease if not exist
        num_before = len(h.cards)
        h.remove_card(hw5_cards_ec1.Card(suit=2, rank=2))
        num_after = len(h.cards)
        self.assertEqual(num_before, num_after, 5)

    def testDraw(self):
        """Test draw() works as specified
        Compare the number of cards before/after the method
        """
        d = hw5_cards_ec1.Deck()
        d_num_before = len(d.cards)
        h = hw5_cards_ec1.Hand([])
        # check if the hand increases by 1
        num_before = len(h.cards)
        h.draw(d)
        num_after = len(h.cards)
        self.assertEqual(num_before + 1, num_after, 1)
        # check if the deck decreases by 1
        d_num_after = len(d.cards)
        self.assertEqual(d_num_before - 1, d_num_after, 51)


if __name__ == "__main__":
    unittest.main()
