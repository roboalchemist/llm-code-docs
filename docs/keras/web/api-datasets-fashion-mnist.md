# Source: https://keras.io/api/datasets/fashion_mnist

Title: Keras documentation: Fashion MNIST dataset, an alternative to MNIST

URL Source: https://keras.io/api/datasets/fashion_mnist

Markdown Content:
Fashion MNIST dataset, an alternative to MNIST
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[MNIST digits classification dataset](https://keras.io/api/datasets/mnist/)[CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)[CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)[IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)[Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)[Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)[California Housing price regression dataset](https://keras.io/api/datasets/california_housing/)[Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[MNIST digits classification dataset](https://keras.io/api/datasets/mnist/)[CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)[CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)[IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)[Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)[Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)[California Housing price regression dataset](https://keras.io/api/datasets/california_housing/)[Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Built-in small datasets](https://keras.io/api/datasets/) / Fashion MNIST dataset, an alternative to MNIST 

Fashion MNIST dataset, an alternative to MNIST
==============================================

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/datasets/fashion_mnist.py#L12)

### `load_data` function

```
keras.datasets.fashion_mnist.load_data()
```

Loads the Fashion-MNIST dataset.

This is a dataset of 60,000 28x28 grayscale images of 10 fashion categories, along with a test set of 10,000 images. This dataset can be used as a drop-in replacement for MNIST.

The classes are:

| Label | Description |
| --- | --- |
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

**Returns**

Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`.

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(60000, 28, 28)`, containing the training data.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(60000,)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes (10000, 28, 28), containing the test data.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(10000,)` for the test data.

**Example**

```
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)
```

License:

The copyright for Fashion-MNIST is held by Zalando SE. Fashion-MNIST is licensed under the [MIT license](https://github.com/zalandoresearch/fashion-mnist/blob/master/LICENSE).

**Guides and examples using `load_data`**

*   [MixUp augmentation for image classification](https://keras.io/examples/vision/mixup/)

* * *

[Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist#fashion-mnist-dataset-an-alternative-to-mnist)

[`load_data` function](https://keras.io/api/datasets/fashion_mnist#loaddata-function)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
