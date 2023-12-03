import re

R_MAX = 12
B_MAX = 14
G_MAX = 13
def check_game(line):
    num = re.search(r'Game (\d+):', line)
    game_number = int(num.group(1))
    #check reds
    red_pattern = re.compile(r'(\d+) red')
    green_pattern = re.compile(r'(\d+) green')
    blue_pattern = re.compile(r'(\d+) blue')
    #check if any number of red cubes is greater than the max
    for match in re.finditer(red_pattern, line):
        num = int(match.group(1))
        if (num > R_MAX):
            return 0
    #check greens
    for match in re.finditer(green_pattern, line):
        if (int(match.group(1)) > G_MAX):
            return 0
    #check blues
    for match in re.finditer(blue_pattern, line):
        if (int(match.group(1)) > B_MAX):
            return 0
    return game_number
def minNumOfCubes(line):
    #create RE patterns
    red_max = 0
    blue_max = 0
    green_max = 0
    red_pattern = re.compile(r'(\d+) red')
    green_pattern = re.compile(r'(\d+) green')
    blue_pattern = re.compile(r'(\d+) blue')
    #check if any number of red cubes is greater than the current max
    for match in re.finditer(red_pattern, line):
        num = int(match.group(1))
        if (num > red_max):
            red_max = num
    #check greens
    for match in re.finditer(green_pattern, line):
        num = int(match.group(1))
        if (int(match.group(1)) > green_max):
            green_max = num
    #check blues
    for match in re.finditer(blue_pattern, line):
        num = int(match.group(1))
        if (int(match.group(1)) > blue_max):
            blue_max = num
    return red_max * blue_max * green_max
def main():
    id_answer = 0
    minCube = 0
    file = open('input.txt', 'r')
    while True:
        content=file.readline()
        if not content:
            break
        id_answer += check_game(content)
        minCube += minNumOfCubes(content) 
    file.close()
    print("The sum of the IDs that match the parameters is: " + str(id_answer))
    print("The sum of the power of the minimum number of cubes that match the parameters is: " + str(minCube) +"\n")

if __name__ == "__main__":
    # This block will be executed only if the script is run directly
    main()