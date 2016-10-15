import math


# 分页器
class Pagination():
    def __init__(self, page, per_num, data):
        self.page = page
        self.per_num = per_num
        self.iterable = data
        self.total = len(data)

    @property
    def total_page(self):
        return int(math.ceil(self.total/self.per_num))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.total_page

    @property
    def pager(self):
        return list(range(1, self.total_page+1))

    @property
    def items(self):
        index = self.page - 1
        start = index * self.per_num
        end = start + self.per_num
        return self.iterable[start: end]

if __name__ == '__main__':
    aa = list(range(1,20))
    data = Pagination(4, 5, aa)
    print(data.items, data.has_next)