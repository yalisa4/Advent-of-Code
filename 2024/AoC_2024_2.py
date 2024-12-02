def red_nosed(datastream: list[list: int]) -> int:
  safe_count = 0
  for record in datastream:
    safe = True
    for index in range(0, len(record) - 1):
      if abs(record[index] - record[index + 1]) > 3:
        safe = False
        break
    
    if all(record[i] <= record[i + 1] for i in range(len(record) - 1)) or all(record[i] >= record[i + 1] for i in range(len(record) - 1)) and safe:
        safe_count += 1

  return safe_count

if __name__ == "__main__":
  with open("2024/AoC_2024_2.txt") as fh:
    content = fh.readlines()
  
  list = [line.split(" ") for line in content]
  cleaned_list = [[item.strip() for item in sublist] for sublist in list]
  list_int = [[int(num) for num in sublist] for sublist in cleaned_list]

  print(red_nosed(list_int))