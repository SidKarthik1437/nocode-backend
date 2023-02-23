import json
from .functions import *


def init():
    pass


# def extractInputs(nodes, fn):
#     for node in nodes:
#         if fn == node['label']:
#             return node['value']


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

    for node in nodes:
        if not node['type'] in ['value', 'output']:

            res = fetch(node['type'])([getattr(__builtins__[i[1].split('_')[0].lower()], '__call__')(i[0]) for i in [((node['value']), node['label'])  # return
                                                                                                                     # for all input nodes
                                                                                                                     for i in node['inputs']
                                                                                                                     # interate nodes to find input nodes
                                                                                                                     for node in nodes
                                                                                                                     # condition to find the input node
                                                                                                                     if i == node['label']

                                                                                                                     ]])
            node['outputs'].append(res)
            node['value'] = res

    for node in nodes:
        if node['type'] == 'output':
            node['value'] = ([node['value'] for i in node['inputs']
                              for node in nodes if i == node['label']])
            # print()

    return (node for node in nodes if node['type'] == 'output')
