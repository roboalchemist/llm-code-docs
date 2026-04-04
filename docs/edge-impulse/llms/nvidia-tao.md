# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/nvidia-tao.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA TAO

<Warning>
  **Deprecated feature**

  This feature has been deprecated. Please see below for additional details.
</Warning>

Edge Impulse support of NVIDIA TAO object detection and image classification models has been deprecated. As of February 28th, 2025, these model options no longer appear within the platform.

## Reason for deprecation

The NVIDIA TAO models that were available directly in the Edge Impulse platform have been deprecated by NVIDIA.

## Impact on existing projects

Your existing projects that use NVIDIA TAO models will continue to work in Studio, including deployment. However, you will not be able retrain these models.

## Alternative options

There are alternative model options with comparable or improved performance available in the Edge Impulse platform.

### Object detection

There are several object detection models built into the platform that are currently available to you, including those based on the Edge Impulse [YOLO-Pro](/studio/projects/learning-blocks/blocks/object-detection/yolo-pro) and [FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo) architectures, in addition to the [MobileNetV2 SSD FPN](/studio/projects/learning-blocks/blocks/object-detection/mobilenetv2-ssd-fpn) architecture. These models can be accessed by adding an [object detection](/studio/projects/learning-blocks/blocks/object-detection) learning block to your impulse, then selecting your desired model on the settings page for the block.

You are also able to train other object detection architectures using [custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks). For example, see this [YOLOv5](https://github.com/edgeimpulse/ml-block-yolov5) learning block.

All of these options can be used as alternatives to the NVIDIA TAO object detection models that were previously available.

### Image classification

In addition to existing models available for image classification found within the platform, the EfficientNet architecture has now been added as well. These models can be accessed by adding a [transfer learning (images)](/studio/projects/learning-blocks/blocks/transfer-learning-images) learning block to your impulse, then selecting your desired model on the settings page for the block.

Similar to the object detection section above, other image classification architectures can be trained using [custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks).

All of these options can be used as alternatives to the NVIDIA TAO image classification models that were previously available.


Built with [Mintlify](https://mintlify.com).