import sys

singles = [
    ":",
    "l",
    "u",
    "c",
    "C",
    "t",
    "r",
    "d",
    "f",
    "{",
    "}",
    "[",
    "]",
    "q",
    "4",
    "6",
    "M",
    "Q",
    "k",
    "K",
    "E"
]

doubles = [
    "T",
    "p",
    "$",
    "^",
    "D",
    "'",
    "@",
    "z",
    "Z",
    "<",
    ">",
    "_",
    "!",
    "/",
    "(",
    ")",
    "L",
    "R",
    "+",
    "-",
    ".",
    ",",
    "y",
    "Y",
    "e"
]

triples = [
    "x",
    "O",
    "i",
    "o",
    "s",
    "=",
    "%",
    "*",
    "3"
]

quads = [
    "X"
]

def print_rule(line, num_args):
    # print the function char
    num_consumed = 0
    print(line[0], end="")
    line = line[1:]
    num_consumed += 1
    # for each arg in function, determine if hex or not and print
    for arg in range(0,num_args):
        if len(line) > 2 and line[0]=='\\' and line[1]=='x':
            print(line[:4], end ="")
            line = line[5:]
            num_consumed += 4
        else:
            print(line[0], end ="")
            line = line[1:]
            num_consumed +=1
    print(" ", end="")
    return num_consumed



def format(rules_file):
    with open(rules_file) as file:
        for line in file:
            line = line.rstrip('\r\n')
            while len(line) != 0:
                if line[0] in singles:
                    num_consumed = print_rule(line=line, num_args=0)
                    line = line[num_consumed:]
                elif line[0] in doubles:
                    num_consumed = print_rule(line=line, num_args=1)
                    line = line[num_consumed:]
                elif line[0] in triples:
                    num_consumed = print_rule(line=line, num_args=2)
                    line = line[num_consumed:]
                elif line[0] in quads:
                    num_consumed = print_rule(line=line, num_args=3)
                    line = line[num_consumed:]
                else:
                    print("ERROR: incompatible rule found")
                    print("rule: {}".format(line))
                    exit()
            print()


def help():
    print("""
          syntax: python rulesformatter.py file
          """)
    exit()

def main():
    if len(sys.argv) != 2:
        help()
    rules_file = sys.argv[1]
    format(rules_file)

if __name__ == "__main__":
    main()
