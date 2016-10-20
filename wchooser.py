
import loader
import functools


def remove_newline(s):
    return s[:s.count(s)-2]


def reverse(s):
    return reduce((lambda x, y: y + x), s)


def replace_e_3(s):
    return


def main():
    lines = loader.read_lines_from("words.txt", 10, 100)
    for line in lines:
        for line2 in lines:
            print remove_newline(line) + remove_newline(line2)
        print line
        print reverse(line)


if __name__ == "__main__":
    main()
