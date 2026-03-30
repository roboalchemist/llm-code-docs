# Source: https://gpiozero.readthedocs.io/en/stable/installing.html

Title: 1. Installing GPIO Zero — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/installing.html

Markdown Content:
GPIO Zero is installed by default in the [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/) desktop image, [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/) Lite image, and the [Raspberry Pi Desktop](https://www.raspberrypi.org/software/raspberry-pi-desktop/) image for PC/Mac, all available from [raspberrypi.org](https://www.raspberrypi.org/software/). Follow these guides to installing on other operating systems, including for PCs using the [remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html) feature.

1.1. Raspberry Pi[](https://gpiozero.readthedocs.io/en/stable/installing.html#raspberry-pi "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

GPIO Zero is packaged in the apt repositories of Raspberry Pi OS, [Debian](https://packages.debian.org/buster/python3-gpiozero) and [Ubuntu](https://packages.ubuntu.com/hirsute/python3-gpiozero). It is also available on [PyPI](https://pypi.org/project/gpiozero/).

### 1.1.1. apt[](https://gpiozero.readthedocs.io/en/stable/installing.html#apt "Link to this heading")

First, update your repositories list:

pi@raspberrypi:~$ sudo apt update

Then install the package for Python 3:

pi@raspberrypi:~$ sudo apt install python3-gpiozero

or Python 2:

pi@raspberrypi:~$ sudo apt install python-gpiozero

### 1.1.2. pip[](https://gpiozero.readthedocs.io/en/stable/installing.html#pip "Link to this heading")

If you’re using another operating system on your Raspberry Pi, you may need to use pip to install GPIO Zero instead. Install pip using [get-pip](https://pip.pypa.io/en/stable/installing/) and then type:

pi@raspberrypi:~$ sudo pip3 install gpiozero

or for Python 2:

pi@raspberrypi:~$ sudo pip install gpiozero

To install GPIO Zero in a virtual environment, see the [Development](https://gpiozero.readthedocs.io/en/stable/development.html) page.

1.2. PC/Mac[](https://gpiozero.readthedocs.io/en/stable/installing.html#pc-mac "Link to this heading")
-------------------------------------------------------------------------------------------------------

In order to use GPIO Zero’s remote GPIO feature from a PC or Mac, you’ll need to install GPIO Zero on that computer using pip. See the [Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html) page for more information.

1.3. Documentation[](https://gpiozero.readthedocs.io/en/stable/installing.html#documentation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

This documentation is also available for offline installation like so:

pi@raspberrypi:~$ sudo apt install python-gpiozero-doc

This will install the HTML version of the documentation under the `/usr/share/doc/python-gpiozero-doc/html` path. To view the offline documentation you have several options:

You can open the documentation directly by visiting [file:///usr/share/doc/python-gpiozero-doc/html/index.html](file:///usr/share/doc/python-gpiozero-doc/html/index.html) in your browser. However, be aware that using `file://` URLs sometimes breaks certain elements. To avoid this, you can view the docs from an `http://` style URL by starting a trivial HTTP server with Python, like so:

$ python3 -m http.server -d /usr/share/doc/python-gpiozero-doc/html

Then visit [http://localhost:8000/](http://localhost:8000/) in your browser.

Alternatively, the package also integrates into Debian’s [doc-base](https://wiki.debian.org/doc-base) system, so you can install one of the doc-base clients (dochelp, dwww, dhelp, doc-central, etc.) and use its interface to locate this document.

If you want to view the documentation offline on a different device, such as an eReader, there are Epub and PDF versions of the documentation available for download from the [ReadTheDocs site](https://gpiozero.readthedocs.io/). Simply click on the “Read the Docs” box at the bottom-left corner of the page (under the table of contents) and select “PDF” or “Epub” from the “Downloads” section.
