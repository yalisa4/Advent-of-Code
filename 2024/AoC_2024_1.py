def AoC_2024_1(datastream: list) -> tuple:
    left_col, right_col = [], []
    total_distance, similarity_score = 0, 0

    for record in datastream:
        line = record.split()
        left_col.append(int(line[0]))
        right_col.append(int(line[1]))

    for number in left_col:
        voorkomst = right_col.count(number)
        similarity_score += voorkomst * number

    left_col.sort()
    right_col.sort()

    for number in range(len(left_col)):
        total_distance += abs(left_col[number] - right_col[number])

    return total_distance, similarity_score


if __name__ == "__main__":
    with open("2024/AoC_2024_1.txt") as file:
        inhoud = file.readlines()

    print(AoC_2024_1(inhoud))
    