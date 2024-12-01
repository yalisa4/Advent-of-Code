def AoC_2024_1(datastream: list) -> tuple:
    links_kol, rechts_kol = [], []
    total_distance, similarity_score = 0, 0

    for regel in datastream:
        line = regel.split()
        links_kol.append(int(line[0]))
        rechts_kol.append(int(line[1]))

    for number in links_kol:
        voorkomst = rechts_kol.count(number)
        similarity_score += voorkomst * number

    while links_kol and rechts_kol:
        left_min = min(links_kol)
        right_min = min(rechts_kol)

        total_distance += abs(left_min - right_min)

        links_kol.remove(left_min)
        rechts_kol.remove(right_min)

    return total_distance, similarity_score


if __name__ == "__main__":
    with open("AoC_2024_1") as file:
        inhoud = file.readlines()

    print(AoC_2024_1(inhoud))
