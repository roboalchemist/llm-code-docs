# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/transfer-learning-keyword.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer learning (keyword spotting)

Transfer learning is the process of taking features learned from one problem and leveraging it on a new but related problem. Most of the time these features are learned from large scale datasets with common objects hence making it faster & more accurate to tune and adapt to new tasks. With Edge Impulse's transfer learning block for audio keyword spotting, we take the same transfer learning technique classically used for image classification and apply it to audio data. This allows you to fine-tune a pre-trained keyword spotting model on your data and achieve even better performance than using a [classification block](/studio/projects/learning-blocks/blocks/classification), even with a relatively small keyword dataset.

<iframe src="https://www.youtube.com/embed/whwds0mfQI8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

Excited? Train your first keyword spotting model in under 5 minutes with the [getting started wizard](https://studio.edgeimpulse.com/studio/profile/projects?createNewProject=1\&tutorial=kws).

To choose transfer learning as your learning block, go to create impulse and click on **Add a Learning Block**, and select **Transfer Learning (Keyword Spotting)**.

<Frame caption="Impulse setup for keyword spotting.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transfer-learning-keyword-spotting-impulse.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=a23a78de5e8e51387aee6d60028ca783" width="1600" height="786" data-path=".assets/images/transfer-learning-keyword-spotting-impulse.png" />
</Frame>

To choose your preferred pre-trained network, select the **Transfer learning** tab on the left side of your screen and click **choose a different model**. A pop up will appear on your screen with a list of models to choose from as shown in the image below.

<Frame caption="Choose different keyword spotting model.">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/tlks-nnarch.png?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=28141f9f0b07dcbbc124ac26007d737f" width="983" height="1000" data-path=".assets/images/tlks-nnarch.png" />
</Frame>

Edge Impulse uses state of the art **MobileNetV1 & V2** architectures trained on an ImageNet dataset as it's **pre-trained network** for you to fine-tune for your specific application.

<Frame caption="Available keyword spotting models.">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/tlks-model.png?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=b6b888d7543e38d61706562b0eaa9079" width="1260" height="1000" data-path=".assets/images/tlks-model.png" />
</Frame>

## Neural Network Settings

Before you start training your model, you need to set the following neural network configurations:

<Frame caption="Neural Network settings.">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/tlks-settings.png?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=bc970585674d4c5aa9a22182f68adaf7" width="1022" height="776" data-path=".assets/images/tlks-settings.png" />
</Frame>

* **Number of training cycles:** Each time the training algorithm makes one complete pass through all of the training data with back-propagation and updates the model's parameters as it goes, it is known as an epoch or training cycle.
* **Learning rate:** The learning rate controls how much the models internal parameters are updated during each step of the training process. Or you can also see it as how fast the neural network will learn. If the network overfits quickly, you can reduce the learning rate
* **Validation set size:** The percentage of your training set held apart for validation, a good default is 20%.

You might also need to enable **auto balance** to prevent model bias or even enable **data augmentation** to increase the size of your dataset and have more diverse dataset to prevent overfitting.

The preset configurations just don't work for your model? No worries, Expert Mode is for you! Expert Mode gives you full control of your model so that you can configure it however you want. To enable the expert mode, just click on the "⋮" button and toggle the expert mode.

<Frame caption="Expert mode.">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/tlks-expert.png?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=41a3c7d934fc959aeb639d100d7174a7" width="1029" height="1000" data-path=".assets/images/tlks-expert.png" />
</Frame>

You can use the expert mode to change your loss function, optimizer, print your model architecture and even set an early stopping callback to prevent overfitting your model.


Built with [Mintlify](https://mintlify.com).