# Source: https://onnxruntime.ai/docs/tutorials/web/performance-diagnosis.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#performance-diagnosis) Performance Diagnosis 

ONNX Runtime Web is designed to be fast and efficient, but there are a number of factors that can affect the performance of your application. This document provides some guidance on how to diagnose performance issues in ONNX Runtime Web.

Before you start, make sure that ONNX Runtime Web successfully loads and runs your model. If you encounter any issues, see the [troubleshooting guide](/docs/tutorials/web/trouble-shooting.html) for help first.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [General performance tips](#general-performance-tips)
  - [Use the right model](#use-the-right-model)
  - [Use the right execution provider](#use-the-right-execution-provider)
  - [Use the diagnostic features](#use-the-diagnostic-features)
- [CPU tips](#cpu-tips)
  - [Enable multi-threading](#enable-multi-threading)
  - [Prefer uint8 quantized models](#prefer-uint8-quantized-models)
  - [Enable Proxy Worker](#enable-proxy-worker)
- [WebGPU tips](#webgpu-tips)
  - [Try Using graph capture](#try-using-graph-capture)
  - [Try using free dimension override](#try-using-free-dimension-override)
  - [Try keep tensor data on GPU](#try-keep-tensor-data-on-gpu)
- [Diagnostic features](#diagnostic-features)
  - [Profiling](#profiling)
    - [CPU profiling](#cpu-profiling)
    - [WebGPU profiling](#webgpu-profiling)
  - [Trace](#trace)
  - [Log level 'verbose'](#log-level-verbose)
  - [Enable debug mode](#enable-debug-mode)
- [Analyze the profiling data](#analyze-the-profiling-data)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#general-performance-tips) General performance tips

Here are some general tips to improve the performance of your application:

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-the-right-model) Use the right model

Choose a model that is appropriate for web scenario. A model that is too large or too complex may not run efficiently on less powerful hardware. Usually, the "tiny" or "small" versions of models are more commonly used in web applications. This does not mean that you cannot use larger models, but you should be aware of the potential hit on user experience due to longer load times and slower inference.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-the-right-execution-provider) Use the right execution provider

Choose the right execution provider for your scenario.

- **WebAssembly (wasm)**: This is the default CPU execution provider for ONNX Runtime Web. Use it for very small models or environments where GPU is not available.

- **WebGPU (webgpu)**: This is the default GPU execution provider. Use it when the device has a decent GPU which supports WebGPU.

- **WebNN (webnn)**: This is the option which offers potential near-native performance on the web. It is currently not supported by default in browsers, but you can enable WebNN feature manually in browser's settings.

- **WebGL (webgl)**: This execution provider is designed to run models using GPU on older devices that do not support WebGPU.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-the-diagnostic-features) Use the diagnostic features

Use the [diagnostic features](#diagnostic-features) to get detailed information about the execution of the model. This can be helpful to understand the performance characteristics of the model and to identify potential problems or bottlenecks.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cpu-tips) CPU tips

If you are using the WebAssembly (wasm) execution provider, you can use the following tips to improve the performance of your application:

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable-multi-threading) Enable multi-threading

Always enable multi-threading if the environment supports it. Multi-threading can significantly improve the performance of your application by utilizing multiple CPU cores.

This feature is enabled by default in ONNX Runtime Web, however it only works when `crossOriginIsolated` mode is enabled. See <https://web.dev/cross-origin-isolation-guide/> for more info.

You can also use flag `ort.env.wasm.numThreads` to set the number of threads to be used.

``` highlight
// Set the number of threads to 4
ort.env.wasm.numThreads = 4;

// Disable multi-threading
ort.env.wasm.numThreads = 1;

// Let ONNX Runtime Web decide the number of threads to use
ort.env.wasm.numThreads = 0;
```

See [API reference: env.wasm.numThreads](https://onnxruntime.ai/docs/api/js/interfaces/Env.WebAssemblyFlags.html#numThreads) for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prefer-uint8-quantized-models) Prefer uint8 quantized models

If you are using a quantized model, prefer uint8 quantized models. Avoid float16 models if possible, as float16 is not natively supported by CPU and it is going to be slow.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable-proxy-worker) Enable Proxy Worker

Proxy worker is a feature that allows ONNX Runtime Web to offload the heavy computation to a separate Web Worker. Using the proxy worker cannot improve the performance of the model, but it can improve the responsiveness of the UI to improve the user experience.

If you didn't import ONNX Runtime Web in a Web Worker, and the model takes a while to inference, it is recommended to enable the proxy worker.

``` highlight
// Enable proxy worker
ort.env.wasm.proxy = true;
```

See [API reference: env.wasm.proxy](https://onnxruntime.ai/docs/api/js/interfaces/Env.WebAssemblyFlags.html#proxy) for more details.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#webgpu-tips) WebGPU tips

If you are using the WebGPU execution provider, you can use the following tips to improve the performance of your application:

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#try-using-graph-capture) Try Using graph capture

See [Graph capture](/docs/tutorials/web/env-flags-and-session-options.html#enablegraphcapture) for feature introduction.

if your model has static shapes, and all its computing kernels are running on the WebGPU EP, you can try to enable the graph capture feature, unless you need to feed input data with dynamic shape (eg. transformer based decoder model). Even with static shape input, this feature does not always work for all models. You can try it out and see if it works for your model. If it doesn't work, the model initialization will fail, and you can disable this feature for this model.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#try-using-free-dimension-override) Try using free dimension override

See [Free dimension override](/docs/tutorials/web/env-flags-and-session-options.html#freedimensionoverrides) for feature introduction.

Using free dimension override does not necessarily improve the performance. It's quite model by model. You can try it out and see if it works for your model. If you see performance degradation or larger memory usage, you may disable this feature.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#try-keep-tensor-data-on-gpu) Try keep tensor data on GPU

See [Keep tensor data on GPU (IO binding)](/docs/tutorials/web/ep-webgpu.html#keep-tensor-data-on-gpu-io-binding) for feature introduction.

Keeping tensor data on GPU can avoid unnecessary data transfer between CPU and GPU, which can improve the performance. Try to find out the best way to use this feature for your model.

Please be careful of the [GPU tensor life cycle management](/docs/tutorials/web/ep-webgpu.html#gpu-tensor-life-cycle-management) when using this feature.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#diagnostic-features) Diagnostic features

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#profiling) Profiling

You can enable profiling to get detailed information about the execution of the model. This can be helpful to understand the performance characteristics of the model and to identify potential bottlenecks.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cpu-profiling) CPU profiling

To enable CPU profiling:

- step.1: Specify the `enableProfiling` option in the session options:

  :::: 
  ::: highlight
  ``` highlight
  const mySessionOptions = ;
  ```
  :::
  ::::

  By specifying this option, ONNX Runtime Web will collect CPU profiling data for each run.

- step.2: Get the profiling data after the inference:

  :::: 
  ::: highlight
  ``` highlight
  mySession.endProfiling();
  ```
  :::
  ::::

  After calling `endProfiling()`, the profiling data will be outputted to the console.

  See [In Code Performance Profiling](/docs/performance/tune-performance/profiling-tools.html#in-code-performance-profiling) for how to use the profiling data.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#webgpu-profiling) WebGPU profiling

To enable WebGPU profiling:

- set `ort.env.webgpu.profiling = ` to enable WebGPU profiling. GPU Profiling data will be outputted to the console with prefix `[profiling]`.

- alternatively, you can set `ort.env.webgpu.profiling` with a function to handle the profiling data:

  :::: 
  ::: highlight
  ``` highlight
   ort.env.webgpu.profiling = 
   };
  ```
  :::
  ::::

  See [API reference: env.webgpu.profiling](https://onnxruntime.ai/docs/api/js/interfaces/Env.WebGpuFlags.html#profiling) for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#trace) Trace

You can enable trace by specifying the following flag:

``` highlight
ort.env.trace = true;
```

This feature uses `console.timeStamp` to log the trace data. You can use the browser's performance tool to analyze the trace data.

See [API reference: env.trace](https://onnxruntime.ai/docs/api/js/interfaces/Env-1.html#trace) for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#log-level-verbose) Log level 'verbose'

You can set the log level to 'verbose' to get more detailed logs:

``` highlight
ort.env.logLevel = 'verbose';
```

See [API reference: env.logLevel](https://onnxruntime.ai/docs/api/js/interfaces/Env-1.html#logLevel) for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable-debug-mode) Enable debug mode

You can enable the debug mode by specifying the following flag:

``` highlight
ort.env.debug = true;
```

In debug mode, ONNX Runtime Web will log detailed information about the execution of the model, and also apply some additional checks. Usually you need to use `verbose` log level to see the debug logs.

See [API reference: env.debug](https://onnxruntime.ai/docs/api/js/interfaces/Env-1.html#debug) for more details.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#analyze-the-profiling-data) Analyze the profiling data

This part is under construction.