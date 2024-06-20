from tkinter import *
from ceaser import cipEncode, cipDecode
from vigenere import vigEncode, vigDecode
from imagecipher import text_to_image, image_to_text
from PIL import Image
import os

# Print the current working directory for debugging purposes
print("Current working directory:", os.getcwd())

# Define global variables to store the text and key
stored_text = ""
result_text = ""
keyword = ""
shift_value = 0
filename = ""

def sanitize_keyword(keyword):
    return ''.join(filter(str.isalpha, keyword))

def encrypter(gui):
    global cipher_method, text_textbox, keyword_textbox, keyword_label, shift_textbox, shift_label, filename_textbox, filename_label
    gui.title("Encrypter")

    cipher_method = StringVar(value="Image")
    cipher_method.trace("w", show_hide_key_fields)

    label = Label(gui, text="Enter text to be processed:")
    label.grid(row=0, column=0, padx=10, pady=10, sticky=W, columnspan=3)

    # Radio buttons for choosing the cipher method
    image_radio = Radiobutton(gui, text="Image Cipher", variable=cipher_method, value="Image")
    image_radio.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    caesar_radio = Radiobutton(gui, text="Caesar Cipher", variable=cipher_method, value="Caesar")
    caesar_radio.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vigenere_radio = Radiobutton(gui, text="Vigenere Cipher", variable=cipher_method, value="Vigenere")
    vigenere_radio.grid(row=2, column=2, padx=5, pady=5, sticky=W)

    # Textbox for the text to be processed
    text_textbox = Text(gui, height=3, width=50, borderwidth=5)
    text_textbox.grid(row=1, column=0, padx=10, pady=1, columnspan=3)
    text_textbox.bind("<Return>", lambda event: "break")

    # Label and textbox for the Caesar shift value (initially hidden)
    shift_label = Label(gui, text="Enter shift value for Caesar:")
    shift_textbox = Text(gui, height=1, width=30, borderwidth=5)

    # Label and textbox for the Vigenere key (initially hidden)
    keyword_label = Label(gui, text="Enter key for Vigenere:")
    keyword_textbox = Text(gui, height=1, width=30, borderwidth=5)

    # Label and textbox for the filename (initially hidden)
    filename_label = Label(gui, text="Enter filename for Image Cipher:")
    filename_textbox = Text(gui, height=1, width=30, borderwidth=5)

    # Buttons for choosing encrypt or decrypt
    encrypt_button = Button(gui, text="Encrypt", command=lambda: process_text("encrypt"))
    encrypt_button.grid(row=7, column=1, padx=10, pady=10, sticky=E)

    decrypt_button = Button(gui, text="Decrypt", command=lambda: process_text("decrypt"))
    decrypt_button.grid(row=7, column=2, padx=0, pady=10, sticky=W)

    global result_label
    result_label = Label(gui, text="")
    result_label.grid(row=9, column=0, padx=10, pady=10, columnspan=3)

def show_hide_key_fields(*args):
    if cipher_method.get() == "Caesar":
        shift_label.grid(row=5, column=0, padx=10, pady=10, sticky=W, columnspan=3)
        shift_textbox.grid(row=6, column=0, padx=10, pady=1, columnspan=3)
        keyword_label.grid_remove()
        keyword_textbox.grid_remove()
        filename_label.grid_remove()
        filename_textbox.grid_remove()
    elif cipher_method.get() == "Vigenere":
        keyword_label.grid(row=5, column=0, padx=10, pady=10, sticky=W, columnspan=3)
        keyword_textbox.grid(row=6, column=0, padx=10, pady=1, columnspan=3)
        shift_label.grid_remove()
        shift_textbox.grid_remove()
        filename_label.grid_remove()
        filename_textbox.grid_remove()
    else:
        filename_label.grid(row=5, column=0, padx=10, pady=10, sticky=W, columnspan=3)
        filename_textbox.grid(row=6, column=0, padx=10, pady=1, columnspan=3)
        shift_label.grid_remove()
        shift_textbox.grid_remove()
        keyword_label.grid_remove()
        keyword_textbox.grid_remove()

def store_text():
    global stored_text
    stored_text = text_textbox.get("1.0", END).strip()
    print(f"Stored text: {stored_text}")  # This is for demonstration purposes

def process_text(action):
    global stored_text, result_text, keyword, shift_value, filename
    store_text()  # Automatically store the input text
    if cipher_method.get() == "Caesar":
        shift_value = int(shift_textbox.get("1.0", END).strip() or "0")  # Get the shift value from the textbox
        if action == "encrypt":
            result_text = cipEncode(stored_text, shift_value)
        elif action == "decrypt":
            result_text = cipDecode(stored_text, shift_value)
    elif cipher_method.get() == "Vigenere":
        keyword = sanitize_keyword(keyword_textbox.get("1.0", END).strip())  # Sanitize the key from the textbox
        if action == "encrypt":
            result_text = vigEncode(stored_text, keyword)
        elif action == "decrypt":
            result_text = vigDecode(stored_text, keyword)
    elif cipher_method.get() == "Image": 
        filename = filename_textbox.get("1.0", END).strip()
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filename += '.png'  # Default to .png if no valid extension is provided
        if action == "encrypt":
            text_to_image(stored_text, filename)
            result_text = f'Image saved as {filename}'
        elif action == "decrypt":
            try:
                decrypted_text = image_to_text(filename)
                result_text = ''.join([char for char in decrypted_text if char != 'ÿ'])
            except Exception as e:
                result_text = f"Error decrypting image: {e}"
    print(f"Processed text ({action}): {result_text}")
    result_label.config(text=f"Processed text: {result_text}")

if __name__ == "__main__":
    gui = Tk()
    encrypter(gui)
    gui.mainloop()