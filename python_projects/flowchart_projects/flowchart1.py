from graphviz import Digraph

dot = Digraph(format='png', graph_attr={
    'dpi': '1000',
    'rankdir': 'LR',
    'nodesep': '1.02',
    'ranksep': '1.1',
    'pad': '1.5',
    'margin': '0',
    'splines': 'true'
    })


dot.node('d', 'start' , shape='oval')
dot.node("a", " inter a num", shape='parallelogram')
dot.node('b', 'input ', shape='parallelogram')
dot.node('c', 'check input' , shape='box' )
dot.node('g', 'if num>1', shape='diamond')
dot.node('f', 'print done', shape='parallelogram')
dot.node('q','num+1', shape='box')
dot.node('w', 'end', shape='oval')


dot.edge('d', 'a')
dot.edge('a', 'b')
dot.edge('b', 'c')
dot.edge('c', 'g')
dot.edge('g', 'f', label='True')
dot.edge('g' ,'q', label='False')
dot.edge('q', 'c', label='chack num')
dot.edge('f', 'w')



dot.render('my flowchart', view=True)