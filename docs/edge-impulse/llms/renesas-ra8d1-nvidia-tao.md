# Source: https://docs.edgeimpulse.com/tutorials/hardware/renesas-ra8d1-nvidia-tao.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas RA8D1 - NVIDIA TAO models

The NVIDIA TAO model zoo offers a large variety of powerful pre-trained models that can help you get started on and make good progress on your projects in a very short period of time. With Edge Impulse's partnership with NVIDIA, these models are now available for you to be used in your projects. The Renesas RA8D1 evaluation kit, equipped with the most advanced Cortex-M85 microcontroller and ARM Helium technology, is a powerhouse for edge AI applications. This tutorial will walk you through the steps of harnessing the combined power of NVIDIA TAO and the Cortex-M85, by running your TAO based projects on the Renesas RA8D1.

## Prerequisites

To follow this tutorial you will need:

* a Renesas EK-RA8D1 evaluation kit. The kit can be purchased [here](https://mou.sr/4dyIQmY).
* the Renesas e2studio IDE and coding tool. This can be downloaded [here](https://www.renesas.com/en/software-tool/e-studio?srsltid=AfmBOoo_VPuui-PvMCN-W1CZCUiiCDT5Ew3q-DlflyStKp2Vx6eaid9H).
* an Edge Impulse project using an NVIDIA TAO training block. This step is detailed in this document.

## Creating a project with NVIDIA TAO blocks

To follow this tutorial, you will need to build an object detection or image classification project. We will create an object detection project using the following steps:

1. Create a new project in Edge Impulse.

2. Make sure to set your labeling method to 'Bounding boxes (object detection)' or 'One label per data item (image classification)'.

3. Collect and prepare your dataset as in [object detection](/tutorials/end-to-end/object-detection-bounding-boxes) or [image classification](/tutorials/end-to-end/image-classification).

4. Create an Impulse with an Object Detection (Images) or Transfer Learning (Images) block.

   <Frame caption="Create Impulse">
     <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/create-impulse-for-nvidia-tao.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=639173c5724cdd8a86a9fa7894291192" width="1600" height="686" data-path=".assets/images/create-impulse-for-nvidia-tao.png" />
   </Frame>

5. Extract your images features.

6. In your Object Detection (Images) or Transfer Learning (Images) view, select your NVIDIA TAO model:

   <Frame caption="Select model">
     <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/nvidia-tao-select-model.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=b18aee359f8962dc211ebdd8f85c604e" width="1449" height="1000" data-path=".assets/images/nvidia-tao-select-model.png" />
   </Frame>

7. Under **NVIDIA TAO...**, select between various parameters, in total there are 88 object detection architectures, and 15 image classification architectures.
   * There are pre-trained 3x224x224 backbones from the [NVIDIA TAO catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_object_detection), and others trained by Edge Impulse on ImageNet.
   * For image classification, pre-trained weights only support 224x224 image resolution. Image width and height must be greater than 32.

<Info>
  There are several pre-trained 3x224x224 backbones from the [NVIDIA TAO catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_object_detection), and others trained by Edge Impulse on ImageNet.
</Info>

1. Click on 'Start training'

   <Columns cols={2}>
     <Frame caption="Object detection view">
       <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-detection-view-tao.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=27416d57f907d03b16bc44a399c8ff17" width="857" height="1000" data-path=".assets/images/object-detection-view-tao.png" />
     </Frame>

     <Frame caption="Image classification view">
       <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/image-classification-view-tao.png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=ee570b7cfaabf14adab414fed94827ef" width="745" height="1000" data-path=".assets/images/image-classification-view-tao.png" />
     </Frame>
   </Columns>

## Deploying on the RA8D1

Once the model has finished training, you will be ready to deploy it to your device. For non-NVIDIA TAO models, the process to deploy on the RA8 is the standard method described [here](/hardware/boards/renesas-ek-ra8d1). However, applications using TAO models require more space to store the model and application, which is why we need to manually allocate the storage location in the RA8 firmware before flashing. This is a multi-step process described below.

1. Download the RA8 firmware from the repository [here](https://github.com/edgeimpulse/firmware-renesas-ek-ra8d1-freertos).

2. Open this firmware in an IDE to access the build settings. We recommend using the renesas e2studio IDE mentioned in the prerequisites. Simply, open the IDE and choose the option to import as preexisting project from folder or archive. Once imported, navigate to `project > settings > C/C++ build > settings > tool settings`.

3. In the 'Tool Settings' tab, navigate to `GNU Arm Cross C++ Compiler > Preprocessor`. Under these settings, under 'Defined symbols (-D)', add `EI_CLASSIFIER_ALLOCATION_STATIC` as an additional defined symbol. This is also shown below:

   <Frame caption="Add symbol to project properties">
     <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-project-properties.jpeg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=e98968810a1fdbb53fb36278eeaa150b" width="1271" height="1000" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-project-properties.jpeg" />
   </Frame>

4. Hit 'Apply and Close' and build the project.

5. Now go back to the project created in studio in the section ['Creating a project with NVIDIA TAO blocks'](/tutorials/hardware/renesas-ra8d1-nvidia-tao#creating-a-project-with-nvidia-tao-blocks). Download the project as a C++ library instead of an RA8 deployment.

   <Frame caption="Download as C++ library">
     <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-download-c++.jpeg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=6e242fc92c158ff64c5ad614e0a51e9f" width="1600" height="568" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-download-c++.jpeg" />
   </Frame>

6. After downloading the project as a C++ library, navigate to `tflite-model/tflite_learn_##_compiled.cpp`. The '##' will be a number that will vary for each download.

7. Within this file, find the following block of code (usually around line 74):

   ```
   #if defined(EI_CLASSIFIER_ALLOCATION_STATIC)
   uint8_t tensor_arena[kTensorArenaSize] ALIGN(16);
   ```

   and replace it with the following:

   ```
   #if defined(EI_CLASSIFIER_ALLOCATION_STATIC)
   uint8_t tensor_arena[kTensorArenaSize] ALIGN(16) __attribute__((section(".sdram")));
   ```

   This will force the tensor arena, the area where the model is stored, to be created in the external storage which has 64MB SDRAM capacity, which is more than the internal 2MB Code Flash, 1MB SRAM capacity.

8. After making these changes, navigate back to the firmware downloaded in step 1. The file structure in this repository is as follows:
   ```bash  theme={"system"}
   /home
   │
   ├── flash-script
   │   ├── flash_linux.sh
   │   ...
   ├── script
   │   └── fsp.ld
   ├── src
   │   ├── edge-impulse-sdk
   │   ├── firmware-sdk
   │   ├── graphic
   │   ├── inference
   │   ├── ingestion-sdk-platform
   │   ├── ingestion-sdk
   │   ├── model
   │       └── model-parameters
   │       └── tflite-model
   │   └── peripheral
   ...
   ```

9. Here, replace the folders `model/model-parameters` and `model/tflite-model`, by the same folders downloaded from the studio as a C++ library. This will overwrite the standard firmware, with the one we modified to accommodate the NVIDIA TAO model.

10. Follow the [build instructions](https://github.com/edgeimpulse/firmware-renesas-ek-ra8d1-freertos/tree/main?tab=readme-ov-file#how-to-build) from the firmware repository to build and flash the firmware to your RA8.

Now you are ready to use your NVIDIA TAO based model on the Renesas RA8 device!

## Troubleshooting

### Failed to install the Renesas e2studio on MacOS

Sometimes after installing the e2studio application on your MacBook, you might see the error `"E2studio.app" is damaged and cannot be opened` when trying to open the application. You can resolve this problem by using the following terminal command to mark the it as “valid” after extracting it from the archive file:

```bash  theme={"system"}
xattr -d com.apple.quarantine /path/to/E2studio.app
```

making sure to replace `/path/to/E2studio.app` with the actual location of your e2studio application. One easy way of doing this is to drag the E2studio.app icon from your Finder window into the Terminal window, right after typing the initial part of the command. After this, you should be able to use the application without any issues.


Built with [Mintlify](https://mintlify.com).