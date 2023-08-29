from flask import Flask, jsonify
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_random_surface(x, y):
    choice = random.randint(0, 2)
    if choice == 0:
        return np.sin(np.sqrt(x**2 + y**2))
    elif choice == 1:
        return np.cos(x) + np.sin(y)
    else:
        return np.exp(-(x**2 + y**2))

@app.route('/generate_image')
def generate_image():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    x, y = np.meshgrid(x, y)
    z = generate_random_surface(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.axis('off')
    ax.set_facecolor((1.0, 1.0, 1.0))
    
    ax.plot_surface(x, y, z, cmap='viridis')

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()

    img_buffer.seek(0)
    
    # Converte l'immagine in base64
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    
    return jsonify({'image': img_base64})

if __name__ == '__main__':
    app.run()
