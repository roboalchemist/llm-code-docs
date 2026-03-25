# Semi-automatic Object Detection Annotation with MMDetection and Label-Studio

Annotation data is a time-consuming and laborious task. This article introduces how to perform semi-automatic annotation using the RTMDet algorithm in MMDetection in conjunction with Label-Studio software. Specifically, using RTMDet to predict image annotations and then refining the annotations with Label-Studio. Community users can refer to this process and methodology and apply it to other fields.

- 

RTMDet: RTMDet is a high-precision single-stage object detection algorithm developed by OpenMMLab, open-sourced in the MMDetection object detection toolbox. Its open-source license is Apache 2.0, and it can be used freely without restrictions by industrial users.

- 

Label Studio [https://github.com/heartexlabs/label-studio] is an excellent annotation software covering the functionality of dataset annotation in areas such as image classification, object detection, and segmentation.

In this article, we will use cat [https://download.openmmlab.com/mmyolo/data/cat_dataset.zip] images for semi-automatic annotation.

## Environment Configuration

To begin with, you need to create a virtual environment and then install PyTorch and MMCV. In this article, we will specify the versions of PyTorch and MMCV. Next, you can install MMDetection, Label-Studio, and label-studio-ml-backend using the following steps:

Create a virtual environment:

```
conda create -n rtmdet python=3.9 -y
conda activate rtmdet

```