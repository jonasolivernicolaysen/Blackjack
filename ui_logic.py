from main import GameEngine, Deck

deck = Deck()
deck.shuffle()
game = GameEngine(deck)
game.start()


while True:
    print(f"your hand: {game.player}, dealers cards: {game.dealer}")
    player_input = input(f"[H]it or [S]tand? ")

    if player_input.lower().startswith("h"):
        game.player.add(game.deck.deal())
        
    if player_input.lower().startswith("s"):
        game.dealer_play()
        print(f"your hand: {game.player}, dealers cards: {game.dealer}")
        result = game.outcome()
        print(result)
        break

        

    
    
       