def AoC_2024_1(datastream: list) -> tuple:
    left_col, right_col = [], []
    total_distance, similarity_score = 0, 0

    for record in datastream:
        line = record.split()
        left_col.append(int(line[0]))
        right_col.append(int(line[1]))

    for number in left_col:
        occurences = right_col.count(number)
        similarity_score += occurences * number

    left_col.sort()
    right_col.sort()

    for num in range(len(left_col)):
        total_distance += abs(left_col[num] - right_col[num])

    return total_distance, similarity_score


if __name__ == "__main__":
    with open("2024/AoC_2024_1.txt") as file:
        content = file.readlines()

    print(AoC_2024_1(content))
