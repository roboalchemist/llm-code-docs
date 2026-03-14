# Source: https://docs.edgeimpulse.com/studio/projects/deployment/eon-compiler.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EON Compiler

The Edge Optimized Neural (EON) compiler is a powerful tool, included in Edge Impulse, that compiles machine learning models into highly efficient and hardware-optimized C++ source code. It supports a wide variety of neural networks trained in TensorFlow or PyTorch - and a large selection of classical ML models trained in scikit-learn, LightGBM or XGBoost. The EON Compiler also runs far more models than other inferencing engines, while saving up to 65% of RAM usage.

This approach eliminates complex code, significantly reduces device resource utilization, and saves inference time.

The EON Compiler also includes an additional option: The [EON Compiler (RAM optimized)](/studio/projects/deployment/eon-compiler#eon-compiler-ram-optimized), to better cater to diverse project requirements and constraints.

<iframe src="https://www.youtube.com/embed/yUre8L9DK-8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

Some of the key advantages of EON Compiler, which include:

## Key Benefits of EON Compiler:

* 25-65% less RAM
* 10-35% less flash
* Same accuracy as TFLite
* Faster inference

The EON Compiler is specifically designed for Edge AI applications where speed is paramount. By focusing on minimizing inference time, this version of the EON Compiler ensures that neural network models can execute as quickly as possible, a critical requirement for real-time or near-real-time applications.

## EON Compiler (RAM optimized)

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

The EON Compiler (RAM optimized) option further reduces memory usage, allowing AI models to run on even smaller microcontrollers (MCUs) without sacrificing the model's accuracy or integrity. This is particularly beneficial for developers looking to minimize hardware costs and enhance the feasibility of deploying advanced AI in resource-constrained environments. We use a method to compute values directly as required, thus minimizing the need to store these results. This approach led to a substantial decrease in RAM usage, for a slightly higher latency cost.

Please note that depending on your neural network architecture, we may not be able to provide this option, see the [Limitations](/studio/projects/deployment/eon-compiler#limitations) section.

### Examples

<Tabs>
  <Tab title="LiteRT (previously Tensorflow Lite)">
    <Frame caption="On-device resource usage - TFlite">
      <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-compiler-tflite.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=e2d8d6f80df2cd5f7ebbb31d93ad987f" width="1034" height="1000" data-path=".assets/images/eon-compiler-tflite.png" />
    </Frame>
  </Tab>

  <Tab title="EON Compiler">
    <Frame caption="On-device resource usage - EON Compiler">
      <img src="https://mintcdn.com/edgeimpulse/d1isFJqReu6pCxs5/.assets/images/eon-compiler-latency-optimized.png?fit=max&auto=format&n=d1isFJqReu6pCxs5&q=85&s=909f68c0b47067bbd69e3c2661e76aa7" width="1035" height="1000" data-path=".assets/images/eon-compiler-latency-optimized.png" />
    </Frame>
  </Tab>

  <Tab title="EON Compiler (RAM optimized)">
    <Frame caption="On-device resource usage - EON Compiler (RAM optimized)">
      <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-compiler-ram-optimized.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=276f254484cb839ce24f409f1f3a825f" width="1035" height="1000" data-path=".assets/images/eon-compiler-ram-optimized.png" />
    </Frame>
  </Tab>
</Tabs>

**What do these metrics mean?**

* **Processing blocks**: Here we can see the optimizations for the DSP components of the compiled model DSP components. e.g. Spectral Features, MFCC, FFT, Image, etc.
* **Learn Blocks**: The performance of the compiled model on the device. Here we see the time it takes to run inference.
* **Latency**: the time it takes to run the model on the device.
* **RAM**: the amount of RAM the model uses.
* **Flash**: the amount of ROM the model uses.
* **Accuracy**: the accuracy of the model.

## How does it work?

The input of the EON compiler is a LiteRT (previously Tensorflow Lite) Flatbuffer file containing model weights. The output is a .cpp and .h files containing unpacked model weights and functions to prepare and run the model inference.

Regular Tflite Micro is based on LiteRT (previously Tensorflow Lite) and contains all the necessary instruments for reading the model weights in Flatbuffer format (which is the content of .tflite file), constructing the inference graph, planning the memory allocation for tensors/data, executing the initialization, preparation and finally invoking the operators in the inference graph to get the inference results.

The advantage of using the traditional Tflite Micro approach is very versatile and flexible. The disadvantage is that all the code for getting the model ready on the device is pretty heavy for embedded systems.

To overcome these limitations, our solution involves performing resource-intensive tasks, such as reading the model from Flatbuffer, constructing the graph, and planning memory allocation directly on our servers.

Subsequently, the EON compiler performs the generation of C++ files, housing the necessary functions for the Init, Prepare, and Invoke stages.

These C++ files can then be deployed on the embedded systems, alleviating the computational burden on those devices.

The **EON Compiler (RAM Optimized)** option adds, on top of the above, a novel approach by computing values directly as needed and minimizing the storage of intermediate results. This method leads to a significant decrease in RAM usage - sometimes at the cost of a slightly higher latency/flash - without impacting the accuracy of model predictions.

In practice, we demonstrated this with our default 2D convolutional model for visual applications. By slicing the model graph into smaller segments, we managed to reduce the RAM usage significantly — by as much as 40 to 65% compared to LiteRT (previously Tensorflow Lite) — without altering the accuracy or integrity of the model's predictions.

## Limitations

The EON Compiler, including the EON Compiler (RAM optimized) version, is a powerful tool for optimizing neural network projects. However, there are some important limitations to keep in mind:

**Unsupported Operators**

Not all operators are supported by our compiler. If your model includes an operator we don't support, the compiler won't be able to fully optimize your model. This means that certain complex operations within your model might prevent the compiler from working as efficiently as possible.

Concerning the EON Compiler (RAM optimized) option, our slicing algorithm currently supports limited operators. For instance, if a standard convolutional model incorporates an unsupported operator in its architecture, the compiler will not be able to perform beyond that point. This limitation could restrict the application of our compiler to models that use only supported operations.

**Residual Layers**

We support models with certain types of residual layers—specifically, those that feed directly into a subsequent layer, like in MobileNet. However, if your model processes residuals in a more complex manner, the EON Compiler may not optimize it effectively.

## More metrics

In this section, we tested many different architectures. Some architectures may not be available with TFLite micro or with the EON-Compiler (RAM-Optimized) - see the [limitations](/studio/projects/deployment/eon-compiler#limitations) section.

### Image classification

<Tabs>
  <Tab title="RAM">
    <Frame caption="RAM usage for Image classification architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-Image-classification.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=19b8cdf4cda215037926f811d6363702" width="1600" height="890" data-path=".assets/images/EON-Image-classification.png" />
    </Frame>
  </Tab>

  <Tab title="ROM">
    <Frame caption="ROM usage for Image classification architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-Image-classification-ROM.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=31a3d817851ad32de688836bc3fa0fc3" width="1600" height="886" data-path=".assets/images/EON-Image-classification-ROM.png" />
    </Frame>
  </Tab>
</Tabs>

### Object Detection

<Tabs>
  <Tab title="RAM">
    <Frame caption="RAM usage for Object Detection architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-OD.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=607bf546ed87a60d2d5bb2bef9ef4c4d" width="1600" height="889" data-path=".assets/images/EON-OD.png" />
    </Frame>
  </Tab>

  <Tab title="ROM">
    <Frame caption="ROM usage for Object Detection architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-OD-ROM.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=cb37ae745667bbdd863449fb559262ce" width="1600" height="890" data-path=".assets/images/EON-OD-ROM.png" />
    </Frame>
  </Tab>
</Tabs>

### Keyword Spotting

<Tabs>
  <Tab title="RAM">
    <Frame caption="RAM usage for Keyword Spotting architectures - 3960 features (MFE 1000ms 16kHz)">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-KWS.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=6c17420d613841cd6b1f5fa01b1c47bd" width="1600" height="881" data-path=".assets/images/EON-KWS.png" />
    </Frame>
  </Tab>

  <Tab title="ROM">
    <Frame caption="ROM usage for Keyword Spotting architectures - 3960 features (MFE 1000ms 16kHz)">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-KWS-ROM.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=ae863e6a3b0a9ccb026f05bc8aed072c" width="1600" height="885" data-path=".assets/images/EON-KWS-ROM.png" />
    </Frame>
  </Tab>
</Tabs>

### Time series

<Tabs>
  <Tab title="RAM">
    <Frame caption="RAM usage for time-series architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-time-series.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=1fe653d9a6532d53aa0384921d67bc3a" width="1600" height="886" data-path=".assets/images/EON-time-series.png" />
    </Frame>
  </Tab>

  <Tab title="ROM">
    <Frame caption="ROM usage for time-series architectures">
      <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/EON-time-series-ROM.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=30c609f40d48a44a09e8b4311db7061f" width="1600" height="890" data-path=".assets/images/EON-time-series-ROM.png" />
    </Frame>
  </Tab>
</Tabs>

### Supported Operators

TensorFlow Lite for Microcontrollers supports a subset of TensorFlow Lite operators.

The matrix compares TensorFlow Lite builtin operators, supported op-version ranges, TFLM coverage, and Edge Impulse support.

Use the TensorFlow docs links in the table for operator-level descriptions.

Open the full-window matrix view: [TensorFlow 2.19 operator matrix](/studio/projects/deployment/eon-compiler-operator-matrix-2-19).

**Legend**

* TFLite builtin: Operator exists in the TensorFlow Lite builtin enum.
* TFLM supported: Operator is wired through the TFLM all-ops resolver in this repo.
* TFLM kind: Whether TFLM exposes the op as `builtin` or `custom`.
* Op version: TensorFlow Lite version range for that operator in this source snapshot (for example `v1-v5`). TFLM in this repo ignores version during resolver lookup.
* EI supported: Operator is wired through the Edge Impulse resolver.
* EI extra: Operator is supported by Edge Impulse but not part of TFLite builtin ops.


Built with [Mintlify](https://mintlify.com).