

# for every element x in the list x=x*2+1
def p1i1lc(inputlist):
    return [x * 2 + 1 for x in inputlist]


# for every element x in the list x=x*2+1
def p1i1fo(inputlist):
    return list(map(lambda x: x * 2 + 1, inputlist))


# for every element x in the list if x divided by 3 without earth division write true otherwise false
def p1i2lc(inputlist):
    return [True if x % 3 == 0 else False for x in inputlist]


# for every element x in the list if x divided by 3 without earth division write true otherwise false
def p1i2fo(inputlist):
    return list(map(lambda x: True if x % 3 == 0 else False, inputlist))


# for every element x in the list x=x^2
def p1i3lc(inputlist):
    return [x*x for x in inputlist]


# for every element x in the list x=x^2
def p1i3fo(inputlist):
    return list(map(lambda x: x*x, inputlist))


# every word on the list converts to the upper case of the first letter
def p1i4lc(inputlist):
    return [x[0].upper() for x in inputlist]


# every word on the list converts to the upper case of the first letter
def p1i4fo(inputlist):
    return list(map(lambda x: x[0].upper(), inputlist))


# return only words with the letter 'p'
def p1i5lc(inputlist):
    return [x for x in inputlist if 'p' in x]


# return only words with the letter 'p'
def p1i5fo(inputlist):
    return list(filter(lambda x: 'p' in x, inputlist))


# for every word in the list word convert to (word,len(word))
def p1i6lc(inputlist):
    return [(word, len(word)) for word in inputlist]


# for every word in the list word convert to (word,len(word))
def p1i6fo(inputlist):
    return list(map(lambda word: (word, len(word)), inputlist))


# shows only the odd numbers of the list
def p1i7lc(inputlist):
    return [x for x in inputlist if x % 2 != 0]


# shows only the odd numbers of the list
def p1i7fo(inputlist):
    return list(filter(lambda x: x % 2 != 0, inputlist))


# shows only the even indexes of the list
def p1i8lc(inputlist):
    return [inputlist[x] for x in range(len(inputlist)) if x % 2 == 0]


# shows only the even indexes of the list
def p1i8fo(inputlist):
    return list(map(lambda index: inputlist[index], filter(lambda x: x % 2 == 0, range(len(inputlist)))))

#
# import time
#
# # Timer Decorator
# def timer(func):
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter() # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter() # 2
#         run_time = end_time - start_time # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer
#


#if __name__ == "__main__":
    # lst1 = [0, 1, 2, 3]
    # lst2 = [3, 5, 9, 8]
    # lst3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # lst4 = ["apple", "orange", "pear"]
    # lst7 = [0, 1, 2, 3, 4, 5, 6, 8]
    # lst8 = [1, 2, 4, 5, 7]
    # print(p1i1lc(lst1))
    # print(p1i1fo(lst1))
    # print(p1i2lc(lst2))
    # print(p1i2fo(lst2))
    # print(p1i3lc(lst3))
    # print(p1i3fo(lst3))
    # print(p1i4lc(lst4))
    # print(p1i4fo(lst4))
    # print(p1i5lc(lst4))
    # print(p1i5fo(lst4))
    # print(p1i6lc(lst4))
    # print(p1i6fo(lst4))
    # print(p1i7lc(lst7))
    # print(p1i7fo(lst7))
    # print(p1i8lc(lst8))
    # print(p1i8fo(lst8))
    # tt = timer(p1i3lc)
    # tt2 = timer(p1i3fo)
    # print(tt2(lst3))
    # print(tt(lst3))



