from main import GameEngine, Deck

deck = Deck()
deck.shuffle()

game = GameEngine(deck)
game.start()

while True:
    print(f"your cards: {game.player}, dealers cards: {game.dealer}")
    player_input = input(f"do you wanna hit or stand? ")

    
    if player_input == "hit":
        game.player.add(game.deck.deal())
        print(game.outcome())
        game.dealer_play()

    if player_input == "stand":
        game.dealer_play()
        print(game.outcome())
        break
    
