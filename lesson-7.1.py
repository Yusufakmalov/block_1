l = lambda x: x**2
print(l(8))

x = [1, 2, 4, "4"]
a = map(lambda d: d*2, x)
print(list(a))
def decrement_list(nums):
    o = list(map(lambda x: x-1, nums))
    return o

print(decrement_list([1, 2, 3, 4, 5,]))


x = [1, 2, 3, "4"]
a = filter(lambda d: d*2 == 4, x)
print(list(a))

x = ["Hello", "Pavel"]
a = filter(lambda d:d == "Hello", x)
print(list(a))

ex = [3.1, 3.4]
b = filter(lambda c: c*2 != 4, ex)

print(list(b))

x = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
y = list(filter(lambda d: d > 0, x))
print(list(y))
