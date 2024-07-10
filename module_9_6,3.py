def all_variants(text):
    for j in range(len(text)):
        for k in range(j + 1, len(text) + 1):
            yield text[j:k]


a = all_variants('abcd')
for i in a:
    print(i)
