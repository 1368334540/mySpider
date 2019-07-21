def add():
    for i in range(1,19):
        yield i
testyield = add()  #生成器对象， 感觉像迭代器一种对象形式哈哈~
print(testyield)
print(next(testyield))

