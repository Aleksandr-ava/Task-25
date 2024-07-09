def all_variants(text):
    for j in text:
        yield j
    for k in text:
        yield k + j
        if k + j == (text[-2] + text[-1]):
            break
    yield text


a = all_variants("abcd")
for i in a:
    print(i)
