def all_variants(text):
    for j in text:
        yield j
    yield text[0:2]
    yield text[1:3]
    yield text


a = all_variants("abc")
for i in a:
    print(i)