"""
given a function f(x) = x^2 + 2x + 2
find the first value of x such that f(x) >= 10^9
"""

f = lambda x: x**2 + 2*x + 2

def ok(x, target):
  return f(x) >= target

def findAtLeast(target):
  l , h = 0, 10**9
  while(l < h):
    mid = l + (h - l) // 2
    if (ok(mid, target)): h = mid
    else: l = mid + 1
  return h
  

if __name__ == '__main__':
  x = findAtLeast(99954)
  print(f(x))
  print(f(x - 1))