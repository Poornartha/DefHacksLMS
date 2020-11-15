import os, io 
from google.cloud import vision
from google.cloud.vision import types
try:
 from PIL import Image
except ImportError:
 import Image

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'env/inbound-augury-295618-714320b1a66f.json'

client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'C:\Users\spoor\Desktop\Git\HackLMS\media'
# IMAGE_FILE = 'handwriting1.png'

def read_image(IMAGE_FILE):
    FILE_PATH = os.path.join(FOLDER_PATH, str(IMAGE_FILE))
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    return docText



