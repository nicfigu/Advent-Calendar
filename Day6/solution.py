def min_max(count, record):
    min = 0
    for i in range(1, count-2):
        if i * (count-i) > record:
            min = i
            max = count-i
            break
    return max - min + 1


def main():
    with open('Day5\input.txt', 'r') as file:
        lines = file.readlines()

    # Extract time and distance values
    time_values = [int(val) for val in lines[0].split()[1:]]
    distance_values = [int(val) for val in lines[1].split()[1:]]
    time_values2 = int(''.join(lines[0].split()[1:]))
    distance_values2 = int(''.join(lines[1].split()[1:]))
    ans = 1
    for i in range(len(time_values)):
        ans *= min_max(time_values[i], distance_values[i])
    print("Part 1: " + str(ans))
    print("Part 2: "+ str(min_max(time_values2, distance_values2)))

if __name__ == "__main__":
    main()