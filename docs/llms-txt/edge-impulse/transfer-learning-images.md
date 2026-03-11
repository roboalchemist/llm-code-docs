# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/transfer-learning-images.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer learning (images)

When creating an impulse to solve an image classification problem, you will most likely want to use transfer learning. This is particularly true when working with a relatively small dataset.

Transfer learning is the process of taking features learned from one problem and leveraging it on a new but related problem. Most of the time these features are learned from large scale datasets with common objects hence making it faster & more accurate to tune and adapt to new tasks.

To choose transfer learning as your learning block, go to create impulse and click on **Add a Learning Block**, and select **Transfer Learning**.

<Frame caption="Impulse setup for image classification.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/TL-set.PNG?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=2e623771800a948bdc63d4ac67002a8a" width="1046" height="468" data-path=".assets/images/TL-set.PNG" />
</Frame>

To choose your preferred pre-trained network, go to Transfer learning on the left side of your screen and click **choose a different model**. A pop up will appear on your screen with a list of models to choose from.

<Frame caption="Choose a different transfer learning model.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Tl-choose.PNG?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=a1950e6e891584c456de3bc22b23f8fa" width="1152" height="766" data-path=".assets/images/Tl-choose.PNG" />
</Frame>

## Models

Edge Impulse uses state of the art architectures available for you to train or fine-tune for your specific application.

<Accordion title="MobileNetV1">
  ### MobileNetV1

  MobileNetV1 is a lightweight and efficient convolutional neural network designed for mobile and embedded vision applications. It leverages depthwise separable convolutions to reduce computational complexity, making it ideal for real-time processing on resource-constrained devices.

  Pre-trained on the ImageNet dataset with a 96x96 resolution, MobileNetV1 supports both RGB and grayscale inputs, offering flexibility for various use cases.

  * **Size (96x96)**: The optimal input image resolution (but you can use another resolution), optimized for capturing essential details while maintaining efficiency.
  * **Alpha (e.g., 0.25)**: A width multiplier that scales the number of channels in each layer, allowing you to balance model size and performance. Lower values create more compact models suitable for constrained devices.

  We offer three variants to cater to different resource constraints:

  * **MobileNetV1 96x96 0.25**: Uses around 105.9K RAM and 301.6K ROM, providing a good balance of performance and efficiency.
  * **MobileNetV1 96x96 0.2**: Optimized for speed with around 83.1K RAM and 218.3K ROM, ideal for applications with tight resource constraints.
  * **MobileNetV1 96x96 0.1**: Ultra-lightweight, using around 53.2K RAM and 101K ROM, perfect for environments with minimal computational resources.

  MobileNetV1 is a reliable choice for developers seeking an efficient and effective solution for image classification tasks on mobile and embedded devices.
</Accordion>

<Accordion title="MobileNetV2">
  ### MobileNetV2

  MobileNetV2 is an advanced architecture designed for efficient image classification. Building on MobileNetV1, it introduces features like inverted residuals and linear bottlenecks to improve accuracy while keeping computational costs low.

  We offer two input resolutions, 96x96 and 160x160, each optimized for different use cases:

  * **Size (e.g., 96x96, 160x160)**: Determines the optimal input image resolution (but you can use another resolution). Larger sizes capture more detail but require more computational resources.
  * **Alpha (e.g., 0.35)**: A width multiplier that adjusts the model's capacity. Lower values create leaner, faster models suitable for edge devices, while higher values enhance accuracy for more complex tasks.

  **Available variants**

  * **MobileNetV2 96x96 0.35**: Balances performance and efficiency, using around 296.8K RAM and 575.2K ROM. Supports both RGB and grayscale inputs.
  * **MobileNetV2 96x96 0.1**: Optimized for speed with around 270.2K RAM and 212.3K ROM. Supports both RGB and grayscale inputs.
  * **MobileNetV2 96x96 0.05**: Ultra-lightweight, using around 265.3K RAM and 162.4K ROM. Supports both RGB and grayscale inputs.
  * **MobileNetV2 160x160 1.0**: High-accuracy model using around 1.3M RAM and 2.6M ROM. Supports RGB inputs only.
  * **MobileNetV2 160x160 0.75**: Offers a balance of performance and resource usage, with around 1.3M RAM and 1.7M ROM. Supports RGB inputs only.
  * **MobileNetV2 160x160 0.5**: Efficient yet powerful, using around 700.7K RAM and 982.4K ROM. Supports RGB inputs only.
  * **MobileNetV2 160x160 0.35**: Lean and efficient, with around 683.3K RAM and 658.4K ROM. Supports RGB inputs only.

  MobileNetV2 is a practical choice for developers needing a reliable and efficient solution for image classification tasks, especially in resource-constrained environments.
</Accordion>

<Accordion title="EfficientNet">
  ### EfficientNet

  EfficientNet is a family of high-performance image classification models designed to scale efficiently across various resource constraints. These models offer a balance between accuracy and computational efficiency, making them suitable for complex use cases, particularly on Linux systems.

  **Model Size**: EfficientNet models range from B0 to B5, scaling from 4M to 28.3M parameters. Larger models offer higher accuracy but require more computational resources.

  * **B0**: 4M parameters, 16 MB
  * **B1**: 6.5M parameters, 26 MB
  * **B2**: 7.7M parameters, 30.8 MB
  * **B3**: 10.7M parameters, 42.8 MB
  * **B4**: 17.5M parameters, 70 MB
  * **B5**: 28.3M parameters, 113.2 MB

  **Use pretrained weights**: EfficientNet supports transfer learning with pre-trained weights from the ImageNet dataset. This feature significantly speeds up training and improves accuracy for most use cases.

  **Freeze % of layers**: You can freeze a percentage of the base model's layers to prevent them from being retrained, which helps in preserving pre-trained features while adapting the model to new data.

  **Customizable Last Layers**: Add extra layers after the EfficientNet base model, such as dense layers or dropout layers, to tailor the model architecture to your specific needs.

  * Valid options: `dense: X` (where X=neurons), `dropout: X` (where X=dropout rate between 0..1).
  * Example: `dense: 32, dropout: 0.1`

  **Data Augmentation**: Enhance your training dataset with augmentations like flip, crop, and brightness adjustments to improve model robustness.

  * Valid options: `flip`, `crop`, `brightness`
  * Example: `flip, crop, brightness`
</Accordion>

## Neural Network settings

See [Neural Network Settings](/studio/projects/learning-blocks#neural-network-settings) on the Learning Block page.

## Expert mode

See [Expert mode](/studio/projects/learning-blocks#expert-mode) on the Learning Block page.

The preset configurations just don't work for your model? No worries, Expert Mode is for you! Expert Mode gives you full control of your model so that you can configure it however you want. To enable the expert mode, just click on the "⋮" button and toggle the expert mode.

<Frame caption="Expert mode.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/TL-expert.PNG?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=461e7b22a6bbee2b7d9f836cf7d51ef2" width="970" height="1000" data-path=".assets/images/TL-expert.PNG" />
</Frame>

You can use the expert mode to change your loss function, optimizer, print your model architecture and even set an early stopping callback to prevent overfitting your model.

See the examples:

* [Customizing loss function in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/loss-functions#customizing-the-loss-function-in-expert-mode)
* [Changing the optimizer in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/optimizers#changing-the-optimizer-in-expert-mode)
* [Changing the epochs in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/epochs#changing-the-epochs-in-expert-mode)
* [Apply Early Stopping in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/epochs#apply-early-stopping-in-expert-mode)


Built with [Mintlify](https://mintlify.com).