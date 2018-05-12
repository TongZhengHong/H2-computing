'''
count = 1

def print_star(num):
    print(count * "*")
    if num != 1:
        count += 1
        return print_star(num - 1)
'''

'''
def calc_average(score1, score2, score3):
    sum = score1 + score2 + score3
    ave = sum / 3
    return round(ave, 2)

def determine_grade(score):
    if score > 90 and score <= 100:
        return "A"
    elif score > 79:
        return "B"
    elif score > 69:
        return "C"
    elif score > 59:
        return "D"
    elif score > 0:
        return "F"
    else:
        return "Invalid score!"
'''

def isPrime(number):
    prime = True
    for value in range(2, number):
        if number % value == 0:
            prime = False
    return prime

def partA():
    num = int(input("Enter an integer to check: "))
    if isPrime(num) and num != 1:
        print("The number is a prime!")
    else:
        print("NOT a prime!")

def partB():
    print("Prime numbers: 2", end = "")
    for num in range(3, 101):
        if isPrime(num):
            print(", ", num, end = "")

def partC():
    test_num = 3
    print("Prime numbers: 2", end = "")

    for count in range(1000):
        while not isPrime(test_num):
            test_num += 1
        print(",", test_num, end = "")
        test_num += 1

def main():
    partC()
        
main()
