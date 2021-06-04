def thesaurus(*name):
    first_dict = dict()
    for i in name:
        first_dict.setdefault(i[0], [])
        first_dict[i[0]].append(i)
    return first_dict

print((thesaurus("Иван", "Мария", "Петр", "Илья")))