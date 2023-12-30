NODES = {
    'vigor': {
        'serial': {
            'device': '/dev/ttyAMA0',
            'baudrate': 19200,
        },
        'byteorder': '>', 'wordorder': '>',
        'slave': 20,
    },
    'calibra': {
        'tcp': {
            'host': '172.16.1.14',
            'port': 502,
        },
        'byteorder': '>', 'wordorder': '>',
        'slave': 1,
    },
    'alfen': {
        'tcp': {
            'host': '172.16.1.25',
            'port': 502,
        },
        'byteorder': '>', 'wordorder': '>',
        'slave': 1,
        'delay': 0.100,
    },
}
