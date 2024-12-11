import skimage.io as io
import numpy as np
from skimage.morphology import opening, disk
import matplotlib.pyplot as plt

# Load the image
c = io.imread('circles.png').astype('bool') * 1

# Add random noise
x = np.random.random_sample(c.shape)
c[np.nonzero(x > 0.95)] = 0
c[np.nonzero(x <= 0.05)] = 1

# Display the noisy image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Noisy Image')
plt.imshow(c, cmap='gray')

# Apply morphological opening to remove noise
cleaned_image = opening(c, disk(1))

# Display the cleaned image
plt.subplot(1, 2, 2)
plt.title('Cleaned Image')
plt.imshow(cleaned_image, cmap='gray')
plt.show()
