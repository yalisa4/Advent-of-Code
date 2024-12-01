def ribbon(dimensions: list) -> int:
    dimensions_copy = dimensions[:]

    bow_ribbon = dimensions[0] * dimensions[1] * dimensions[2]

    dimensions_copy.remove(max(dimensions_copy))
    feet_ribbon = dimensions_copy[0] + dimensions_copy[0] + dimensions_copy[1] + dimensions_copy[1]

    return feet_ribbon + bow_ribbon


def wrapping_paper(input_file: list) -> 0:
    total_wrapping_paper, total_ribbon = 0, 0
    for line in input_file:
        line = line.replace("x", " ")
        numbers_list = [int(num) for num in line.split()]

        surface_area = (2*numbers_list[0]*numbers_list[1] + 2*numbers_list[1]*numbers_list[2] +
                        2*numbers_list[2]*numbers_list[0])

        min_surface = min([numbers_list[0]*numbers_list[1], numbers_list[1]*numbers_list[2],
                           numbers_list[2]*numbers_list[0]])

        total_wrapping_paper += surface_area + min_surface
        total_ribbon += ribbon(numbers_list)

    return total_wrapping_paper, total_ribbon


if __name__ == "__main__":
    with open("2015_day2.txt") as file:
        inhoud = file.readlines()

    print(wrapping_paper(inhoud))
