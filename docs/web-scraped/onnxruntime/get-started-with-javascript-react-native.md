# Source: https://onnxruntime.ai/docs/get-started/with-javascript/react-native.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#get-started-with-onnx-runtime-for-react-native) Get started with ONNX Runtime for React Native

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Install](#install)
- [Import](#import)
  - [Enable ONNX Runtime Extensions for React Native](#enable-onnx-runtime-extensions-for-react-native)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install) Install

``` highlight
# install latest release version
npm install onnxruntime-react-native
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#import) Import

``` highlight
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-react-native';
```

``` highlight
// or use CommonJS style import syntax
const ort = require('onnxruntime-react-native');
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable-onnx-runtime-extensions-for-react-native) Enable ONNX Runtime Extensions for React Native

To enable support for [ONNX Runtime Extensions](https://github.com/microsoft/onnxruntime-extensions) in your React Native app, you need to specify the following configuration as a top-level entry (note: usually where the package `name`and `version`fields are) in your project's root directory `package.json` file.

``` highlight
"onnxruntimeExtensionsEnabled": "true"
```