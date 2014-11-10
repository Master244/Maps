import networkx as nx 
import matplotlib.pyplot as plt

gr = nx.Graph()

counties = ['leo', 'zam', 'jae', 'bur', 'gui', 'mur', 'gua', 'vall', 'ast', 
'ter', 'sor', 'seg', 'hues', 'nav', 'mal', 'tar', 'ler', 'lar', 'tol', 'can', 'bad', 'ali',
'ore', 'pon', 'ciu', 'lug', 'huel', 'gra', 'lac', 'sal', 'bar', 'cad', 'sev', 
'ger', 'mad', 'vale', 'viz', 'ala', 'alm', 'bal', 'las', 'san', 'cor', 'cac',
'alb', 'zar', 'cas']

position = [(1,7),(1,6),(2,7),(2,6),(3,7),(3,6),(4,7),(4,6),(5,6),(5,7),(6,7),
(6,6.5),(6,6),(7,6),(8,6),(9,6),(10,5.5),(11,6),(3,5),(4,5),(5.5,5),(7,5),(9,5),
(3,4),(4,4),(4.5,4.5),(4.5,3.5),(5.5,4),(6.5,4),(8,4),(3,3),(5,3),(7,3),(8,3),(3,2),
(5,2),(7,2),(8,2),(3,1),(4,1),(5,1),(6,1),(7,1),(4,0),(5,0),(6,0),(7,0)]

nodes = ['leo', 'zam', 'jae', 'bur', 'gui', 'mur', 'gua', 'vall', 'ast', 
'ter', 'sor', 'seg', 'hues', 'nav', 'mal', 'tar', 'ler', 'lar', 'tol', 'can', 'bad', 'ali',
'ore', 'pon', 'ciu', 'lug', 'huel', 'gra', 'lac', 'sal', 'bar', 'cad', 'sev', 
'ger', 'mad', 'vale', 'viz', 'ala', 'alm', 'bal', 'las', 'san', 'cor', 'cac',
'alb', 'zar', 'cas']

labels = dict(zip(counties, nodes))

print len(position), len(counties)

pos = dict(zip(counties, position))

print pos['pon']

neighbours = [('leo','zam'),('leo','jae'),('zam','jae'),('zam','bur'),('bur','jae'),('jae','gui'),('bur','mur'),('jae','mur'),('gui', 'mur'),
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

gr.add_nodes_from(counties)
gr.add_edges_from(neighbours)



nx.draw(gr,pos)
#nx.draw_networkx_labels(gr,pos,labels)
plt.savefig("simple_path.png") # save as png
plt.show() # display

print counties[:10]