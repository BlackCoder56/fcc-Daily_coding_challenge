def count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    conso_count = 0

    for i in s.lower():
        if i.isalpha() and i in vowels:
            vowel_count += 1
        elif i.isalpha() and i not in vowels:
            conso_count += 1

    return [vowel_count, conso_count]


print(count("HellO"))