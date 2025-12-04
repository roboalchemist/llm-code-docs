# Source: https://onnxruntime.ai/docs/get-started/with-javascript/node.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#get-started-with-onnx-runtime-nodejs-binding) Get started with ONNX Runtime Node.js binding 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Install](#install)
- [Import](#import)
- [Examples](#examples)
- [Supported Versions](#supported-versions)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install) Install

``` highlight
# install latest release version
npm install onnxruntime-node
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#import) Import

``` highlight
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-node';
```

``` highlight
// or use CommonJS style import syntax
const ort = require('onnxruntime-node');
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#examples) Examples

- Follow the [Quick Start](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/quick-start_onnxruntime-node) instructions for ONNX Runtime Node.js binding.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-versions) Supported Versions

The following table lists the supported versions of ONNX Runtime Node.js binding provided with pre-built binaries.

  EPs/Platforms   Windows x64   Windows arm64   Linux x64   Linux arm64   MacOS x64   MacOS arm64
  --------------- ------------- --------------- ----------- ------------- ----------- -------------
  CPU             ✔️            ✔️              ✔️          ✔️            ✔️          ✔️
  DirectML        ✔️            ✔️              ❌          ❌            ❌          ❌
  CUDA            ❌            ❌              ✔️^\[1\]^   ❌            ❌          ❌

- \[1\]: CUDA v11.8.

For platforms not on the list or want a custom build, you can [build Node.js binding from source](/docs/build/inferencing.html#apis-and-language-bindings) and consume using `npm install <onnxruntime_repo_root>/js/node/`.