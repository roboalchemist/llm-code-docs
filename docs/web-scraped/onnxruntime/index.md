# Source: https://onnxruntime.ai/docs/

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#welcome-to-onnx-runtime) Welcome to ONNX Runtime 

ONNX Runtime is a cross-platform machine-learning model accelerator, with a flexible interface to integrate hardware-specific libraries. ONNX Runtime can be used with models from PyTorch, Tensorflow/Keras, TFLite, scikit-learn, and other frameworks.

# An error occurred. 

Unable to execute JavaScript.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#how-to-use-onnx-runtime) How to use ONNX Runtime

  --------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
  [ [Get started with ORT](./get-started) ]                                                      [ [API Docs](./api) ]
  [ [Tutorials](./tutorials) ]                                                                         [ [Ecosystem](./ecosystem) ]
  [[ONNX Runtime YouTube](https://www.youtube.com/channel/UC_SJk17KdRvDulXz-nc1uFg/featured) ]    
  --------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contribute-and-customize) Contribute and Customize

  ---------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
  [ [Build ORT Packages](./build) ]   [[ONNX Runtime GitHub](https://github.com/microsoft/onnxruntime) ]
  ---------------------------------------------------------------------- -------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#quickstart-template) QuickStart Template

  ------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  [ [ORT Web JavaScript Site Template](https://github.com/microsoft/onnxruntime-nextjs-template) ]   [ [ORT C# Console App Template](https://github.com/microsoft/onnxruntime-csharp-cv-template) ]
  ------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-for-inferencing) ONNX Runtime for Inferencing

ONNX Runtime Inference powers machine learning models in key Microsoft products and services across Office, Azure, Bing, as well as dozens of community projects.

Examples use cases for ONNX Runtime Inferencing include:

- Improve inference performance for a wide variety of ML models
- Run on different hardware and operating systems
- Train in Python but deploy into a C#/C++/Java app
- Train and perform inference with models created in different frameworks

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#how-it-works) How it works 

The premise is simple.

1.  **Get a model.** This can be trained from any framework that supports export/conversion to ONNX format. See the [tutorials](./tutorials) for some of the popular frameworks/libraries.
2.  **Load and run the model with ONNX Runtime.** See the [basic tutorials](./tutorials/api-basics) for running models in different languages.
3.  ***(Optional)* Tune performance using various runtime configurations or hardware accelerators.** There are lots of options here - see the [Performance section](./performance) as a starting point.

Even without step 3, ONNX Runtime will often provide performance improvements compared to the original framework.

ONNX Runtime applies a number of graph optimizations on the model graph then partitions it into subgraphs based on available hardware-specific accelerators. Optimized computation kernels in core ONNX Runtime provide performance improvements and assigned subgraphs benefit from further acceleration from each [Execution Provider](./execution-providers).

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-for-training) ONNX Runtime for Training

- [Large Model Training](/docs/get-started/training-pytorch.html)
- [On-Device Training](/docs/get-started/training-on-device.html)