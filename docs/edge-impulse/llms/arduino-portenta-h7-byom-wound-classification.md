# Source: https://docs.edgeimpulse.com/projects/expert-network/arduino-portenta-h7-byom-wound-classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 'Bring Your Own Model' Image Classifier for Wound Identification

Created By: Jackline Tum

Public Project: [https://studio.edgeimpulse.com/public/240673/latest](https://studio.edgeimpulse.com/public/240673/latest)

> **Warning** Trigger warning: this post contains graphic images of wounds.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/edgeimpulse.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=175f8f2f179ec23dad5fa10d6566ad2f" width="1280" height="720" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/edgeimpulse.png" />
</Frame>

## Introduction

Wound classification is a crucial step in wound diagnosis. This process helps clinicians to identify the right treatment procedure for a type of wound. Chronic wounds have an impact on human health and affects the quality of life, both emotionally and financially. According to the [Wound Care Learning Network](https://www.hmpgloballearningnetwork.com/site/wounds/article/wound-care-outcomes-and-associated-cost-among-patients-treated-us-outpatient-wound-centers-d), an estimate of more than \$50bn is spent on caring for wounds.

Wound Classification has been a manual process done by specialists, but in the current age of AI advancements and intelligent machines, tools such as AI cameras can reduce the cost and time in wound diagnosis and with the right data, make better predictions. This can be of importance to patients who might not have access to clinicians and perform self diagnosis on themselves, or in remote rural areas where there is no access to good wound care practices.

Overall, proper wound classification will result in the right treatment, improving the healing process and in general human health.

## Solution

In this tutorial we will perform wound classification to distinguish between a bruise and a diabetic wound with a custom model deployed on an Arduino Portenta H7 + Vision Shield using the newly unveiled Edge Impulse [Bring Your Own Model (BYOM)](/studio/projects/dashboard/byom) capability. With this feature, Machine learning engineers can build state of the art models and deploy them to their target edge devices with minimal effort.

### Hardware

An Arduino Portenta is a great fit for our use case because it is a powerful board that has two processors, a **Cortex M7** running 480 MHZ and a **Cortex M4** running at 240 MHZ. Both the the processors share the on-chip peripherals and can run Tensorflow Lite and Micropython, which we’ll need to deploy our model.

<Frame caption="Fig 1: Portenta H7">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/portenta.jpg?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=12543868f58efbd3e3e1783625b4df85" width="259" height="194" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/portenta.jpg" />
</Frame>

The Vision Shield has an ultra low power camera , with 320 x 320 pixel resolution and support for QVGA which captures images for inference.

<Frame caption="Fig 2: Vision Shield">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/vision-shield.jpg?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=24ca06a311e26e80c0dc794fb4656932" width="259" height="194" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/vision-shield.jpg" />
</Frame>

#### Hardware Requirements

1. Arduino Portenta H7
2. Portenta Vision Shield
3. USB-C cable

#### Software Requirements

1. [Edge Impulse Account](https://edgeimpulse.com/)
2. [Arduino IDE](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE)
3. [OpenMV IDE](https://openmv.io/pages/download)

### Hardware Setup

First, Install both the Arduino IDE and OpenMV IDE.

OpenMV IDE is used to view the camera output and run inference scripts, while the Arduino IDE is used to update the bootloader on the Portenta H7.

Follow the steps below to ensure you have the latest version of the bootloader:

Connect the Vision Shield to the Portenta H7.

Connect the Board to your computer with a USB-C cable.

Open your Arduino IDE, make sure your board is connected, then click **Files** > **Examples** > **STM\_32H747\_System** > **STM\_32H747\_manageBootloader** .

<Frame caption="Update Bootloader">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/arduino-bootloader.png?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=59f74effeaf9113a9e8554048fae2e4f" width="1366" height="768" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/arduino-bootloader.png" />
</Frame>

A new window with a sketch to update bootloaders for different Arduino boards pops up.

<Frame caption="Update Bootloader">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/bootloader.PNG?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=686b012bb8f6a1584a18eafe62441c2f" width="897" height="566" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/bootloader.PNG" />
</Frame>

Compile and upload the Sketch, and when done **Double press the reset button** on the board. The built-in green LED will start fading in and out.

Open your OpenMV IDE, and click on the **Connect** Icon.

<Frame caption="OpenMV CONNECT">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/CONNECT.PNG?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=528c204cebbbd8c0096353ac0424355f" width="67" height="132" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/CONNECT.PNG" />
</Frame>

A screen will appear with the message **A board in DFU mode was detected**. Select the "Install the latest release firmware". This will install the latest openMV firmware in the development board. Optionally, leave the "Erase all files" option as it is and click **OK**.

<Frame caption="OpenMV CONNECT">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/install-latest-firmware.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=ff3400f08162483984f3ce9e018c1c27" width="483" height="112" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/install-latest-firmware.png" />
</Frame>

The green LED will flash as the firmware is being updated. Once the process ends, a **DFU update complete** message appears on the screen.

<Frame caption="OpenMV CONNECT">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/firmware-update-complete.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=2f04dd803fbcb99fe7e032a06e41df39" width="508" height="247" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/firmware-update-complete.PNG" />
</Frame>

With this process completed the Portenta Board is now connected to OpenMV IDE and ready for deployment.

## Data Collection

Wound diagnosis is a critical step in wound care and therefore requires an accurate dataset. In order to collect a dataset, there is a need to do so with the help of a licensed clinician. We use the AZH dataset for Diabetic Images, which was labeled by a specialist from the [AZH Wound and Vascular Center](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9681740/). This ensures that the model is trained with accurate data. For the Bruise Images we use a curated dataset from Kaggle.

We then perform data cleaning to remove any images that appear blurred, empty or distorted. I also wrote a custom script to perform augmentation on the data using Keras data generator in order to increase the number of images in the dataset. This script performs various transforms such as rotation and flipping.

The code in [this notebook](https://github.com/tum-jackie/Wound-Classification-with-Edge-Impulse/blob/main/Notebooks/Data_Augmentation.ipynb) performs various data augmentation on the dataset, and then saves the data in a directory to be used in training the model.

### Link to the Datasets

[AZH DATASET](https://github.com/uwm-bigdata/wound_classification)

[KAGGLE DATASET](https://www.kaggle.com/datasets/yasinpratomo/wound-dataset)

## Model Training

In this project, we leverage Bring Your Own Model (BYOM) capabilities offered by Edge Impulse, which enables easy deployment of models trained on various development platforms onto edge devices.

The model training process took place on Google Colab. We utilize Transfer Learning with a MobileNet architecture and TensorFlow framework. By using the pre-trained MobileNetV2, we can benefit from its high-performance feature extraction capabilities while training on the wound dataset.

We then optimize the model for edge deployment by applying **Post Training Quantization**, a technique that reduces the model size without significant loss in accuracy. This technique aids in minimizing the memory footprint and storage requirements of the model while maintaining its performance.

Once the model is trained and optimized, we converted it to the TensorFlow Lite format, which is compatible with the Edge Impulse Platform. We saved and downloaded the model for further use. Find all the [code on GitHub](https://github.com/tum-jackie/Wound-Classification-with-Edge-Impulse/tree/main) with the necessary steps, including training, quantization, conversion, and saving, to enable the deployment of the Model to Edge Impulse Platform.

## Model Deployment

Create an account on [Edge Impulse](https://edgeimpulse.com/) if you haven't yet, create a new project, name it and then select "Developer" for the project type.

Because we want to deploy our model to our device and not collect data, select **Upload Model**. If you have an existing testing set, you can upload the images with the Existing data tab.

<Frame caption="Upload Model">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/upload-model.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=fc1078392fa527c526e41108831bccfc" width="686" height="296" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/upload-model.PNG" />
</Frame>

Upload the model in any of the formats accepted by Edge Impulse platform. Select the **Target device** and perform profiling for it.

Profiling lets us know how much of the device resources our model will use up once deployed on the target board.

Alternatively, select to **Profile** for a range of devices to get information on how the model will perform on other devices.

<Frame caption="Upload Model">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/Upload-TFModel.PNG?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=5172532b4797046d0f6e4dc05f0370c3" width="686" height="488" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/Upload-TFModel.PNG" />
</Frame>

Once the model is uploaded, set the model configurations. The **Model input** is the image input shape that was set when training the model. In this case, the input shape accepted by the model is an image with 96 x 96 resolution. The model output is **Classification** and then we enter the class labels. We have two classes, **bruise** and **diabetic**. Save the model and head to the **Deployment** tab.

<Frame caption="Upload Model">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/step2.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=483dababa48ff3c5f9f746b3ee5db884" width="508" height="507" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/step2.PNG" />
</Frame>

These are the **Profiling** results. The model uses 338.7KB of RAM and 573.6KB of Flash memory.

<Frame caption="Profiling Model">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/device-performance.png?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=f996e833c41bc3dbbe7516fce60a453f" width="505" height="175" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/device-performance.png" />
</Frame>

We can check the model behavior by uploading a test image. We use an image that was not used during the training process in order to better identify how the model performs with unseen data.

<Frame caption="Test Model">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/test-model.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=2ae27918d2284f257306ceeffbffb61d" width="494" height="546" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/test-model.PNG" />
</Frame>

The model performs well on one image. We then upload a set of images as Test images to further test the model performance before deploying the model on Arduino Portenta.

From the **Dashboard**, head to the **Data acquisition** tab, and upload a set of images as test data.

<Frame caption="Test Model">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/test-data.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=f2d65d9a8c83a7b48638d9ff866e1b6c" width="795" height="539" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/test-data.PNG" />
</Frame>

From the Dashboard, head to the **Model testing** tab and click **Classify all** to see how the model performs.

<Frame caption="Test Model">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/classifyall.PNG?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=9be8bc640e6f8107c10734aea5a80039" width="1053" height="444" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/classifyall.PNG" />
</Frame>

The model performance is quite satisfactory and we can now deploy to our target device.

There are different ways to deploy a model to the Arduino Portenta H7: as an arduino library, an OpenMV library, firmware, or a C++ library.

In this tutorial we will deploy to the Portenta as an OpenMV library. Head to the **Deployment tab**, search for the OpenMV library and click **Build**.

<Frame caption="Deploy Model">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/OPENMV-LIBRARY.PNG?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=e45a64ce77afd5d45abfbbdd759d70f8" width="890" height="524" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/OPENMV-LIBRARY.PNG" />
</Frame>

Once downloaded, extract the `.zip` file and copy the **.tflite** file and **labels.txt** file from the extracted folder to the connected Arduino Portenta.

<Frame caption="Portenta Disk">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/portenta-disk.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=824aba1a2eded93d7401fce638519e43" width="269" height="127" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/portenta-disk.PNG" />
</Frame>

Open the **ei\_classify** python script from the OpenMV IDE.

<Frame caption="OpenMV IDE">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/openMVIDE.PNG?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=5feb32fde54a7a0bec6c3d3149fc56a9" width="910" height="703" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/openMVIDE.PNG" />
</Frame>

Click **Connect** and the Impulse will now be running on the Arduino Portenta. Aim it at set of images and the classification results will get printed on the serial terminal.

Be sure to also set the **sensor.Pixformat** as Grayscale, as the Vision Shield takes images in Grayscale.

```
sensor.set_pixformat(sensor.GRAYSCALE)    # Set pixel format to RGB565 (or GRAYSCALE)
```

Here is a sample **bruise** classification:

<Frame caption="Bruise Classification">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/bruise.png?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=6f3794197958a56bf1ff946300faf493" width="1366" height="768" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/bruise.png" />
</Frame>

And a sample **diabetic wound** classification:

<Frame caption="Diabetic Classification">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-portenta-h7-byom-wound-classification/diabetic.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=7692c5599e8b0c499918919b13a3a547" width="1360" height="688" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/diabetic.png" />
</Frame>

## Conclusion

In this project, we have seen how it is possible to leverage AI-powered cameras to classify wounds, which offers a great advantage in reducing the time taken to diagnose wounds as well as reduce cost associated with the process.

This project could be scaled further by sending the inference results over a web platform for results to be conveniently accessed by clinicians. This enables accurate administration of treatment to patients regardless of their location and mitigates the severe effects of misdiagnosis, leading to improved human health, especially in rural areas without local expertise. Adding more dataset images in order to improve the model performance on diabetic wound classification would also be helpful.

With **Bring Your Own Model** on Edge Impulse, ML engineers can build robust, state of the art models and deploy to edge devices. This creates a huge opportunity to solve challenges with Machine Learning and deploy to suitable hardware devices.

This project is **Public**, you can clone and modify it for your own use case, as well as further optimize it.

<Frame caption="Project Setup">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-portenta-h7-byom-wound-classification/VIDEO.gif?s=b2190ab1fed99dd4ccd23e931bcf83bb" width="213" height="120" data-path=".assets/images/arduino-portenta-h7-byom-wound-classification/VIDEO.gif" />
</Frame>

## Credits

1. *Anisuzzaman, D.M., Patel, Y., Rostami, B. et al. Multi-modal wound classification using wound image and location by deep neural network. Sci Rep 12, 20057 (2022). [https://doi.org/10.1038/s41598-022-21813-0](https://doi.org/10.1038/s41598-022-21813-0)*
2. *[https://www.kaggle.com/datasets/yasinpratomo/wound-dataset](https://www.kaggle.com/datasets/yasinpratomo/wound-dataset)*


Built with [Mintlify](https://mintlify.com).