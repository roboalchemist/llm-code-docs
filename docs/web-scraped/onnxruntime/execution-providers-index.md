# Source: https://onnxruntime.ai/docs/execution-providers/

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-execution-providers) ONNX Runtime Execution Providers 

ONNX Runtime works with different hardware acceleration libraries through its extensible **Execution Providers** (EP) framework to optimally execute the ONNX models on the hardware platform. This interface enables flexibility for the AP application developer to deploy their ONNX models in different environments in the cloud and the edge and optimize the execution by taking advantage of the compute capabilities of the platform.

![Executing ONNX models across different HW environments](https://www.onnxruntime.ai/images/ONNX_Runtime_EP1.png)

ONNX Runtime works with the execution provider(s) using the `GetCapability()` interface to allocate specific nodes or sub-graphs for execution by the EP library in supported hardware. The EP libraries that are pre-installed in the execution environment process and execute the ONNX sub-graph on the hardware. This architecture abstracts out the details of the hardware specific libraries that are essential to optimize the execution of deep neural networks across hardware platforms like CPU, GPU, FPGA or specialized NPUs.

![ONNX Runtime GetCapability()](https://www.onnxruntime.ai/images/ONNX_Runtime_EP3.png)

ONNX Runtime supports many different execution providers today. Some of the EPs are in production for live service, while others are released in preview to enable developers to develop and customize their application using the different options.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#summary-of-supported-execution-providers) Summary of supported Execution Providers

  CPU                                                                                            GPU                                                                            IoT/Edge/Mobile                                                                                                Other
  ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------
  Default CPU                                                                                    [NVIDIA CUDA](/docs/execution-providers/CUDA-ExecutionProvider.html)           [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html)                                    [Rockchip NPU](/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html) (*preview*)
  [Intel DNNL](/docs/execution-providers/oneDNN-ExecutionProvider.html)                          [NVIDIA TensorRT](/docs/execution-providers/TensorRT-ExecutionProvider.html)   [Arm Compute Library](/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html) (*preview*)   [Xilinx Vitis-AI](/docs/execution-providers/Vitis-AI-ExecutionProvider.html) (*preview*)
  [TVM](/docs/execution-providers/community-maintained/TVM-ExecutionProvider.html) (*preview*)   [DirectML](/docs/execution-providers/DirectML-ExecutionProvider.html)          [Android Neural Networks API](/docs/execution-providers/NNAPI-ExecutionProvider.html)                          [Huawei CANN](/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html) (*preview*)
  [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html)                    [AMD MIGraphX](/docs/execution-providers/MIGraphX-ExecutionProvider.html)      [Arm NN](/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html) (*preview*)              [AZURE](/docs/execution-providers/Azure-ExecutionProvider.html) (*preview*)
  [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html)                            [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html)    [CoreML](/docs/execution-providers/CoreML-ExecutionProvider.html) (*preview*)                                   
  [AMD ROCm](/docs/execution-providers/ROCm-ExecutionProvider.html)(*deprecated*)                [Qualcomm QNN](/docs/execution-providers/QNN-ExecutionProvider.html)           [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html)                                             

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-an-execution-provider) Add an Execution Provider

Developers of specialized HW acceleration solutions can integrate with ONNX Runtime to execute ONNX models on their stack. To create an EP to interface with ONNX Runtime you must first identify a unique name for the EP. See: [Add a new execution provider](/docs/execution-providers/add-execution-provider.html) for detailed instructions.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-onnx-runtime-package-with-eps) Build ONNX Runtime package with EPs

The ONNX Runtime package can be built with any combination of the EPs along with the default CPU execution provider. **Note** that if multiple EPs are combined into the same ONNX Runtime package then all the dependent libraries must be present in the execution environment. The steps for producing the ONNX Runtime package with different EPs is documented [here](/docs/build/inferencing.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#apis-for-execution-provider) APIs for Execution Provider

The same ONNX Runtime API is used across all EPs. This provides the consistent interface for applications to run with different HW acceleration platforms. The APIs to set EP options are available across Python, C/C++/C#, Java and node.js.

**Note** we are updating our API support to get parity across all language binding and will update specifics here.

``` highlight
`get_providers`: Return list of registered execution providers.
`get_provider_options`: Return the registered execution providers' configurations.
`set_providers`: Register the given list of execution providers. The underlying session is re-created. 
    The list of providers is ordered by Priority. For example ['CUDAExecutionProvider', 'CPUExecutionProvider']
    means execute a node using CUDAExecutionProvider if capable, otherwise execute using CPUExecutionProvider.
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-execution-providers) Use Execution Providers

``` highlight
import onnxruntime as rt

#define the priority order for the execution providers
# prefer CUDA Execution Provider over CPU Execution Provider
EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']

# initialize the model.onnx
sess = rt.InferenceSession("model.onnx", providers=EP_list)

# get the outputs metadata as a list of :class:`onnxruntime.NodeArg`
output_name = sess.get_outputs()[0].name

# get the inputs metadata as a list of :class:`onnxruntime.NodeArg`
input_name = sess.get_inputs()[0].name

# inference run using image_data as the input to the model 
detections = sess.run([output_name], )[0]

print("Output shape:", detections.shape)

# Process the image to mark the inference points 
image = post.image_postprocess(original_image, input_size, detections)
image = Image.fromarray(image)
image.save("kite-with-objects.jpg")

# Update EP priority to only CPUExecutionProvider
sess.set_providers(['CPUExecutionProvider'])

cpu_detection = sess.run(...)
```

------------------------------------------------------------------------

## Table of contents 

- [NVIDIA - CUDA](/docs/execution-providers/CUDA-ExecutionProvider.html)
- [NVIDIA - TensorRT](/docs/execution-providers/TensorRT-ExecutionProvider.html)
- [NVIDIA - TensorRT RTX](/docs/execution-providers/TensorRTRTX-ExecutionProvider.html)
- [Intel - OpenVINO™](/docs/execution-providers/OpenVINO-ExecutionProvider.html)
- [Intel - oneDNN](/docs/execution-providers/oneDNN-ExecutionProvider.html)
- [Windows - DirectML](/docs/execution-providers/DirectML-ExecutionProvider.html)
- [Qualcomm - QNN](/docs/execution-providers/QNN-ExecutionProvider.html)
- [Android - NNAPI](/docs/execution-providers/NNAPI-ExecutionProvider.html)
- [Apple - CoreML](/docs/execution-providers/CoreML-ExecutionProvider.html)
- [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html)
- [AMD - ROCm](/docs/execution-providers/ROCm-ExecutionProvider.html)
- [AMD - MIGraphX](/docs/execution-providers/MIGraphX-ExecutionProvider.html)
- [AMD - Vitis AI](/docs/execution-providers/Vitis-AI-ExecutionProvider.html)
- [Cloud - Azure](/docs/execution-providers/Azure-ExecutionProvider.html)
- [Community-maintained](/docs/execution-providers/community-maintained/)
- [Add a new provider](/docs/execution-providers/add-execution-provider.html)
- [EP Context Design](/docs/execution-providers/EP-Context-Design.html)
- [Plugin EP libraries](/docs/execution-providers/plugin-ep-libraries.html)