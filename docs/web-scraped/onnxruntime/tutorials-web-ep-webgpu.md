# Source: https://onnxruntime.ai/docs/tutorials/web/ep-webgpu.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#using-the-webgpu-execution-provider) Using the WebGPU Execution Provider 

This document explains how to use the WebGPU execution provider in ONNX Runtime.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Basics](#basics)
  - [What is WebGPU? Should I use it?](#what-is-webgpu-should-i-use-it)
  - [How to use WebGPU EP in ONNX Runtime Web](#how-to-use-webgpu-ep-in-onnx-runtime-web)
- [WebGPU EP features](#webgpu-ep-features)
  - [Graph Capture](#graph-capture)
  - [Using `ort.env.webgpu` flags](#using-ortenvwebgpu-flags)
- [Keep tensor data on GPU (IO binding)](#keep-tensor-data-on-gpu-io-binding)
  - [Create input tensor from a GPU buffer](#create-input-tensor-from-a-gpu-buffer)
  - [Use pre-allocated GPU tensors](#use-pre-allocated-gpu-tensors)
  - [Specify the output data location](#specify-the-output-data-location)
- [Notes](#notes)
  - [Zero-sized tensors](#zero-sized-tensors)
  - [GPU tensor life cycle management](#gpu-tensor-life-cycle-management)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#basics) Basics

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#what-is-webgpu-should-i-use-it) What is WebGPU? Should I use it?

WebGPU is a new web standard for general purpose GPU compute and graphics. It is designed to be a low-level API, based on D3D12, Vulkan and Metal, and is designed to be used in the browser. It is designed to be more efficient and performant than WebGL, and is designed to be used for machine learning, graphics, and other compute tasks.

WebGPU is available out-of-box in latest versions of Chrome and Edge on Windows, macOS, Android and ChromeOS. It is also available in Firefox behind a flag and Safari Technology Preview. Check [WebGPU status](https://webgpu.io/status/) for the latest information.

If you are using ONNX Runtime Web for inferencing very lightweight models in you web application, and you want to have a small binary size, you can keep using the default WebAssembly (WASM) execution provider. If you want to run more compute intensive models, or you want to take advantage of the GPU in the client's device, you can use the WebGPU execution provider.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#how-to-use-webgpu-ep-in-onnx-runtime-web) How to use WebGPU EP in ONNX Runtime Web

This section assumes you have already set up your web application with ONNX Runtime Web. If you haven't, you can follow the [Get Started](/docs/get-started/with-javascript/web.html) for some basic info.

To use WebGPU EP, you just need to make 2 small changes:

1.  Update your import statement:

    - For HTML script tag, change `ort.min.js` to `ort.webgpu.min.js`:

      :::: 
      ::: highlight
      ``` highlight
      <script src="https://example.com/path/ort.webgpu.min.js"></script>
      ```
      :::
      ::::
    - For JavaScript import statement, change `onnxruntime-web` to `onnxruntime-web/webgpu`:

      :::: 
      ::: highlight
      ``` highlight
      import * as ort from 'onnxruntime-web/webgpu';
      ```
      :::
      ::::

    See [Conditional Importing](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/importing_onnxruntime-web#conditional-importing) for details.

2.  Specify 'webgpu' EP explicitly in session options:

    :::: 
    ::: highlight
    ``` highlight
    const session = await ort.InferenceSession.create(modelPath, );
    ```
    :::
    ::::

You might also consider installing the latest nightly build version of ONNX Runtime Web (onnxruntime-web@dev) to benefit from the latest features and improvements.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#webgpu-ep-features) WebGPU EP features

ONNX Runtime Web offers the following features which may be helpful to use with WebGPU EP:

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#graph-capture) Graph Capture

You can try the graph capture feature if your model has static shapes and all its computing kernels are running on WebGPU EP. This feature may potentially improve the performance of your model.

See [Graph Capture](/docs/tutorials/web/env-flags-and-session-options.html#enablegraphcapture) for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#using-ortenvwebgpu-flags) Using `ort.env.webgpu` flags 

See [`env.webgpu`](/docs/tutorials/web/env-flags-and-session-options.html#envwebgpu) for more details.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#keep-tensor-data-on-gpu-io-binding) Keep tensor data on GPU (IO binding)

By default, a model's inputs and outputs are tensors that hold data in CPU memory. When you run a session with WebGPU EP, the data is copied to GPU memory, and the results are copied back to CPU memory. If you get your input data from a GPU-based source, or you want to keep the output data on GPU for further processing, you can use IO binding to keep the data on GPU. This will be especially helpful when running transformer based models, which usually runs a single model multiple times with previous output as the next input.

For model input, if your input data is a WebGPU storage buffer, you can [create a GPU tensor and use it as input tensor](#create-input-tensor-from-a-gpu-buffer).

For model output, there are 2 ways to use the IO binding feature:

- [Use pre-allocated GPU tensors](#use-pre-allocated-gpu-tensors)
- [Specify the output data location](#specify-the-output-data-location)

Please also check the following topics:

- [Zero-sized tensors](#zero-sized-tensors)
- [GPU tensor life cycle management](#gpu-tensor-life-cycle-management)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-input-tensor-from-a-gpu-buffer) Create input tensor from a GPU buffer

If your input data is a WebGPU storage buffer, you can create a GPU tensor and use it as input tensor:

``` highlight
const inputTensor = ort.Tensor.fromGpuBuffer(inputGpuBuffer, );
```

Use this tensor as model inputs(feeds) so that the input data will be kept on GPU.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-pre-allocated-gpu-tensors) Use pre-allocated GPU tensors

If you know the output shape in advance, you can create a GPU tensor and use it as output tensor:

``` highlight

// Create a pre-allocated buffer and the corresponding tensor. Assuming that the output shape is [10, 1000].
const bufferSize = (10 * 1000) /* number of elements */ * 4 /* bytes per element */;
const device = ort.env.webgpu.device;
const myPreAllocatedBuffer = device.createBuffer();

const myPreAllocatedOutputTensor = ort.Tensor.fromGpuBuffer(myPreAllocatedBuffer, );

// ...

// Run the session with fetches
const feeds = ;
const fetches = ;
const results = await mySession.run(feeds, fetches);
```

By specifying the output tensor in the fetches, ONNX Runtime Web will use the pre-allocated buffer as the output buffer. If there is a shape mismatch, the `run()` call will fail.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#specify-the-output-data-location) Specify the output data location

If you don't want to use pre-allocated GPU tensors for outputs, you can also specify the output data location in the session options:

``` highlight
const mySessionOptions1 = ;

const mySessionOptions2 = 
};
```

By specifying the config `preferredOutputLocation`, ONNX Runtime Web will keep the output data on the specified device.

See [API reference: preferredOutputLocation](https://onnxruntime.ai/docs/api/js/interfaces/InferenceSession.SessionOptions.html#preferredOutputLocation) for more details.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#notes) Notes

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#zero-sized-tensors) Zero-sized tensors

If a tensor's shape contains 1 or more dimensions with size 0, the tensor is considered as a zero-sized tensor. Zero-sized tensors do not have any data, so the data location is not applied. ONNX Runtime Web always treats zero-sized tensors as CPU tensors. To create a zero-sized tensor, you can use the following code:

``` highlight
const zeroSizedTensor = new ort.Tensor('float32', [], [3, 256, 0, 64]);
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#gpu-tensor-life-cycle-management) GPU tensor life cycle management

It is important to understand how the underlying GPU buffer is managed so that you can avoid memory leaks and improve buffer usage efficiency.

A GPU tensor is created either by user code or by ONNX Runtime Web as model's output.

- When it is created by user code, it is always created with an existing GPU buffer using `Tensor.fromGpuBuffer()`. In this case, the tensor does not "own" the GPU buffer.

  - It is user's responsibility to make sure the underlying buffer is valid during the inference, and call `buffer.destroy()` to dispose the buffer when it is no longer needed.
  - Avoid calling `tensor.getData()` and `tensor.dispose()`. Use the GPU buffer directly.
  - Using a GPU tensor with a destroyed GPU buffer will cause the session run to fail.

- When it is created by ONNX Runtime Web as model's output (not a pre-allocated GPU tensor), the tensor "owns" the buffer.

  - You don't need to worry about the case that the buffer is destroyed before the tensor is used.
  - Call `tensor.getData()` to download the data from the GPU buffer to CPU and get the data as a typed array.
  - Call `tensor.dispose()` explicitly to destroy the underlying GPU buffer when it is no longer needed.