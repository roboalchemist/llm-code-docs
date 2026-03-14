# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/expert-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Expert mode

Expert Mode is designed for users with advanced knowledge of machine learning and [Keras](https://keras.io/), offering greater control over model customization. This mode is useful when working on complex models or when you need specific adjustments beyond the pre-built learning blocks in Edge Impulse Studio. It's also great if you want to copy and paste existing models or code for quick modifications.

If you have expertise in machine learning and Keras, you can switch to *Expert Mode* to access the entire [Keras API](https://keras.io/api/) and bring in your models or custom architectures:

<Frame caption="Switch to expert mode">
  <img src="https://mintcdn.com/edgeimpulse/bl3dk7kPQkfGIkjp/.assets/images/switch-to-expert-mode.png?fit=max&auto=format&n=bl3dk7kPQkfGIkjp&q=85&s=680616322dfe9397f6a4c25725df070e" width="1116" height="304" data-path=".assets/images/switch-to-expert-mode.png" />
</Frame>

<br />

<Frame caption="NN expert mode">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/NN-expert-mode.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=a33aa1802039c835e12c9403fc649348" width="1175" height="1000" data-path=".assets/images/NN-expert-mode.png" />
</Frame>

<Info>
  #### Already got a trained model?

  If you already have a trained model, you can bring this model to Edge Impulse using our [BYOM feature](/studio/projects/dashboard/byom).

  **Bring your own model** or **BYOM** allows you to profile, optimize and deploy your own pretrained model (TensorFlow SavedModel, ONNX, or LiteRT (previously Tensorflow Lite)) to any edge device, directly from your Edge Impulse project.
</Info>

## How do I enable Keras (expert) mode?

To enable Keras (expert) mode in Edge Impulse:

1. Navigate to the model configuration page in Edge Impulse Studio.
2. Click on the "⋮" button (three vertical dots) to open the options menu.
3. Toggle the "Expert Mode" option.

Once enabled, you can access and modify the full Keras code for your model. This unlocks advanced customization features, allowing you to train your model to meet specific requirements.

## What can I do in Keras (expert) mode?

In expert mode, you have access to a wide range of advanced features, including:

* **Custom Architectures:** Use the full Keras API to create and modify neural network architectures. This includes changing loss functions, optimizers, and printing model architectures.

* **Early Stopping Callback:** Prevent overfitting by setting up early stopping callbacks, with control over parameters such as `monitor`, `min_delta`, `patience`, and `restore_best_weights`. [Learn more about Early Stopping](/knowledge/concepts/machine-learning/neural-networks/epochs#changing-the-epochs-in-expert-mode).

* **Object Weighting for FOMO:** Adjust the weighting of object output cells in the loss function, particularly useful for rare object detection scenarios. [Expert Mode Tips for FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo#expert-mode-tips).

* **MobileNet Cut Point Adjustment:** Customize cut points in the MobileNetV2 architecture to modify spatial reduction and model capacity. [MobileNet Cut Point Adjustment](/studio/projects/learning-blocks#expert-mode).

* **FOMO Classifier Capacity Enhancement:** Increase the capacity of the FOMO classifier by adding layers or increasing filters. [Enhance FOMO Classifier](/studio/projects/learning-blocks/blocks/object-detection/fomo#expert-mode-tips).

* **Transfer Learning Adjustments:** Customize the final layers of pre-trained models like MobileNetV1 for specific tasks, such as audio or image classification. [Learn more about Transfer Learning](/studio/projects/learning-blocks#expert-mode).

* **Activation Functions:** Implement custom activation functions to enhance model performance. [Implementing Activation Functions](/knowledge/concepts/machine-learning/neural-networks/activation-functions#implementing-activation-functions-in-expert-mode).

* **Optimizer Customization:** Integrate advanced optimizers like VeLO for superior training efficiency. [Using VeLO Optimizer](/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo).

* **Loss Function Customization:** Define and implement custom loss functions tailored to your specific problem. [Customizing Loss Functions](/knowledge/concepts/machine-learning/neural-networks/epochs#changing-the-epochs-in-expert-mode).

* **Epoch Management:** Control the number of training cycles and apply early stopping techniques to optimize training time and model accuracy. [Epoch Management](/knowledge/concepts/machine-learning/neural-networks/epochs#changing-the-epochs-in-expert-mode).

## Limitations

For security reasons, network access is not enabled for jobs triggered by learning blocks, so external pre-trained weights cannot be fetched. Enterprise users can contact their solution engineer if network access is needed.

## Conclusion

Expert Mode provides ML experts access and flexibility to fine-tune their machine-learning models for optimal performance. By accessing the [Keras API](https://keras.io/api/),users can customize every aspect of their models, including architecture design, loss functions, and optimizers. Features such as early stopping, object weighting, and MobileNet cut-point adjustment enable the creation of highly specialized models tailored to their unique project requirements.

This advanced level of customization accelerates experimentation and ensures models are precisely optimized to meet the specific constraints and demands of each project.


Built with [Mintlify](https://mintlify.com).