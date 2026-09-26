def count_parentheses(n, l = 0, r = 0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r :
        total+= count_parentheses(n,l , r+1)
    if l < n :
        total+= count_parentheses(n,l+1,r)
    return total

print(count_parentheses(8))
print(count_parentheses(7))
n = int(input("Enter a number : "))
print(count_parentheses(n))