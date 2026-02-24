from PIL import Image

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

     # Swap again to restore
    for x in range(0, width - 1, 2):
        for y in range(height):
            pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]

    img.save(output_path)
    print("Decryption Complete!")

# Run
decrypt_image("encrypted.png", "decrypted.png", key=50)