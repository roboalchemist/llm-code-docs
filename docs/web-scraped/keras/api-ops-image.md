# Source: https://keras.io/api/ops/image/

Title: Keras documentation: Image ops

URL Source: https://keras.io/api/ops/image/

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L453)

### `affine_transform` function

```
keras.ops.image.affine_transform(
    images,
    transform,
    interpolation="bilinear",
    fill_mode="constant",
    fill_value=0,
    data_format=None,
)
```

Applies the given transform(s) to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **transform**: Projective transform matrix/matrices. A vector of length 8 or tensor of size N x 8. If one row of transform is `[a0, a1, a2, b0, b1, b2, c0, c1]`, then it maps the output point `(x, y)` to a transformed input point `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`, where `k = c0 x + c1 y + 1`. The transform is inverted compared to the transform mapping input points to output points. Note that gradients are not backpropagated into transformation parameters. Note that `c0` and `c1` are only effective when using TensorFlow backend and will be considered as `0` when using other backends.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill_mode**: Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel.

*   **fill_value**: Value used for points outside the boundaries of the input if `fill_mode="constant"`. Defaults to `0`.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Applied affine transform image or batch of images.

**Examples**

```
>>> x = np.random.random((2, 64, 80, 3)) # batch of 2 RGB images
>>> transform = np.array(
...     [
...         [1.5, 0, -20, 0, 1.5, -16, 0, 0],  # zoom
...         [1, 0, -20, 0, 1, -16, 0, 0],  # translation
...     ]
... )
>>> y = keras.ops.image.affine_transform(x, transform)
>>> y.shape
(2, 64, 80, 3)
```

```
>>> x = np.random.random((64, 80, 3)) # single RGB image
>>> transform = np.array([1.0, 0.5, -20, 0.5, 1.0, -16, 0, 0])  # shear
>>> y = keras.ops.image.affine_transform(x, transform)
>>> y.shape
(64, 80, 3)
```

```
>>> x = np.random.random((2, 3, 64, 80)) # batch of 2 RGB images
>>> transform = np.array(
...     [
...         [1.5, 0, -20, 0, 1.5, -16, 0, 0],  # zoom
...         [1, 0, -20, 0, 1, -16, 0, 0],  # translation
...     ]
... )
>>> y = keras.ops.image.affine_transform(x, transform,
...     data_format="channels_first")
>>> y.shape
(2, 3, 64, 80)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1266)

### `crop_images` function

```
keras.ops.image.crop_images(
    images,
    top_cropping=None,
    left_cropping=None,
    bottom_cropping=None,
    right_cropping=None,
    target_height=None,
    target_width=None,
    data_format=None,
)
```

Crop `images` to a specified `height` and `width`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **top_cropping**: Number of columns to crop from the top.
*   **left_cropping**: Number of columns to crop from the left.
*   **bottom_cropping**: Number of columns to crop from the bottom.
*   **right_cropping**: Number of columns to crop from the right.
*   **target_height**: Height of the output images.
*   **target_width**: Width of the output images.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Cropped image or batch of images.

**Example**

```
>>> images = np.reshape(np.arange(1, 28, dtype="float32"), [3, 3, 3])
>>> images[:,:,0] # print the first channel of the images
array([[ 1.,  4.,  7.],
       [10., 13., 16.],
       [19., 22., 25.]], dtype=float32)
>>> cropped_images = keras.image.crop_images(images, 0, 0, 2, 2)
>>> cropped_images[:,:,0] # print the first channel of the cropped images
array([[ 1.,  4.],
       [10., 13.]], dtype=float32)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1702)

### `elastic_transform` function

```
keras.ops.image.elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,
)
```

Applies elastic deformation to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **alpha**: Scaling factor that controls the intensity of the deformation.
*   **sigma**: Standard deviation of the Gaussian filter used for smoothing the displacement fields.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill_mode**: Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel.

*   **fill_value**: Value used for points outside the boundaries of the input if `fill_mode="constant"`. Defaults to `0`.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Transformed image or batch of images with elastic deformation.

**Examples**

```
>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images
>>> y = keras.ops.image.elastic_transform(x)
>>> y.shape
(2, 64, 80, 3)
```

```
>>> x = np.random.random((64, 80, 3))  # single RGB image
>>> y = keras.ops.image.elastic_transform(x)
>>> y.shape
(64, 80, 3)
```

