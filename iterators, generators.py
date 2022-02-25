nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, list_):
        self.list = list_
        self.lev_1 = 0
        self.lev_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.item = self.list[self.lev_1][self.lev_2]
        self.lev_2 += 1
        if len(self.list[self.lev_1]) == self.lev_2:
            self.lev_2 = 0
            self.lev_1 += 1
        if len(self.list) == self.lev_1:
            raise StopIteration
        return self.item

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


nested_list_ = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def flat_generator(nested_list_):
    for value in nested_list_:
        for item_ in value:
            yield item_

for item_ in flat_generator(nested_list_):
    print(item_)

