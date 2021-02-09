def is_pangram(sentence):
    base = set('abcdefghijklmnopqrstuvwxyz')
    given = set(filter(lambda c: 'a' <= c <= 'z', sentence.lower()))
    return base == given
