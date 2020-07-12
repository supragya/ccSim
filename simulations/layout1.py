layout = {
    'relay_network': {
        'nodes': {
            'relay_01': {
                'location': (15,20),
                'uptime': 1
            },
            'relay_02': {
                'location': (40,2),
                'uptime': 1
            },
            'relay_03': {
                'location': (40,22),
                'uptime': 1
            },
            'relay_04': {
                'location': (20, 60),
                'uptime': 1
            }
        },
        'connections': {
            'r_01_02': {
                'from': 'relay_01',
                'to': 'relay_02',
                'type': 'bi_rel_rel',
                'latency': 20,
                'packet_loss': 0.01
            },
            'r_02_03': {
                'from': 'relay_02',
                'to': 'relay_03',
                'type': 'bi_rel_rel',
                'latency': 50,
                'packet_loss': 0.2
            },
            'r_03_04': {
                'from': 'relay_03',
                'to': 'relay_04',
                'type': 'bi_rel_rel',
                'latency': 40,
                'packet_loss': 0.03
            },
            'r_01_04': {
                'from': 'relay_01',
                'to': 'relay_04',
                'type': 'bi_rel_rel',
                'latency': 20,
                'packet_loss': 0.07
            },
            'r_01_03': {
                'from': 'relay_01',
                'to': 'relay_03',
                'type': 'bi_rel_rel',
                'latency': 40,
                'packet_loss': 0.01
            }
        }
    },
    'consumer_nodes': {
        'nodes': {
            'cons_01': {
                'location': (10,5),
                'connection': 'dynamic',
                'uptime': 0.7
            },
            'cons_02': {
                'location': (0,4),
                'connection': 'dynamic',
                'uptime': 0.2
            },
            'cons_03': {
                'location': (20,7),
                'connection': 'dynamic',
                'uptime': 1
            },
            'cons_04': {
                'location': (1,10),
                'connection': 'dynamic',
                'uptime': 1
            },
            'cons_05': {
                'location': (10,71),
                'connection': 'dynamic',
                'uptime': 0.8
            },
            'cons_06': {
                'location': (20,80),
                'connection': 'dynamic',
                'uptime': 1
            },
            'cons_07': {
                'location': (55,24),
                'connection': 'dynamic',
                'uptime': 0.5
            },
            'cons_08': {
                'location': (50,10),
                'connection': 'dynamic',
                'uptime': 1
            },
            'cons_09': {
                'location': (50,45),
                'connection': 'dynamic',
                'uptime': 0.9
            },
            'cons_10': {
                'location': (37,12),
                'connection': 'dynamic',
                'uptime': 1
            }
        },
        'connections': {
            'c_01_r01': {
                'from': 'cons_01',
                'to': 'relay_01',
                'type': 'bi_cons_rel',
                'latency': 20,
                'packet_loss': 0.01
            },
            'c_02_r01': {
                'from': 'cons_02',
                'to': 'relay_01',
                'type': 'bi_cons_rel',
                'latency': 20,
                'packet_loss': 0.01
            },
            'c_03_r01': {
                'from': 'cons_03',
                'to': 'relay_01',
                'type': 'bi_cons_rel',
                'latency': 20,
                'packet_loss': 0.01
            },
            'c_04_r01': {
                'from': 'cons_04',
                'to': 'relay_01',
                'type': 'bi_cons_rel',
                'latency': 20,
                'packet_loss': 0.4
            },
            'c_05_r04': {
                'from': 'cons_05',
                'to': 'relay_04',
                'type': 'bi_cons_rel',
                'latency': 20,
                'packet_loss': 0.01
            },
            'c_06_r04': {
                'from': 'cons_06',
                'to': 'relay_04',
                'type': 'bi_cons_rel',
                'latency': 30,
                'packet_loss': 0.02
            },
            'c_07_r03': {
                'from': 'cons_07',
                'to': 'relay_03',
                'type': 'bi_cons_rel',
                'latency': 30,
                'packet_loss': 0.2
            },
            'c_08_r03': {
                'from': 'cons_08',
                'to': 'relay_03',
                'type': 'bi_cons_rel',
                'latency': 30,
                'packet_loss': 0.01
            },
            'c_09_r03': {
                'from': 'cons_09',
                'to': 'relay_03',
                'type': 'bi_cons_rel',
                'latency': 30,
                'packet_loss': 0.4
            },
            'c_10_r03': {
                'from': 'cons_10',
                'to': 'relay_03',
                'type': 'bi_cons_rel',
                'latency': 30,
                'packet_loss': 0.9
            }
        }
    }    
}