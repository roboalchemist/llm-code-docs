# Source: https://docs.edgeimpulse.com/knowledge/metrics/inference-performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inference performance

This is an overview of the performance metrics (time per inference, RAM and ROM usage) of typical models built with Edge Impulse, for both DSP code, neural networks, and other ML blocks. This page should give some guidance on which microcontroller to use for which task. Note that this page is only applicable to general purpose microcontrollers, performance numbers on specialized silicon like the [Syntiant Tiny ML Board](/hardware/boards/syntiant-tinyml-board) will look different.

Some notes:

* The memory usage numbers exclude boot code, peripheral drivers, printf, and memory tracking functions. This is done by first compiling a basic benchmarking application and subtracting the RAM and ROM used.
* The models were compiled in bare-metal mode (no RTOS), compiled with a release profile.
* All neural networks are 8-bit quantized, and were compiled with the Edge Impulse EON compiler.
* On the Cortex-M4F and Cortex-M7 MCUs CMSIS-DSP and CMSIS-NN are enabled to take advantage of the vector extensions on the platform (this is done automatically by the Edge Impulse SDK).
* All DSP code uses floating point math.
* RAM usage denotes the combined static RAM and the peak heap usage - the Edge Impulse SDK frees all allocated memory on the heap after each inference.
* The RAM usage does not include the input buffer, which contains your raw sensor data. Depending on your device you can either keep this in RAM, or in (external) flash and page the data in (the `signal_t` structure has methods to do so).

### Continuous gestures

Model built in the [Continuous gestures](/tutorials/end-to-end/motion-recognition) tutorial. Consists of a spectral analysis DSP block (lowpass filter, FFT length 128), a neural network (33x20x10x4 fully connected layers), and an anomaly detection block (3 axes selected), analyzing 2 seconds of accelerometer data.

**RAM:** 6.4K **ROM:** 42.5K

| MCU              | DSP Latency | Neural Network Latency | Anomaly Latency | Total Latency |
| ---------------- | ----------- | ---------------------- | --------------- | ------------- |
| Cortex-M0+ 48MHz | 370ms.      | 2ms.                   | 4ms.            | **376ms.**    |
| Cortex-M4F 80MHz | 15ms.       | 1ms.                   | 1ms.            | **17ms.**     |
| Cortex-M7 216MHz | 2ms.        | under 1ms.             | under 1ms.      | **2ms.**      |

### Keyword spotting / scene recognition

A model similar to [Sound recognition](/tutorials/end-to-end/sound-recognition) for detecting keywords or scene recognition in a realtime audio stream. Consists of an MFCC DSP block (13 coefficients, 0.02 frame length / stride, FFT length 256), a neural network (two 2D convolutional / pooling layers of 10 and 5 neurons, and two dense layers of 12 and 3 neurons), analyzing 1 second of audio data.

**RAM:** 19.6K **ROM:** 47.3K

| MCU              | DSP Latency | Neural Network Latency | Total Latency |
| ---------------- | ----------- | ---------------------- | ------------- |
| Cortex-M4F 80MHz | 168ms.      | 57ms.                  | **225ms.**    |
| Cortex-M7 216MHz | 39ms.       | 15ms.                  | **54ms.**     |

#### Continuous audio inferencing

See [Continuous audio sampling](/tutorials/topics/inference/sample-audio-continuously) to enable realtime audio classification multiple times a second, even on the Cortex-M4F mentioned above.

### Image recognition (32x32 grayscale)

Model similarly built in the [Image classification](/tutorials/end-to-end/image-classification/) tutorial. Consists of a 32x32 input image (grayscale), trained with the MobileNetV2 0.05 transfer learning block with additionally two dense layers of 10 and 3 neurons, analyzing a single image.

**RAM:** 70.2K **ROM:** 164.2K

| MCU              | Neural Network Latency |
| ---------------- | ---------------------- |
| Cortex-M4F 80MHz | **186ms.**             |
| Cortex-M7 216MHz | **39ms.**              |
| Cortex-M7 480MHz | **13ms.**              |

### Image recognition (96x96 color)

Model similarly built in the [Image classification](/tutorials/end-to-end/image-classification/) tutorial. Consists of a 96x96 input image (RGB), trained with the MobileNetV2 0.35 transfer learning block with additionally two dense layers of 10 and 3 neurons, analyzing a single image.

**RAM:** 297.0K **ROM:** 577.5K

| MCU                     | Neural Network Latency |
| ----------------------- | ---------------------- |
| Cortex-M7 480MHz        | **140ms.**             |
| Cortex-M55 + U55 160MHz | **3ms.**               |


Built with [Mintlify](https://mintlify.com).