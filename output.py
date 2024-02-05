import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

def plot_all_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only image files
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Calculate the number of rows and columns for subplots
    num_images = len(image_files)
    num_cols = min(4, num_images)  # Adjust the number of columns as needed
    num_rows = (num_images - 1) // num_cols + 1

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    # Plot each image in a subplot
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(folder_path, image_file)
        image = imread(image_path)

        if num_rows == 1:
            ax = axes[i % num_cols]
        else:
            ax = axes[i // num_cols, i % num_cols]

        ax.imshow(image)
        ax.set_title(image_file)
        ax.axis('off')

    # Adjust layout for better visualization
    plt.tight_layout()
    plt.show()

# Example usage: replace 'path/to/your/images' with the actual path to your image folder
plot_all_images('E:\StudyFPT\Do an\Style-Your-Hair-main\style_your_hair_output\source_target_flip_final')