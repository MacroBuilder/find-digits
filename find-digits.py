def digit(n):
    count = 0
    for i in n:
        if int(i) > 0 and int(n) % int(i) == 0:
            count += 1
    print count

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    number = raw_input().strip()
    digit(number)
