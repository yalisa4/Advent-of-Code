def safe_check(record):
  for number in range(0, len(record)-1, 1):
    if abs(record[number] - record[number + 1]) > 3 or abs(record[number] - record[number + 1]) < 1:
      return False
    
  if sorted(record) not in [record, record[::-1]]:
    return False
  
  else:
    return True
      

def red_nosed(datastream: list[list: int]) -> int:
  safe_count = 0
  for record in datastream:
    safe_count += 1 if safe_check(record) else 0

  return safe_count


if __name__ == "__main__":
  with open("2024/AoC_2024_2.txt") as fh:
    content = fh.readlines()
  
  list_ = [line.split(" ") for line in content]
  cleaned_list = [[item.strip() for item in sublist] for sublist in list_]
  list_int = [[int(num) for num in sublist] for sublist in cleaned_list]

  print(red_nosed(list_int))
