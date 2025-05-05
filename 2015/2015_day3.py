def aoc_3(content):
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
    with open("2015/2015_day3.txt") as file:
        content = file.read()

    print(aoc_3(content))
