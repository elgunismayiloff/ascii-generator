#!/usr/bin/env python3
"""
🎨 Interactive ASCII Art Generator
Converts images to beautiful ASCII art with interactive file selection and customization.
"""

import os
import sys
from PIL import Image, ImageEnhance
import tkinter as tk
from tkinter import filedialog, messagebox
import platform

class ASCIIArtGenerator:
    def __init__(self):
        # Different ASCII character sets for different styles
        self.char_sets = {
            '1': {"name": "Detailed", "chars": "@%#*+=-:. "},
            '2': {"name": "Blocks", "chars": "█▉▊▋▌▍▎▏ "},
            '3': {"name": "Classic", "chars": "@#S%?*+;:,."},
            '4': {"name": "Minimal", "chars": "██▓▒░  "},
            '5': {"name": "Dots", "chars": "●◐◑◒◓◔◕○ "},
            '6': {"name": "Simple", "chars": "█▓▒░ "}
        }
        
        self.colors = {
            '1': {"name": "No Color", "code": None},
            '2': {"name": "Red", "code": '\033[91m'},
            '3': {"name": "Green", "code": '\033[92m'},
            '4': {"name": "Yellow", "code": '\033[93m'},
            '5': {"name": "Blue", "code": '\033[94m'},
            '6': {"name": "Purple", "code": '\033[95m'},
            '7': {"name": "Cyan", "code": '\033[96m'},
            '8': {"name": "White", "code": '\033[97m'}
        }
        
        self.reset_color = '\033[0m'

    def select_image_file(self):
        """Open file dialog to select image"""
        try:
            # Hide the root tkinter window
            root = tk.Tk()
            root.withdraw()
            
            # Open file dialog
            file_path = filedialog.askopenfilename(
                title="🖼️ Select an Image File",
                filetypes=[
                    ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
                    ("JPEG files", "*.jpg *.jpeg"),
                    ("PNG files", "*.png"),
                    ("All files", "*.*")
                ]
            )
            
            root.destroy()
            return file_path
        except Exception as e:
            print(f"❌ Error opening file dialog: {e}")
            return None

    def get_user_preferences(self):
        """Get user preferences interactively"""
        print("🎨 ASCII Art Generator - Interactive Mode")
        print("=" * 50)
        
        # Display style options
        print("\n🎯 Choose ASCII Style:")
        for key, value in self.char_sets.items():
            print(f"  {key}. {value['name']} - {value['chars'][:5]}...")
        
        while True:
            style_choice = input("\nEnter style number (1-6): ").strip()
            if style_choice in self.char_sets:
                break
            print("❌ Invalid choice! Please enter 1-6")
        
        # Display color options
        print("\n🌈 Choose Color:")
        for key, value in self.colors.items():
            print(f"  {key}. {value['name']}")
        
        while True:
            color_choice = input("\nEnter color number (1-8): ").strip()
            if color_choice in self.colors:
                break
            print("❌ Invalid choice! Please enter 1-8")
        
        # Get width
        while True:
            try:
                width = input("\n📏 Enter width (20-200, default 100): ").strip()
                if width == "":
                    width = 100
                else:
                    width = int(width)
                if 20 <= width <= 200:
                    break
                else:
                    print("❌ Width must be between 20 and 200!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Get brightness
        while True:
            try:
                brightness = input("\n💡 Brightness (0.5-2.0, default 1.0): ").strip()
                if brightness == "":
                    brightness = 1.0
                else:
                    brightness = float(brightness)
                if 0.5 <= brightness <= 2.0:
                    break
                else:
                    print("❌ Brightness must be between 0.5 and 2.0!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Get contrast
        while True:
            try:
                contrast = input("🔆 Contrast (0.5-2.0, default 1.0): ").strip()
                if contrast == "":
                    contrast = 1.0
                else:
                    contrast = float(contrast)
                if 0.5 <= contrast <= 2.0:
                    break
                else:
                    print("❌ Contrast must be between 0.5 and 2.0!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        return {
            'style': self.char_sets[style_choice]['chars'],
            'style_name': self.char_sets[style_choice]['name'],
            'color': self.colors[color_choice]['code'],
            'color_name': self.colors[color_choice]['name'],
            'width': width,
            'brightness': brightness,
            'contrast': contrast
        }

    def resize_image(self, image, new_width=100):
        """Resize image while maintaining aspect ratio"""
        width, height = image.size
        ratio = height / width / 1.65  # Adjust for character height
        new_height = int(new_width * ratio)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def grayscale_to_ascii(self, image, chars):
        """Convert grayscale image to ASCII"""
        pixels = image.getdata()
        
        ascii_str = ""
        for pixel in pixels:
            # Map pixel value (0-255) to character index
            char_index = int(pixel * (len(chars) - 1) / 255)
            ascii_str += chars[char_index]
        
        return ascii_str

    def add_color(self, ascii_art, width, color_code):
        """Add color to ASCII art"""
        if not color_code:
            return ascii_art
        
        lines = []
        for i in range(0, len(ascii_art), width):
            line = ascii_art[i:i+width]
            colored_line = color_code + line + self.reset_color
            lines.append(colored_line)
        
        return '\n'.join(lines)

    def generate_ascii_art(self, image_path, preferences):
        """Main function to generate ASCII art"""
        try:
            print(f"\n📸 Processing image: {os.path.basename(image_path)}")
            print("⏳ Please wait...")
            
            # Open and process image
            image = Image.open(image_path)
            
            # Adjust brightness and contrast
            if preferences['brightness'] != 1.0:
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(preferences['brightness'])
            
            if preferences['contrast'] != 1.0:
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(preferences['contrast'])
            
            # Convert to grayscale and resize
            image = image.convert('L')
            image = self.resize_image(image, preferences['width'])
            
            # Generate ASCII art
            ascii_art = self.grayscale_to_ascii(image, preferences['style'])
            
            # Format into lines
            img_width = image.size[0]
            ascii_lines = []
            for i in range(0, len(ascii_art), img_width):
                ascii_lines.append(ascii_art[i:i+img_width])
            
            ascii_result = '\n'.join(ascii_lines)
            
            # Add color if specified
            if preferences['color']:
                ascii_result = self.add_color(ascii_art, img_width, preferences['color'])
            
            return ascii_result
            
        except Exception as e:
            return f"❌ Error processing image: {str(e)}"

    def save_to_file(self, ascii_art, filename=None):
        """Save ASCII art to file"""
        if not filename:
            filename = f"ascii_art_{self.get_timestamp()}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Remove color codes when saving to file
                clean_art = ascii_art
                for color_info in self.colors.values():
                    if color_info['code']:
                        clean_art = clean_art.replace(color_info['code'], '')
                clean_art = clean_art.replace(self.reset_color, '')
                f.write(clean_art)
            return filename
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            return None

    def get_timestamp(self):
        """Get current timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def display_summary(self, preferences, image_path):
        """Display settings summary"""
        print("\n" + "="*50)
        print("⚙️  SETTINGS SUMMARY")
        print("="*50)
        print(f"📁 Image: {os.path.basename(image_path)}")
        print(f"🎯 Style: {preferences['style_name']}")
        print(f"🌈 Color: {preferences['color_name']}")
        print(f"📏 Width: {preferences['width']}")
        print(f"💡 Brightness: {preferences['brightness']}")
        print(f"🔆 Contrast: {preferences['contrast']}")
        print("="*50)

def main():
    generator = ASCIIArtGenerator()
    
    print("🎨 Welcome to ASCII Art Generator!")
    print("🖼️  This tool converts your images into beautiful ASCII art")
    print("-" * 60)
    
    while True:
        # Step 1: Select image file
        print("\n🖼️  Step 1: Select your image file")
        image_path = generator.select_image_file()
        
        if not image_path:
            print("❌ No file selected!")
            if input("\n🔄 Try again? (y/n): ").lower() != 'y':
                print("👋 Goodbye!")
                return
            continue
        
        if not os.path.exists(image_path):
            print(f"❌ File not found: {image_path}")
            continue
        
        # Step 2: Get user preferences
        try:
            preferences = generator.get_user_preferences()
        except KeyboardInterrupt:
            print("\n\n👋 Operation cancelled. Goodbye!")
            return
        
        # Step 3: Display summary
        generator.display_summary(preferences, image_path)
        
        # Step 4: Generate ASCII art
        ascii_art = generator.generate_ascii_art(image_path, preferences)
        
        if ascii_art.startswith("❌"):
            print(ascii_art)
            continue
        
        # Step 5: Display result
        print("\n🎉 ASCII ART RESULT:")
        print("="*60)
        print(ascii_art)
        print("="*60)
        
        # Step 6: Save option
        save_choice = input("\n💾 Save to file? (y/n): ").lower()
        if save_choice == 'y':
            filename = generator.save_to_file(ascii_art)
            if filename:
                print(f"✅ Saved as: {filename}")
            else:
                print("❌ Failed to save file")
        
        # Step 7: Continue or exit
        if input("\n🔄 Convert another image? (y/n): ").lower() != 'y':
            print("\n🎨 Thanks for using ASCII Art Generator!")
            print("⭐ Don't forget to star this project on GitHub!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue on GitHub!")