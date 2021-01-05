def layers(atomic_number):
    layer = {
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0
    }
    i = 0
    while i < atomic_number:
        if layer['K'] < 2:
            layer['K'] += 1
        elif layer['L'] < 8:
            layer['L'] += 1
        elif layer['M'] < 18:
            layer['M'] += 1
        elif layer['N'] < 32:
            layer['N'] += 1
        elif layer['O'] < 32:
            layer['O'] += 1
        elif layer['P'] < 18:
            layer['P'] += 1
        elif layer['Q'] < 8:
            layer['Q'] += 1
        i += 1
    return layer


def sublayers():
    pass


def orbit():
    pass


def spin():
    pass
