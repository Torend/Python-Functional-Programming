

# returns the n-grams of a given list of words <---
def generate_n_grams(size, words_list):
    for i in range(len(words_list) - size + 1):
        yield [words_list[i+j] for j in range(size)]


# generate all sentences of the format ‘subject verb object'
def generate_sentence(subjects, verbs, objects):
    for i, _ in enumerate(subjects):
        yield ' '.join([subjects[i], verbs[i], objects[i]])


# generate all the permutations of a given list of elements
def generate_permutations(some_list):
    n = len(some_list)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    yield tuple(some_list[i] for i in indices[:n])
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(some_list[i] for i in indices[:n])
                break
        else:
            return

if __name__ == "__main__":
    # sentence1 = "the quick red fox jumps over the lazy brown dog"
    # print(generate_n_grams(3, sentence1))  # <generator object ngrams at 0x109a36ca8>
    # for x in generate_n_grams(3, sentence1.split()):
    #     print(x)
    #
    # s = ["I", "You"]
    # v = ["play", "love"]
    # o = ["Basketball", "Football"]
    # print(generate_sentence(s, v, o))
    # for sentence in generate_sentence(s, v, o):
    #     print(sentence)
    # x = generate_sentence(s, v, o)
    # print(next(x))
    # print(next(x))
    # for p in permutation([1, 2, 3]):
    #     print(p)
    for perm in generate_permutations([1,'a',True]): print(perm)

