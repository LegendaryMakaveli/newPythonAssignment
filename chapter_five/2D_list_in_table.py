def display_table(table):
    rows =  len(table)
    cols = len(table[0])

    print("    ", end="")
    for c in range(cols):
        print(f"{c:4}", end="")
    print()

    for r in range(rows):
        print(f"{r:3}", end=" ")
        for c in range(cols):
            print(f"{table[r][c]:4}", end="")
        print()


data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
display_table(data)
