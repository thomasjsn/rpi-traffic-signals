import time, os

symbols = {
    "empty": [
        r"      ",
        r"      ",
        r"      ",
        r"      ",
        r"      "
    ],
    "cross": [
        r" \  / ",
        r"  \/  ",
        r"  /\  ",
        r" /  \ ",
        r"      "
    ],
    "left_arrow": [
        [
            r"    / ",
            r"   /  ",
            r"  /   ",
            r" /    ",
            r"      "
        ],
        [
            r"    / ",
            r"|  /  ",
            r"| /   ",
            r"|/    ",
            r" ---- "
        ]
    ],
    "warning": [
        r"|    |",
        r"      ",
        r"      ",
        r"      ",
        r"      "
    ]
}


gpio = [
    [ 1, 2, 0, 0, 3, 4],
    [ 5, 0, 6, 7, 0, 8],
    [ 9, 0,10,11, 0,12],
    [13,14, 0, 0,15,16],
    [ 0,17,18,19,20, 0]
]


def show(symbol):
    os.system('clear')

    for i in range(len(symbol)):

        for i2 in range(len(symbol[i])):
            print(symbol[i][i2], end="")
            #if symbol[i][i2] != " ":
                #print(gpio[i][i2])

        print()


while(True):
    for _ in range(4):
        show(symbols["warning"])
        time.sleep(0.1)
        show(symbols["empty"])
        time.sleep(0.1)

    for arrow in symbols["left_arrow"]:
        show(arrow)
        time.sleep(0.2)
    time.sleep(0.3)
