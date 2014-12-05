import networkx as nx 
import matplotlib.pyplot as plt
from collections import defaultdict
import random

gr = nx.Graph()

# Het invoer werk eerst

# Posities van deze provincies in een grid. 
position = [(1,7),(1,6),(2,7),(2,6),(3,7),(3,6),(4,7),(4,6),(5,6),(5,7),(6,7),
(6,6.5),(6,6),(7,6),(8,6),(9,6),(10,5.5),(11,6),(3,5),(4,5),(5.5,5),(7,5),(9,5),
(3,4),(4,4),(4.5,4.5),(4.5,3.5),(5.5,4),(6.5,4),(8,4),(3,3),(5,3),(7,3),(8,3),(3,2),
(5,2),(7,2),(8,2),(3,1),(4,1),(5,1),(6,1),(7,1),(4,0),(5,0),(6,0),(7,0)]

# Lijst van alle provincies, die de nodes vormen in de graaf
nodes = ['leo', 'zam', 'jae', 'bur', 'gui', 'mur', 'gua', 'vall', 'ast', 
'ter', 'sor', 'seg', 'hues', 'nav', 'mal', 'tar', 'ler', 'lar', 'tol', 'can', 'bad', 'ali',
'ore', 'pon', 'ciu', 'lug', 'huel', 'gra', 'lac', 'sal', 'bar', 'cad', 'sev', 
'ger', 'mad', 'vale', 'viz', 'ala', 'alm', 'bal', 'las', 'san', 'cor', 'cac',
'alb', 'zar', 'cas']

# Provincies die een grens delen krijgen een edge toebedeeld in onderstaande lijst
edges = [('leo','zam'),('leo','jae'),('zam','jae'),('zam','bur'),('bur','jae'),('jae','gui'),('bur','mur'),('jae','mur'),('gui', 'mur'),
('gui','gua'),('mur','gua'),('mur','vall'),('mur','tol'),('mur','can'),('gua','vall'),('gua','ter'),('gua','ast'),('vall','ast'),('vall','can'),
('ast','ter'),('ast','seg'),('ast','hues'),('ast','bad'),('ast','lug'),('ter','sor'),('ter','seg'),('sor','seg'),('seg','hues'),('seg','nav'),
('hues','bad'),('sor','nav'),('hues','nav'),('hues','ali'),('nav','mal'),('nav','ali'),('ali','mal'),('ali','tar'),('mal','tar'),('tar','ore'),
('ali','ore'),('tar','ler'),('tar','lar'),('ore','ler'),('ler','lar'),('tol','can'),('tol','pon'),('can','lug'),('can','ast'),('lug','ciu'),
('lug','huel'),('lug','gra'),('lug','bad'),('bur','tol'),('can','pon'),('can','ciu'),('bad','gra'),('bad','ali'),('ali','gra'),('ali','lac'),
('ore','lac'),('ore','sal'),('pon','ciu'),('pon','bar'),('ciu','bar'),('ciu','cad'),('ciu','huel'),('huel','cad'),('huel','gra'),('huel','sev'),
('gra','sev'),('gra','lac'),('lac','sev'),('lac','ger'),('lac','sal'),('sal','ger'),('bar','cad'),('bar','mad'),('cad','sev'),('cad','mad'),
('cad','vale'),('sev','vale'),('sev','viz'),('sev','ger'),('ger','viz'),('ger','ala'),('cac', 'alb'),('cac','bal'),('cac','alm'),('alm','bal'),
('alm','mad'),('bal','mad'),('bal','las'),('bal','alb'),('alb','las'),('alb','zar'),('zar','las'),('zar','san'),('zar','viz'),('zar','cor'),
('zar','cas'),('cas','cor'),('las','mad'),('las','vale'),('las','san'),('san','vale'),('san','viz'),('mad','vale'),('vale','viz'),('viz','ala'),
('viz','cor'),('cor','ala')]

# De zelfde edges, maar dan andere kant op (dus ook ('zam', 'leo') ipv ('leo','zam'))
otheredges = []
for a, b in edges: 
	otheredges.append((b,a))

# Alle edges bij elkaar gevoegd in 1 lijst
alledges = edges + otheredges

# Een dictionary met als key een provincie en als value alle provincies waar de key een grens mee deelt
dicti = defaultdict(list)
for v, k in alledges: 
	dicti[v].append(k)

# Lijst van (random) kleuren
colors = ['#000000','g','b','r','y', '#660099', '#AA8899', '#DD4477', '#0000AA', '#222222']

# Labelen van de nodes
count = 0
for node in nodes:
	gr.add_node(node, name = nodes[count], color = colors[0])
	count += 1

# Posities van de nodes gekoppeld in een dictionary
pos = dict(zip(nodes, position))

# De lijst van kleuren die mee wordt gegeven bij het tekenen van de graaf
nocolor = []

'''
Het kleur bepalen, dat werkt nu als volgt: 
In het begin heeft elke node de kleur groen. Vervolgens wordt er per node gecheckt of er collisions zijn. 
De eerste for loop itereert over alle nodes. De tweede for loop loopt door de lijst van buren en checkt of 
een buur dezelfde kleur heeft. Zo ja, dan wordt counter groter waardoor er later een andere kleur uit de 
kleurlijst wordt gekozen voor de node. Als er een collision is dan breakt de for loop en zorgt de while loop 
ervoor dat alle buren weer van voor af aan gecontroleerd worden op kleur. Als er geen collisions zijn, 
regelt de tweede if statement dat de while loop niet infinite is. 
Uiteindelijk wordt er een kleur (afhankelijk van het aantal botsingen en dus van counter) toegekend aan 
een node en die kleur wordt vastgelegd in een lange lijst die wordt gebruikt bij het maken van de graaf. 
That's it that's all, folks! 
'''
loops = 0
numcol = []
while loops < 1:
	
	for node in nodes:
		neighbours = dicti[node]
		col = ['g','b','r','y', '#FF0099', '#AA9999', '#DD4477']
		cst = 0
		counter = 0
		while cst == 0:
			x = 0
			if gr.node[node]['color'] == '#000000':
				gr.node[node]['color'] = col[0]
			for n in neighbours: 
				x += 1
				if gr.node[node]['color'] == gr.node[n]['color']:
					counter += 1
					break
				if x == len(neighbours): 
					cst = 1
			gr.node[node]['color'] = col[counter]
		nocolor.append(gr.node[node]['color'])
	numcol.append(len(set(nocolor)))
	loops+=1

# Het tekenen van de graaf (met labeling en kleur)
gr.add_edges_from(edges)

nx.draw(gr,pos)
node_labels = nx.get_node_attributes(gr,'name')

nx.draw_networkx_nodes(gr, pos, nodes, node_color = nocolor)

nx.draw_networkx_labels(gr, pos, labels = node_labels)

plt.savefig("simple_path.png") # save as png
plt.show() # display
