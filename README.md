Python Image Watermarker
A simple yet powerful Python script to automatically add a text watermark to all images in a specified folder. This tool is perfect for photographers, content creators, and businesses who need to protect their digital assets before sharing them online.

Features
Batch Processing: Add watermarks to an entire folder of images at once.

Customizable Text: Easily change the watermark text to your name, brand, or copyright notice.

Adjustable Appearance: Modify the font, size, color, and opacity of the watermark.

Automatic Positioning: The script intelligently places the watermark in the bottom-right corner of each image, regardless of its dimensions.

Cross-Platform: Runs on any system with Python and the Pillow library installed.

Safe Processing: Your original images are kept untouched. The script saves the new watermarked images in a separate output folder.

Requirements
Before you begin, ensure you have the following installed:

Python 3.x

Pillow Library: The Python Imaging Library fork.

You can install Pillow using pip:

pip install Pillow

How to Use
Clone the Repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

Create the Input Folder:
In the main project directory, create a folder named input_images.

Add Your Images:
Place all the images you want to watermark inside the input_images folder.

Run the Script:
Execute the script from your terminal:

python main.py

Find Your Watermarked Images:
The script will automatically create an output_images folder containing all the processed images.

Customization
You can easily customize the watermark by editing the main.py script.

Change Watermark Text
To change the text of the watermark, modify the watermark_text argument in the function call at the bottom of the script (line 102):

if __name__ == '__main__':
    # Change the text inside the quotes
    add_watermark(watermark_text="© Your Brand 2025")

Change Font, Color, and Size
To adjust the appearance, you can change the variables near the top of the add_watermark function:

def add_watermark(...):
    # ...
    # --- 2. Font and Text Configuration ---
    font_size = 36
    text_color = (255, 255, 255, 128)  # RGBA: (Red, Green, Blue, Opacity)
    margin = 20

    try:
        # You can change "arial.ttf" to another font file
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    # ...
