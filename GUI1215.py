from tkinter import *

# CARD START
from functools import total_ordering
import random


@total_ordering
class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 14:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __lt__(self, other):
        return self.__str__() < other.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(2, 15)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

    """回傳手牌中有的花色   e.g：['♠', '♣', '♥', '♦']"""

    def suites_on_hand(self):
        suites = []
        for card in self._cards_on_hand:
            if card.suite not in suites:
                suites.append(card.suite)
        return suites

    """列出某種花色的手牌"""

    def find_suite(self, suite):
        suites = []

        if suite == -1:
            return suites

        for card in self._cards_on_hand:
            if card.suite == suite:
                suites.append(card)

        return suites

    def __str__(self):
        return self._name

    def __repr__(self):
        return self.__str__()


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)


def okay():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)

    for player in players:
        if player.name == "南帝":
            print(player.name + ':', end=' ')
            player.arrange(get_key)
            south = player.cards_on_hand
            # print(len(south))
            # print(type(south))
            for i in south:
                if i == "♠2":
                    photo_42 = PhotoImage(file='2-spades.png')
                    button_42 = Button(root, text="♠2", image=photo_42, compound=CENTER)
                    button_42.pack()

                elif i == "♠3":
                    photo_43 = PhotoImage(file='3-spades.png')
                    button_43 = Button(root, text="♠3", image=photo_43, compound=CENTER)
                    button_43.pack()
                elif i == "♠4":
                    photo_44 = PhotoImage(file='4-spades.png')
                    button_44 = Button(root, text="♠4", image=photo_44, compound=CENTER)
                    button_44.pack()
                elif i == "♠5":
                    photo_45 = PhotoImage(file='5-spades.png')
                    button_45 = Button(root, text="♠5", image=photo_45, compound=CENTER)
                    button_45.pack()
                elif i == "♠6":
                    photo_46 = PhotoImage(file='6-spades.png')
                    button_46 = Button(root, text="♠6", image=photo_46, compound=CENTER)
                    button_46.pack()
                elif i == "♠7":
                    photo_47 = PhotoImage(file='7-spades.png')
                    button_47 = Button(root, text="♠7", image=photo_47, compound=CENTER)
                    button_47.pack()
                elif i == "♠8":
                    photo_48 = PhotoImage(file='8-spades.png')
                    button_48 = Button(root, text="♠8", image=photo_48, compound=CENTER)
                    button_48.pack()
                elif i == "♠9":
                    photo_49 = PhotoImage(file='9-spades.png')
                    button_49 = Button(root, text="♠2", image=photo_49, compound=CENTER)
                    button_49.pack()
                elif i == "♠10":
                    photo_410 = PhotoImage(file='10-spades.png')
                    button_410 = Button(root, text="♠10", image=photo_410, compound=CENTER)
                    button_410.pack()
                elif i == "♠J":
                    photo_411 = PhotoImage(file='11-spades.png')
                    button_411 = Button(root, text="♠11", image=photo_411, compound=CENTER)
                    button_411.pack()
                elif i == "♠Q":
                    photo_412 = PhotoImage(file='12-spades.png')
                    button_412 = Button(root, text="♠12", image=photo_412, compound=CENTER)
                    button_412.pack()
                elif i == "♠K":
                    photo_413 = PhotoImage(file='13-spades.png')
                    button_413 = Button(root, text="♠13", image=photo_413, compound=CENTER)
                    button_413.pack()
                elif i == "♠A":
                    button_414 = Button(root)
                    photo = PhotoImage(file='14-spades.png')
                    button_414.config(image=photo)
                    button_414.pack()
            return (south)


def start():
    btn.destroy()

    n = Label(root, text='北丐', anchor=N)
    n.config(width=50)
    n.pack()
    w = Label(root, text='西毒', anchor=W)
    w.config(width=50)
    e = Label(root, text='東邪', anchor=E)
    e.config(width=50)
    me = Label(root, text='me', anchor=S)
    me.config(width=50)
    n.pack()
    w.pack()
    e.pack()
    me.pack()
    p = Label(root, text=okay(), anchor=CENTER)
    p.config(width=60)
    p.pack()


# END

# button

root = Tk()  # 常駐主視窗
root.title("Bridge_Card")
root.geometry("400x200")
btn = Button(text="START", command=start)
btn.pack()
root.mainloop()
