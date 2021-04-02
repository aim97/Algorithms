def canBeMade(count, need, have, price, money):
  """
  count: the number of Hamburgers to be made
  need, have, price: arrays of 3 elements
    the ith element of each corresponds to the ith ingredient and represents
    1. the needed amount of that ingredient in the Hamburger
    2. the amount we have of that ingredient
    3. the price per unit of that ingredient
  money: the amount of money we can spend
  """
  for (needed, present, cost) in zip(need, have, price):
    m = max((count * needed - present) * cost, 0)
    if m > money: return False
    else: money -= m
  return True

def main():
  dic = {"B":0, "S":0, "C":0}
  for i in input(): dic[i] += 1
  need = list(dic.values())
  have = [int(v) for v in input().split(' ')]
  price = [int(v) for v in input().split(' ')]

  money = int(input())

  l , h = 0, int(10**15)
  # ||||||||||__________
  #          ^
  # the answer is in low
  while(l < h):
    mid = (l + h + 1) // 2
    # print(l, h, mid)
    if (canBeMade(mid, need, have, price, money)): l = mid
    else: h = mid - 1

  print(l)

if __name__ == '__main__':
  main()