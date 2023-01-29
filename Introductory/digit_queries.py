import itertools


def iter_number_groups():
    processed = 0
    for digits in itertools.count(start=1):
        number_cnt = 10 ** digits - 1 - processed
        yield digits, number_cnt
        processed += number_cnt


def get_pos_in_group(abs_pos):
    for digit_cnt, number_cnt in iter_number_groups():
        if abs_pos < number_cnt * digit_cnt:
            return digit_cnt, abs_pos
        abs_pos -= number_cnt * digit_cnt


def get_pos_in_number(digit_cnt, pos):
    number_pos, pos_in_number = divmod(pos, digit_cnt)
    number = 10 ** (digit_cnt - 1) + number_pos
    return number, pos_in_number


def get_digit(pos):
    digit_cnt, number_cnt = get_pos_in_group(pos)
    number, pos_in_number = get_pos_in_number(digit_cnt, number_cnt)
    return str(number)[pos_in_number]


def main():
    q = int(input())
    for _ in range(q):
        pos = int(input())
        print(get_digit(pos - 1))


main()
