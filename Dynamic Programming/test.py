mem = []

# def solve():
  # if computed: return saved

  # base case

  # solve sub problems

  # merge

  # save result

"""
1. queries
2. overlapping sub problems
"""
# 21 7 25 3 9 ...

# W = 70
# [(w, p)]
# [(80, 200), (40, 1000), ....]
# w - 40, 200
# 
# 100
n = 5
arr = [(2, 5), (4, 10), (3, 20), (2, 19), (1, 3)]
mem = [[-1] * 1000 for i in range(1000)]
sol = []

def solve(i, W ):
  if mem[i][W] != -1: return mem[i][W]
  # base case
  if i == n: return 0

  p1 = solve(i + 1, W)
  p2 = solve(i + 1, W - arr[i][0]) + arr[i][1] if (W >= arr[i][0]) else 0
  
  ret = max(p1, p2)
  
  mem[i][W] = ret

  return ret

# (i, w) => (i+1, w) , (i+1, W - weight(i)) + gain(i)

def getSolution(i, w):
  if i == n: return
  if w >= arr[i][0] and mem[i][w] == mem[i + 1][w - arr[i][0]] + arr[i][1]:
    sol.append(i)
    getSolution(i + 1, w - arr[i][0])
  else:
    getSolution(i + 1, w)

# 0 1 2 3 4

def solveIter(n, W):
  # can't gain money with a bag that can carry nothing
  for i in range(n): mem[i][0] = 0

  for i in range(0, n):
    for w in range(1, W+1):
      if i > 0:
        p1 = mem[i - 1][w]
        p2 = mem[i - 1][w - arr[i][0]] + arr[i][1] if w >= arr[i][0] else 0
        mem[i][w] = max(p1, p2)
      else:
        mem[i][w] = arr[i][1] if w >= arr[i][0] else 0
  return mem[n - 1][W]

def solution(i, w):
  if i == 0:
    if mem[i][w] == arr[i][1]: sol.append(i)
  elif w != 0:
    if mem[i][w] == mem[i - 1][w]:
      solution(i - 1, w)
    else:
      sol.append(i)
      solution(i - 1, w - arr[i][0])

if __name__ == '__main__':
  print(solve(0, 4))
  getSolution(0, 4)
  print(sol)
