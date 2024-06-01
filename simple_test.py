import hyperloglog
hll = hyperloglog.HyperLogLog(0.01)  # accept 1% counting error
hll.add("hello")
print(len(hll))  # 1
hll.add("hello")
print(len(hll))  # 1 as items aren't added more than once
hll.add("hello again")
print(len(hll))  # 2

# add 1000 random 30 char strings to hll
import random
import string
[hll.add("".join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for n in range(30)])) for m in range(1000)]
print(len(hll))  # 1007
