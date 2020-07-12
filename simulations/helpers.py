import numpy as np
import matplotlib.pyplot as plt

def show_topology(layout):
    plt.figure(figsize=(30,30))
    for node in layout['relay_network']['nodes']:
        x, y = layout['relay_network']['nodes'][node]['location']
        plt.scatter(x, y, marker='o', color='red')
        plt.text(x+.43, y+.43, f"""{node} UPT{layout['relay_network']['nodes'][node]['uptime']}""", fontsize=12, backgroundcolor='0.85')

    for conn in layout['relay_network']['connections']:
        frm = layout['relay_network']['connections'][conn]['from']
        to = layout['relay_network']['connections'][conn]['to']
        x1, y1 = layout['relay_network']['nodes'][frm]['location']
        x2, y2 = layout['relay_network']['nodes'][to]['location']
        plt.plot((x1, x2), (y1, y2), color='red')
        plt.text((x1+x2)/2.0+.03, (y1+y2)/2.0+.03, f"""{conn} LAT{layout['relay_network']['connections'][conn]['latency']} PKL{layout['relay_network']['connections'][conn]['packet_loss']} {layout['relay_network']['connections'][conn]['type']}""", fontsize=8, backgroundcolor='0.85')
    
    for cnode in layout['consumer_nodes']['nodes']:
        x, y = layout['consumer_nodes']['nodes'][cnode]['location']
        plt.scatter(x, y, marker='x', color='blue')
        plt.text(x+.43, y+.43, f"""{cnode} UPT{layout['consumer_nodes']['nodes'][cnode]['uptime']}""", fontsize=8)
    
    for conn in layout['consumer_nodes']['connections']:
        frm = layout['consumer_nodes']['connections'][conn]['from']
        to = layout['consumer_nodes']['connections'][conn]['to']
        x1, y1 = layout['consumer_nodes']['nodes'][frm]['location']
        if layout['consumer_nodes']['connections'][conn]['type'] == 'bi_cons_rel':
            x2, y2 = layout['relay_network']['nodes'][to]['location']
        plt.plot((x1, x2), (y1, y2), color='#ddd')
        plt.text((x1+x2)/2.0+.03, (y1+y2)/2.0+.03, f"""{conn} LAT{layout['consumer_nodes']['connections'][conn]['latency']} PKL{layout['consumer_nodes']['connections'][conn]['packet_loss']} {layout['consumer_nodes']['connections'][conn]['type']}""", fontsize=8, backgroundcolor='0.85')
    plt.show()

def generate_adjecency_list(layout):
    adjecency_list = dict()

    relay = layout['relay_network']
    consumers = layout['consumer_nodes']
    for node in relay['nodes']:
        adjecency_list[node] = list()

    for cnode in consumers['nodes']:
        adjecency_list[cnode] = list()

    for conn in relay['connections']:
        frm = relay['connections'][conn]['from']
        to  = relay['connections'][conn]['to']
        lat = relay['connections'][conn]['latency']
        pkl = relay['connections'][conn]['packet_loss']
        typ = relay['connections'][conn]['type']
        adjecency_list[frm].append({'to': to, 'latency': lat, 'packet_loss': pkl, 'type': typ})
        if typ == 'bi_rel_rel':
            adjecency_list[to].append({'to': frm, 'latency': lat, 'packet_loss': pkl, 'type': typ})
    
    print(adjecency_list)

    for conn in consumers['connections']:
        frm = consumers['connections'][conn]['from']
        to  = consumers['connections'][conn]['to']
        lat = consumers['connections'][conn]['latency']
        pkl = consumers['connections'][conn]['packet_loss']
        typ = consumers['connections'][conn]['type']
        adjecency_list[frm].append({'to': to, 'latency': lat, 'packet_loss': pkl, 'type': typ})
        if typ == 'bi_cons_rel':
            adjecency_list[to].append({'to': frm, 'latency': lat, 'packet_loss': pkl, 'type': typ})
    
    return adjecency_list