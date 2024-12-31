from PIL import Image, ImageFilter
import numpy as np
import sys
from scipy.spatial import ConvexHull

def generate_shape_outside_coordinates(image_path):
    # Open the image
    image = Image.open(image_path).convert('RGBA')

    # Extract the alpha channel
    alpha = image.split()[3]

    # Find edges in the alpha channel
    edges = alpha.filter(ImageFilter.FIND_EDGES)

    # Convert edges to numpy array
    edges_array = np.array(edges)

    # Get the coordinates of the non-transparent pixels
    coordinates = np.column_stack(np.where(edges_array > 0))

    # Normalize coordinates to percentages
    height, width = edges_array.shape
    normalized_coordinates = [(x / width * 100, y / height * 100) for y, x in coordinates]

    # Use ConvexHull to sort the coordinates around the perimeter
    hull = ConvexHull(normalized_coordinates)
    hull_coordinates = [normalized_coordinates[i] for i in hull.vertices]

    # Format coordinates for CSS
    css_coordinates = ', '.join([f'{x:.2f}% {y:.2f}%' for x, y in hull_coordinates])

    print(f'shape-outside: polygon({css_coordinates});')
    return f'shape-outside: polygon({css_coordinates});'

if __name__== "__main__":
    generate_shape_outside_coordinates(sys.argv[1])
