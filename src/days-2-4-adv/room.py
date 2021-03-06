# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, light, *item):
        self.name = name
        self.description = description
        self.light = light
        self.items = [*item]
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def getItem(self):
        if len(self.items) != 0:
            print ("you see some thing/s on a the ground... a..\n")
            for item in self.items:
                print (f"{item.name}\n")
        else:
            print ("nothing to take here\n")

    def toggleItem(self, cmd, item):
        if cmd == "take":
            for each in self.items:
                if each.name == item:
                    global removingItem
                    removingItem = each
            if "removingItem" not in globals():
                return None
            elif removingItem.name == item:
                self.items.remove(removingItem)
                return removingItem
        elif cmd == "drop" and item not in self.items:
            self.items.append(item)
            return item
        else:
            return None

    def getRoom(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
        
        