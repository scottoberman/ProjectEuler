inputs = [3, 5]

multipleLimit = 1000

multiples = set()

for curInput in inputs:
    x = 1
    curMultiple = x * curInput
    while curMultiple < multipleLimit:
        multiples.add(curMultiple)
        x += 1
        curMultiple = x * curInput

print(sum(multiples))
