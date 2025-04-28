import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import uuid

def create_wbs_box(ax, text, x, y, width, height, level=0):
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                        facecolor=colors[level % len(colors)], edgecolor='black')
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', wrap=True)

def draw_wbs():
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Level 1: Project
    create_wbs_box(ax, "Project", 40, 90, 20, 8, 0)

    # Level 2: Main Categories
    categories = ["Frontend", "Backend", "Database", "Documentation", "Testing", "Deployment"]
    for i, cat in enumerate(categories):
        x = 10 + (i % 3) * 30
        y = 70 - (i // 3) * 20
        create_wbs_box(ax, cat, x, y, 25, 8, 1)

    plt.savefig('wbs_diagram.png')
    plt.close()

if __name__ == "__main__":
    draw_wbs()