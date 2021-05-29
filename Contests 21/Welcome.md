# Welcome Contest tutorial

## A - 1

**Source:** [Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem)  
As you may have noticed only the hours change, so you only need to read the hours from the string, and depending on the time `AM` or `PM`, you change the value of the hours, then reattach it back to the string.

```python
# In PM, we only need to add 12 to the hours.
# Except for the case of 12, we don't need to add anything
pmh = lambda h: h + 12 if h != 12 else 12
# In AM, we only need to make sure the value is less than 12
# this is done specially for 12 AM which translates to 00:mm:ss in the problem description
# since all AM hours should be <= 12 
# it also be written as lambda h: h if h != 12 else 0
amh = lambda h: h % 12

# M is the time specifier AM or PM
# h is the hour value 
# in case of AM return amh(h)
# in case of PM return pmh(h)
transformHour = lambda h, M: amh(h) if M=='AM' else pmh(h)

def timeConversion(s): 
    hour = transformHour(int(s[:2]), s[-2:])
    # make sure to format the hours number to have leading zeros
    # attach the rest of the string (ignore the last two characters for AM/PM)
    return '{:02d}'.format(hour) + s[2:-2]

print(timeConversion(input()))
```

**Complexity:** *O(1)*
Since the input length is small constant, the cost for slicing the strings is small constant,
and the rest of the operations are just math.

## A - 2

**Source:** [characters patterns](https://www.spoj.com/problems/CPTTRN1/en/)
The main point here, is when to print '*' and when to print '.', if you check the example
carefully, you can see that '*' is printed when `i` and `j` are both even or both odd,
in case when one of them is even and the other is odd, '.' is printed.

```python
# your code goes here
n = int(input())

while(n > 0):
  n -= 1
  [a, b] = [int(i) for i in input().split(' ')]
  for i in range(a):
    for j in range(b):
      # a number is odd if its first bit is 1
      # read the first bit of i and j using & gate
      # xor the two bits together
      if (i&1) ^ (j&1):
        print('.', end='')
      else:
        print("*", end='')
    print()
  print()

```

**Complexity**: O(a\*b) for each test case so overall *O(n a b)*

## A - 3

**Source:** [Fun with Sequences](https://www.spoj.com/problems/SMPSEQ3/)
the limits for the problem are small (100 element in both arrays), simply going over array `s` and checking if the current value exists in `q`, if it doesn't then print it out, otherwise move to the next value.

```python
# your code goes here
n = int(input())
s = [int(i) for i in input().split(' ')]
m = int(input())
q = [int(i) for i in input().split(' ')]

for i in s:
  for j in q:
    if i == j: break
  else:
    print(i, end=" ")
```

or a simpler syntax:

```python
n = int(input())
s = [int(i) for i in input().split(' ')]
m = int(input())
q = [int(i) for i in input().split(' ')]

for i in s:
  if i not in q:
    print(i, end=" ")
```

**Complexity:** *O(|s| \* |q|)* the product of two strings lengths.

## A - 4

**Source:** [Mini-Max-Sum](https://www.hackerrank.com/contests/university-codesprint/challenges/mini-max-sum)  
find the minimum, the maximum and the sum, subtract minimum from sum to get maximum sum, subtract maximum from sum to get minimum sum.

```python
a = [int(i) for i in input().split(' ')]
s, mx, mn= sum(a), max(a), min(a)
print(str(s - mx) + ' ' + str(s - mn))
```

**Complexity:** *O(n)* length of sequence, but in this case the length is always 5, so it's basically *O(1)*.

## B - 1

**Source:** [Recusrive-digit-Sum](https://www.hackerrank.com/challenges/recursive-digit-sum/submissions/code/207405339)  

From the problem statement n has 100000 digits at most, so the some of them won't exceed 9 * 10^5, so it's safe to sum all digits of n in an integer.  

Since we have k of n's concatenated together, we multiple the sum by k to get the total sum, which has has a miximum of 9 * 10^10, this may not fit in cpp integer so you may want to use long long type to hold it.  

then iteratively sum the digits of the result until it's less than 10

```python
# Sums the digits of a given integer
def sumDigits(n):
  c = 0
  while(n):
    c += n % 10 # add the first digit to c
    n //= 10 # remove the first digit from n
  return c

def superDigit(n, k):
  n = k * sum([int(digit) for digit in n])
  while(n > 9):
    n = sumDigits(n)
  return n
    
n, k = input().split()
print(superDigit(n, k))
```

**Complexity:** summing up the digits in n takes *O(|n|)*, the number of digits after this sep should be no more than 10, which can be counted as a constant compared to the previous part, so the overall Complexity is *O(n)*.

## B - 2

**Source:** [The power sum](https://www.hackerrank.com/challenges/the-power-sum/problem)  
this is a divide and Conquer problem.  
**The problem state:** it's trivial to have `x` as part of the state, but we also need an additional value `sm` that represents the smallest number you CAN use, and even though here we pass the power `n` to the function as well, it doesn't count as part of the problem state, since it doesn't change through out the recursion tree, So we won't include it in the explanation below.  

**The sub problems:** let's call our function f then the answer we are looking for is *f(x, sm)*.
at this state we can decide either of:

1. Try to use `sm + 1` in the sequence: Subtract `sm + 1` from `x`.
2. Decide not to use `sm + 1` in the sequence: leave `x` as is.

in both cases the value of `sm`  becomes `sm + 1` to signify that all values < `sm + 1` aren't to be used in the sequence.  

This definition is correct because there are no other possible actions to take, we can either have `sm + 1` as part of the sequence exactly once, or not have it at all, since we cover all possible options, then we necessaily cover all possible cases.

so `f(x, sm + 1)`: number of all possible paths to reach `x` without using `(sm + 1)^n`.  
`f(x - sm - 1, sm + 1)`: number of all possible paths to reach `x` that include `(sm + 1)^n`.  

`f(x, sm)`: the number of all path to reach x.  
So to merge the sub problems we need to add their results:  
`f(x, sm)` = `f(x, sm + 1)` + `f(x - sm - 1, sm + 1)`

The only difference introduced by the addition of the power `n` is that you subtract `sm^n` instead of just `sm`.

```cpp
#include <bits/stdc++.h>
using namespace std;

// the power p in this problem is at most 10
// so fast power is not required
int power(int v, int p) {
    int ret = 1;for(int i = 0;i < p;i++) ret *= v;
    return ret;
}

int powerSum(int x, int n, int sm = 1) {
    if (x == 0) return 1;
    int p = power(sm, n);
    if (p > x) return 0;
    return powerSum(x, n, sm + 1) + powerSum(x - p, n, sm + 1);
}

int main(){
    int X, N;
    cin >> X >> N;
    int result = powerSum(X, N);
    cout << result << "\n";
    return 0;
}
```

**Complexity:** *TBD*
