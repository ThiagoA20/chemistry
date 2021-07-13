import matplotlib.pyplot as plt
import matplotlib as mpl
import base64
from io import BytesIO
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8, 5))
    plt.title('test1')
    plt.grid()
    plt.plot(x, y, color='k')
    plt.xlabel('x side')
    plt.ylabel('y side')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_variation(x1, x2, p):
    x = np.linspace(x1, x2, p)
    return x

def get_function(x):
    y = []
    for i in x:
        y.append(np.sin(i))
    return y