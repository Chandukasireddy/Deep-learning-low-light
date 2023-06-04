import urllib.request
import cv2
from google.colab.patches import cv2_imshow

# Load the low light image from URL
url = 'https://media.istockphoto.com/id/906520112/photo/ovary-cystadenoma-biopsy-under-light-microscopy-in-different-area.jpg?s=612x612&w=is&k=20&c=5xIQfP89V0gq8auswNgA_pTjeeZZoJKBKanZYZkjPxc='
urllib.request.urlretrieve(url, 'low_light_image.jpg')
img = cv2.imread('low_light_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive histogram equalization to improve contrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
equalized = clahe.apply(gray)

# Apply bilateral filter to reduce noise while preserving edges
filtered = cv2.bilateralFilter(equalized, 9, 75, 75)

# Display the original and enhanced images side by side
cv2_imshow(img)
cv2_imshow(filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
