# main.py
import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_folder='input_images', output_folder='output_images', watermark_text='Confidential'):
    """
    Adds a text watermark to all images in a specified folder.

    Args:
        input_folder (str): The folder containing the original images.
        output_folder (str): The folder where watermarked images will be saved.
        watermark_text (str): The text to be used as the watermark.
    """
    # --- 1. Setup: Create folders if they don't exist ---
    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)
        
    if not os.path.exists(input_folder):
        print(f"Creating input folder: {input_folder}")
        os.makedirs(input_folder)
        print(f"Please add images to the '{input_folder}' directory and run the script again.")
        return

    # --- 2. Font and Text Configuration ---
    font_size = 36
    text_color = (255, 255, 255, 128)  # White with 50% opacity (R, G, B, A)
    margin = 20

    try:
        # Try to load a common font.
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # If the font is not found, use the default PIL font.
        print("Arial font not found. Using default font.")
        font = ImageFont.load_default()

    # --- 3. Process Images ---
    processed_count = 0
    for filename in os.listdir(input_folder):
        # Check for common image file extensions
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Construct full file paths
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                # Open the image
                with Image.open(input_path).convert("RGBA") as base_image:
                    # Create a transparent layer for the text
                    txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))

                    # Get a drawing context
                    draw = ImageDraw.Draw(txt_layer)

                    # --- 4. Calculate Text Position ---
                    # Get the width and height of the text
                    try:
                        # Use getbbox for newer Pillow versions
                        _, _, text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)
                    except AttributeError:
                        # Fallback for older Pillow versions
                        text_width, text_height = draw.textsize(watermark_text, font=font)


                    # Get image dimensions
                    image_width, image_height = base_image.size

                    # Position at the bottom-right corner
                    x = image_width - text_width - margin
                    y = image_height - text_height - margin

                    # --- 5. Add Watermark and Save ---
                    # Draw the text on the transparent layer
                    draw.text((x, y), watermark_text, font=font, fill=text_color)

                    # Composite the text layer onto the base image
                    watermarked_image = Image.alpha_composite(base_image, txt_layer)
                    
                    # Convert back to RGB to save as JPG if needed
                    final_image = watermarked_image.convert("RGB")

                    # Save the final image
                    final_image.save(output_path)
                    print(f"Added watermark to {filename}")
                    processed_count += 1

            except Exception as e:
                print(f"Could not process {filename}. Reason: {e}")

    if processed_count == 0:
        print(f"No images found to process in '{input_folder}'.")
    else:
        print(f"\nWatermarking complete. Processed {processed_count} images.")
        print(f"Check the '{output_folder}' directory for your watermarked images.")

if __name__ == '__main__':
    # You can customize the watermark text here
    add_watermark(watermark_text="© The Digital Nomad")

