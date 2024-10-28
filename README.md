# Speechify
NeoVim Plugin for Policy Debate
5. README.md

markdown

# Speechify

A timer application designed for policy debate rounds that integrates with Neovim. It tracks time for speeches and cross-examinations while displaying a speech in a webview. The app can be invoked using a Neovim command, and it will update the displayed content based on the current buffer's HTML.

## Features

- Timer for different segments of a policy debate: 8 min constructives, 3 min CX, 5 min rebuttals.
- Webview displaying speech content.
- Pagination for easy navigation through the speech text.
- Integration with Neovim through a Lua plugin.
- Update functionality via HTTP requests to reflect changes in the current buffer.

## File Structure
speechify/
├── lua/
│   └── plugins/
│       └── speechify.lua          # Neovim plugin Lua file
├── css/
│   └── universal.css              # CSS file for formatting the speech document
├── python/
│   └── timer_app.py               # Python script for the timer GUI and webview
├── install.sh                     # Installation script for dependencies
└── README.md                      # Documentation file with instructions for setup and use

Installation Instructions
Prerequisites

    Ensure you have the following installed:
        Python 3
        Node.js
        Pip
        Neovim
        LazyVim

Step 1: Clone the Repository

bash

git clone https://github.com/yourusername/speechify.git
cd speechify

Step 2: Install Python Dependencies

Create a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:

bash

pip install cefpython3 flask

Step 3: Install Lua Dependencies

Ensure that you have luarocks installed and then install any necessary Lua packages. You may need to add nvim-lua/plenary.nvim for better Lua utilities in your Neovim configuration.

bash

luarocks install plenary

Step 4: Run the Installation Script

To ensure everything is set up correctly, run the installation script:

bash

bash install.sh

Step 5: Configure Neovim

Add the following to your Neovim configuration file (usually located at ~/.config/nvim/init.lua):

lua

require('plugins')  -- Ensure your plugins are loaded, if using lazy loading

Step 6: Usage

    Open Neovim and load your speech content into a buffer.
    Type :Speechify in command mode to start the timer application and display the speech in the webview.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    CEF Python for embedding webviews in Python applications.
    Neovim community for their excellent plugin architecture.
    Policy debate community for their insights on timer needs.

sql


### Summary

This complete set of files and their contents will help you set up the Speechify project for your policy debate needs. Each file serves a specific purpose, from the Lua plugin for Neovim to the Python script for the timer and webview, alongside the necessary CSS for formatting. If you have any questions or need further assistance, feel free to ask!

You said:
Should this work first try?
ChatGPT said:
ChatGPT

While the provided code and setup instructions are intended to work together, there are a few considerations and potential pitfalls that could affect the first run. Here's what to keep in mind to improve your chances of success:
1. Environment Setup

    Ensure that all dependencies (Python packages, Lua packages, etc.) are installed correctly. Pay attention to any error messages during the installation process.
    Make sure you have python3, pip, and luarocks installed on your system.
    Verify that cefpython3 is installed successfully, as it sometimes has specific system requirements.

2. File Paths

    Check that the path to timer_app.py in your speechify.lua file is correct. Update /path/to/timer_app.py to the actual path where your Python file is located.
    Make sure the temporary HTML file path (/tmp/current_buffer.html) is writable by your user.

3. Neovim Configuration

    Ensure that your Neovim configuration file correctly loads the plugin and that your Neovim version supports Lua configuration. You might need to add or adjust your configuration based on your Neovim setup.
    If you're using LazyVim or another package manager, ensure it's set up properly to load your Lua plugin.

4. Testing the Command

    After everything is set up, open a file in Neovim, type some HTML content into the buffer, and run the :Speechify command.
    If it fails, check for any error messages in the Neovim command line or terminal where you're running it.

5. Debugging

    If there are issues with the webview or timer, consider adding print statements in the Python code for debugging or checking the terminal output for errors.
    Ensure that the Python HTTP server is running and able to accept requests. Check the server logs for any errors when trying to update the HTML content.

6. Dependencies and Compatibility

    Ensure that your system's architecture is compatible with the dependencies, especially for cefpython3, which may have specific requirements for certain operating systems.
