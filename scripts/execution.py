import json
from .functions import *


def fetchInputs(ip, nodes):
    res = []
    for node in nodes:
        if node['label'] == ip:
            res.append(node)
            
    return res

def process(dump):

    # print(fetch('add')('aa', 'a'))
    # print()

    nodes = [node['data'] for node in eval((dump['nodes']).replace("'", '"'))]
    edges = eval((dump['edges']).replace("'", '"'))

    for node in nodes:
        node['inputs'] = []
        node['outputs'] = []
        for edge in edges:
            if (node['label'] == edge['target']):
                # print(node['label'], edge['source'])
                node['inputs'].append(edge['source'])
    filtered = [node for node in nodes if node['inputs']]
    for node in filtered:
        for ip in node['inputs']:
                for n in filtered:
                    if n['label'] == ip:
                        inputs = fetchInputs(ip, nodes)
                        for i in inputs:
                                for j in (i['inputs']):
                                    print(j)
                                    for k in nodes:
                                        if k['label'] == j:
                                            # temp.append(k['value'])
                                            n.setdefault('inputValues', []).append(k['value'])
        if (node['inputValues']):
             print(node['label'], node['inputValues'])
                                            

    return nodes, filtered
