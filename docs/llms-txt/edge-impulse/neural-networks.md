# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Neural networks

Neural networks are a set of algorithms, modeled loosely after the human brain, designed to recognize patterns. They interpret sensory data through a kind of machine perception, labeling, or clustering of raw input. The patterns they recognize are numerical, contained in vectors, into which all real-world data, be it images, sound, text, or time series, must be translated.

<Info>
  #### What about anomaly detection with K-Means or GMM?

  Please note that [K-Means](/studio/projects/learning-blocks/blocks/anomaly-detection-k-means) and [Gaussian Mixture Models (GMM)](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm) are not neural networks. They are algorithms used in unsupervised machine learning, specifically for clustering tasks.

  In Edge Impulse, Neural Networks can be used for supervised learning tasks such as [Image or Audio Classification](/studio/projects/learning-blocks/blocks/classification), [Regression](/studio/projects/learning-blocks/blocks/regression), [Object Detection](/studio/projects/learning-blocks/blocks/object-detection) either using Transfer Learning, using pre-set neural network architectures or by designing your own.
</Info>

## How do they work?

Neural networks consist of layers of interconnected nodes, also known as neurons.

### Neurons (or nodes)

Each node receives input from its predecessors, processes it, and passes its output to succeeding nodes. The processing involves weighted inputs, a bias (threshold), and an [activation function](/knowledge/concepts/machine-learning/neural-networks/activation-functions) that determines whether and to what extent the signal should progress further through the network.

<Frame caption="Single Neuron">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Single-Neuron.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=846fc0ee47684619d425a10b593eac21" width="962" height="604" data-path=".assets/images/Single-Neuron.png" />
</Frame>

### Layers

Neurons are organized into [layers](/knowledge/concepts/machine-learning/neural-networks/layers): input, hidden, and output layers. The complexity of the network depends on the number and size of these layers.

* **Input Layer:** Receives raw input data.
* **Hidden Layers:** Perform computations using weighted inputs.
* **Output Layer:** Produces the final output.

<Frame caption="Neural networks layers">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/deep-neural-network.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=31ee41b6ef2985bb6fcb2b473f4b5d63" width="1333" height="1000" data-path=".assets/images/deep-neural-network.png" />
</Frame>

### Neural network architectures

Neural networks can vary widely in architecture, adapting to different types of problems and data.

<Frame caption="Neural Network architecture example in Edge Impulse Studio">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Neural-networks-architecture.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=cf0ea4943ae1dabe70635665bc10d26e" width="1111" height="1000" data-path=".assets/images/Neural-networks-architecture.png" />
</Frame>

### Learning process

The power of neural networks lies in their ability to learn. Learning occurs through a process called training, where the network adjusts its weights based on the difference between its output and the desired output. This process is facilitated by an [optimizer](/knowledge/concepts/machine-learning/neural-networks/optimizers), which guides the network in adjusting its weights to minimize error (the [loss](/knowledge/concepts/machine-learning/neural-networks/loss-functions)).

* **Training:** Neural networks learn by adjusting weights based on the error in predictions. This process is repeated over many [training cycles, or epochs](/knowledge/concepts/machine-learning/neural-networks/epochs), using training data.
* **Backpropagation:** A key mechanism where the network adjusts its weights starting from the output layer and moving backward through the hidden layers, minimizing error with each pass.

## Neural networks in Edge AI

In Edge AI, neural networks operate under constraints of lower computational power and energy efficiency. They need to be optimized for speed and size without compromising too much on accuracy. This often involves techniques like feature extraction, neural network architectures, transfer learning, quantization, and model pruning.

* **Feature Extraction:** Extracting meaningful features from the raw data that can be effectively processed by the neural network on resource-constrained devices.
* **Neural Networks Architectures**: Selecting a model architecture that is designed to run efficiently on the type of processor you are targeting, and fit within memory constraints.
* **Transfer Learning:** Using a pre-trained model and retraining it with a specific smaller dataset relevant to the edge application.
* **Quantization:** Reducing the precision of the numbers used in the model to decrease the computational and storage burden.
* **Model Pruning:** Reducing the size of the model by eliminating unnecessary nodes and layers.

Neural networks, in the context of Edge AI, must be designed and optimized to function efficiently in resource-constrained environments, balancing the trade-off between accuracy and performance.

To learn more about Neural Networks, see the “Introduction to Neural Networks” video in our “Introduction to Embedded Machine Learning” course:

<iframe src="https://www.youtube.com/embed/c1pgVaEFxjM" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />


Built with [Mintlify](https://mintlify.com).