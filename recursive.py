#!/usr/bin/env pyton

def fact(n):
    if n <= 0:
        return 1

    print("{0} * {1}".format(n, n-1))
    return n * fact(n - 1)


def reverse(li):

    if not li:
        print("li is empty")
        return []

    return reverse(li[1:]) + li[:1]

def flatten(li):

    if not li:
        return li 
    elif type(li[0]) == list:
        return flatten(li[0]) + flatten(li[:1])
    elif type(li[0]) == int:
        return li[:1] + flatten(li[:1])
    else:
        print("{0} is not list".format(li[0]))
    return
                

print(fact(3))


reli = reverse([1,2,3,4])


print(reli)

flatten([[23],[23],[32]])

