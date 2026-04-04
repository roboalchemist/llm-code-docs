# Source: https://keras.io/api/datasets/cifar10

Title: Keras documentation: CIFAR10 small images classification dataset

URL Source: https://keras.io/api/datasets/cifar10

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/datasets/cifar10.py#L13)

### `load_data` function

```
keras.datasets.cifar10.load_data()
```

Loads the CIFAR10 dataset.

This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 10 categories. See more info at the [CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html).

The classes are:

| Label | Description |
| --- | --- |
| 0 | airplane |
| 1 | automobile |
| 2 | bird |
| 3 | cat |
| 4 | deer |
| 5 | dog |
| 6 | frog |
| 7 | horse |
| 8 | ship |
| 9 | truck |

**Returns**

*   **Tuple of NumPy arrays**: `(x_train, y_train), (x_test, y_test)`.

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(50000, 32, 32, 3)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(50000, 1)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 32, 32, 3)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(10000, 1)` for the test data.

**Example**

```
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
assert x_train.shape == (50000, 32, 32, 3)
assert x_test.shape == (10000, 32, 32, 3)
assert y_train.shape == (50000, 1)
assert y_test.shape == (10000, 1)
```

**Note**: The CIFAR-10 dataset is known to have a small percentage of mislabeled samples, which is inherent to the original dataset. This label noise may impact training and evaluation. For more details, refer to discussions in the research literature on CIFAR-10 label quality.

**Guides and examples using `load_data`**

*   [The Functional API](https://keras.io/guides/functional_api/)
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)
*   [Image classification with ConvMixer](https://keras.io/examples/vision/convmixer/)
*   [Involutional neural networks](https://keras.io/examples/vision/involution/)
*   [A Vision Transformer without Attention](https://keras.io/examples/vision/shiftvit/)
*   [When Recurrence meets Transformers](https://keras.io/examples/vision/temporal_latent_bottleneck/)
*   [CutMix data augmentation for image classification](https://keras.io/examples/vision/cutmix/)
*   [RandAugment for Image Classification for Improved Robustness](https://keras.io/examples/vision/randaugment/)

* * *
