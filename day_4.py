g_input_file = "d4_input" + ".txt"

def first_part():
    result = 0
    with open(g_input_file, 'r') as input:
        for line in input:
            _, card_nums = line.split(":")
            winning_nums, drawn_nums = card_nums.split("|")
            winning_nums = winning_nums.strip().replace("\n", "").split(" ")
            drawn_nums = drawn_nums.strip().replace("\n", "").split(" ")
            winning_nums = set([int(n) for n in winning_nums if n != ''])
            drawn_nums = set([int(n) for n in drawn_nums if n != ''])
            matching_nums = winning_nums.intersection(drawn_nums)
            count_points =  1 if len(matching_nums) > 0 else 0  
            for p in range(1, len(matching_nums)):
                count_points *= 2
            result += count_points
    print("Res: ", result)

def second_part():
    result = 0
    with open(g_input_file, 'r') as input:
        for line in input:
            pass
    print("Res: ", result)

if __name__ == '__main__':
    first_part()