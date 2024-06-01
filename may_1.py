import hyperloglog
import random


def get_random_view(no_of_viewers, no_of_shows):
    """

    :param no_of_viewers: The number of potential viewers
    :param no_of_shows: The number of potential shows
    :return: A tuple of the form (n, k) where n is a random viewer ID in the range 1..no_of_viewers
        and k is a random show in the range 1..no_of_shows
    """
    v = random.randint(1, no_of_viewers)
    s = random.randint(1, no_of_shows)

    return v,s


def t_random():

    for i in range(0, 10):
        r = get_random_view(10, 10)
        print(r)


def t_random_2():

    no_of_tests = 10000000
    v_total = 0
    s_total = 0

    for i in range(0, no_of_tests):
        v,s = get_random_view(100, 1000000)
        v_total += v
        s_total += s

    a_v = v_total/no_of_tests
    a_s = s_total/no_of_tests

    print (a_v, a_s)


def t_hll_1():

    hll = hyperloglog.HyperLogLog(0.01)
    the_set = set()

    for i in range(0, 1000000):
        s, v = get_random_view(10, 10)
        el = str(v) + "." + str(s)
        the_set.add(el)
        hll.add(el)

    print("The set = ", the_set)
    print("The length of the set = ", len(the_set))
    print("HLL length = ", len(hll))


def t_hll_2():

    hll = hyperloglog.HyperLogLog(0.01)
    the_set = set()

    for i in range(0, 1000000):
        s, v = get_random_view(100, 1000000)
        el = str(v) + "." + str(s)
        the_set.add(el)
        hll.add(el)

    # print("The set = ", the_set)
    print("The length of the set = ", len(the_set))
    print("HLL length = ", len(hll))


def t_hll_3():

    full_hll = hyperloglog.HyperLogLog(0.01)
    the_set = set()
    v_hlls = list()
    v_sets = list()
    for i in range(0, 100):
        v_hlls.append(hyperloglog.HyperLogLog(0.01))
        v_sets.append(set())

    for i in range(0, 1000000):
        v, s = get_random_view(100, 10000)
        el = str(v) + "." + str(s)
        the_set.add(el)
        v_sets[v-1].add(s)
        full_hll.add(el)
        v_hlls[v-1].add(s)

    # print("The set = ", the_set)
    print("The length of the set = ", len(the_set))
    print("Full HLL length = ", len(full_hll))

    for i in range(0, 100):
        print("For viewer ", i, "Set = ", len(v_sets[i]), "HLL = ", len(v_hlls[i]))


if __name__ == "__main__":
    # t_random()
    # t_random_2()
    # t_hll_1()
    # t_hll_2()
    t_hll_3()


