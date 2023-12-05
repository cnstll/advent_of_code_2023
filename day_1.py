
def first_part():
    with open('d1_input.txt', 'r') as input:
        sum_calibration_values = 0
        for line in input:
            values = list(filter(lambda c: c.isdigit(), line))
            first_calibration_value = values[0]
            last_calibration_value = values[-1]
            sum_calibration_values += int(first_calibration_value + last_calibration_value)
        print(sum_calibration_values)


def sorted_dict_by_keys(dict_to_sort):
    return dict(sorted(dict_to_sort.items()))

def second_part():
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open('d1_input.txt', 'r') as input:
        sum_calibration_values = 0
        for i, line in enumerate(input):
            digit_words_found = {}
            print(line)
            for index, word in enumerate(digit_words):
                  pos = line.find(word)
                  if pos > -1:
                    digit_words_found[pos] = word
            print(digit_words_found)
            digit_words_found = sorted_dict_by_keys(digit_words_found)
            for _, word in digit_words_found.items():
                digit = str(digit_words.index(word) + 1)
                line = line.replace(word, digit)
            print(line)
            values = list(filter(lambda c: c.isdigit(), line))
            print(values)
            first_calibration_value = values[0]
            last_calibration_value = values[-1]
            print(first_calibration_value, last_calibration_value)
            sum_calibration_values += int(first_calibration_value + last_calibration_value)
        print(sum_calibration_values)


if __name__ == '__main__':
    second_part()
