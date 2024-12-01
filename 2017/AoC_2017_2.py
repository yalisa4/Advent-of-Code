def AoC_2017_2(file: list) -> int:
    for regel in file:
        ag_regel = regel.strip().replace(" ", "").replace("\t", " ")
        digits = [int(num) for num in regel if num.isdigit()]

    return 0


if __name__ == "__main__":
    with open("2015/AoC_2017_2", "r") as fh:
        inhoud = fh.readlines()

    print(AoC_2017_2(inhoud))
