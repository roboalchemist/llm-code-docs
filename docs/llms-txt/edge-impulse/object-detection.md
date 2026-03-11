# Source: https://docs.edgeimpulse.com/tools/specifications/data-annotation/object-detection.md

# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/object-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Object detection

Object detection takes an image and outputs information about the class and number of objects, position, (and, eventually, size) in the image.

Edge Impulse provides several object detection model architectures built into the platform, in addition to the providing the ability to use a [custom learning block](/studio/organizations/custom-blocks/custom-learning-blocks) to bring in your own architectures. The built-in options are:

* [YOLO-Pro](/studio/projects/learning-blocks/blocks/object-detection/yolo-pro)
* [FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo)
* [MobileNetV2 SSD FPN](/studio/projects/learning-blocks/blocks/object-detection/mobilenetv2-ssd-fpn)

***

| Specification          | YOLO-Pro                        | FOMO                                           | MobileNetV2 SSD FPN                                              |
| ---------------------- | ------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| **Labelling method**   | Bounding boxes                  | Bounding boxes                                 | Bounding boxes                                                   |
| **Input image size**   | Multiples of 32<br />(square)   | Any<br />(square)                              | 320x320                                                          |
| **Input image colour** | RGB                             | Greyscale or RGB                               | RGB                                                              |
| **Output format**      | Bounding boxes                  | Centroids                                      | Bounding boxes                                                   |
| **MCU inference**      | ✅                               | ✅                                              | ❌                                                                |
| **CPU/GPU inference**  | ✅                               | ✅                                              | ✅                                                                |
| **Limitations**        | Currently in developer preview. | Objects should have similar sizes and shapes.  | Objects should be large relative to the image.                   |
|                        |                                 | Objects should not be too close to each other. | Models use high compute resources (in the edge computing world). |
|                        |                                 | Object size not available.                     | Input image size is fixed.                                       |


Built with [Mintlify](https://mintlify.com).