check = [0] * 10

def calc(n, ten):
    while n > 0:
        check[n % 10] += ten
        n //= 10

def solve(A, B, ten):
    while A % 10 != 0 and A <= B:
        calc(A, ten)
        A += 1
    
    if A > B:
        return
    
    while B % 10 != 9 and B >= A:
        calc(B, ten)
        B -= 1

    cnt = (B // 10 - A // 10 + 1)
    for i in range(10):
        check[i] += cnt * ten

    solve(A // 10, B // 10, ten * 10)

if __name__ == "__main__":
    n = int(input())
    solve(1, n, 1)
    print(" ".join(map(str, check)))
