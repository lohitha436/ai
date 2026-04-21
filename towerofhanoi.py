def hanoi(n, source, target, aux):
    if n == 1:
        print(source, "->", target)
        return
    hanoi(n-1, source, aux, target)
    print(source, "->", target)
    hanoi(n-1, aux, target, source)

hanoi(3, 'A', 'C', 'B')
