import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the gradient using Sobel filters
gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the magnitude of the gradient
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Normalize the gradient to the range [0, 255]
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Convert the gradient magnitude back to uint8 data type
gradient_magnitude = np.uint8(gradient_magnitude)

# Sharpen the image by adding the gradient back to the original image
sharpened_image = cv2.addWeighted(image, 1.5, cv2.cvtColor(gradient_magnitude, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the original image and sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened_image)

