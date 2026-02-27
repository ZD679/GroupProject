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


# CALL THE FUNCTION
print(longest_un_word("text.txt"))