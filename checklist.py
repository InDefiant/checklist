debugger = True


class Creature:
    health = 100
    exp = 0

    def add_hp_xp(self, add_hp, add_xp):
        self.health += add_hp
        self.exp += add_xp


c1 = Creature()
print('Creature HP:' + str(c1.health))
print('Creature XP:' + str(c1.exp))


class Item:
    item_complete = False
    reward_xp = 0
    reward_hp = 0

    def __init__(self, time_to_do, what_to_do):
        self.time_to_do = time_to_do
        self.what_to_do = what_to_do

    def reward_amt(self):
        self.reward_xp = self.time_to_do / 2
        if self.time_to_do / 2 > 25:
            self.reward_hp = 25
        else:
            self.reward_hp = self.time_to_do / 2

    def complete_task(self):
        self.item_complete = True
        self.reward_amt()
        c1.add_hp_xp(self.reward_hp, self.reward_xp)


class Checklist:
    to_do_list = []

    def add_list(self, value):

        if len(self.to_do_list) < 8:
            self.to_do_list.append(value)
        else:
            for each_item in self.to_do_list:
                if each_item.item_complete:
                    self.to_do_list.remove(each_item)
                    break
            self.to_do_list.append(value)

    def del_list(self, value, index):
        self.to_do_list.remove()


if debugger:
    test = Checklist()
    test_item1 = Item(30, "Fix my Checklist")
    test_item2 = Item(30, "Create a check off function")
    test_item3 = Item(30, "Figure out the rest of the details on the list")
    test_item4 = Item(30, "Apologize to sarah because I used lists over arrays")
    test_item5 = Item(30, "Finally get sleep after tormenting self past 4am")
    test_item6 = Item(30, "Try to wake up for breakfast.")
    test_item7 = Item(30, "Most issues get fixed.")
    test_item8 = Item(30, "Attempt to test crossout function.")
    test_item9 = Item(30, "The Bed Calls to me.")
    test.add_list(test_item1)
    test.add_list(test_item2)
    test.add_list(test_item3)
    test.add_list(test_item4)
    test.add_list(test_item5)
    test.add_list(test_item6)
    test.add_list(test_item7)
    test_item2.complete_task()
    test.add_list(test_item8)
    test.add_list(test_item9)

    for item in test.to_do_list:
        print(item.what_to_do)

    print('Creature HP:' + str(c1.health))
    print('Creature XP' + str(c1.exp))