```
>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images
>>> y = keras.ops.image.elastic_transform(
...     x, data_format="channels_first")
>>> y.shape
(2, 3, 64, 80)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L610)

```
keras.ops.image.extract_patches(
    images, size, strides=None, dilation_rate=1, padding="valid", data_format=None
)
```

Extracts patches from the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **size**: Patch size int or tuple (patch_height, patch_width)
*   **strides**: strides along height and width. If not specified, or if `None`, it defaults to the same value as `size`.
*   **dilation_rate**: This is the input stride, specifying how far two consecutive patch samples are in the input. For value other than 1, strides must be 1. NOTE: `strides > 1` is not supported in conjunction with `dilation_rate > 1`
*   **padding**: The type of padding algorithm to use: `"same"` or `"valid"`.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Extracted patches 3D (if not batched) or 4D (if batched)

**Examples**

```
>>> image = np.random.random(
...     (2, 20, 20, 3)
... ).astype("float32") # batch of 2 RGB images
>>> patches = keras.ops.image.extract_patches(image, (5, 5))
>>> patches.shape
(2, 4, 4, 75)
>>> image = np.random.random((20, 20, 3)).astype("float32") # 1 RGB image
>>> patches = keras.ops.image.extract_patches(image, (3, 3), (1, 1))
>>> patches.shape
(18, 18, 27)
```

**Guides and examples using `extract_patches`**

*   [Image classification with Vision Transformer](https://keras.io/examples/vision/image_classification_with_vision_transformer/)
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)
*   [Object detection with Vision Transformers](https://keras.io/examples/vision/object_detection_using_vision_transformer/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1603)

### `gaussian_blur` function

```
keras.ops.image.gaussian_blur(
    images, kernel_size=(3, 3), sigma=(1.0, 1.0), data_format=None
)
```

Applies a Gaussian blur to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **kernel_size**: A tuple of two integers, specifying the height and width of the Gaussian kernel.
*   **sigma**: A tuple of two floats, specifying the standard deviation of the Gaussian kernel along height and width.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Blurred image or batch of images.

**Examples**

```
>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images
>>> y = keras.ops.image.gaussian_blur(x)
>>> y.shape
(2, 64, 80, 3)
```

```
>>> x = np.random.random((64, 80, 3))  # single RGB image
>>> y = keras.ops.image.gaussian_blur(x)
>>> y.shape
(64, 80, 3)
```

```
>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images
>>> y = keras.ops.image.gaussian_blur(
...     x, data_format="channels_first")
>>> y.shape
(2, 3, 64, 80)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L176)

### `hsv_to_rgb` function

```
keras.ops.image.hsv_to_rgb(images, data_format=None)
```

Convert HSV images to RGB.

`images` must be of float dtype, and the output is only well defined if the values in `images` are in `[0, 1]`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

RGB image or batch of RGB images.

**Examples**

```
>>> import numpy as np
>>> from keras import ops
>>> x = np.random.random((2, 4, 4, 3))
>>> y = ops.image.hsv_to_rgb(x)
>>> y.shape
(2, 4, 4, 3)
```

```
>>> x = np.random.random((4, 4, 3)) # Single HSV image
>>> y = ops.image.hsv_to_rgb(x)
>>> y.shape
(4, 4, 3)
```

```
>>> x = np.random.random((2, 3, 4, 4))
>>> y = ops.image.hsv_to_rgb(x, data_format="channels_first")
>>> y.shape
(2, 3, 4, 4)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L928)

### `map_coordinates` function

```
keras.ops.image.map_coordinates(
    inputs, coordinates, order, fill_mode="constant", fill_value=0
)
```

Map the input array to new coordinates by interpolation.

Note that interpolation near boundaries differs from the scipy function, because we fixed an outstanding bug [scipy/issues/2640](https://github.com/scipy/scipy/issues/2640).

**Arguments**

*   **inputs**: The input array.
*   **coordinates**: The coordinates at which inputs is evaluated.
*   **order**: The order of the spline interpolation. The order must be `0` or `1`. `0` indicates the nearest neighbor and `1` indicates the linear interpolation.
*   **fill_mode**: Points outside the boundaries of the inputs are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"mirror"` and `"reflect"`. Defaults to `"constant"`.
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The inputs is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The inputs is extended by the nearest pixel.
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The inputs is extended by wrapping around to the opposite edge.
    *   `"mirror"`: `(c d c b | a b c d | c b a b)` The inputs is extended by mirroring about the edge.
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The inputs is extended by reflecting about the edge of the last pixel.

*   **fill_value**: Value used for points outside the boundaries of the inputs if `fill_mode="constant"`. Defaults to `0`.

**Returns**

Output input or batch of inputs.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1039)

### `pad_images` function

```
keras.ops.image.pad_images(
    images,
    top_padding=None,
    left_padding=None,
    bottom_padding=None,
    right_padding=None,
    target_height=None,
    target_width=None,
    data_format=None,
)
```

