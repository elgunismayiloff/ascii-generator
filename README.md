
# 🎨 Interactive ASCII Art Generator

Convert your images into stunning ASCII art right from the terminal — with color, style, and precision. This interactive Python tool helps you select an image, adjust style and brightness/contrast, and save beautiful ASCII renderings effortlessly.

## 🚀 Features

- 🖼️ **Interactive Image Picker** (GUI File Dialog)
- 🎯 **6 Unique ASCII Styles** to choose from
- 🌈 **Optional Colored Output** (Terminal ANSI colors)
- 📏 **Adjustable Width, Brightness & Contrast**
- 💾 **Save ASCII Output to Text File**
- 🧠 **Optimized Character Mapping** for smooth gradients
- 💡 **Cross-platform Support** (Linux, macOS, Windows)

## 📸 Preview

Example output (with different styles and widths):


@@@@@@@@@@%%#*+=-::..
██████████▉▊▋▌▍▎▏
@#S%?*+;:,.
██▓▒░
●◐◑◒◓◔◕○


## 🧰 Requirements

-   Python 3.6+
    
-   [Pillow](https://python-pillow.org/) (PIL fork)
    
-   Tkinter (comes with standard Python installation)
    

Install dependencies with:

`pip install Pillow` 

✅ Tkinter is pre-installed with most Python distributions. If not, install it via your package manager (e.g., `sudo apt install python3-tk` on Ubuntu).

## ⚙️ Usage

Run the tool directly from terminal:


`python3 ascii.py` 

You will be prompted to:

1.  **Choose a style** (e.g., Detailed, Minimal, Classic...)
    
2.  **Pick a color** (or none)
    
3.  **Adjust width** (20-200 characters wide)
    
4.  **Set brightness and contrast**
    
5.  **Save the final output** as a `.txt` file (optional)
    

## 🧠 How It Works

-   Converts the image to grayscale
    
-   Resizes it based on character aspect ratios
    
-   Maps each pixel to a corresponding ASCII character
    
-   Applies optional ANSI color codes for terminal rendering
    
-   Outputs to terminal and optionally to a `.txt` file
    


## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Contributing

Contributions are welcome! Feel free to fork this repo, submit issues, or make pull requests.

## 👤 Author

Created with 💻 and ☕ by [Elgun Ismayilov](https://github.com/elgunismayiloff)
