debugger = True


class Creature:
    health = 100
    exp = 0

    def add_hp_xp(self, add_hp, add_xp):
        self.health += add_hp
        self.exp += add_xp

    def time_up(self):
        lose_hp = -15
        self.add_hp_xp(lose_hp, 0)


c1 = Creature()
print('Creature HP:' + str(c1.health))
print('Creature XP:' + str(c1.exp))


class Item:
    item_complete = False
    reward_xp = 0
    reward_hp = 0

    def __init__(self, timer_start, timer_end, what_to_do, item_value):
        self.timer_start = timer_start
        self.timer_end = timer_end
        self.what_to_do = what_to_do
        self.item_value = item_value

    def reward_amt(self):
        self.reward_xp = (self.timer_end - self.timer_start) * self.item_value / 2
        if (self.timer_end - self.timer_start) / 2 > 25:
            self.reward_hp = 25
        else:
            self.reward_hp = (self.timer_end - self.timer_start) / 2

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

    time_start = 30
    time_end = 60
    item_weight = 2
    test = Checklist()
    test_item1 = Item(time_start, time_end, "Fix my Checklist", item_weight)
    test_item2 = Item(time_start, time_end, "Create a check off function", item_weight)
    test_item3 = Item(time_start, time_end, "Figure out the rest of the details on the list", item_weight)
    test_item4 = Item(time_start, time_end, "Apologize to sarah because I used lists over arrays", item_weight)
    test_item5 = Item(time_start, time_end, "Finally get sleep after tormenting self past 4am", item_weight)
    test_item6 = Item(time_start, time_end,"Try to wake up for breakfast.", item_weight)
    test_item7 = Item(time_start, time_end, "Most issues get fixed.", item_weight)
    test_item8 = Item(time_start, time_end, "Attempt to test crossout function.", item_weight)
    test_item9 = Item(time_start, time_end, "The Bed Calls to me.", item_weight)
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
