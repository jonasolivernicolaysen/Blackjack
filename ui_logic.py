from main import GameEngine, Deck

deck = Deck()
deck.shuffle()
game = GameEngine(deck)
game.start()


while True:
    print(f"your hand: {game.player}, dealers cards: {game.dealer}")
    player_input = input(f"[H]it or [S]tand? ")

    if player_input.lower().startswith("h"):
        game.hit_player()
        if game.player.current_hand_value() > 21:
            print(f"your hand: {game.player}, dealers cards: {game.dealer}")
            result = game.outcome()
            print(result)
            break
        
    if player_input.lower().startswith("s"):
        game.dealer_play()
        print(f"your hand: {game.player}, dealers cards: {game.dealer}")
        result = game.outcome()
        print(result)
        break

        

    
    
       