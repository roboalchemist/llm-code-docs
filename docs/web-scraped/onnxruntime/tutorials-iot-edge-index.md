# Source: https://onnxruntime.ai/docs/tutorials/iot-edge/

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#deploy-ml-models-on-iot-and-edge-devices) Deploy ML Models on IoT and Edge Devices

ONNX Runtime allows you to deploy to many IoT and Edge devices to support a variety of use cases. There are packages available to support many board architectures [included when you install ONNX Runtime](https://pypi.org/project/onnxruntime/#files). Below are some considerations when deciding if deploying on-device is right for your use case.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#benefits-and-limitations-to-doing-on-device-inference) Benefits and limitations to doing on-device inference

- It's faster. That's right, you can cut inferencing time down when inferencing is done right on the client for models that are optimized to work on less powerful hardware.
- It's safer and helps with privacy. Since the data never leaves the device for inferencing, it is a safer method of doing inferencing.
- It works offline. If you lose internet connection, the model will still be able to inference.
- It's cheaper. You can reduce cloud serving costs by offloading inference to the device.
- Model size limitation. If you want to deploy on device you need to have a model that is optimized and small enough to run on the device.
- Hardware processing limitation. The model needs to be optimized to run on less powerful hardware.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#examples) Examples

- [Raspberry Pi on Device inference](/docs/tutorials/iot-edge/rasp-pi-cv.html)
- [Jetson Nano embedded device: Fast model inferencing](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-arm64.md)
- [Intel VPU edge device with OpenVINO: Deploy small quantized model](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-OpenVINO.md)

------------------------------------------------------------------------

## Table of contents 

- [IoT Deployment on Raspberry Pi](/docs/tutorials/iot-edge/rasp-pi-cv.html)