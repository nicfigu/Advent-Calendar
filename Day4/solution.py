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
def num_of_scorecards(count, game_num, my_array):
    for i in range(1, count+1):
        if game_num+i in range(len(my_array)):
            my_array[game_num+i] += my_array[game_num]

def main():
    total_points = 0
    file = open("Day4\input.txt", 'r')
    game_num = 0
    arr_of_scorecard_count = [1] * 208
    while True:
        content=file.readline()
        if not content:
            break
        ans = get_card_points(content)
        total_points += ans[0]
        num_of_scorecards(ans[1], game_num, arr_of_scorecard_count)
        game_num +=1
    print("Total points (part 1): ", int(total_points))
    print("Total number of scorecards: " + str(sum(arr_of_scorecard_count)))


if __name__ == "__main__":
    main()