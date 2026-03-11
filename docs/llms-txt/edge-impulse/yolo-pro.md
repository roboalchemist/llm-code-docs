# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/object-detection/yolo-pro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# YOLO-Pro

<Warning>
  **Developer preview**

  This feature is a developer preview. Changes and improvements can still be made without prior notice and there are no guarantees that this feature will be fully released in future.
</Warning>

We’re excited to announce the initial release of YOLO-Pro, a new family of object detection architectures designed by Edge Impulse, purpose-built for edge devices, and available directly in Studio. Whether you're working with high-end microcontrollers, GPUs, accelerators, or anything in between, YOLO-Pro is designed to deliver top-tier performance where it matters most, on the edge.

## Use cases

Traditional YOLO models are powerful, but they were designed for cloud environments and academic datasets like COCO in mind, not to mention the restrictive licensing for commercial use. YOLO-Pro flips that paradigm. These architectures and training scripts are engineered from the ground up to excel in real-word edge deployments, with future optimizations specifically for industrial applications coming. That means better performance, lower latency, and smarter resource usage for your embedded object detection projects.

As we work towards a full release of the models, we will provide a list of example use cases where these models excel.

## Metrics

YOLO-Pro will be optimized against benchmarks that are relevant for industrial situations, leading to better performance at real-world tasks. Future releases of YOLO-Pro will be accompanied by benchmarks.

## Using the models in a project

The YOLO-Pro models can be accessed in your project in the same way as other object detection models.

<Frame caption="YOLO-Pro architecture selection">
  <img src="https://mintcdn.com/edgeimpulse/A42v1WryK4YjrnJB/.assets/images/yolo-pro-architecture-selection.png?fit=max&auto=format&n=A42v1WryK4YjrnJB&q=85&s=adeb0cd9d825bd929432e982372b7f61" width="1538" height="1000" data-path=".assets/images/yolo-pro-architecture-selection.png" />
</Frame>

<Steps>
  <Step title="Add learning block">
    Add an [object detection](/studio/projects/learning-blocks/blocks/object-detection) learning block to your [impulse](/studio/projects/impulse-design).
  </Step>

  <Step title="Select YOLO-Pro architecture">
    Select YOLO-Pro as your neural network architecture on the settings page for the object detection learning block.
  </Step>

  <Step title="Configure training settings">
    Configure your desired model size, architecture type, augmentation, and additional training parameters.
  </Step>
</Steps>

## Training settings

There are a number of settings specific to the YOLO-Pro models that can be configured. When in doubt, the best approach is to use the [EON Tuner](/studio/projects/eon-tuner) to help you decide. Please refer to the learning blocks [overview](/studio/projects/learning-blocks) for settings that are common across all learning blocks.

<Frame caption="YOLO-Pro training settings">
  <img src="https://mintcdn.com/edgeimpulse/A42v1WryK4YjrnJB/.assets/images/yolo-pro-training-settings.png?fit=max&auto=format&n=A42v1WryK4YjrnJB&q=85&s=739417d1b39c7eee20b5dbae3b967639" width="1538" height="1000" data-path=".assets/images/yolo-pro-training-settings.png" />
</Frame>

### Model size

The table below shows approximate sizes for the YOLO-Pro models. To help you choose the appropriate model size for your edge hardware based on its available memory, there is an `Auto configure` button. You must first select your [target device](/studio/projects/dashboard/target-device) to use this functionality.

| Model size | Parameters |
| ---------- | ---------- |
| `pico`     | 682 K      |
| `nano`     | 2.4 M      |
| `small`    | 6.9 M      |
| `medium`   | 16.6 M     |
| `large`    | 30 M       |
| `xlarge`   | 35 M       |

### Use pre-trained weights

The YOLO-Pro models can use pre-trained weights or be trained from scratch. For most use cases, you will want to enable the use of pre-trained weights, as this will substantially reduce the amount of data and time required for training. If you have a very large dataset (e.g. 100,000+ images), disabling the use of pre-trained weights may lead to better model performance.

### Freeze backbone

<Info>
  **Parameter is conditionally shown**

  The freeze backbone parameter is conditionally shown based on the selection for the use pre-trained weights parameter. It will be shown if the use pre-trained weights option is enabled.
</Info>

There are three parts of the YOLO-Pro architecture: the backbone, the feature pyramid network (FPN), and the box and class heads. If the freeze backbone option is enabled, the backbone and FPN portions will be frozen during training, meaning that their weights will not be updated. Only the box and class heads will be trained.

This can be useful when you have a small dataset, as it prevents overfitting and reduces the amount of computation required for training.

### Architecture type

Besides selecting the model size, there are two options for the architecture type: `Attention with SiLU` and `No attention with ReLU`. The two options are described below.

#### Attention with SiLU

The attention with SiLU option is the more traditional of the two, and is similar to many modern YOLO architectures. The final block of the backbone uses partial self-attention, and all convolutional blocks use SiLU as the activation function.

This is the preferred option for most use cases, and is the default selection.

#### No Attention with ReLU

The no attention with ReLU option is a custom variant developed by Edge Impulse. It has two key differences when compared to the attention with SiLU option. First, the backbone does not use partial self-attention. This choice was made because not all edge hardware is able to efficiently run the operations required in the attention layer. Secondly, all convolutional blocks use ReLU as the activation function since some edge hardware will run ReLU notably faster.

This option is recommended when deploying to hardware that does not efficiently support attention layers or SiLU activations. It has been developed to provide a wider compatibility with edge hardware, but may not perform as well as the attention with SiLU option.

### Augmentation

The data used for training the YOLO-Pro models can be augmented using both spatial transformations and color space transformations. The transformations applied are from the [KerasCV](https://github.com/keras-team/keras-cv) preprocessing layers.

Spatial transformations change the locations of pixels but not their colors, whereas color transformations change pixel colors, but not their location. These can be used to tune augmentation based on the application. For example, a fixed camera use case may benefit from lower spatial transformations and color sensitive use cases may want no color space transformations.

#### Spatial transformations

When spatial transformations are selected, the applied augmentation includes random flips, crops, resizes, shears, rotations, and mosaic. The table below shows the specific transformations for each spatial augmentation option.

| Spatial augmentation      | Transformations applied                                    |
| ------------------------- | ---------------------------------------------------------- |
| `No spatial augmentation` | -                                                          |
| `Low`                     | RandomCropAndResize                                        |
| `Medium`                  | RandomCropAndResize + RandomRotation + RandomFlip          |
| `High`                    | RandomCropAndResize + RandomRotation + RandomFlip + Mosaic |

#### Color space transformations

When color space transformations are selected, the applied augmentation includes random transforms according to the method defined in [RandAugment: Practical automated data augmentation with a reduced search space](https://arxiv.org/abs/1909.13719). The low, medium, and high level options correspond to increasing amounts of augmentation being applied.

### Early stopping start epoch

If an early stopping start epoch is set, early stopping conditions are ignored until that epoch is reached. This is used to allow the model to "settle in". After that epoch, the early stopping callback is used. Currently, the early stopping condition is based on improvement of validation loss.

## Examples

In future, please see this section for a list of example projects that use YOLO-Pro.

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Learning blocks](/studio/projects/learning-blocks)
* [Object detection](/studio/projects/learning-blocks/blocks/object-detection)
* [Impulses](/studio/projects/impulse-design)
* [EON Tuner](/studio/projects/eon-tuner)


Built with [Mintlify](https://mintlify.com).