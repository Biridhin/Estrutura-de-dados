from object import Queue


def hot_potato(step: int, namelist: list):
    names = Queue()
    for name in namelist:
        names.enqueue(name)

    while names.size > 1:
        for c in range(step):
            names.enqueue(names.dequeue())
        names.dequeue()
    return names.dequeue()


print(hot_potato(7, ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]))

