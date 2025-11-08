import cv2
from io import BytesIO
import numpy as np

## uploaded file is image_file
## in_memory_file is only in the memory
def process_image(image_file):
  ## save the uploaded file to memory
  in_memory_file = BytesIO()
  image_file.save(in_memory_file)

  ## get byte data of the image
  image_bytes = in_memory_file.getvalue()
  ## convert byte data to np array
  nparr = np.frombuffer(image_bytes, np.uint8)

  ## convert np array to opencv format
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  ## get a grayscale image of the color image, from RGB to gray
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  ## pre-trained model to detect face
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

  faces = face_cascade.detectMultiScale(gray, 1.1, 5)

  ## if no faces in the image
  if len(faces) == 0:
    return image_bytes, None
  
  ## if >1 faces, get the largest of the multiple faces
  largest_face = max(faces, key=lambda r:r[2] * r[3])

  ## x-axis, y-axis, width, height of the largest face
  (x, y, w, h) = largest_face

  ## draw the rectangle on the largest face in green color (0,255,0)
  ## 3 is thickness
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

  ## encode the image to JPG
  is_success, buffer = cv2.imencode(".jpg", img)

  return buffer.tobytes(), largest_face
