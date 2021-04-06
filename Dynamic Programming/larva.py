# https://www.spoj.com/problems/MBEEWALK/
dX = [-1, -1, 0, 0, 1, 1]
dY = [1, -1, 2, -2, 1, -1]

m = [[[-1 for i in range(100)] for j in range(100)] for k in range(15)]

def solve(n, x = 0, y = 0):
  # print(x, y, n)
  if (m[n][x+50][y+50] != -1): return m[n][x+50][y+50]
  if (n == 0 and x == 0 and y == 0): return 1
  elif n == 0: return 0

  count = 0
  for (dx, dy) in zip(dX, dY):
    count += solve(n-1, x+dx, y+dy)
  m[n][x+50][y+50] = count
  return count

if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    res = solve(n)
    print(res)