# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C++ library

Below is information to help you better understand how to run your impulses in C++ applications. For more details, see the specific C++ library tutorials.

## Input to the run\_classifier function

The input to the `run_classifier` function is always a `signal_t` structure with raw sensor values. This structure has two properties:

* `total_length` - the total number of values. This should be equal to `EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE` (from `model_metadata.h`). E.g. if you have 3 sensor axes, 100Hz sensor data, and 2 seconds of data this should be 600.
* `get_data` - a function that retrieves slices of data required by the DSP process. This is used in some DSP algorithms (like all audio-based ones) to page in the required data, and thus saves memory. Using this function you can store (f.e.) the raw data in flash or external RAM, and page it in when required.

F.e. this is how you would page in data from flash:

```
// this is placed in flash
const float features[300] = { 0 };

// function that pages the data in
int raw_feature_get_data(size_t offset, size_t length, float *out_ptr) {
    memcpy(out_ptr, features + offset, length * sizeof(float));
    return 0;
}

int main() {
    // construct the signal
    signal_t signal;
    signal.total_length = 300;
    signal.get_data = &raw_feature_get_data;
    // ... rest of the application
```

If you have your data already in RAM you can use the [signal\_from\_buffer](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/67f085eb39033edf80e1ea8e41f5c089b65187e3/dsp/numpy.hpp#L1327) function to construct the signal:

```
float features[30] = { 0 };
signal_t signal;
numpy::signal_from_buffer(features, 30, &signal);
// ... rest of the application
```

The `get_data` function expects floats to be returned, but you can use the [int8\_to\_float](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/67f085eb39033edf80e1ea8e41f5c089b65187e3/dsp/numpy.hpp#L1306) and [int16\_to\_float](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/67f085eb39033edf80e1ea8e41f5c089b65187e3/dsp/numpy.hpp#L1288) helper functions if your own buffers are `int8_t` or `int16_t` (useful to save memory). E.g.:

```
const int16_t features[300] = { 0 };

int raw_feature_get_data(size_t offset, size_t length, float *out_ptr) {
    return numpy::int16_to_float(features + offset, out_ptr, length);
}

int main() {
    signal_t signal;
    signal.total_length = 300;
    signal.get_data = &raw_feature_get_data;
    // ... rest of the application
```

## Signal layout for time-series data

Signals are always a flat buffer, so if you have multiple sensor data you'll need to flatten it. E.g. for sensor data with three axes:

```
Input data:
Axis 1:  9.8,  9.7,  9.6
Axis 2:  0.3,  0.4,  0.5
Axis 3: -4.5, -4.6, -4.8

Signal: 9.8, 0.3, -4.5, 9.7, 0.4, -4.6, 9.6, 0.5, -4.8
```

## Signal layout for image data

The signal for image data is also flattened, starting with row 1, then row 2 etc. And every pixel is a single value in HEX format (RRGGBB). E.g.:

```
Input data (3x2 pixel image):
BLACK RED  RED
GREEN BLUE WHITE

Signal: 0x000000, 0xFF0000, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFFFF
```

We do have an end-to-end example on constructing a signal from a frame buffer in RGB565 format, which is easily adaptable to other image formats, see: [example-signal-from-rgb565-frame-buffer](https://github.com/edgeimpulse/example-signal-from-rgb565-frame-buffer).

## Directly quantize image data

If you're doing image classification and have a quantized model, the data is automatically quantized when reading the data from the signal to save memory. This is automatically enabled when you call `run_impulse`. To control the size of the buffer that's used to read from the signal in this case you can set the `EI_DSP_IMAGE_BUFFER_STATIC_SIZE` macro (which also allocates the buffer statically).

## Static allocation

To statically allocate the neural network model, set this macro:

* `EI_CLASSIFIER_ALLOCATION_STATIC=1`

You can easily control where the tensor arena is allocated by defining the EI\_TENSOR\_ARENA\_LOCATION macro, specifying .where\_to\_allocate. This is particularly useful for large size requirements and when the target has external RAM:

For example:

* `EI_TENSOR_LOCATION="<.where_to_allocate>"` - Here, `<.where_to_allocate>` can be a memory region such as ".sram," depending on your target's linker file.

Additionally we support full static allocation for quantized image models. To do so set this macro:

* `EI_DSP_IMAGE_BUFFER_STATIC_SIZE=1024`

Static allocation is not supported for other DSP blocks at the moment.


Built with [Mintlify](https://mintlify.com).