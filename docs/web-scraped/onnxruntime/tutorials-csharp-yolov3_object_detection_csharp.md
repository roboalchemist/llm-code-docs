# Source: https://onnxruntime.ai/docs/tutorials/csharp/yolov3_object_detection_csharp.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#object-detection-with-yolov3-in-c-using-openvino-execution-provider) Object detection with YOLOv3 in C# using OpenVINO Execution Provider: 

1.  The object detection sample uses YOLOv3 Deep Learning ONNX Model from the ONNX Model Zoo.

2.  The sample involves presenting an image to the ONNX Runtime (RT), which uses the OpenVINO Execution Provider for ONNX RT to run inference on Intel^®^ NCS2 stick (MYRIADX device). The sample uses ImageSharp for image processing and ONNX Runtime OpenVINO EP for inference.

The source code for this sample is available [here](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/c_sharp/OpenVINO_EP/yolov3_object_detection).

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#how-to-build) How to build

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

1.  Install [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1) or higher for you OS (Mac, Windows or Linux).

2.  [The Intel^®^ Distribution of OpenVINO toolkit](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

3.  Use any sample Image as input to the sample.

4.  Download the latest YOLOv3 model from the ONNX Model Zoo. This example was adapted from [ONNX Model Zoo](https://github.com/onnx/models). Download the latest version of the [YOLOv3](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/yolov3) model from here.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-for-openvino-execution-provider) Install ONNX Runtime for OpenVINO Execution Provider

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-steps) Build steps

[build instructions](/docs/build/eps.html#openvino)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#reference-documentation) Reference Documentation

[Documentation](/docs/execution-providers/OpenVINO-ExecutionProvider.html)

To build nuget packages of onnxruntime with openvino flavour

``` highlight
./build.sh --config Release --use_openvino MYRIAD_FP16 --build_shared_lib --build_nuget
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-sample-c-application) Build the sample C# Application

1.  Create a new console project

``` highlight
dotnet new console
```

1.  Install Nuget Packages of Onnxruntime and [ImageSharp](https://www.nuget.org/packages/SixLabors.ImageSharp)

    1.  Open the Visual C# Project file (.csproj) using VS19.
    2.  Right click on project, navigate to manage Nuget Packages.
    3.  Install SixLabors.ImageSharp Package from nuget.org.
    4.  Install Microsoft.ML.OnnxRuntime.Managed and Microsoft.ML.OnnxRuntime.Openvino from your build directory nuget-artifacts.

2.  Compile the sample

``` highlight
dotnet build
```

1.  Run the sample

``` highlight
dotnet run [path-to-model] [path-to-image] [path-to-output-image]
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#references) References:

[fasterrcnn_csharp](https://github.com/microsoft/onnxruntime/blob/gh-pages/docs/tutorials/csharp/fasterrcnn_csharp.md)

[resnet50_csharp](https://github.com/microsoft/onnxruntime/blob/gh-pages/docs/tutorials/csharp/resnet50_csharp.md)