Pad `images` with zeros to the specified `height` and `width`.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **top_padding**: Number of rows of zeros to add on top.
*   **left_padding**: Number of columns of zeros to add on the left.
*   **bottom_padding**: Number of rows of zeros to add at the bottom.
*   **right_padding**: Number of columns of zeros to add on the right.
*   **target_height**: Height of output images.
*   **target_width**: Width of output images.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Padded image or batch of images.

**Example**

```
>>> images = np.random.random((15, 25, 3))
>>> padded_images = keras.ops.image.pad_images(
...     images, 2, 3, target_height=20, target_width=30
... )
>>> padded_images.shape
(20, 30, 3)
```

```
>>> batch_images = np.random.random((2, 15, 25, 3))
>>> padded_batch = keras.ops.image.pad_images(
...     batch_images, 2, 3, target_height=20, target_width=30
... )
>>> padded_batch.shape
(2, 20, 30, 3)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1476)

### `perspective_transform` function

```
keras.ops.image.perspective_transform(
    images,
    start_points,
    end_points,
    interpolation="bilinear",
    fill_value=0,
    data_format=None,
)
```

Applies a perspective transformation to the image(s).

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **start_points**: A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the source points in the original image that define the transformation.
*   **end_points**: A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the target points in the output image after transformation.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`.
*   **fill_value**: Value used for points outside the boundaries of the input if extrapolation is needed. Defaults to `0`.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Applied perspective transform image or batch of images.

**Examples**

```
>>> x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images
>>> start_points = np.array(
...     [
...         [[0, 0], [0, 64], [80, 0], [80, 64]],
...         [[0, 0], [0, 64], [80, 0], [80, 64]],
...     ]
... )
>>> end_points = np.array(
...     [
...         [[3, 5], [7, 64], [76, -10], [84, 61]],
...         [[8, 10], [10, 61], [65, 3], [88, 43]],
...     ]
... )
>>> y = keras.ops.image.perspective_transform(x, start_points, end_points)
>>> y.shape
(2, 64, 80, 3)
```

```
>>> x = np.random.random((64, 80, 3))  # single RGB image
>>> start_points = np.array([[0, 0], [0, 64], [80, 0], [80, 64]])
>>> end_points = np.array([[3, 5], [7, 64], [76, -10], [84, 61]])
>>> y = keras.ops.image.perspective_transform(x, start_points, end_points)
>>> y.shape
(64, 80, 3)
```

```
>>> x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images
>>> start_points = np.array(
...     [
...         [[0, 0], [0, 64], [80, 0], [80, 64]],
...         [[0, 0], [0, 64], [80, 0], [80, 64]],
...     ]
... )
>>> end_points = np.array(
...     [
...         [[3, 5], [7, 64], [76, -10], [84, 61]],
...         [[8, 10], [10, 61], [65, 3], [88, 43]],
...     ]
... )
>>> y = keras.ops.image.perspective_transform(
...     x, start_points, end_points, data_format="channels_first"
... )
>>> y.shape
(2, 3, 64, 80)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L274)

### `resize` function

```
keras.ops.image.resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,
)
```

Resize images to size using the specified interpolation method.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **size**: Size of output image in `(height, width)` format.
*   **interpolation**: Interpolation method. Available methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. Defaults to `"bilinear"`.
*   **antialias**: Whether to use an antialiasing filter when downsampling an image. Defaults to `False`.
*   **crop_to_aspect_ratio**: If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved.
*   **pad_to_aspect_ratio**: If `True`, pad the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be evenly padded on the short side.
*   **fill_mode**: When using `pad_to_aspect_ratio=True`, padded areas are filled according to the given mode. Only `"constant"` is supported at this time (fill with constant value, equal to `fill_value`).
*   **fill_value**: Float. Padding value to use when `pad_to_aspect_ratio=True`.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Resized image or batch of images.

**Examples**

```
>>> x = np.random.random((2, 4, 4, 3)) # batch of 2 RGB images
>>> y = keras.ops.image.resize(x, (2, 2))
>>> y.shape
(2, 2, 2, 3)
```

```
>>> x = np.random.random((4, 4, 3)) # single RGB image
>>> y = keras.ops.image.resize(x, (2, 2))
>>> y.shape
(2, 2, 3)
```

```
>>> x = np.random.random((2, 3, 4, 4)) # batch of 2 RGB images
>>> y = keras.ops.image.resize(x, (2, 2),
...     data_format="channels_first")
>>> y.shape
(2, 3, 2, 2)
```

**Guides and examples using `resize`**

*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)
*   [Creating TFRecords](https://keras.io/examples/keras_recipes/creating_tfrecords/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L35)

### `rgb_to_grayscale` function

```
keras.ops.image.rgb_to_grayscale(images, data_format=None)
```

Convert RGB images to grayscale.

This function converts RGB images to grayscale images. It supports both 3D and 4D tensors.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

Grayscale image or batch of grayscale images.

**Examples**

```
>>> import numpy as np
>>> from keras import ops
>>> x = np.random.random((2, 4, 4, 3))
>>> y = ops.image.rgb_to_grayscale(x)
>>> y.shape
(2, 4, 4, 1)
```

```
>>> x = np.random.random((4, 4, 3)) # Single RGB image
>>> y = ops.image.rgb_to_grayscale(x)
>>> y.shape
(4, 4, 1)
```

```
>>> x = np.random.random((2, 3, 4, 4))
>>> y = ops.image.rgb_to_grayscale(x, data_format="channels_first")
>>> y.shape
(2, 1, 4, 4)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L104)

