# Source: https://docs.edgeimpulse.com/projects/expert-network/sony-spresense-smart-hvac-system.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart HVAC System with a Sony Spresense

Created By: Jallson Suryo

Public Project Link: [https://studio.edgeimpulse.com/public/215243/latest](https://studio.edgeimpulse.com/public/215243/latest)

GitHub Repo: [https://github.com/Jallson/Smart\_HVAC](https://github.com/Jallson/Smart_HVAC)

## Introduction

A common problem found in HVAC systems is that energy is wasted, because the system uses more energy than necessary, or the system cannot quickly adjust to the changing needs in a dynamic environment. To tackle the problem, we need a system that manages its power intensity based on what is necessary for each zone in real-time for a given environment. The power intensity necessary for each zone can be derived from the following data: number of people, time or duration spent inside, and/or the person's activity.

## Our Solution

To overcome this challenge, a Smart HVAC System that can optimize energy consumption by adjusting the power intensity in different zones inside an office or a residential space (zones with more people, more activity, and longer time durations will need more cooling/heating and vice versa) could be created. The zone heat mapping will be generated using data obtained from a Sony Spresense microcontroller (with Edge Impulse's FOMO Machine Learning model embedded) that's mounted like a surveillance camera inside the space.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image17.jpg?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=bea0e513664084a8a8719dd7acab22bb" width="762" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image17.jpg" />
</Frame>

## Description

The project uses Edge Impulse's FOMO to detect multiple objects and its coordinates using a compact microcontroller with an on-board camera (the Sony Spresense). The object detection ML model will use the top view of miniature figures with standing and sitting positions as objects. The data captured will be divided into Training and Test data. Then the Impulse with Image and Object Detection as learning blocks and grayscale color blocks will be created.

The accuracy result for this training and test model is above 90%, so there is a higher degree of confidence when counting the number of objects (persons) and tracking their centroid coordinates.

The ML model is then deployed to the Spresense. The number of objects in each zone is displayed on an OLED display. The Spresense also communicates to an Arduino Nano via I2C which we are using for the fan speed controller.

This system will increase fan intensity on areas/zone that need more cooling/heating, which means more activity/people in a certain zone will increase fan intensity in that zone. The total HVAC power output can also be adjusted based on the total number of people in the space.

The project is a proof of concept (PoC) using a 1:50 scale model with an office interior with several partitions and furniture and miniature figures. The space is divided into 4 zones, and each zone has a small fan installed. The OLED display is used in this PoC to show the output of this simulation.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image20.jpg?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=c67e9f6a01852e4c876cbce71230e968" width="1000" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image20.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image18.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=5977bbcfec56036c4577948d5df95e95" width="661" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image18.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image21.jpg?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=69490c9528e2f5abd2e200509dbf2b7a" width="997" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image21.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image04.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=b4650a6e995795cd13aaad8712896d88" width="1334" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image04.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image05.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=41ba373d31d68fc655215634ce5c5e21" width="1184" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image05.jpg" />
</Frame>

Sony Spresense, aluminium extrusion frame, and 3D printed miniature model (1:50)

System Diagram, prototyping in breadboard, and Smart HVAC System with custom design PCB

### Hardware Components:

* Sony Spresense
* Arduino Nano
* 2x TB6612 Motor drivers
* 4x DC 5V mini fan 3cm
* 0.96inch OLED display
* Aluminium extrusion as a camera stand
* 3D printed (case, office interior 1:50 miniature)
* Powerbank & battery for Sony Spresense

### Software & Online Services:

* Edge Impulse Studio
* Arduino IDE

## Steps

### 1. Prepare Data / Photos

In this project we will use a smartphone camera to capture the images for data collection for ease of use. Take pictures from above in different positions with backgrounds of varying angles and lighting conditions to ensure that the model can work under slightly different conditions (to prevent overfitting). Lighting and object size are crucial aspects to ensure the performance of this model.

> Note: Keep the size of the objects similar in size in the pictures. Significant difference in object size will confuse the FOMO algorithm.

### 2. Data Acquisition and Labelling

Open [studio.edgeimpulse.com](http://studio.edgeimpulse.com), login (or create an account first), then create a new Project.

Choose the **Images** project option, then **Classify Multiple Objects**. In Dashboard > Project Info, choose Bounding Boxes for labelling method and Sony Spresense for target device. Then in Data acquisition, click on Upload Data tab, choose your photo files, auto split, then click Begin upload.

Click on Labelling queue tab then start drag a box around an object and label it (person) and Save. Repeat until all images are labelled.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image06.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=c296b90c96b9d1492d4b9c781463fc02" width="1043" height="945" data-path=".assets/images/sony-spresense-smart-hvac-system/image06.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image07.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=45cd42780ce7c52c0a1af684ba257bc7" width="748" height="657" data-path=".assets/images/sony-spresense-smart-hvac-system/image07.png" />
</Frame>

Make sure that the ratio between Training and Test data is ideal, around 80/20.

### 3. Training and Building Model using FOMO Object Detection

Once you have the dataset ready, go to Create Impulse and set 96 x 96 as the image width - height (this helps in keeping the ML model small). Then choose Fit shortest axis, and choose **Image** and **Object Detection** as learning and processing blocks.

Go to Image parameter section, select color depth as Grayscale, then press Save parameters. Then click on Generate and navigate to Object Detection section, and leave training settings for the Neural Network as it is — in our case the defaults work quite well, then we choose **FOMO (MobileNet V2 0.35)**. Train the model by pressing the Start training button. You can see the progress on the right side.

If everything is OK, then we can test the model. Go to Model Testing on the left, then click Classify all. Our result is above 90%, then we can move on to the next step -- deployment.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image08.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=6146ffb5367fe842ca55d8251fe324df" width="1600" height="406" data-path=".assets/images/sony-spresense-smart-hvac-system/image08.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image09.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=62adf30aaf06ff4e90e9572a7cf5b014" width="1600" height="777" data-path=".assets/images/sony-spresense-smart-hvac-system/image09.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image24.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=855ba3063bb6f2001d4511a84333e339" width="1467" height="929" data-path=".assets/images/sony-spresense-smart-hvac-system/image24.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image11.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=77115b2a84ad80adbccf2c22492fc6bc" width="1600" height="840" data-path=".assets/images/sony-spresense-smart-hvac-system/image11.png" />
</Frame>

### 4. Deploy and Build an Arduino Program

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/sony-spresense-smart-hvac-system/image15.png?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=59956856a37a6e9d6bca6f3b39ebd1ae" width="1588" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image15.png" />
</Frame>

You should have the Arduino IDE installed on your computer for the following step. On the navigation menu, choose **Deployment** on the left, search for and select Arduino Library in the Selected Deployment box, and then click **Build**. Once the Edge Impulse Arduino Library is built, downloaded and unzipped, you should download the *spresense\_camera\_smartHVAC\_oled.ino* code which [can be found here](https://github.com/Jallson/Smart_HVAC/blob/main/spresense_camera_smartHVAC_oled.ino) and place it inside the unzipped folder from Edge Impulse. Once the *.ino* code is inside Edge Impulse unzipped folder, move it to your Arduino folder on your computer. Now you can upload the *.ino* code to your Spresense board via the Arduino IDE.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image19.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=0aa7e50b97b577adb5ddd590d969e62a" width="1600" height="973" data-path=".assets/images/sony-spresense-smart-hvac-system/image19.png" />
</Frame>

The *.ino code* is a modified version of the Edge Impulse example code for object detection on Spresense. The modification adds capability to display person count on each room to the OLED screen and act as the controller to the Arduino Nano I2C peripheral. The code distinguishes the four rooms using four quadrants and by knowing the X, Y coordinates of the object’s centroid we can locate the person. The Arduino Nano adjusts the fan motor using PWM based on the number of persons present in the room.

The code for the Arduino Nano peripheral *Nano\_SmartHVAC\_I2C\_Peripheral.ino* can be [downloaded here](https://github.com/Jallson/Smart_HVAC/blob/main/Nano_SmartHVAC_I2C_Peripheral.ino).

Here is a quick prototype video showing the project:

<iframe src="https://www.youtube.com/embed/LLYOtY7svDQ" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

Finally, we have successfully implemented this object detection model on an Sony Spresense, and use the data captured from the camera to automatically control the HVAC system's fan power intensity and display the occupancy number and power meter for each zone. I believe this Proof of Concept project can be implemented in a real-world HVAC system, so that the goal of optimizing room temperature and saving energy can be achieved for a better, more sustainable future.

## Resources

Additional 3D-printed case design for Sony Spresense and the office configuration for this project can be found in the GitHub repo at [https://github.com/Jallson/Smart\_HVAC/tree/main/3d\_files](https://github.com/Jallson/Smart_HVAC/tree/main/3d_files):

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image22.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=b72150fa8fb52c8d6b885604a2ab5c64" width="1042" height="837" data-path=".assets/images/sony-spresense-smart-hvac-system/image22.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony-spresense-smart-hvac-system/image23.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=4473c26c9727ca3e2e9927fd76e2ebb1" width="820" height="1000" data-path=".assets/images/sony-spresense-smart-hvac-system/image23.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).