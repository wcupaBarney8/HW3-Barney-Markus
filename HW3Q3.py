import skimage.io as io
from skimage.filters import sobel_h, sobel_v
import matplotlib.pyplot as plt

# Load an image of your choice
image = io.imread('flying.png', as_gray=True)

# Apply Sobel filters
sobel_x = sobel_h(image)
sobel_y = sobel_v(image)

# Display the results
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 3, 2)
plt.title('Sobel X-Filter')
plt.imshow(sobel_x, cmap='gray')
plt.subplot(1, 3, 3)
plt.title('Sobel Y-Filter')
plt.imshow(sobel_y, cmap='gray')
plt.show()
