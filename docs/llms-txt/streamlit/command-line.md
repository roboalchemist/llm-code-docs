# Source: https://docs.streamlit.io/get-started/installation/command-line

# Install Streamlit using command line

This page will walk you through creating an environment with `venv` and installing Streamlit with `pip`. These are our recommended tools, but if you are familiar with others you can use your favorite ones too. At the end, you'll build a simple "Hello world" app and run it. If you prefer to have a graphical interface to manage your Python environments, check out how to [Install Streamlit using Anaconda Distribution](/get-started/installation/anaconda-distribution).

## Prerequisites

As with any programming tool, in order to install Streamlit you first need to make sure your computer is properly set up. More specifically, you’ll need:

1. **Python**

   We support [version 3.9 to 3.13](https://www.python.org/downloads/).

2. **A Python environment manager** (recommended)

   Environment managers create virtual environments to isolate Python package installations between projects.

   We recommend using virtual environments because installing or upgrading a Python package may cause unintentional effects on another package. For a detailed introduction to Python environments, check out [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

   For this guide, we'll be using `venv`, which comes with Python.

3. **A Python package manager**

   Package managers handle installing each of your Python packages, including Streamlit.

   For this guide, we'll be using `pip`, which comes with Python.

4. **Only on MacOS: Xcode command line tools**

   Download Xcode command line tools using [these instructions](https://mac.install.guide/commandlinetools/4.html) in order to let the package manager install some of Streamlit's dependencies.

5. **A code editor**

   Our favorite editor is [VS Code](https://code.visualstudio.com/download), which is also what we use in all our tutorials.

## Create an environment using `venv`

1. Open a terminal and navigate to your project folder.

2. In your terminal, type:

   ```bash
   # Windows command prompt
   .venv\Scripts\activate.bat

   # Windows PowerShell
   .venv\Scripts\Activate.ps1

   # macOS and Linux
   source .venv/bin/activate
   ```

3. Once activated, you will see your environment's name in parentheses at the beginning of your terminal prompt. `.venv`

4. Run your Streamlit app.

   ```bash
   streamlit run app.py
   ```

   If this doesn't work, use the long-form command:

   ```bash
   python -m streamlit run app.py
   ```

5. To stop the Streamlit server, press `Ctrl+C` in the terminal.

6. When you're done using this environment, return to your normal shell by typing:

   ```bash
   deactivate
   ```

## What's next?

Read about our [Basic concepts](/get-started/fundamentals/main-concepts) to understand Streamlit's dataflow model.

[Previous: Use Streamlit Playground](/get-started/installation/streamlit-playground) [Next: Install via Anaconda Distribution](/get-started/installation/anaconda-distribution)