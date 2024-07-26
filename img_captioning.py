# -*- coding: utf-8 -*-
"""img_captioning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MFXrygw8R0z7ANto10p96Sl5FMY0GOT9
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Load the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    # Check if the image path is a URL
    if image_path.startswith("http"):
        # Load image from URL
        response = requests.get(image_path)
        image = Image.open(BytesIO(response.content))
    else:
        # Load image from file system
        image = Image.open(image_path)

    # Preprocess the image
    inputs = processor(images=image, return_tensors="pt")

    # Generate captions
    outputs = model.generate(**inputs)

    # Decode the generated captions
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption,image

# Example usage
print()
print()
image_path = input("ENTER IMG PATH")
print()
 # Replace with your image path
caption,image = generate_caption(image_path)

# Display the image with the caption
plt.imshow(image)
plt.title(caption, fontsize=15)
plt.axis('off')
plt.show()
