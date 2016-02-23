def get_algorithm_result(num_list):
    if type(num_list) == type([]):
        Largest = num_list[0]
        for item in range(0,len(num_list)):
            if Largest < num_list[item]:
                Largest = num_list[item]
        return Largest


def prime_number(integer):
  if integer == 1:
    return False
  elif integer == 3:
    return True
  if integer > 3:
    for i in range(3, (integer-1)):
      if integer % i == 0:
        return False
      else:
        return True
