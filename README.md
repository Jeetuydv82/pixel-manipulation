🖼️ Image Encryption & Decryption Tool (Python)
This is a simple Python project that encrypts and decrypts images using basic pixel manipulation. It modifies the RGB values of each pixel using a numeric key, making the image unreadable until decrypted with the correct key.

🔧 Features
🔐 Encrypts an image by altering RGB pixel values using a key.

🔓 Decrypts the image using the same key to restore the original.

🖼️ Supports .jpg, .png, and other formats supported by Pillow (PIL).

🧠 Simple math-based logic: (R + key) % 256 for encryption, (R - key) % 256 for decryption.

📦 Requirements
Python 3

Pillow (PIL fork)

Install Pillow:

bash
Copy
Edit
pip install Pillow
🚀 How It Works
Encryption Logic:
Each pixel’s RGB value is increased by the key (modulo 256):

python
Copy
Edit
R' = (R + key) % 256
G' = (G + key) % 256
B' = (B + key) % 256
Decryption Logic:
The encrypted image is reversed using:

python
Copy
Edit
R = (R' - key) % 256
G = (G' - key) % 256
B = (B' - key) % 256
💻 How to Use
Place an image in the project folder (e.g., cat.jpg).

Run the script:

bash
Copy
Edit
python image_encryptor.py
Follow prompts:

mathematica
Copy
Edit
Do you want to (E)ncrypt or (D)ecrypt? E
Enter the input image file path: cat.jpg
Enter the output image file path: encrypted_cat.jpg
Enter the encryption/decryption key (integer): 42
To decrypt:

mathematica
Copy
Edit
Do you want to (E)ncrypt or (D)ecrypt? D
Enter the input image file path: encrypted_cat.jpg
Enter the output image file path: decrypted_cat.jpg
Enter the encryption/decryption key (integer): 42
📁 File Structure
matlab
Copy
Edit
project-folder/
├── image_encryptor.py
├── cat.jpg
├── encrypted_cat.jpg
└── decrypted_cat.jpg
⚠️ Notes
You must use the same key for decryption as you used during encryption.

Does not provide cryptographic security — it’s for educational/demo purposes only.
