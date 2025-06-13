from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGB')  # Ensure it's in RGB mode
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGB')
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def main():
    print("=== Simple Image Encryptor ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()
    input_path = input("Enter the input image file path: ").strip()
    output_path = input("Enter the output image file path: ").strip()
    key = int(input("Enter the encryption/decryption key (integer): "))

    if not os.path.exists(input_path):
        print("❌ Error: File not found!")
        return

    if choice == 'E':
        encrypt_image(input_path, output_path, key)
    elif choice == 'D':
        decrypt_image(input_path, output_path, key)
    else:
        print("❌ Invalid option. Please choose E or D.")

if __name__ == "__main__":
    main()
