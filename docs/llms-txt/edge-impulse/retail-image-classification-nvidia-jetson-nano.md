# Source: https://docs.edgeimpulse.com/projects/expert-network/retail-image-classification-nvidia-jetson-nano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retail Image Classification - Nvidia Jetson Nano

Created By: [Adam Milton-Barker](https://www.adammiltonbarker.com/)

Public Project Link: [https://studio.edgeimpulse.com/public/176144/latest](https://studio.edgeimpulse.com/public/176144/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/intro.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=ab7fa5e51509a1cc3cd2a8d4e787d0d3" width="1500" height="1000" data-path=".assets/images/retail-image-classification-jetson-nano/intro.jpg" />
</Frame>

## Introduction

Even with the current limitations of Artificial Intelligence, it is still a very useful tool, and many tasks can be automated with the technology. As more tasks become automated, human resources are freed up, allowing them to spend more time focusing on what really matters to businesses: their customers.

The retail industry is a prime example of an industry that can be automated through the use of Artificial Intelligence, the Internet of Things, and Robotics.

## Solution

Computer Vision is a very popular field of Artificial Intelligence, with many possible applications. This project is a proof of concept that shows how Computer Vision can be used to create an automated checkout process using the NVIDIA Jetson Nano and the Edge Impulse platform.

## Hardware

* NVIDIA Jetson Nano [Buy](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
* USB webcam

## Platform

* Edge Impulse [Visit](https://www.edgeimpulse.com)

## Project Setup

Head over to [Edge Impulse](https://www.edgeimpulse.com) and create your account or login. Once logged in you will be taken to the project selection/creation page.

### Create New Project

Your first step is to create a new project.

<Frame caption="Create Edge Impulse project">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/retail-image-classification-jetson-nano/1-create-project.jpg?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=8ca3c83cf862d307f6c6be6c28786c7c" width="1600" height="743" data-path=".assets/images/retail-image-classification-jetson-nano/1-create-project.jpg" />
</Frame>

Enter a **project name**, select **Developer** or **Enterprise**, and click **Create new project**.

<Frame caption="Choose project type">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/2-choose-project-type.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=9995aa79e595228e2c7ffd81e0394ed4" width="1600" height="740" data-path=".assets/images/retail-image-classification-jetson-nano/2-choose-project-type.jpg" />
</Frame>

We are going to be creating a computer vision project, so now we need to select **Images** as the project type.

### Connect Your Device

<Frame caption="Connect device">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/3-connect-device.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=22028d969b580377610c0f1fb9e93e45" width="1600" height="750" data-path=".assets/images/retail-image-classification-jetson-nano/3-connect-device.jpg" />
</Frame>

You need to install the required dependencies that will allow you to connect your device to the Edge Impulse platform. This process is documented on the [Edge Impulse Website](/hardware/boards/nvidia-jetson) and includes:

* Running the Edge Impulse NVIDIA Jetson Nano setup script
* Connecting your device to the Edge Impulse platform

Once the firmware has been installed enter the following command:

```
edge-impulse-linux
```

If you are already connected to an Edge Impulse project, use the following command:

```
edge-impulse-linux --clean
```

Follow the instructions to log in to your Edge Impulse account.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/3a-device-connected.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=5a72dfaad8f7dfb82168dc98928a9d7f" width="1600" height="741" data-path=".assets/images/retail-image-classification-jetson-nano/3a-device-connected.jpg" />
</Frame>

Once complete, head over to the **Devices** tab of your project and you should see the connected device.

## Dataset

<Frame caption="Download data">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/4-download-data.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=068c81d350ab063ca52ff9118a171874" width="1600" height="755" data-path=".assets/images/retail-image-classification-jetson-nano/4-download-data.jpg" />
</Frame>

We are going to use the [Fruit and Vegetables SSM](https://www.kaggle.com/datasets/shadikfaysal/fruit-and-vegetables-ssm). This dataset has 18,000 images of various fruits and vegetables.

In this example we will use images from the Apples, Bananas, Chillis and Broccoli classes.

<Frame caption="Upload data">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/5-data-upload.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=2d3ed608693ce1df525a0a5bfabfdc07" width="1600" height="782" data-path=".assets/images/retail-image-classification-jetson-nano/5-data-upload.jpg" />
</Frame>

Once downloaded, unzip the data and navigate to the **Train** folder. Then proceed to upload the contents of **Train/Apples**, **Train/Bananas**, **Train/Chillis** and **Train/Brocolli**. Make sure to select **Automatically split between training and testing**, and enter the correct label.

<Frame caption="Uploaded data">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/6-uploaded-data.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=356aed5e08b62570d2484d2ae882109f" width="1600" height="779" data-path=".assets/images/retail-image-classification-jetson-nano/6-uploaded-data.jpg" />
</Frame>

Once you have completed these steps, you should be able to see and filter your uploaded dataset.

## Create Impulse

Now we are going to create our neural network and train our model.

<Frame caption="Add processing block">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/9-impulse-design-processing-block.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=a3564b342127a84d4d77a1bb865e3a52" width="1600" height="779" data-path=".assets/images/retail-image-classification-jetson-nano/9-impulse-design-processing-block.jpg" />
</Frame>

Head to the **Create Impulse** tab. Next click **Add processing block** and select **Image**.

<Frame caption="Created Impulse">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/10-impulse-design-learning-block.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=8f4c30fb833a0a83e652e86c2064bf83" width="1600" height="778" data-path=".assets/images/retail-image-classification-jetson-nano/10-impulse-design-learning-block.jpg" />
</Frame>

Now click **Add learning block** and select **Transfer Learning (Images)**.

Now click **Save impulse**.

### Transfer Learning

#### Parameters

<Frame caption="Parameters">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/11-impulse-design-image-parameters.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=5ec4aa446eaa63b5b275ae1b943ca65f" width="1600" height="778" data-path=".assets/images/retail-image-classification-jetson-nano/11-impulse-design-image-parameters.jpg" />
</Frame>

Head over to the **Image** tab and click on the **Save parameters** button to save the parameters.

#### Generate Features

<Frame caption="Generate Features">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/12-impulse-design-generate-features.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=18f42dd89f31559cf4006cdb4344602f" width="1600" height="777" data-path=".assets/images/retail-image-classification-jetson-nano/12-impulse-design-generate-features.jpg" />
</Frame>

If you are not automatically redirected to the **Generate features** tab, click on the **Image** tab and then click on **Generate features** and finally click on the **Generate features** button.

<Frame caption="Generated Features">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/13-impulse-design-generated-features.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=77b1527793ced066253528794310adfb" width="1600" height="783" data-path=".assets/images/retail-image-classification-jetson-nano/13-impulse-design-generated-features.jpg" />
</Frame>

Your data should be nicely clustered and there should be as little mixing of the classes as possible. You should inspect the clusters and look for any data that is clustered incorrectly. If you find any data out of place, you can relabel or remove it. If you make any changes click **Generate features** again.

## Training

<Frame caption="Training">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/14-training.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=efb543a4ce447515a88e351a927de994" width="1600" height="782" data-path=".assets/images/retail-image-classification-jetson-nano/14-training.jpg" />
</Frame>

Now we are going to train our model. Click on the **Transfer Learning** tab then click **Auto-balance dataset**, **Data augmentation** and then **Start training**.

<Frame caption="Training complete">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/14-training-results.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=3a91a994a4a45d779d9b3257e5ecadba" width="1600" height="749" data-path=".assets/images/retail-image-classification-jetson-nano/14-training-results.jpg" />
</Frame>

Once training has completed, you will see the results displayed at the bottom of the page. Here we see that we have 96.1% accuracy. Lets test our model and see how it works on our test data.

## Testing

### Platform Testing

Head over to the **Model testing** tab where you will see all of the unseen test data available. Click on the **Classify all** and sit back as we test our model.

<Frame caption="Test model results">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/15-testing-results.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=cea7d66a2b735592366d9ac2fa41b2dc" width="1600" height="781" data-path=".assets/images/retail-image-classification-jetson-nano/15-testing-results.jpg" />
</Frame>

You will see the output of the testing in the output window, and once testing is complete you will see the results. In our case we can see that we have achieved 91.46% accuracy on the unseen data.

### On Device Testing

Before we deploy the software to the NVIDIA Jetson Nano, lets test using the Edge Impulse platform whilst connected to the Jetson Nano. For this to work make sure your device is currently connected and that your webcam is attached.

<Frame caption="Live testing: Apple">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/16-live-testing-apple.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=e843df515c07e9e1ede183296ee276c7" width="1600" height="747" data-path=".assets/images/retail-image-classification-jetson-nano/16-live-testing-apple.jpg" />
</Frame>

<br />

<Frame caption="Live testing: Banana">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/16-live-testing-banana.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=29c1f63bd520ae642d1eb8595f6cd120" width="1600" height="752" data-path=".assets/images/retail-image-classification-jetson-nano/16-live-testing-banana.jpg" />
</Frame>

<br />

<Frame caption="Live testing: Broccoli">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/16-live-testing-broccoli.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=8066052c17e3bfab1a3ea806c42be0e1" width="1600" height="748" data-path=".assets/images/retail-image-classification-jetson-nano/16-live-testing-broccoli.jpg" />
</Frame>

<br />

<Frame caption="Live testing: Chilli">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/16-live-testing-chilli.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=83250dce9aab318806b0448e46998246" width="1600" height="752" data-path=".assets/images/retail-image-classification-jetson-nano/16-live-testing-chilli.jpg" />
</Frame>

Use the **Live classification** feature to record some samples for classification from the webcam connected to the Jetson Nano. Your model should be able to correctly identify the class for each sample. If you are not getting accurate detections, you may need to provide more data samples, or fine tune the training parameters to increase your accuracy. First, you will want to save a **Version** though.

## Versioning

<Frame caption="Versioning">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/17-versioning.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=8e0d367a853bf8f8159e63c9e2396f9d" width="1600" height="743" data-path=".assets/images/retail-image-classification-jetson-nano/17-versioning.jpg" />
</Frame>

We can use the versioning feature to save a copy of the existing network. To do so head over to the **Versioning** tab and click on the **Create first version** button.

<Frame caption="Versions">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/17b-versions.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=b9c5784968ed546e5d1a32bfd441ed4a" width="1600" height="745" data-path=".assets/images/retail-image-classification-jetson-nano/17b-versions.jpg" />
</Frame>

This will create a snapshot of your existing model that we can come back to at any time.

## Deployment

Now we will deploy the software directly to the NVIDIA Jetson Nano. To do this simply head to the terminal on your Jetson Nano, and enter:

```
edge-impulse-linux-runner
```

This will then download the built model from Edge Impulse and start local inferencing on the Nano. Keep an eye out for a message that gives you a URL to view the results in your browser.

<Frame caption="Live Inferencing">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retail-image-classification-jetson-nano/18-testing-live-apple.jpg?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=d9d52e30c44b26bbdde644783cfef62b" width="1600" height="756" data-path=".assets/images/retail-image-classification-jetson-nano/18-testing-live-apple.jpg" />
</Frame>

## Conclusion

Here we have created a simple but effective solution for classifying various fruits and vegetables using computer vision powered on an NVIDIA Jetson Nano, using Edge Impulse.

You can train a network with your own images, or build off the model and training data provided in this tutorial.


Built with [Mintlify](https://mintlify.com).