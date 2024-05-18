# 682 Baseball Game

def calPoints(operations):

    r = []

    for op in operations:
        if op == "+":
            r.append(r[-1] + r[-2])

        elif op == "D":
            r.append(r[-1] * 2)

        elif op == "C":
            r.pop()

        else:
            r.append(int(op))
    print(sum(r))

ops = ["5","2","C","D","+"]
calPoints(ops)