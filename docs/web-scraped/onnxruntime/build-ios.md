# Source: https://onnxruntime.ai/docs/build/ios.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-onnx-runtime-for-ios) Build ONNX Runtime for iOS 

Follow the instructions below to build ONNX Runtime for iOS.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [General Info](#general-info)
- [Prerequisites](#prerequisites)
- [Build Instructions](#build-instructions)
  - [Cross compile for iOS simulator](#cross-compile-for-ios-simulator)
  - [Cross compile for iOS device](#cross-compile-for-ios-device)
  - [CoreML Execution Provider](#coreml-execution-provider)
    - [Build Instructions](#build-instructions-1)
- [Building a Custom iOS Package](#building-a-custom-ios-package)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#general-info) General Info

- iOS Platforms

  The following two platforms are supported

  - iOS device (iPhone, iPad) with arm64 architecture
  - iOS simulator with x86_64 architecture

  The following platforms are *not* supported

  - armv7
  - armv7s
  - i386 architectures
  - tvOS
  - watchOS platforms are not currently supported.

- apple_deploy_target

  Specify the minimum version of the target platform (iOS) on which the target binaries are to be deployed.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

- A Mac computer with latest macOS
- Xcode, https://developer.apple.com/xcode/
- CMake, https://cmake.org/download/
- Python 3, https://www.python.org/downloads/mac-osx/

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions) Build Instructions

Run one of the following build scripts from the ONNX Runtime repository root:

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cross-compile-for-ios-simulator) Cross compile for iOS simulator

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo|MinSizeRel> --use_xcode \
           --ios --apple_sysroot iphonesimulator --osx_arch x86_64 --apple_deploy_target <minimal iOS version>
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cross-compile-for-ios-device) Cross compile for iOS device

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo|MinSizeRel> --use_xcode \
           --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target <minimal iOS version>
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#coreml-execution-provider) CoreML Execution Provider

If you want to use CoreML Execution Provider on iOS or macOS, see [CoreML Execution Provider](../execution-providers/CoreML-ExecutionProvider).

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-1) Build Instructions

CoreML Execution Provider can be built using building commands in [iOS Build instructions](#build-instructions-1) with `--use_coreml`

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#building-a-custom-ios-package) Building a Custom iOS Package

Refer to the documentation for [custom builds](/docs/build/custom.html). In particular, see the section about the [iOS Package](/docs/build/custom.html#ios).