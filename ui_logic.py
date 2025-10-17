from main import GameEngine, Deck, Hand

deck = Deck()
deck.shuffle()
game = GameEngine(deck)
game.start()


while True:
    bet = input(f"Balance: {game.balance}: How much do you wanna bet? press [q] to quit ")
    if bet == "q":
        break
    if not bet.isdigit():
        print("Enter a number")
        continue

    bet = int(bet)
    if bet < 0:
        print("Bet must be larger than 0")
        continue
    if bet > game.balance:
        print(f"Insufficient funds. ")
        continue

    game.new_round()

    while True:
        print(f"your hand: {game.player}, dealers cards: {game.dealer}")
        player_input = input(f"[H]it or [S]tand? ")

        if player_input.lower().startswith("h"):
            game.hit_player()
            if game.player.current_hand_value() > 21:
                print(f"your hand: {game.player}, dealers cards: {game.dealer}")
                result = game.outcome()
                print(result)
                game.balance -= int(bet)
                break
            
        if player_input.lower().startswith("s"):
            game.dealer_play()
            print(f"your hand: {game.player}, dealers cards: {game.dealer}")
            result = game.outcome()

            if result == "Player wins":
                game.balance += int(bet)
            elif result == "Dealer wins":
                game.balance -= int(bet)  

            print(result)
            print(f"Your balance: {game.balance}")
            break

    if game.balance == 0:
            print(f"Game over ")
            break
        

    
    
       