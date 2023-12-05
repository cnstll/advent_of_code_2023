# 12 red cubes, 13 green cubes, and 14 blue cubes
g_input_file = "d2_input" + ".txt"
g_max_rgb = {"red": 12, "green": 13, "blue": 14}

def get_game_id(line):
    game = line.split(":")[0]
    game_id = int(game.split(" ")[1])
    return game_id

def first_part():
    result = 0
    with open(g_input_file, 'r') as input:
        for i, line in enumerate(input):
            feasible_game = True
            print(line, end='')
            game_id = get_game_id(line)
            game_sets = (line.replace("\n","").split(":")[1]).split(";")
            # print(game_sets)
            for game_set in game_sets:
                cubes = game_set.lstrip().split(", ")
                for i, cube in enumerate(cubes):
                    cube_count, cube_color = cube.split(" ")
                    if g_max_rgb.get(cube_color) < int(cube_count):
                        feasible_game = False
                        break
                if feasible_game == False:
                    break
            if feasible_game == True:
                result += game_id    
            # print(game_id)
            # print(game_sets)
    print("\nRes: ", result)

def second_part():
    result = 0
    with open(g_input_file, 'r') as input:
        for i, line in enumerate(input):
            current_max_rgb = {"red": 0, "green": 0, "blue": 0}
            game_sets = (line.replace("\n","").split(":")[1]).split(";")
            for game_set in game_sets:
                cubes = game_set.lstrip().split(", ")
                for i, cube in enumerate(cubes):
                    cube_count, cube_color = cube.split(" ")
                    if current_max_rgb.get(cube_color) < int(cube_count):
                        current_max_rgb[cube_color] = int(cube_count)
            power = 1
            for value in current_max_rgb.values():
                power *= value
            result += power
            if i> 2: exit()
    print("\nRes: ", result)

if __name__ == '__main__':
    second_part()