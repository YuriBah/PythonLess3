import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    joke = []
    for i in range(num):
        dif_nonus = random.choice(nouns)
        dif_adverbs = random.choice(adverbs)
        dif_adjectives = random.choice(adjectives)
        joke.append((f'{dif_nonus} {dif_adverbs} {dif_adjectives}'))
    return joke

print(get_jokes(1))
print(get_jokes(2))
print(get_jokes(3))
