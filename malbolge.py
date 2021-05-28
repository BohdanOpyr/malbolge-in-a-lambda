crz = lambda a, b: [(digits_c := [[[1, 0, 0],[1, 0, 2],[2, 2, 1]][db][da] for da, db in zip([a//(3**(9-x))%3 for x in range(10)], [b//(3**(9-x))%3 for x in range(10)])]), sum(digits_c[x]*(3**(9-x)) for x in range(10))][1]
rotate = lambda i: i//3+(i%3)*(3**9)

def mal(code):
#    memory = functools.reduce(lambda x, _: x+[crz(x[-1], x[-2])], range(3**10-len(code)), [ord(x) for x in code])# Works kinda the same way as finding fibonacci with a lambda; turned out way too slow :(
    [(memory := [ord(x) for x in code]), (memory.append(crz(memory[-1], memory[-2])) for x in range(3**10-len(code)))]
    c = [0]
    a = [0]
    d = [0]
    while 1:
        if not 33 <= memory[c[0]] <= 126:
            break
        instruction = (memory[c[0]]+c[0])%94
        if instruction == 4:
            c[0] = memory[d[0]]
        elif instruction == 5:
            print(end=chr(a[0]%256))
        elif instruction == 23:
            a[0] = ord(input())
        elif instruction == 39:
            memory[d[0]] = a[0] = rotate(memory[d[0]])
        elif instruction == 40:
            d[0] = memory[d[0]]
        elif instruction == 62:
            memory[d[0]] = a[0] = crz(a[0], memory[d[0]])
        elif instruction == 68:
            pass
        elif instruction == 81:
            break
        if 33 <= memory[c[0]] <= 126:
            memory[c[0]] %= 94
            memory[c[0]] = {0: 57, 19: 108, 38: 113, 57: 91, 76: 79, 1: 109, 20: 125, 39: 116, 58: 37, 77: 65, 2: 60, 21: 82, 40: 121, 59: 92, 78: 49, 3: 46, 22: 69, 41: 102, 60: 51, 79: 67, 4: 84, 23: 111, 42: 114, 61: 100, 80: 66, 5: 86, 24: 107, 43: 36, 62: 76, 81: 54, 6: 97, 25: 78, 44: 40, 63: 43, 82: 118, 7: 99, 26: 58, 45: 119, 64: 81, 83: 94, 8: 96, 27: 35, 46: 101, 65: 59, 84: 61, 9: 117, 28: 63, 47: 52, 66: 62, 85: 73, 10: 89, 29: 71, 48: 123, 67: 85, 86: 95, 11: 42, 30: 34, 49: 87, 68: 33, 87: 48, 12: 77, 31: 105, 50: 80, 69: 112, 88: 47, 13: 75, 32: 64, 51: 41, 70: 74, 89: 56, 14: 39, 33: 53, 52: 72, 71: 83, 90: 124, 15: 88, 34: 122, 53: 45, 72: 55, 91: 106, 16: 126, 35: 93, 54: 90, 73: 50, 92: 115, 17: 120, 36: 38, 55: 110, 74: 70, 93: 98, 18: 68, 37: 103, 56: 44, 75: 104}[memory[c[0]]]
        c[0] = (c[0]+1)%(3**10)
        d[0] = (d[0]+1)%(3**10)
assert crz(11355, 1131) == 20650
assert rotate(1823) == 39973
mal('''(=<`#9]~6ZY327Uv4-QsqpMn&+Ij"'E%e{Ab~w=_:]Kw%o44Uqp0/Q?xNvL:`H%c#DD2^WV>gY;dts76qKJImZkj''')