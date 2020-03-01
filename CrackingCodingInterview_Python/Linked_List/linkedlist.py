class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def addFromList(self,items):
        if not items:
            return 'Nothing in list'
        items = items[::-1]
        for item in items:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def linkedToList(self):
        current = self.head
        inList = []
        while current is not None:
            inList.append(current.data)
            current = current.next
        return inList

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found  = True
            else: 
                current = current.next

        return found


    def display(self):
        current = self.head
        while current is not None:
            print(current.data , end = ' ')
            current = current.next

    # def remove_duplicate(self):
    #     current = self.head
    #     unique = set()
    #     prev = None
    #     while current != None:
    #         if current.data in unique:
    #             #remove
    #             prev.next = current.next
    #         else:
    #             unique.add(current.data)
    #             prev = current
    #         current = current.next
        


# l1 = UnorderedList()
# l1.add(1)
# l1.add(2)
# l1.add(1)
# l1.add(4)
# l1.display()
# l1.remove_duplicate()
# print()
# l1.display()
