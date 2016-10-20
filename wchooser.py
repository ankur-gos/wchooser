
import loader


def remove_newline(s):
    return s[:s.count(s)-2]


def reverse(s):
    return reduce((lambda x, y: y + x), s)


def replace_e_3(s):
    return s.replace('e', '3')


def replace_i_1(s):
    return s.replace('i', '1')


def replace_i_exc(s):
    return s.replace('i', '!')


def main():
    lines = loader.read_lines_from("words.txt", 10, 100)
    for line in lines:
        for line2 in lines:
            print remove_newline(line) + remove_newline(line2)
        print line
        print reverse(line)
        print replace_e_3(line)
        print replace_i_1(line)
        print replace_i_exc(line)


if __name__ == "__main__":
    main()
