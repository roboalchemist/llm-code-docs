# Source: https://docs.edgeimpulse.com/tutorials/topics/data/collect-image-data-openmv-h7-plus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect image data using OpenMV Cam H7 Plus

This page is part of [Image classification](/tutorials/hardware/sony-spresense-image-classification) and describes how you can use the OpenMV Cam H7 Plus to build a dataset, and import the data into Edge Impulse.

### 1. Setting up your environment

To set up your OpenMV camera, and collect some data:

1. Install the [OpenMV IDE](https://openmv.io/pages/download).
2. Follow the [OpenMV hardware setup guide](https://docs.openmv.io/openmvcam/tutorial/hardware_setup.html) to clean the sensor and focus the lens.
3. Connect a micro-USB cable to the camera, and open the OpenMV IDE. The camera should automatically update to the latest firmware.
4. Verify that the camera can capture live images, by clicking on the **Connect** button in the bottom left corner, then pressing **Play** to run the application.

<Frame caption="Set up your OpenMV camera. Press the 'Connect' button, then press 'Play' to run the application.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4740f0a-connect.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=46a8f0b4d7f14741680b3a6c2cf2382e" width="436" height="200" data-path=".assets/images/4740f0a-connect.png" />
</Frame>

A live feed from your camera will be displayed in the top right corner of the IDE.

### 2. Collecting images

Once your camera is up and running, it's time to start capturing some images and build our dataset.

First, set up a new dataset via **Tools -> Dataset Editor**, select **New Dataset**.

<Frame caption="Creating a new dataset in the OpenMV IDE">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/5fdf04b-01newdataset.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=641c34c1f65d23cf5f8250e4c494301d" width="1600" height="768" data-path=".assets/images/5fdf04b-01newdataset.png" />
</Frame>

This opens the 'Dataset editor' panel on the left side, and the 'dataset capture script' in the main panel of the IDE. Here, create three classes: "plant", "lamp" and "unknown". It's important to add an unknown class that contains random images which are neither lamps nor plants.

<Frame caption="Create three classes in the OpenMV IDE by clicking the 'New class folder' (highlighted in yellow).">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/315e800-screenshot_2020-07-16_at_134902.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=158bea75e306b13d1d5ca84b780a7f7f" width="1447" height="753" data-path=".assets/images/315e800-screenshot_2020-07-16_at_134902.png" />
</Frame>

As we'll build a model that takes in square images, change the 'Dataset capture script' to read:

```py  theme={"system"}
import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # Modify as you like.
sensor.set_framesize(sensor.QVGA) # Modify as you like.
sensor.set_windowing((240, 240)) # Modify as you like.
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
```

Now you can capture data for the three classes.

1. Click the **Play** icon to run the 'dataset capture script' on your OpenMV camera.
2. Select one of the classes by clicking on the folder name in the 'Dataset editor'.
3. Take a snap by clicking the **Capture data** (camera icon) button.

Do this until you have captured 30 images per class from a variety of angles. Also make sure to vary the things you capture for the unknown class.

<Frame caption="Capturing data (a plant image shown on the left) into a dataset using the OpenMV camera">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dd0a7ed-screenshot_2020-07-16_at_140105.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=5c680872b6071447a5d526885913a3e9" width="1447" height="753" data-path=".assets/images/dd0a7ed-screenshot_2020-07-16_at_140105.png" />
</Frame>

### 3. Sending the dataset to Edge Impulse

To import the dataset into Edge Impulse go to **Tools > Dataset Editor > Export > Upload to Edge Impulse project**.

<Frame caption="Synchronize your dataset with Edge Impulse straight from the OpenMV IDE">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/88a6079-upload.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=660df50482e73fe3af494293440b2c57" width="1258" height="762" data-path=".assets/images/88a6079-upload.png" />
</Frame>

Then, choose the project name, and the split between training and testing data (recommended to keep this to 80/20).

<Frame caption="Choose a project, and then the dataset split to upload your data">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6b4faf5-split.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=35d39e4578f8048a8adc02da5afdea6e" width="527" height="326" data-path=".assets/images/6b4faf5-split.png" />
</Frame>

A duplicate check runs when you upload new data, so you can upload your dataset multiple times (for example, when you've added new files) without adding the same data twice.

<Info>
  **Training and testing data split**

  The split between training and testing data is based on the hash of the file in order to have a deterministic process. As a consequence you may not have a perfect 80/20 split between training and testing, but this process ensures samples are always placed in the same category.
</Info>

Our dataset now appears under the **Data acquisition** section of our project.

<Frame caption="Collected data">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/548bb69-screenshot_2020-07-16_at_141213.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=b18c2f404b6c0e18931f86820bd083ac" width="1441" height="1000" data-path=".assets/images/548bb69-screenshot_2020-07-16_at_141213.png" />
</Frame>

You can now go back to the [Image classification](/tutorials/hardware/sony-spresense-image-classification) tutorial to build your machine learning model.


Built with [Mintlify](https://mintlify.com).