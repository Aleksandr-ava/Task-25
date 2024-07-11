def all_variants(text):
    length = len(text)
    for j in range(length):
        for k in range(j + 1, length + 1):
            yield text[j:k]


a = all_variants('abcd')
for i in a:
    print(i)
