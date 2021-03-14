#########################################
##### Name:     Moeki Kurita        #####
##### Uniqname: mkurita             #####
#########################################

import unittest
import hw5_cards_ec2


class TestHand(unittest.TestCase):

    def test_remove_pairs(self):
        """Test if Hand.remove_pairs() works as specified
        Apply remove_paris() on three different scenarios
        (one pair, three of a kind, four of a kind)
        """
        # four cards of the same rank
        dupe1 = hw5_cards_ec2.Card(suit=0, rank=3)
        dupe2 = hw5_cards_ec2.Card(suit=1, rank=3)
        dupe3 = hw5_cards_ec2.Card(suit=2, rank=3)
        dupe4 = hw5_cards_ec2.Card(suit=3, rank=3)
        # unrelated cards
        c1 = hw5_cards_ec2.Card(suit=1, rank=5)
        c2 = hw5_cards_ec2.Card(suit=3, rank=10)

        # test one pair
        h = hw5_cards_ec2.Hand([dupe1, dupe2, c1, c2])
        h.remove_pairs()
        self.assertEqual(h.cards, [c1, c2])
        # test three of a kind
        h = hw5_cards_ec2.Hand([dupe1, dupe2, dupe3, c1, c2])
        h.remove_pairs()
        self.assertEqual(len(h.cards), 3)
        # test four of a kind
        h = hw5_cards_ec2.Hand([dupe1, dupe2, dupe3, dupe4, c1, c2])
        h.remove_pairs()
        self.assertEqual(h.cards, [c1, c2])

    def test_deal(self):
        """Test if Deck.deal() works as specified
        Apply four different combinations of arguments
        (exceed deck size, normal case, -1 when even, -1 not even)
        """
        # exceed limit (request more than 52 cards)
        d = hw5_cards_ec2.Deck()
        hands = d.deal(num_hands=6, num_cards=10)
        self.assertEqual(hands, [])

        # 4 players with 5 cards each
        d = hw5_cards_ec2.Deck()
        hands = d.deal(num_hands=4, num_cards=5)
        self.assertEqual(len(hands), 4)
        for hand in hands:
            self.assertEqual(len(hand.cards), 5)
            self.assertIsInstance(hand, hw5_cards_ec2.Hand)
        
        # 4 players, deal all the cards in the deck (even)
        d = hw5_cards_ec2.Deck()
        hands = d.deal(num_hands=4, num_cards=-1)
        for hand in hands:
            self.assertEqual(len(hand.cards), 13)

        # 5 players, deal all the cards in the deck (not even)
        d = hw5_cards_ec2.Deck()
        hands = d.deal(num_hands=5, num_cards=-1)
        # first two players should have 11 cards
        for hand in hands[:2]:
            self.assertEqual(len(hand.cards), 11)
        # the rests should have 10 cards
        for hand in hands[2:]:
            self.assertEqual(len(hand.cards), 10)


if __name__ == "__main__":
    unittest.main()
