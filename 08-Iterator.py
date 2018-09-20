from collections.abc import Iterator,Iterable,Generator

# la = 'abc'

# lg = (x for x in la)
# print(lg)

# lat = iter(la)
# print(lat)


# print(isinstance(lg, Iterator))
# # True
# lgt = iter(lg)
# print(isinstance(lgt, Iterator))
# # True
# print(isinstance(lg, Generator))
# # True


def numbers():
    n = 1
    yield n
    n += 1

print(next(numbers()))
print(isinstance(numbers(), Iterator))
print(isinstance(numbers(), Generator))
print(numbers())
