import sys

def Fib(fibPrev, fibPrevPrev, target, fibEles):
    fibCur = fibPrev + fibPrevPrev
    if fibCur < target:
        fibEles.append(fibCur)
        Fib(fibCur, fibPrev, target, fibEles)
        
fibEles = []
target = 4000000

Fib(1, 0, target, fibEles)
print(fibEles)

sum = 0
for x, y in enumerate(fibEles):
    if y % 2 == 0:
        sum +=  y

print(sum)