import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/hi/OneDrive/Pictures/cat.jpeg")

# Define a kernel for image blurring (e.g., a 5x5 Gaussian kernel)
kernel_size = (5, 5)
sigma = 1.0
blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)

# Define a high-boost mask (A value typically greater than 1, e.g., 2)
A = 2
high_boost_mask = np.array([[-1, -1, -1],
                            [-1, A+8, -1],
                            [-1, -1, -1]])

# Apply the high-boost filter
sharpened_image = cv2.filter2D(image, -1, high_boost_mask)

# Display the original image, blurred image, and sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Sharpened Image', sharpened_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened_image)

