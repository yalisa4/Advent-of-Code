def AoC_2023_1(fh: str) -> int:
    som = 0
    uitgeschreven = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                     "eight": "8", "nine": "9"}
    for regel in fh:
        getallen = []
        letters = ""
        for char in regel:
            if char.isdigit():
                getallen.append(char)
                letters = ""
            else:
                letters += char

                for key in uitgeschreven.keys():
                    if key in letters:
                        getallen.append(uitgeschreven[key])
                        letters = letters[-1]

        volledige_getal = int(getallen[0] + getallen[-1])
        som += volledige_getal

    return som


if __name__ == "__main__":
    with open("2015/AoC_2023_1", "r") as file:
        inhoud = file.readlines()

    print(AoC_2023_1(inhoud))
