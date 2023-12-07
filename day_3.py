g_input_file = "d3_input" + ".txt"

def is_symbol(char):
    return not char.isdigit() and char not in ['.', '\n'] # Add more symbols as needed

def sum_of_part_numbers(engine_schematic):
    rows = engine_schematic.split('\n')
    schematic = [list(row) for row in rows]

    total_sum = 0

    print(len(schematic))
    for i in range(len(schematic)):
        is_part_number = False
        current_number = ''
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit():
                current_number += schematic[i][j]
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(schematic) and 0 <= j + y < len(schematic[i]) and is_symbol(schematic[i + x][j + y]):
                            is_part_number = True
            else:
                if is_part_number:
                    total_sum += int(current_number)
                is_part_number = False
                current_number = ''

    return total_sum

def first_part():
    result = 0
    with open(g_input_file, 'r') as input:
        matrix = input.read()
        print(matrix)
        result = sum_of_part_numbers(matrix)
    print("Res: ", result)

def second_part():
    result = 0
    with open(g_input_file, 'r') as input:
        for line in input:
            pass
    print("Res: ", result)

if __name__ == '__main__':
    first_part()
    print(is_symbol("."))
    print(is_symbol("1"))