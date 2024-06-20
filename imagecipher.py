from PIL import Image
import os

def text_to_image(text, image_filename):
    # Check if the image file exists
    if os.path.isfile(image_filename):
        # If the file exists, open the preexisting image and convert it to RGB
        image = Image.open(image_filename).convert("RGB")
    else:
        # If the file does not exist, create a new image with a default size
        image = Image.new("RGB", (200, 200), "white")
    
    pixels = list(image.getdata())
    width, height = image.size
    
    # Flatten the pixel list for easy manipulation
    flat_pixels = [list(pixel) for pixel in pixels]
    
    # Encode the text into the image
    text += chr(0)  # Null terminator for the end of the message
    index = 0
    for i in range(len(flat_pixels)):
        if index < len(text):
            flat_pixels[i][0] = ord(text[index])
            index += 1
        else:
            break
    
    # If the message is longer than the image can hold, throw an error
    if index < len(text):
        raise ValueError("The text is too long to fit in the provided image.")
    
    # Convert the flat pixel list back to tuples
    new_pixels = [tuple(pixel) for pixel in flat_pixels]
    
    # Create a new image with the modified pixels
    new_image = Image.new(image.mode, (width, height))
    new_image.putdata(new_pixels)
    
    # Save the new image
    new_image.save(image_filename)
    print(f"Image saved as {image_filename}")

def image_to_text(image_filename):
    try:
        # Open the image and convert it to RGB
        image = Image.open(image_filename).convert("RGB")
        pixels = list(image.getdata())
        
        # Decode the text from the image
        chars = []
        for pixel in pixels:
            char = chr(pixel[0])
            if char == chr(0):  # Null terminator indicates the end of the message
                break
            chars.append(char)
        
        return ''.join(chars)
    except Exception as e:
        return f"Error: {e}"