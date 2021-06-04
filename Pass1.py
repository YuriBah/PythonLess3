my_trans = {"zero": "ноль", "one": "один", "two": "два", "threee": "три",
            "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
            "eight": "восемь", "nine": "девять", "ten": "десять"}

def my_translate_adv(word):
    if word[0] == word[0].upper():
        word = word.lower()
        return my_trans[word].capitalize()
    else:
        return my_trans[word]

print(my_translate_adv('nine'))
print(my_translate_adv('Nine'))
