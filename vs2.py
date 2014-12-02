import networkx as nx 
import matplotlib.pyplot as plt
from collections import defaultdict

gr = nx.Graph()

counties = ['bri', 'war', 'mck', 'pot', 'tio', 'bra', 'sus', 'way', 'cra', 'mer', 'ver', 'for', 'bk', 
'came', 'cli', 'lyc', 'sul', 'wyo', 'lac', 'pik', 'law', 'but', 'cla', 'jef', 'cle', 'cen', 'uri', 
'noru', 'mont', 'col', 'luz', 'monr', 'bea', 'all', 'arm', 'ind', 'cam', 'bla', 'hun', 'mif', 'sny', 
'sch', 'car', 'nora', 'was', 'wes', 'jur', 'dau', 'leb', 'ber', 'leh', 'gre', 'fay', 'som', 'bec', 
'ful', 'fra', 'per', 'cum', 'ada', 'yor', 'lan', 'che', 'mon', 'buc', 'phi', 'del']

position = [(1,8.5),(2.5,8),(4,8),(5,8),(6.5,8),(8,8),(9.5,8),(10.5,7),(1,7),(1,5.5),(2,5.5),(3,5.5),(4,5.5),(4.5,5.5),
(6,5),(7,5.5),(8,6),(9,6),(9.5,6),(11.5,6),(1,4.5),(2.5,4.5),(3,4.5),(3.5,3.75),(4,4),(5,4),(6,4),(6.5,3.5),(7,4),(7.5,4),
(8.5,4.5),(10,4.5),(1,3.5),(2,3),(3,4),(3.5,3),(4,3),(4.5,3),(5,3),(5.5,3.5),(6,3.5),(8,3.5),(9,4),(10,3.5),(1,2),(3,2),
(5.5,3),(6.5,2.5),(7,2.5),(8,2.5),(9,3),(1,1),(2.5,1),(3.5,1),(4.5,1),(5,1),(5.5,1),(5.5,2.5),(6,2),(6,1),(7,1),(7.5,1),
(8,1),(9,1.5),(10,2),(9.5,1),(9,1)]

nodes = ['bri', 'war', 'mck', 'pot', 'tio', 'bra', 'sus', 'way', 'cra', 'mer', 'ver', 'for', 
'bk', 'came', 'cli', 'lyc', 'sul', 'wyo', 'lac', 'pik', 'law', 'but', 'cla', 'jef', 'cle', 
'cen', 'uri', 'noru', 'mont', 'col', 'luz', 'monr', 'bea', 'all', 'arm', 'ind', 'cam', 'bla', 
'hun', 'mif', 'sny', 'sch', 'car', 'nora', 'was', 'wes', 'jur', 'dau', 'leb', 'ber', 'leh', 
'gre', 'fay', 'som', 'bec', 'ful', 'fra', 'per', 'cum', 'ada', 'yor', 'lan', 'che', 'mon', 'buc', 'phi', 'del']

labels = dict(zip(counties, nodes))

print len(position), len(counties)

pos = dict(zip(counties, position))

print pos

edges = [('bri','cra'),('bri','war'),('war','cra'),('war','ver'),('war','for'),('war','mck'),('mck','bk'),('mck','came'),('mck', 'pot'),
('pot','came'),('pot','cli'),('pot','lyc'),('pot','tio'),('tio','lyc'),('tio','bra'),('bra','sul'),('bra','wyo'),('bra','sus'),('sus','wyo'),
('sus','lac'),('sus','way'),('way','lac'),('way','monr'),('way','pik'),('cra','mer'),('cra','ver'),('mer','ver'),('mer','but'),('mer','law'),
('ver','but'),('ver','cla'),('ver','for'),('for','cla'),('for','jef'),('for','bk'),('bk','jef'),('bk','cle'),('bk','came'),('came','cle'),
('came','cli'),('cli','cle'),('cli','cen'),('cli','uri'),('cli','lyc'),('lyc','uri'),('lyc','noru'),('lyc','mont'),('lyc','col'),('lyc','sul'),
('sul','col'),('sul','luz'),('sul','wyo'),('wyo','luz'),('wyo','lac'),('lac','luz'),('lac','monr'),('pik','monr'),('law','bea'),('law','but'),
('but','bea'),('but','all'),('but','arm'),('but','cla'),('cla','arm'),('cla','jef'),('jef','arm'),('jef','ind'),('jef','cle'),('cle','ind'),
('cle','cam'),('cle','cen'),('cen','bla'),('cen','hun'),('cen','mif'),('cen','uri'),('uri','sny'),('uri','noru'),('noru','sny'),('noru','jur'),
('noru','dau'),('noru','sch'),('noru','col'),('noru','mont'),('mont','col'),('col','sch'),('col', 'luz'),('luz','sch'),('luz','car'),
('luz','monr'),('monr','car'),('monr','nora'),('bea','all'),('bea','was'),('all','was'),('all','wes'),('wes','was'),('wes','fay'),('wes','som'),
('wes','cam'),('wes','ind'),('wes','arm'),('arm','ind'),('ind','cam'),('cam','som'),('cam','bec'),('cam','bla'),('bla','bec'),('bla','hun'),
('hun','bec'), ('hun','ful'),('hun','fra'), ('hun','jur'),('hun','mif'), ('mif','jur'),('mif','sny'),('jur','fra'),('jur','per'),('jur','sny'),
('per','fra'),('per','cum'),('per','dau'),('dau','cum'),('dau','yor'),('dau','lan'),('dau','leb'),('dau','sch'),('leb','lan'),('leb','ber'),
('leb','sch'),('sch','ber'),('sch','leh'),('sch','car'),('car','leh'),('car','nora'),('nora','leh'),('nora','buc'),('was','gre'),('was','fay'),
('fay','gre'),('fay','som'),('som','bec'),('bec','ful'),('ful','fra'),('fra','ada'),('fra','cum'),('cum','ada'),('cum','yor'),('ada','yor'),
('yor','lan'),('lan','ber'),('lan','che'),('ber','leh'),('ber','mon'),('ber','che'),('leh','mon'),('leh','buc'),('buc','mon'),('buc','phi'),
('che','mon'),('che','del'),('mon','phi'),('mon','del'),('del','phi')]

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
colors = ['g','b','r','y', '#660099', '#AA8899', '#DD4477', '#0000AA', '#222222']

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

print dicti

# Het tekenen van de graaf (met labeling en kleur)
gr.add_edges_from(edges)

nx.draw(gr,pos)
node_labels = nx.get_node_attributes(gr,'name')

nx.draw_networkx_nodes(gr, pos, nodes, node_color = nocolor)

nx.draw_networkx_labels(gr, pos, labels = node_labels)

plt.savefig("simple_path.png") # save as png
plt.show() # display
