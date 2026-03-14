# Source: https://docs.edgeimpulse.com/projects/expert-network/silabs-xg24-card-sorting-and-robotics-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SiLabs xG24 Plus Arducam - Sorting Objects with Computer Vision and Robotics - Part 1

Created By: Thomas Vikstrom

Public Project Link: [https://studio.edgeimpulse.com/public/193509/latest](https://studio.edgeimpulse.com/public/193509/latest)

## Introduction - Playing Poker at the Edge, Part 1 of 2

As sometimes happens to all of us, we are presented with a solution but don't yet have a problem to solve! In this case the solution was that I got the chance to borrow a programmable robot arm for a few weeks, but as the robot was delivered much earlier than expected, I had not yet thought about a use case for it. Among other things I needed to decide about what objects to pick and place using the suction cup, and also what software to use for controlling the robot. What came to the objects to use, I decided after some quick deliberation to use playing cards as they are uniform in size and also lightweight. For the controlling software I had initially thought about only using Python (without any AI), but I quickly moved on to explore how to also use TinyML (Tiny Machine Learning) for a more rewarding experience.

This project is part one of two, showing how to classify poker cards into three categories, by using Edge Impulse and a supported board, SiLabs xG24. Part two continues with using the same hardware setup for controlling the aforementioned robot arm to sort cards, but also showcases how to easily adapt the setup to sorting waste.

While one might think that classifying playing cards into only three classes is a piece of cake - actually it is when using Edge Impulse - the project also serves as a base to get started using the hardware and with a low learning curve. After you've got used with it, you can easily step up the ladder to more advanced projects.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-01.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=41bd5f880d7e893d2d0460bb575adb1e" width="972" height="557" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-01.png" />
</Frame>

## Use-Case Explanation

As earlier mentioned I chose to classify playing cards for this project. While it is possible to classify cards into different suits, I decided to start simple by using three classes or labels: red cards, black cards, and cards with back side up. In addition I added a no card label to avoid the risk of an empty table being classified as a card. While classifying cards is pretty much straightforward, the typical rules also applied in this project: more images and also different type of images --> better performing model.

After initially having tested another board, I found that board to be a tad slow for my use case as the inferencing took over 1.2 seconds. Browsing through the boards Edge Impulse supports, I then decided to use the SiLabs xG24 Dev Kit together with an Arducam camera as I believed they would fit my purposes better. As it turned out, the inferencing was 3 times faster than with the other board I'd tried!

The SiLabs xG24 Dev Kit is packed with sensors and features. Among the sensors are e.g. a relative humidity and temperature sensor, inertial sensor, stereo microphones, pressure sensor etc. Important features for this project was the Cortex-M33 processor, 256 kB RAM, and especially the AI/ML Hardware accelerator, and it can even be operated with a coin-cell battery! While it is not equipped with a camera, it supports e.g. the Arducam OV2640 board which I also used.

## Components and Hardware Configuration

### Hardware Used:

* [SiLabs xG24-DK2601B EFR32xG24 Dev Kit](https://www.silabs.com/development-tools/wireless/efr32xg24-dev-kit?tab=overview)
* [Arducam B0067 2MP OV2640 SPI Camera for Arduino](https://www.welectron.com/Arducam-B0067-2MP-OV2640-SPI-Camera-for-Arduino_1)
* [Pin Header 2.54mm 1x20 Pin](https://www.welectron.com/Pin-Header-254mm-1x20-Pin) for soldering to the SiLabs board

### Configure the Hardware:

* Solder the header to the board
* Connect the Dupont cable (came with the Arducam) to the headers according to the [camera assembly](/tutorials/hardware/silabs-xg24-devkit-object-detection#camera-assembly)
  * Before powering on, double-check and triple-check the connection

**Important:** Avoid touching the board or camera when they are powered. I learned this the hard way and burned one board, probably through ESD (electrostatic discharge) when pressing the reset button. The blue magic smoke that was released was unhealthy both for me, and especially for my wallet...

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-05_2.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=79dbb35a61ac8f5a26f92f38da53cf32" width="640" height="687" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-05_2.png" />
</Frame>

## Data Collection Process

When collecting data for a machine learning (ML) application, it is generally better to use same device as will be used for inferencing. I started out with this assumption, but found it quite tedious to capture hundreds and hundreds of images with the xG24 and Arducam as it took up to 5 seconds per image. The reason for the slowness might be that the 256 kB RAM is not enough for storing one image, and instead the much slower flash memory needs to be used. Instead I moved onto using a mobile phone camera which made the data gathering process much faster, and almost fun, as I could take 3-4 images per second!

### Software and Hardware Used to Capture Data:

* [Edge Impulse Studio & CLI (Command-Line Interface)](https://www.edgeimpulse.com/)
* SiLabs xG24 was used for \~10 % of the data
  * to use this with Edge Impulse, you first need to flash the Edge Impulse firmware, detailed steps are found in the [documentation](/hardware/boards/silabs-xg24-devkit)
* mobile phone camera (iPhone 12) was used for \~90 % of the data

### Steps to Reproduce

* Collecting data with Edge Impulse is extremely easy with supported devices
  * You can either use the [CLI (Command-Line Interface)](/tools/clis/edge-impulse-cli), or like I did, use Studio by choosing `Connect a device` from the `Data acquisition` menu when using e.g. a mobile phone.
  * For details about how to use a mobile phone, please see the [documentation](/hardware/devices/mobile-phone).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-02.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=2c5b8d877e806ee122cdcb8c57515d50" width="1321" height="412" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-02.png" />
</Frame>

* When connecting directly to a development board, you instead choose `Connect using WebUSB`. Depending on the board, you can choose different sensors, or combination of sensors. In this case, I chose to use 96x96 as image size when capturing images with the xG24 board, this to avoid the need of resampling.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-03.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=f2f8c037b38d1505dcb38b51496ab36f" width="1600" height="501" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-03.png" />
</Frame>

* To improve the accuracy of the model, I varied the illumination between using daylight and artificial light, and also by taking images from various angles and distances. Some of the images are even a bit blurry, but this is probably also making the model more robust. To be able to reuse the same images in part two, I deliberately also placed several cards on top of each other, sometimes with part of the underlying cards being visible.
* As mentioned, the different classes (labels) I used are red cards, black cards, and cards with back side up. In addition, I also collected background and random images without having any card in them.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-01.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=e66d5198126ef166f33ee2d7410c2b9a" width="192" height="197" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-01.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-03.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=144cd63fed2efd9a6285538b1010e4a5" width="196" height="197" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-03.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-02.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=8e2f91a8757c2ea86c8703de3bf608ba" width="197" height="197" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/Card-02.png" />
</Frame>

Developing ML models is an agile and iterative process where it is often better to as quickly as possible test the model before spending too much time on it. Following this, I initially took only a few tens of images per class to test with, knowing that I'd most probably would need to gather more later. As is seen in the picture below, I ended up with a total of 1339 images with a 80% / 20% split between training and test data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-01.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=d7c1b36ee8184969cea318c1bae687b9" width="767" height="102" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-01.png" />
</Frame>

## Building, Training, and Testing the Model

After you've collected some data, you need to build and train the model. The main steps in this process are to create an impulse, extract features, and finally train the model. Again, with image classification and when using Edge Impulse, this is often pretty straightforward.

### Steps to reproduce

In this project I knew beforehand that the 256 kB RAM memory would put some constraints on what model configuration to use. With 512 kB RAM I'd been able to use MobileNetV2 and 96x96 image size, and with 1M or more RAM I'd even been able to use MobileNetV2 and 160x160 image size. On the other hand, even if more memory can be beneficial, larger image sizes typically leads to longer inferencing times on the same device.

* Creating an impulse
  * Based on general recommendations, I chose to start with an image size of 96x96 pixels. I also chose to use `Squash` as `Resize mode` to not lose any data because of cropping. It might not actually have mattered in the end in this case, but as I used two completely different cameras (Arducam & mobile phone), having different aspect ratios, I wanted to avoid images from one camera being cropped where images from the other camera perhaps were not cropped similarly.
  * Unless you have specific needs, it is best to use `Ìmage` as `Processing block` and `Transfer Learning (Images)` as `Learning block`. Transfer learning means that you'll use a pre-trained image classification model on your data with only some fine-tuning. This generally leads to good performance even with relatively small image datasets.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-06.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=7285f1d1a4c8787de99d9131fe3a4eca" width="1471" height="528" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-06.png" />
</Frame>

* Next step is to extract features
  * For images you can choose between color or grayscale images. Whenever possible you should aim to use grayscale images as they consume much less memory and also can be processed much faster than colour images. In this project however, I chose to use RGB (colour) images as red and black look quite similar in grayscale, and the ML model might struggle to differentiate between them.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-08.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=f5b27da28da0a25d4fc38ff2544f04fd" width="772" height="720" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-08.png" />
</Frame>

* Click on ´Generate features\`, after a while you'll see the feature explorer visualizing how similar or dissimilar the classes are.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-10.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=c6b2651ab3da22cbd15a84e96c46be80" width="727" height="558" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-10.png" />
</Frame>

* Next step is to train the model
  * While it generally is best to start with the default settings, I needed to switch to MobileNetV1 instead of MobileNetV2 due to the memory constraints. MobileNetV2 *can* be used with 256 kB RAM, but then you need to reduce from 96x96 to e.g. 64x64 pixels. I'd tried this, but the results were not good.
  * I discovered that changing the final layer to use 32 neurons, and the dropout rate to 0.01 worked well for this project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-12.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=e901f30ab154fdca9cc6374185016fa0" width="1600" height="915" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-12.png" />
</Frame>

* Click on `Start training` when you are ready to train the model
  * Depending on the number of images and training cycles, this step might take some time. Once it is ready you can see the performance in the graphs on the right.
  * Apart from when using "real" computers (e.g. Raspberry PI, Jetson Nano, etc.), you should only consider using quantized (int8) models as unoptimized (float32) models consumes much more memory and inferencing will be many times slower.
  * In the bottom right corner you'll see an estimation of the on-device performance. Use this to validate if the performance is acceptable for your use case, or if you need to rethink your model - or perhaps even change device - to accomplish your goals.
  * To speed up the search for an optimal ML model, you should take a look at the [EON Tuner](/studio/projects/eon-tuner) as well!

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-14.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=8ab24f335e98cb8bf16ed7f66408bdb4" width="712" height="135" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-14.png" />
</Frame>

## Testing the Model

Before deploying the model to the device itself, you should check how well it works on data it has not seen before. This is where the 20 % test data that was put aside comes into play. If the model performs poorly on test data, you can expect real performance to be even worse. But even a 100 % accuracy on test data does not guarantee success in real life, so don't open the champagne bottle yet :-).

If the training performance is very good, but the test performance is poor, the reason might be that your model is overfitting on the training data. In that case you might need to collect more data, change the model or reduce its complexity. Now would be a good time to try the EON Tuner mentioned earlier.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-16.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=88c7d1655228c0a8ee99ba3fc14990f3" width="1600" height="675" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-16.png" />
</Frame>

In my case, after having deployed and tested the first model with the xG24 device, I found out that the real model performance was much worse than when testing with Edge Impulse. To troubleshoot this, I tested with my mobile phone instead and saw that the model performed close to 100 %. My hypothesis was that the cameras were too different, but perhaps by adding a few images taken by the device itself would make the model stronger. As a matter of fact, this was also what happened.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-03.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=ecd44d59660a222f598bda1c0bee1841" width="640" height="658" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/xG24-03.png" />
</Frame>

## Model Deployment

When deploying the model to the xG24 device, you can choose between deploying a Simplicity Studio Component, or a firmware binary. Deploying as a Simplicity Studio Component means you'll have to use an external tool to compile a C++ program yourself, but on the other hand it provides you with many more options and features.

* In this project, I chose to deploy as a firmware binary.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-18.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=57932fc9452fd40d604225948aa8a93f" width="952" height="447" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-18.png" />
</Frame>

* To reduce the memory footprint, it is recommended to enable the EON Compiler.
* Once ready, click on `Build` to create the files to be deployed.
* After a few minutes the build process is complete, and instructions for flashing the firmware is shown. Follow the instructions to flash using the same Simplicity Commander you used earlier.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-19.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=156b8d46a5d6716e536a9baf70f73994" width="909" height="625" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-19.png" />
</Frame>

## Results

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/inferencing.gif?s=c5411d88b830c37de18c7db46c2dd73e" width="861" height="451" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/inferencing.gif" />
</Frame>

When you want to use the deployed model in a real scenario, you can again choose between different options, one of them being the command-line interface.

* When using the CLI for an image classification project, I recommend you use `edge-impulse-run-impulse --debug` as you can see a live picture and the inferencing result in a web browser. Note that this is the same picture as is used for inferencing, in this case 96x96 pixels which explains the pixelation and unsharpness.
* In addition you'll also see results as a running log

The results of this project were more or less as expected. A bit surprising was that it was possible to collect images with a phone camera and by adding a relatively small number of images taken with the end device, the resulting model turned out be quite robust. I have also tested the model with other card decks, and they work as well as the one used for collecting images.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-21.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=aa8a8e6f45be84833de39b8f8193fa5d" width="341" height="463" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-21.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-22_2.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=3da64758a188e8335cf8cf9c534499a7" width="574" height="268" data-path=".assets/images/silabs-xg24-card-sorting-and-robotics-1/EI-22_2.png" />
</Frame>

## Conclusion

The main deliverables of this project were twofold: getting started with and understanding the SiLabs xG24 Dev Kit together with the Arducam camera, as well as building and deploying an image classification ML model with Edge Impulse. You have also learned that building a ML model is not like a project, where you plan meticulously and then carefully follow the plan, but instead that it is an iterative process where you try out different things, fail sometimes, and hopefully succeed more often. In addition, what you've learned is a stepping stone to build more advanced models, e.g. by classifying different card suits, or even suit and value! In part two we will use what we've learned to control a robot arm to sort cards and also other objects.


Built with [Mintlify](https://mintlify.com).