def floor(input_file: str) -> 0:
    floor_up, floor_down, current_floor = "(", ")", 0
    count_char = 0
    for char in input_file:
        count_char += 1
        if char == floor_up:
            current_floor += 1
        else:
            current_floor -= 1
            if current_floor == -1:
                return count_char
    #return(current_floor)


if __name__ == "__main__":
    with open("2015/2015_day1.txt") as file:
        inhoud = file.read()

    print(floor(inhoud))
