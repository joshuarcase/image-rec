import os
from PIL import Image
from transformers import pipeline

# Number of images
photo_count = 0
dir = './input'
for path in os.listdir(dir):
  if os.path.isfile(os.path.join(dir, path)):
    photo_count += 1
print('Photos detected: ', photo_count, '\n')

# Fun image code
def photo_id(path):
  image_opened = Image.open(path)
  vision_classifier = pipeline(task="image-classification")
  result = vision_classifier(image_opened)
  print("\n".join([f"Class {d['label']} with score {round(d['score'], 4)}" for d in result]))

photo_id('test-image.jpg')
