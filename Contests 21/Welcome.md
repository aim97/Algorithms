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

## A - 3

## A - 4

## B - 1

## B - 2