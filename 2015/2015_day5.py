def correct_naughty(input_file):
    vowel = 'aeiou'
    forbidden_list = ["ab", "cd", "pq", "xy"]
    nice, naughty = 0, 0

    for line in input_file:
        twice_row, forbidden, count_vowel = False, True, 0
        for char in range(len(line) - 1):
            if line[char] == line[char + 1]:
                twice_row = True
            elif line[char:char + 2] in forbidden_list:
                forbidden = True
            elif line[char] in vowel:
                count_vowel += 1

        if count_vowel > 2 and twice_row and forbidden:
            nice += 1

    return nice


def parttwo(datastream):
    nice = 0
    for line in datastream:
        ppair, pair_gap = False, False
        seen_pairs = {}

        for char in range(len(line) - 1):
            pair = line[char:char + 2]
            if pair in seen_pairs and seen_pairs[pair] < char - 1:
                ppair = True
            seen_pairs[pair] = char

            if char + 2 < len(line) and line[char] == line[char + 2]:
                pair_gap = True

            if ppair and pair_gap:
                break

        if ppair and pair_gap:
            nice += 1

    return nice


if __name__ == "__main__":
    with open("2015_day5.txt") as file:
        inhoud = file.readlines()

    #print(correct_naughty(inhoud))
    print(parttwo(inhoud))
