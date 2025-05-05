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

    current_pos = (0,0)
    visited = set()
    visited.add(current_pos)

    for char in content:
        if char in commando:
            current_pos = commando[char](current_pos)
            visited.add(current_pos)
    
    return len(visited)

if __name__ == "__main__":
    with open("2015/2015_day3.txt") as file:
        content = file.read()

    print(aoc_3(content))
