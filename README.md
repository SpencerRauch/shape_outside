# PNG Outline to CSS Shape-Outside Polygon

This project provides a Python script that uses the Pillow library to generate `shape-outside: polygon` coordinates for the outline of the visible elements in a PNG image with a transparent border.

## Features

- Load a PNG image with a transparent border.
- Detect the edges of the visible elements.
- Generate `shape-outside: polygon` coordinates for the outline.

## Requirements

- Python 3.x
- Pillow
- NumPy
- SciPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SpencerRauch/png-outline-to-css-shape-outside.git
    cd png-outline-to-css-shape-outside
    ```

2. Install the required packages:
    ```bash
    pip install Pillow numpy scipy
    ```

## Usage

1. Place your PNG image in the project directory.

2. Run the script:
    ```bash
    python shape_outside.py your_image.png
    ```

3. The script will output the `shape-outside: polygon` coordinates and save an image of the outline as `outline.png`.

## Example

Here's an example of how to use the generated `shape-outside: polygon` coordinates in your CSS:

```css
.shape {
    float: left;
    width: 300px;
    height: 300px;
    shape-outside: polygon(20% 10%, 30% 5%, 40% 10%, 50% 20%, 60% 30%, 70% 40%, 80% 50%, 70% 60%, 60% 70%, 50% 80%, 40% 90%, 30% 85%, 20% 80%, 10% 70%, 5% 60%, 10% 50%, 15% 40%, 20% 30%);
}
