# Source: https://learn.sparkfun.com/tutorials/working-with-qwiic-on-a-jetson-nano-through-jupyter-notebooks

## Introduction

Let's face it\... SSH or VNC can be frustrating and a barrier to entry at times for people looking to get started with remote computing. Luckily, services like [Project Jupyter](https://jupyter.org/) help make remote computing a little more accessible. Jupyter Notebooks have been around for a while and a number of people use them for a variety of applications; from data visualization to teaching and learning computer science.

![](https://raw.githubusercontent.com/jupyter/design/master/logos/Rectangle%20Logo/rectanglelogo-greytext-orangebody-greymoons/rectanglelogo-greytext-orangebody-greymoons.png)

In a nutshell you can think of Jupyter Notebooks as an IDE and documentation repository in one platform that is accessible remotely through a web browser. Jupyter then grants access to the file directories of the host computer, a terminal to run Linux commands to install software on it as well as run required commands and processes. The "Notebooks" are files where you can create interactive Python scripts through intermixing markdown documentation with code so that your Notebook is both a "Notebook" and the program you end up running. Common applications for Jupyter Notebooks include building data visualization displays or GUI interfaces.

Jupyter Notebooks are accessed through a web browser interface. From a client computer on the same network you can access the Notebooks and edit, run and/or modify the Python scripts that are hosted as well as create new ones. This makes working with a single board computer much easier and cleaner in terms of required hardware peripherals, but it also lowers the barrier of entry in terms of those who are new to the topic and feel overwhelmed.

## Jupyter Notebooks for SparkFun Qwiic on the Jetson Nano

A great example of using Jupyter Notebooks as both a development and a learning platform is the NVIDIA Jetson Nano.

We carry two kits: the [DLI Course Kit](https://www.sparkfun.com/products/16308) and [JetBot AI Kit](https://www.sparkfun.com/products/16390) that can use Jupyter Notebooks as a way to deliver tutorial content to get users up and running easily as well as empower them to go further with those products. Jupyter Notebooks are especially helpful with topics and projects that can be mentally taxing and hard to understand such as Machine Learning and Computer Vision.

[![SparkFun DLI Kit for Jetson Nano](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/0/1/1/16308-SparkFun_DLI_Kit_for_Jetson_Nano_V3-01.jpg)](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano.html)

### [SparkFun DLI Kit for Jetson Nano](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano.html) 

[ KIT-16308 ]

With the release of the Jetson Nano™ Developer Kit, NVIDIA® empowers developers, researchers, students, and hobbyists to e...

**Retired**

[![SparkFun JetBot AI Kit v2.1 Powered by Jetson Nano](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/1/5/8/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-jetbot-ai-kit-v2-1-powered-by-jetson-nano.html)

### [SparkFun JetBot AI Kit v2.1 Powered by Jetson Nano](https://www.sparkfun.com/sparkfun-jetbot-ai-kit-v2-1-powered-by-jetson-nano.html) 

[ KIT-16417 ]

Utilize this kit to turn your Jetson Nano into a mobile machine with things like object following, collision avoidance via th...

**Retired**

This tutorial covers a set of Jupyter Notebooks that we created for our Python supported Qwiic boards and their use with the NVIDIA Jetson Nano!

With Python support for the ever growing catalog of [SparkFun Qwiic boards](https://www.sparkfun.com/qwiic) we thought that a Jupyter Notebook collection built around using our Qwiic boards with the NVIDIA Jetson Nano would be a good idea. We have created eight different notebooks that give you a "Hello World" example for each of the currently supported boards. Each Notebook breaks down the Python script into manageable chunks giving explanation and context to what is happening and in the end we get you enough knowledge to be dangerous!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/20200421_114158.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/20200421_114158.jpg)

When you feel comfortable and want to dig into creating your own Python scripts for a project, you can create your own Notebook and execute the code right from Jupyter Notebooks. You can even try your hand at integrating some of the sensors into a Machine Learning project as all of the Qwiic libraries will be installed on your Jetson Nano!

This tutorial will get you up and running on an NVIDIA Jetson Nano and Jupyter Notebooks using SparkFun Qwiic Boards!

## Hardware Overview and Assembly

We will obviously need an NVIDIA Jetson Nano (we recommend starting with the DLI Course Kit) as well as some Qwiic hardware. We recommend starting with the SparkFun Qwiic Kit for Raspberry Pi but we have Python packages for many Qwiic boards. The most up to date list of Python-supported Qwiic boards can be found in the [Qwiic Py GitHub Repository](https://github.com/sparkfun/Qwiic_Py).

\

![qwiic kit](https://cdn.sparkfun.com//assets/parts/1/3/9/1/2/15367-SparkFun_Qwiic_Kit_for_Raspberry_Pi-01.jpg)

\

**Note:** At the time of writing we used the Qwiic pHAT v1.0. The Qwiic pHAT v2.0 is functionally the same with additional features and can be used with this guide.

Hooking up your Qwiic kit to the NVIDIA Jetson Nano is straight forward. The kit comes with our Qwiic pHAT which plugs in to the Jetson Nano via the 2x20 GPIO header.

\

[![Qwiic pHAT connected to the Jetson Nano](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/20200421_112535.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/20200421_112535.jpg)

\

The orientation of the pHAT is very important here. It should hang off the Jetson Nano Developer Kit carrier board and not over the top of the heat sync. Think "spoiler" for your Jetson Nano and you will get it!

Once the pHAT is in place we can now add the distance sensor and environmental combo board as well as the micro OLED display using the Qwiic cables included in the kit.

\

[![Qwiic breakouts connected to the pHAT on the Nano](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/20200421_111356.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/20200421_111356.jpg)

\

You can configure your hookup of the Qwiic boards in any combination you like as long as you have both boards connected to the pHAT. Personally, I like to daisy chain them together but you can go with the flavor that suits you and your needs.

## Software Setup and Installation

Once you have everything connected to the pHAT, it is now time to get the Python libraries and Jupyter Notebooks installed.

This tutorial assumes you have already gone through the process of burning an OS image to a microSD card, ran initial setup and have your Nano connected to the internet either through Ethernet or WiFi. If you are just opening the box at this point take a moment to set your board up by going through the following tutorials:

- [Jetson Nano Initial Setup](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) - General setup guide from NVIDIA!
- [Installing the Edimax WiFi adapter](https://learn.sparkfun.com/tutorials/adding-wifi-to-the-nvidia-jetson) - adding WiFi connectivity using a USB adapter.

**Note:** We will be working from a DLI Course image with network connection already setup. If you are looking for a shortcut, using our JetBot Image with your Jetson Nano will get you the drivers for the Edimax USB adapter and Qwiic Python libraries installed for you!

[Download the SparkFun JetBot Image](https://static.sparkfun.com/large/sparkfun_jetbot_v01-00.zip)

### Navigating to Jupyter Notebooks

To access Jupyter Notebooks on your Jetson Nano you will need to know its IP address. There are a number of ways to find it. The most straightforward way is to hook the Jetson Nano up to a monitor and keyboard, open a terminal and type the following:

`ifconfig`[\[Enter\]]

This command will list off all of your network connections and the IP address for that connection. If you have followed the instructions for the WiFi setup tutorial linked above we will assume you know your IP address and have your Jetson Nano connected to your network.

Open a browser window and type the following in the address bar: http://\[IP ADDRESS\]:8888 with `[IP ADDRESS]` being your Jetson Nanos IP Address.

The first time you connect it may take a bit of time for Jupyter Notebooks to load, but you should be greeted by a loading page and then a sign-in page asking for a password. The password for the DLI image is `dlinano` and the password for the Jetbot image is `jetbot`.

\

[![Screenshot showing Jupyter Notebook Launcher](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/jupyterNB.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/jupyterNB.PNG)

\

Once you are logged into Jupyter Notebooks you will need to open a new terminal window to download the Jupyter Notebooks for the Qwiic Boards as well as install the Qwiic Python libraries.

\

[![Terminal opened and command to download Qwiic Jupyter entered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/cl_snip.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/cl_snip.PNG)

*Having trouble seeing details in the image? Click on it for a larger view!*

\

Once you open the terminal window from the Launcher window, navigate to the DLI-Nano Notebooks directory by typing the following command:

`cd nvdli-nano`[\[Enter\]]

You can then download the SparkFun Qwiic Jupyter Notebooks from [GitHub](https://github.com/d1runberg/qwiic-jupyter-nb) with the following command:

`sudo git clone https://github.com/d1runberg/qwiic-jupyter-nb.git` [\[Enter\]]

This command will download a folder with the contents of our Jupyter Notebooks as well as the assets required to display images, etc. You should now be able to see the SparkFun Qwiic Notebooks directory in the directory tree on the left side of Jupyter Notebooks!

Once the SparkFun Qwiic Notebooks downloads you need to install the Qwiic Python libraries before digging in and using them.

### Installing Qwiic Libraries

With the terminal window in Jupyter Notebooks still opened you can install the SparkFun Qwiic Python libraries through pip by typing the following command:

`sudo pip3 install sparkfun-qwiic`[\[Enter\]]

This will install the entire Qwiic Py package with libraries for the Qwiic boards that are supported in Python.

\

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/python_install.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/python_install.PNG)

\

Once the installation is complete, you should be good to go and can close the terminal window.

## Running an Example in Jupyter Notebooks

With our Qwiic boards connected to the Jetson Nano we have two different options of Notebooks to choose from! For the sake of simplicity I chose the OLED notebook to walk you through, but once you run the first Notebook the other will be simple enough to run as well. Open the SparkFun Qwiic Notebooks directory by double clicking on it. Find the OLED.ipynb notebook file and open it by double clicking it as well.

\

[![Screenshot of SparkFun Qwiic OLED Notebook](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/oled_capture.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/oled_capture.PNG)

\

Notebooks work in Jupyter Notebooks by running your code in a kernel which you need to start and stop. It is a good habit to make sure that you are not running other Notebook kernels before starting one. To check if any kernels are running select the small running man icon on the far left toolbar. Any kernels that are running will be listed here and you can click "SHUTDOWN" to close any that are open.

\

[![Screenshot showing SHUTDOWN for Jupyter Notebooks](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/kernel.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/kernel.PNG)

\

To run the OLED Notebook we need to specify what type of kernel we want to run it as. In the upper right hand corner there is a small text box next to a circle. It should say "Python 3", but if it says "No Kernel" click on it and select Python 3 from the options provided. We can now run the python code in the Notebook!

\

[![Screenshot showing selecting the Kernel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/kernel_select.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/kernel_select.PNG)

\

Next, interact with the Notebook by clicking on the first cell which is the product description for the OLED and then click the \"Play\" button in the top menu bar. This play button steps you through each cell (either text or code) and moves you to the next one.

\

[![Screenshot showing the Play button](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/play.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/play.PNG)

\

You may notice that each cell has a box next to it. For code cells there will be an '\*' in that box while the code is executing and when it completes its execution the asterisk will turn to a number. So, you can follow through the Notebook by clicking the Play button as code executes combined with reading the explanation through the tutorial text.

In the end your OLED should display some text on it.

\

[![The OLED displaying text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/8/20200421_120449.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/8/20200421_120449.jpg)

\

The code cells in the Notebook are interactive and you can make changes. So changing the string that the display changes is as simple as double clicking on that code cell and changing the string to your name for example. You then need to reselect the code cell and re-run it.