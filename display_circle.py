import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import colorsys

# Génération de couleurs aléatoires
def generate_random_colors(n):
    colors = []
    for i in range(n):
        # Utiliser HSV pour générer des couleurs vives et variées
        h = random.random()  # Teinte aléatoire entre 0 et 1
        s = 0.8 + random.random() * 0.2  # Saturation entre 0.8 et 1.0
        v = 0.8 + random.random() * 0.2  # Luminosité entre 0.8 et 1.0
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        colors.append((r, g, b))
    return colors

# Fonction de tri à bulles qui enregistre les états intermédiaires
def bubble_sort(arr, colors):
    n = len(arr)
    # Tableaux pour stocker les états intermédiaires
    states = [arr.copy()]
    color_states = [colors.copy()]

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Échanger les valeurs
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Échanger également les couleurs correspondantes
                colors[j], colors[j+1] = colors[j+1], colors[j]
                states.append(arr.copy())
                color_states.append(colors.copy())
    
    # Add this return statement
    return states, color_states
# Paramètres
n = 50  # Nombre d'éléments
arr = list(range(1, n+1))
random.shuffle(arr)  # Mélanger les valeurs
colors = generate_random_colors(n)  # Générer des couleurs aléatoires

# Obtenir les états intermédiaires du tri
states, color_states = bubble_sort(arr.copy(), colors.copy())

# Créer la figure et l'axe
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Fonction pour dessiner le cercle de couleurs
def draw_color_circle(values, colors, ax):
    ax.clear()
    ax.set_axis_off()  # Masquer les axes
    
    # Calculer l'angle pour chaque segment
    segment_angle = 2 * np.pi / len(values)
    
    # Dessiner chaque segment coloré
    for i, (value, color) in enumerate(zip(values, colors)):
        # Calculer les angles de début et de fin pour ce segment
        start_angle = i * segment_angle
        end_angle = (i + 1) * segment_angle
        
        # Créer un secteur pour chaque segment
        wedge = plt.matplotlib.patches.Wedge(
            center=(0, 0),
            r=0.8 + 0.2 * (value / max(values)),  # Rayon proportionnel à la valeur
            theta1=np.rad2deg(start_angle),
            theta2=np.rad2deg(end_angle),
            width=0.6,  # Largeur du secteur
            facecolor=color,
            edgecolor='white',
            linewidth=0.5
        )
        ax.add_patch(wedge)
    
    # Ajouter un cercle au centre pour l'esthétique
    circle = plt.Circle((0, 0), 0.2, color='white')
    ax.add_patch(circle)
    
    return ax

# Fonction d'initialisation pour l'animation
def init():
    return draw_color_circle(states[0], color_states[0], ax)

# Fonction de mise à jour pour l'animation
def update(frame):
    ax.set_title(f'Tri à bulles - Étape {frame}/{len(states)-1}', fontsize=14)
    return draw_color_circle(states[frame], color_states[frame], ax)

# Créer l'animation
ani = animation.FuncAnimation(fig, update, frames=len(states),
                              init_func=init, blit=False, interval=10)

plt.tight_layout()
plt.show()

# Pour sauvegarder l'animation (optionnel, nécessite ffmpeg)
# ani.save('tri_cercle_couleurs.mp4', writer='ffmpeg', fps=30)