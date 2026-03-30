# Migrate Configuration File from MMDetection 2.x to 3.x

The configuration file of MMDetection 3.x has undergone significant changes in comparison to the 2.x version. This document explains how to migrate 2.x configuration files to 3.x.

In the previous tutorial Learn about Configs, we used Mask R-CNN as an example to introduce the configuration file structure of MMDetection 3.x. Here, we will follow the same structure to demonstrate how to migrate 2.x configuration files to 3.x.

## Model Configuration

There have been no major changes to the model configuration in 3.x compared to 2.x. For the model’s backbone, neck, head, as well as train_cfg and test_cfg, the parameters remain the same as in version 2.x.

On the other hand, we have added the `DataPreprocessor` module in MMDetection 3.x. The configuration for the `DataPreprocessor` module is located in `model.data_preprocessor`. It is used to preprocess the input data, such as normalizing input images and padding images of different sizes into batches, and loading images from memory to VRAM. This configuration replaces the `Normalize` and `Pad` modules in `train_pipeline` and `test_pipeline` of the earlier version.

2.x Config

```
# Image normalization parameters
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53],
    std=[58.395, 57.12, 57.375],
    to_rgb=True)
pipeline=[
    ...,
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),  # Padding the image to multiples of 32
    ...
]

```