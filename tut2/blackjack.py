import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, n):
        if len(self.cards) > 0:
            return [self.cards.pop() for _ in range(n)]
        return []



class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value == 21

    def display(self, show_all=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for idx, card in enumerate(self.cards):
            if idx == 0 and self.dealer and not show_all and not self.is_blackjack():
                print("Hidden card")
                continue
            print(card)
        if not self.dealer:
            print(f"Value: {self.get_value()}")



class Game:
    def play(self):
        game_number = 0
        while True:
            try:
                games_to_play = int(input("How many games would you like to play? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                break

        while game_number < games_to_play:
            game_number += 1
            print(f"Starting game {game_number} of {games_to_play}...")

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print("*" * 30)
            player_hand.display()
            print()
            dealer_hand.display()
            print("*" * 30)

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Would you like to hit or stand? ").lower()
                while choice not in ["h", "hit", "s", "stand"]:
                    choice = input("Invalid input. Please enter 'Hit' or 'Stand' (or H/S). ").lower()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    print("*" * 30)
                    player_hand.display()
                    print("*" * 30)

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print(f"Final Results\nYour hand: {player_hand_value}\nDealer's hand: {dealer_hand_value}")
            self.check_winner(player_hand, dealer_hand, game_over=True)
            print("*" * 30)
            print("Thanks for playing!")


    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if player_hand.get_value() > 21:
            print("Dealer wins!")
            return True
        elif dealer_hand.get_value() > 21:
            print("You win!")
            return True
        elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("Tie")
            return True
        elif player_hand.is_blackjack():
            print("You win!")
            return True
        elif dealer_hand.is_blackjack():
            print("Dealer wins!")
            return True
        elif player_hand.get_value() > dealer_hand.get_value() and game_over:
            print("You win!")
            return True
        elif player_hand.get_value() < dealer_hand.get_value() and game_over:
            print("Dealer wins!")
            return True
        elif player_hand.get_value() == dealer_hand.get_value() and game_over:
            print("Tie")
            return True
        return False


game = Game()
game.play()