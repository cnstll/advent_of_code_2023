g_input_file = "d6_input" + ".txt"
from math import sqrt, ceil, floor

def first_part():
    result = 1
    with open(g_input_file, 'r') as input:
        # Extract data
        _, race_duration = input.readline().rstrip('\n').split(":")
        _, distances = input.readline().rstrip('\n').split(":")
        race_duration = [int(t) for t in race_duration.split(" ") if t.isdigit()]
        distances = [int(d) for d in distances.split(" ") if d.isdigit()]
        # Go through each races and determine the num of optimal press time
        for duration, best_distance in zip(race_duration, distances):
            # Optimizing for (duration - press_time) * press_time > best_distance
            # Comes down to solving a polynomial equation of 2nd order for 0
            # - t^2 + duration * t - best_distance > 0 
            # Solve t^2 - duration * t + best_distance < 0 
            # with a = 1, b = - duration, c = best_distance
            # delta = b^2 - 4ac
            # delta = duration^2 - 4 * best_distance
            delta = duration * duration - 4 * best_distance
            t1 = round((duration - sqrt(delta)) / 2)
            t2 = round((duration + sqrt(delta)) / 2)
            def sol(t): return - t * t + duration * t - best_distance
            if sol(t1 - 1) >= 0:
                if sol(t1) <= 0:
                    t1 -= 1
                if sol(t2) <= 0:
                    t2 += 1
            if sol(t1 + 1) >= 0:
                if sol(t1) <= 0:
                    t1 += 1
                    print(sol(t1))
                if sol(t2) <= 0:
                    t2 -= 1
            num_of_solutions = t2 - t1 + 1
            result *= num_of_solutions
    print("Res: ", result)

def second_part():
    result = 0
    with open(g_input_file, 'r') as input:
        # Extract data
        _, race_duration = input.readline().rstrip('\n').split(":")
        _, best_distance = input.readline().rstrip('\n').split(":")
        race_duration = int(race_duration.replace(" ", ""))
        best_distance = int(best_distance.replace(" ", ""))

        delta = race_duration * race_duration - 4 * best_distance
        t1 = round((race_duration - sqrt(delta)) / 2)
        t2 = round((race_duration + sqrt(delta)) / 2)
        def sol(t): return - t * t + race_duration * t - best_distance
        if sol(t1 - 1) >= 0:
            if sol(t1) <= 0:
                t1 -= 1
            if sol(t2) <= 0:
                t2 += 1
        if sol(t1 + 1) >= 0:
            if sol(t1) <= 0:
                t1 += 1
                print(sol(t1))
            if sol(t2) <= 0:
                t2 -= 1
        num_of_solutions = t2 - t1 + 1        
    print(race_duration, best_distance)
    print("Res: ", num_of_solutions)

if __name__ == '__main__':
    second_part()