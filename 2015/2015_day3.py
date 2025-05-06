def aoc_3(content: str) -> tuple:
    """
    Calculate how many unique houses recieve at least
    one present in part 1 and part 2 of Advent of Code 2015 - Day 3.

    param:
        content: A string of directional instructions, consisting of 
        the characters '^', 'v', '<', and '>'.
    
    returns:
        tuple: Two integers:
            - The number of unique houses visited by Santa alone (part 1)
            - The number of unique houses visited by both Santa and 
            Robo-Santa (part 2).
    """
    
    def right_dir(pos):
        return (pos[0], pos[1] + 1)

    def left_dir(pos):
        return (pos[0], pos[1] - 1)

    def up_dir(pos):
        return (pos[0] - 1, pos[1])

    def down_dir(pos):
        return (pos[0] + 1, pos[1])
    
    commando = {
        ">": right_dir,
        "<": left_dir,
        "^": up_dir,
        "v": down_dir
    }

    # part 1
    current_pos = (0,0)
    visited = set()
    visited.add(current_pos)

    # part 2
    current_pos_santa, current_pos_robot = (0,0), (0,0)
    visited_santa_robot = set()
    visited_santa_robot.add(current_pos)

    for index, char in enumerate(content):
        if char not in commando:
            continue

        current_pos = commando[char](current_pos)
        visited.add(current_pos)

        if index % 2 == 0:
            current_pos_santa = commando[char](current_pos_santa)
            visited_santa_robot.add(current_pos_santa)
        else:
            current_pos_robot = commando[char](current_pos_robot)
            visited_santa_robot.add(current_pos_robot)

    return len(visited), len(visited_santa_robot)

if __name__ == "__main__":
    """
    This script reads movement instructions from a text file and
    calculates how many unique houses receive presents from Santa
    alone (part 1) and from both Santa and Robo-Santa (part 2).
    """
    with open("2015/2015_day3.txt") as file:
        content = file.read()

    print(aoc_3(content))
