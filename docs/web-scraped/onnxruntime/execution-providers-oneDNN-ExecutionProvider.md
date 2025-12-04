# Source: https://onnxruntime.ai/docs/execution-providers/oneDNN-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onednn-execution-provider) oneDNN Execution Provider 

*Formerly "DNNL"*

Accelerate performance of ONNX Runtime using Intel® Math Kernel Library for Deep Neural Networks (Intel® DNNL) optimized primitives with the Intel oneDNN execution provider.

Intel® oneAPI Deep Neural Network Library is an open-source performance library for deep-learning applications. The library accelerates deep-learning applications and frameworks on Intel® architecture and Intel® Processor Graphics Architecture. Intel DNNL contains vectorized and threaded building blocks that you can use to implement deep neural networks (DNN) with C and C++ interfaces.

The oneDNN Execution Provider (EP) for ONNX Runtime is developed by a partnership between Intel and Microsoft.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Build](#build)
- [Usage](#usage)
  - [C/C++](#cc)
  - [Python](#python)
  - [Subgraph Optimization](#subgraph-optimization)
    - [Subgraph (IR) Internal Representation](#subgraph-ir-internal-representation)
    - [Subgraph Classes](#subgraph-classes)
    - [Subgraph Execution](#subgraph-execution)
- [Support Coverage](#support-coverage)
- [Additional Resources](#additional-resources)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build) Build

For build instructions, please see the [BUILD page](/docs/build/eps.html#onednn).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#usage) Usage

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cc) C/C++

The DNNLExecutionProvider execution provider needs to be registered with ONNX Runtime to enable in the inference session.

``` highlight
Ort::Env env = Ort::Env;
Ort::SessionOptions sf;
bool enable_cpu_mem_arena = true;
Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_Dnnl(sf, enable_cpu_mem_arena));
```

The C API details are [here](/docs/get-started/with-c.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python) Python

When using the python wheel from the ONNX Runtime built with DNNL execution provider, it will be automatically prioritized over the CPU execution provider. Python APIs details are [here](https://aka.ms/onnxruntime-python).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#subgraph-optimization) Subgraph Optimization

DNNL uses blocked layout (example: nhwc with channels blocked by 16 -- nChw16c) to take advantage of vector operations using AVX512. To get best performance, we avoid reorders (example. Nchw16c to nchw) and propagate blocked layout to next primitive.

Subgraph optimization achieves this in the following steps.

1.  Parses ONNX Runtime graph and creates an Internal Representation of subgraph..
2.  Subgraph Operator (DnnlFunKernel) iterates through DNNL nodes and creates a vector DNNL Kernels
3.  Compute Function of DnnlFunKernel iterates and binds data to DNNL primitives in the vector and submits vector for execution.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#subgraph-ir-internal-representation) Subgraph (IR) Internal Representation

DnnlExecutionProvider::GetCapability() parses ONNX model graph and creates IR (Internal Representation) of subgraphs of DNNL operators. Each subgraph contains a vector DnnlNodes, inputs, outputs and attributes for all its DnnlNodes. There can be attributes of same name. So, we prefix attribute names with Node name and its index. Unique id for subgraph is set as an attribute.

DnnlNode has an index to its inputs and outputs and pointer to its parent nodes. DnnlNode directly reads blocked memory from its parent to avoid data reordering.

![MKL-DNN Node](/images/mkl-dnn_node.png)

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#subgraph-classes) Subgraph Classes

Primitive like DnnlConv, DnnlPool, etc are derived from DnnlKernel base class.

The following UML diagram captures Subgraph classes.

![MKL-DNN subgraph](/images/mkl-dnn_subgraph.png)

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#subgraph-execution) Subgraph Execution

DnnlExecutionProvicer::Compute() function creates DnnlFuncKernel and call it's Compute Function.

DnnlFuncKernel::Compute function creates SubgraphPrimitve pool and add the object to a map.

SubgraphPrimitve constructor calls the following member functions

``` highlight
SubgraphPrimitve::CreatePrimitives()
    for (auto& mklnode : mklnodes)  else if (mklnode.name == "BatchNormalization-Relu")  else if (mklnode.name == "MaxPool")  
      .
      .
      .
```

In CreatePrimitives method, we iterate DnnlNodes and creates DnnlKernel objects and add DNNL primitive to a vector. It also reads attributes. This is done only once, at first iteration.

``` highlight
SubgraphPrimitve::Compute()
   for (auto& kernel : kernels) 
    stream->submit(net);
```

In SubgraphPrimitve::Compute() method, we iterate thru Dnnl Kernels and bind input data. Then we submit the vector of Primitives to DNNL stream.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#support-coverage) Support Coverage

**Supported OS**

- Ubuntu 16.04
- Windows 10
- Mac OS X

**Supported backend**

- CPU

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#additional-resources) Additional Resources

- [oneDNN documentation](https://oneapi-src.github.io/oneDNN/index.html)