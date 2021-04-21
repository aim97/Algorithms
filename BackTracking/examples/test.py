# generate all possible combinations of a given string
# that has a given length
# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=382

import sys

sys.stdin = open('in')
sys.stdout = open('out', 'w')

# global state 
# this array is shared between recursive calls to hold the 
# numbers currently accepted in that list
arr = []

def solve(s, l, i = 0):
  # bases cases
  if l == 0:
    # print the sequence if the required count is reached
    print(' '.join([str(i) for i in arr]))
    # if the required count can't be reached return
  elif (len(s) - i) < l: return
  else: 
    ch = s[i]
    # try to include the current number in the sequence
    arr.append(ch)
    solve(s, l - 1, i + 1)
    arr.pop(-1)
    # try not to include it

    # since not taking doesn't change the array we don't need to do anything
    # and subsequently there is nothing to undo in this case
    solve(s, l, i + 1)

    
if __name__ == '__main__':
  f = False
  while(True):
    n = [int(i) for i in input().split()]
    k = n[0]
    if k == 0: break # the program terminates if k = 0 as per input description
    elif not f: f=True
    else: print()
    seq = n[1:]  # ignore the first number that holds the count
    solve(seq, 6)
    