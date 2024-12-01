import re


def AoC_2015_4(input: str) -> list:
    afstanden = []

    for reindeer in input:
        reindeer_digits = [int(num) for num in re.findall(r'\d+', reindeer)]
        at_seconden, afstand = 2503, 0
        afstand_vliegtijd, rest = [reindeer_digits[0], reindeer_digits[1]], reindeer_digits[2]

        while at_seconden > 0:
            if at_seconden > afstand_vliegtijd[1]:
                at_seconden -= afstand_vliegtijd[1]
                afstand += afstand_vliegtijd[0] * afstand_vliegtijd[1]

            else:
                afstand += at_seconden * afstand_vliegtijd[0]

            at_seconden -= rest

        afstanden.append(afstand)

    return max(afstanden)


if __name__ == "__main__":
    with open("2015_day14") as file:
        inhoud = file.readlines()

    print(AoC_2015_4(inhoud))
