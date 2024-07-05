def all_variants(text):
    for j in text:
        yield j
    for k in text:
        yield k + j
        if k + j == 'bc':
            break
    yield text


a = all_variants("abc")
for i in a:
    print(i)
