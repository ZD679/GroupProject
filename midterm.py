#Q1
import random


random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))


for i in range(10):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"


print(random_numbers)

['XX', 27, 'XX', 'XX', 22, 50, 'XX', 29, 'XX', 20]

#Q2
def days_since_birthday(birthday):

    parts = birthday.split("-")

    birth_year = int(parts[2])

    current_year = 2026

    full_years = current_year - birth_year - 1

    days = full_years * 365

    return days

print(days_since_birthday("10-12-2005"))

#Q3
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


#Q4
print(2 + 3 * 4 ** 2)

#Q5
def longest_un_word(filename):
    longest = ""
    file = open(filename, "r")

    for line in file:
        words = line.split()
        for word in words:
            if word[0:2] == "un":
                if len(word) > len(longest):
                    longest = word

    file.close()
    return longest

print(longest_un_word("text.txt"))

#Q6
def is_valid_url(url):

    if " " in url:
        return False

    if url[0:7] == "http://":
        rest = url[7:]
    elif url[0:8] == "https://":
        rest = url[8:]
    else:
        return False

    if len(rest) == 0:
        return False

    slash_index = rest.find("/")
    if slash_index == -1:
        domain = rest
    else:
        domain = rest[0:slash_index]

    if "." not in domain:
        return False

    parts = domain.split(".")
    for p in parts:
        if len(p) == 0:
            return False

    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    for ch in domain:
        if ch not in allowed:
            return False
    return True

print(is_valid_url("https://google.com"))

#Q7
a = 10

a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2

#Q8
import datetime

a = 3
b = 4

today = datetime.datetime.today()
day_of_week = today.weekday()   # Friday = 4
month_of_year = today.month     # February = 2

a = a + day_of_week   # 3 + 4 = 7
b += month_of_year    # 4 + 2 = 6

print(a)   # 7
print(b)   # 6

c = a + b   # 7 + 6 = 13
print(c)    # 13

d = "abc" * (c // 3)
print(d)
# abcabcabcabc

#Q9
# LIST 
nums = [1, 2, 3]
nums[1] = 99
print("List:", nums)

# STRING
word = "cat"

# Cannot do this:
# word[0] = "C"  -> error

# Must create a new string
word = "C" + word[1:]
print("String:", word)