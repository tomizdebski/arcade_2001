"""
2001
Warsztat: Salon gier (*)

Zaimplementuj grę 2001. Poniżej znajdziesz zasady.

2001 – Zasady Gry
Każdy z graczy zaczyna z liczbą punktów równą 0.
W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów.
Począwszy od drugiej tury:
jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową,
jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.
Implementacja
Zaimplementuj grę w wersji dla dwóch graczy.
Niech będzie to aplikacja konsolowa.
Niech drugim graczem będzie komputer.
Po każdej turze wyświetl aktualną liczbę punktów.
Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter. 
Rzut komputera następuje automatycznie, po rzucie gracza. 
Zakończ program w momencie, gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.
Modyfikacja 1
Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko i wyłącznie, do klikania klawisza enter.
 Spróbujmy uczynić ją trochę bardziej interaktywną.

Przed każdym rzutem, daj graczowi wybór.
Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100.
Kości mogą się powtarzać, gracz może też użyć 2 różnych kości.
Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego łańcucha znaków przez gracza (po jednym na każdą z kości).
Możesz wykorzystać kod z zadania Kostka do gry.
Wybór kości przez komputer niech będzie losowy.
Reszta zasad pozostaje bez zmian.

Modyfikacja 2
Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. 
Aby przechowywać informację między turami, wykorzystaj ukryte pola formularza. 
Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie), ale na tę chwilę się tym nie przejmujemy. 
Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.
"""""

import random

DICES = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')


def throw_a_dice(input_dice):
    """
    The player rolls the dice
    :param input_dice: str  the function takes the dice roll code
    :return: int
    """
    for dice in DICES:
        if dice in input_dice:
            multiply, modifier = input_dice.split(dice)
            dice_value = int(dice[1:])
            if multiply:
                multiply = int(multiply)
            else:
                multiply = 0
            if modifier:
                modifier = int(modifier)
            else:
                modifier = 0
    score = sum([random.randint(1, dice_value) for i in range(multiply)]) + modifier
    return score


def player_throw():
    """
    main game function
    :return: str game score
    """
    player_1 = 0
    player_2 = 0
    dice = "2D6"
    dice_temp_1 = 0
    dice_temp_1 = 0
    tura = 0

    input("Start press ENTER")
    for i in range(1):  # pierwszy rzut
        player_1 = throw_a_dice(dice)
        player_2 = throw_a_dice(dice)
        tura += 1
        print(f'Po {tura} turze: player 1 = {player_1}  i player 2 ={player_2}')

    while True:
        input("kolejna tura")  # następne rzuty
        tura += 1
        dice_temp_1 = throw_a_dice(dice)
        dice_temp_2 = throw_a_dice(dice)
        if dice_temp_1 == 7:
            player_1 = int(player_1 / 7)
        elif dice_temp_1 == 11:
            player_1 = player_1 * 11
        else:
            player_1 += dice_temp_1

        if dice_temp_2 == 7:
            player_2 = int(player_2 / 7)
        elif dice_temp_1 == 11:
            player_2 = player_2 * 11
        else:
            player_2 += dice_temp_2
        print(f'Po {tura} turze: player 1 = {player_1}  i player 2 ={player_2}')

        if player_1 >= 2001 and player_2 >= 2001:
            break

    return f'player_1 wyrzucił {player_1} a player_2 wyrzucił {player_2}'


if __name__ == '__main__':
    print(player_throw())
