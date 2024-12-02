def AoC_2023_2(games: dict) -> int:
  max_loaded = {"red": 12, "green": 13, "blue": 14}
  sum_ids, check = 0, []

  for key, item in games.items():
    for index in item:
      gooi = index.split(",")
      current_load = {"red": 0, "green": 0, "blue": 0}
      is_valid = True
      for beurt in gooi:
        kleur = [char for char in beurt.split(" ") if char.isalpha()]
        aantal = [char for char in beurt.split(" ") if char.isdigit()]
        current_load[kleur[0]] = int(aantal[0])
      
        if current_load[kleur[0]] > max_loaded[kleur[0]]:
          is_valid = False
          break

      if not is_valid:
        break
    
    if is_valid:
      sum_ids += key

  return sum_ids


if __name__ == "__main__":
  games_dict = {}
  with open("2023/AoC_2023_2.txt", "r") as fh:
    for game in fh.read().split("\n"):
      game_id = [char for char in game.split(":")[0] if char.isdigit()]
      game_value = ''.join(game.split(":")[1]).split(";")
      games_dict[int(''.join(game_id))] = game_value

  print(AoC_2023_2(games_dict))
  