import re

def get_card_points(line):
    #get winning numbers by starting after card num and ending at break char
    start_index = line.find(':')
    end_index = line.find('|', start_index + 1)  # Start searching after the start_char
    result = line[start_index + 1:end_index]
    win_nums_arr = result.split()
    win_set = set()
    for i in win_nums_arr:
        win_set.add(i)
    my_nums = line[end_index+2: len(line)]
    my_nums = my_nums.split()
    count = 0
    points = 0
    for i in my_nums:
        if i in win_set:
            count += 1
            if count == 1:
                points = 1
            else:
                points *= 2
    return [points, count]
def main():
    total_points = 0
    file = open("Day4\input.txt", 'r')
    while True:
        content=file.readline()
        if not content:
            break
        total_points += get_card_points(content)[0]
    print("Total points (part 1): ", int(total_points))


if __name__ == "__main__":
    main()