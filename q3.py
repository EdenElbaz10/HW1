def is_it_palindrome(n, beginning, end):
    n = str(n)
    x = 0
    i = beginning
    j = end
    while i <= j:
        if n[i] != n[j]:
            return False
        i = i + 1
        j = j - 1

    return True


def check_palindrome():
    for number in range(100000, 1000000):
        if is_it_palindrome(number, 2, 5) == 1:
            n = number + 1
            if is_it_palindrome(n, 1, 5) == 1:
                n = n + 1
                if is_it_palindrome(n, 1, 4) == 1:
                    n = n + 1
                    if is_it_palindrome(n, 0, 5) == 1:
                        print(number)


check_palindrome()
