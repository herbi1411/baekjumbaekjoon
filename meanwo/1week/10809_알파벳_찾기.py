s = input()
spell_str = 'abcdefghijklmnopqrstuvwxyz'

for spell in spell_str:
    if spell in s:
        print(s.index(spell))
    else:
        print(-1)
