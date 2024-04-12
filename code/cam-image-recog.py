from PIL import Image

def compress_and_find_black(image_path):
    # Open the image
    img = Image.open(image_path)

    # Resize the image to 480x480
    img = img.resize((480, 480))

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Threshold the image to get a binary image
    threshold = 128
    img_binary = img_gray.point(lambda p: p < threshold and 255)

    # Get the coordinates of black pixels
    black_pixels = []
    width, height = img_binary.size
    for y in range(height):
        for x in range(width):
            if img_binary.getpixel((x, y)) == 0:  # 0 represents black
                black_pixels.append((x, y))

    return black_pixels

# Example usage:
image_path = "test\one.jpg"
black_coordinates = compress_and_find_black(image_path)
print("Coordinates of black pixels:", black_coordinates)
