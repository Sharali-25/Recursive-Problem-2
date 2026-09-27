# part 1 stairs combination
def ways(stairs):
    if stairs <0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs-1)+ways(stairs-2)
print(ways(7))
print(ways(8))
o = int(input("Enter a number : "))
print(ways(o))
# part 2 counting parentheses combinations
def brackets(s,l=0,r=0):
    if l == s  and r == s:
        return 1
    total = 0
    if l > r:
        total += brackets(s, l, r+1)
    if l < r:
        total +=brackets(s,l+1,r)
    return total
print(brackets(4))
print(brackets(2))
r=int(input("Enter a number : "))
print(brackets(r))