### `rgb_to_hsv` function

```
keras.ops.image.rgb_to_hsv(images, data_format=None)
```

Convert RGB images to HSV.

`images` must be of float dtype, and the output is only well defined if the values in `images` are in `[0, 1]`.

All HSV values are in `[0, 1]`. A hue of `0` corresponds to pure red, `1/3` is pure green, and `2/3` is pure blue.

**Arguments**

*   **images**: Input image or batch of images. Must be 3D or 4D.
*   **data_format**: A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://keras.io/api/utils/config_utils#imagedataformat-function).

**Returns**

HSV image or batch of HSV images.

**Examples**

```
>>> import numpy as np
>>> from keras import ops
>>> x = np.random.random((2, 4, 4, 3))
>>> y = ops.image.rgb_to_hsv(x)
>>> y.shape
(2, 4, 4, 3)
```

```
>>> x = np.random.random((4, 4, 3)) # Single RGB image
>>> y = ops.image.rgb_to_hsv(x)
>>> y.shape
(4, 4, 3)
```

```
>>> x = np.random.random((2, 3, 4, 4))
>>> y = ops.image.rgb_to_hsv(x, data_format="channels_first")
>>> y.shape
(2, 3, 4, 4)
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/image.py#L1811)

### `scale_and_translate` function

```
keras.ops.image.scale_and_translate(
    images, output_shape, scale, translation, spatial_dims, method, antialias=True
)
```

Apply a scale and translation to the images.

Generates a new image of `output_shape` by resampling from the input image using the sampling method corresponding to method. For 2D images, this operation transforms a location in the input images, (x, y), to a location in the output image according to:

`(x * scale[1] + translation[1], y * scale[0] + translation[0])`.

(Note the inverse warp is used to generate the sample locations.) Assumes half-centered pixels, i.e the pixel at integer location row, col has coordinates y, x = row + 0.5, col + 0.5, and similarly for other input image dimensions.

If an output location(pixel) maps to an input sample location that is outside the input boundaries then the value for the output location will be set to zero.

The `method` argument expects one of the following resize methods:

*   `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`: Linear interpolation. If `antialias` is True, uses a triangular filter when downsampling.
*   `"cubic"`, `"bicubic"`, `"tricubic"`: Cubic interpolation, using the Keys cubic kernel.
*   `"lanczos3"`: Lanczos resampling, using a kernel of radius 3.
*   `"lanczos5"`: Lanczos resampling, using a kernel of radius 5.

**Arguments**

*   **images**: The input array.
*   **output_shape**: The output shape, as a sequence of integers with length equal to the number of dimensions of image.
*   **scale**: A [K] array with the same number of dimensions as `images`, containing the scale to apply in each dimension.
*   **translation**: A [K] array with the same number of dimensions as `images`, containing the translation to apply in each dimension.
*   **spatial_dims**: A length K tuple specifying the spatial dimensions that the passed `scale` and `translation` should be applied to.
*   **method**: A string specifying the resizing method to use. Available methods are `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`, `"cubic"`, `"bicubic"`, `"tricubic"`, `"lanczos3"` and `"lanczos5"`.
*   **antialias**: Whether an antialiasing filter should be applied when downsampling. Has no effect when upsampling. Defaults to `True`.

**Returns**

The scale and translated images.

**Example**

```
>>> images = np.arange(9, dtype="float32").reshape((3, 3))
>>> scale = np.array([2.0, 2.0]).astype("float32")
>>> translation = -(scale / 2.0 - 0.5)
>>> resized_images = keras.image.scale_and_translate(
...     images, (5, 5), scale, translation, (0, 1), "linear"
... )
>>> resized_images
array([[0.0 0.5 1.0 1.5 2.0]
       [1.5 2.0 2.5 3.0 3.5]
       [3.0 3.5 4.0 4.5 5.0]
       [4.5 5.0 5.5 6.0 6.5]
       [6.0 6.5 7.0 7.5 8.0]], dtype=float32)
```

* * *
