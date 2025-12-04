# Source: https://onnxruntime.ai/docs/get-started/with-obj-c.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#get-started-with-ort-for-objective-c) Get started with ORT for Objective-C 

ONNX Runtime provides an Objective-C API for running ONNX models on iOS devices.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Supported Versions](#supported-versions)
- [Builds](#builds)
- [Swift Usage](#swift-usage)
- [API Reference](#api-reference)
- [Samples](#samples)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-versions) Supported Versions

See iOS [compatibility info](/docs/reference/compatibility.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#builds) Builds

The artifacts are published to CocoaPods.

  Artifact           Description      Supported Platforms
  ------------------ ---------------- ---------------------
  onnxruntime-objc   CPU and CoreML   iOS

Refer to the [installation instructions](/docs/install/#install-on-ios).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#swift-usage) Swift Usage

The Objective-C API can be called from Swift code. To enable this, use a bridging header (more info [here](https://developer.apple.com/documentation/swift/importing-objective-c-into-swift)) that imports the ORT Objective-C API header.

``` highlight
// In the bridging header, import the ORT Objective-C API header.
#import <onnxruntime.h>
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#api-reference) API Reference

[Objective-C API Reference](/docs/api/objectivec/index.html)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#samples) Samples

See the iOS examples [here](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile).