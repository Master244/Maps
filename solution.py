from collections import defaultdict
colors = ['Red', 'Yellow', 'Green', 'Blue']
mapColors = defaultdict(str)

def okToColor(Map ,country, color):
    for c in Map[country]:
        if mapColors[c] == color: return False
    return True

def explore(Map, country, color):
    if country >= len(Map): return True
    if okToColor(Map, country, color):
        mapColors[country] = color
        for color in colors:
            if explore(Map, country + 1, color): return True
            #explore(Map, country + 1, color)   
    return False

def printMap():
    for c in mapColors:
        print c, mapColors[c]
        #"map[" + str(i) + "] is " + mapColors[i]

Map = [[1, 4, 2, 5], [0, 4, 6, 5], [0, 4, 3, 6, 5], [2, 4, 6],
        [0, 1, 6, 3, 2], [2, 6, 1, 0], [2, 3, 4, 1, 5]]
result = explore(Map, 0, 'Red')
print result
printMap()