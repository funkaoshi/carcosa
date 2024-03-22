import collections

f = open('villages.txt')
settlements = []

for line in f:
    line = line.split('\t')
    s = {}
    for i, key in enumerate(['type', 'population', 'colour', 'ruled', 'alignment',
            'level', 'class']):
        s[key] = line[i].strip()
    for key in ['population', 'level']:
        s[key] = int(s[key])
    settlements.append(s)

print("Total # of Settlements: %d" % len(settlements))

for key in ['type', 'colour', 'ruled', 'alignment', 'class']:
    l = collections.Counter(s[key] for s in settlements)
    for key, val in l.items():
        l[key] = round(float(val) / 233 * 100)
    print(l)

levels = collections.Counter(s['level'] for s in settlements if s['level'])
for key, val in levels.items():
    levels[key] = round(float(val) / 231 * 100)
print(levels)
