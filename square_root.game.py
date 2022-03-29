from math import*
number_of_coins = 101


def display_state():
    global number_of_coins
    print("number of coins = ", number_of_coins)


def get_input(player):
    message = player + " : pls enter number of coins: \n "
    number_1 = int(input(message))
    if number_1 % sqrt(number_1) == 0 and number_1 <= number_of_coins:
        return number_1
    else:
        print("Error \nTry again!")


def update_state(coins_taken):
    global number_of_coins
    number_of_coins -= coins_taken


def is_loser():
    global number_of_coins
    if number_of_coins < 1:
        return True


def play_game():
    display_state()
    while True:
        player_1 = get_input("player_1")
        update_state(int(player_1))
        display_state()
        if is_loser():
            print("player 1 is winner")
            break
        player_2 = get_input("player_2")
        update_state(int(player_2))
        display_state()
        if (is_loser()):
            print("player 2 is winner")
            break


play_game()
