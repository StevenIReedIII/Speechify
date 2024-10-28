# Speechify
NeoVim Plugin for Policy Debate
5. README.md

## Speechify

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

##Installation Instructions
Prerequisites

    Ensure you have the following installed:
        Python 3
        Node.js
        Pip
        Neovim
        LazyVim

###Step 1: Clone the Repository

    git clone https://github.com/yourusername/speechify.git
    cd speechify

###Step 2: Install Python Dependencies

Create a virtual environment (optional but recommended):

    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:

    pip install cefpython3 flask

###Step 3: Install Lua Dependencies

Ensure that you have luarocks installed and then install any necessary Lua packages. You may need to add nvim-lua/plenary.nvim for better Lua utilities in your Neovim configuration.

    luarocks install plenary

###Step 4: Configure Neovim

Add the following to your Neovim configuration file (usually located at ~/.config/nvim/init.lua):

lua

    require('plugins')  -- Ensure your plugins are loaded, if using lazy loading

###Step 5: Usage

    Open Neovim and load your speech content into a buffer.
    Type :Speechify in command mode to start the timer application and display the speech in the webview.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    CEF Python for embedding webviews in Python applications.
    Neovim community for their excellent plugin architecture.
    Policy debate community for their insights on timer needs.
