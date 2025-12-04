# Source: https://onnxruntime.ai/docs/tutorials/accelerate-pytorch/resnet-inferencing.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-pytorch-models-on-different-hardware-targets-with-onnx-runtime) Inference PyTorch models on different hardware targets with ONNX Runtime 

As a developer who wants to deploy a PyTorch or ONNX model and maximize performance and hardware flexibility, you can leverage ONNX Runtime to optimally execute your model on your hardware platform.

In this tutorial, you'll learn:

1.  how to use the [PyTorch](https://pytorch.org/vision/stable/models.html) ResNet-50 model for image classification
2.  convert to ONNX, and
3.  deploy to the default CPU, NVIDIA CUDA (GPU), and Intel OpenVINO with ONNX Runtime -- using the same application code to load and execute the inference across hardware platforms.

[ONNX](https://onnx.ai/) was developed as the open-sourced ML model format by Microsoft, Meta, Amazon, and other tech companies to standardize and make it easy to deploy Machine Learning models on various types of hardware. [ONNX Runtime](https://onnxruntime.ai/) was contributed and is maintained by Microsoft to optimize ONNX model performance over frameworks like PyTorch, Tensorflow, and more. When trained with the ImageNet dataset, the ResNet-50 model is commonly used for image classification.

This tutorial demonstrates how to run an ONNX model on CPU, GPU, and Intel hardware with OpenVINO and ONNX Runtime, using [Microsoft Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setup) Setup

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#os-prerequisities) OS Prerequisities

Your environment should have [curl](https://curl.se/download.html) installed.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#device-prerequisites) Device Prerequisites

The onnxruntime-gpu library needs access to a [NVIDIA CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#:~:text=You%20can%20verify%20that%20you,that%20GPU%20is%20CUDA%2Dcapable.) accelerator in your device or compute cluster, but running on just CPU works for the CPU and OpenVINO-CPU demos.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-prerequisites) Inference Prerequisites

Ensure that you have an image to inference on. For this tutorial, we have a "cat.jpg" image located in the same directory as the Notebook files.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#environment-prerequisites) Environment Prerequisites

In Azure Notebook Terminal or AnaConda prompt window, run the following commands to create your 3 environments for CPU, GPU, and/or OpenVINO (differences are bolded).

*CPU*

``` highlight
conda create -n cpu_env_demo python=3.8
conda activate cpu_env_demo
conda install -c anaconda ipykernel
conda install -c conda-forge ipywidgets
python -m ipykernel install --user --name=cpu_env_demo
jupyter notebook
```

*GPU*

``` highlight
conda create -n gpu_env_demo python=3.8
conda activate gpu_env_demo 
conda install -c anaconda ipykernel
conda install -c conda-forge ipywidgets
python -m ipykernel install --user --name=gpu_env_demo 
jupyter notebook
```

*OpenVINO*

``` highlight
conda create -n openvino_env_demo python=3.8
conda activate openvino_env_demo 
conda install -c anaconda ipykernel
conda install -c conda-forge ipywidgets
python -m ipykernel install --user --name=openvino_env_demo
python -m pip install --upgrade pip
pip install openvino
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#library-requirements) Library Requirements

In the first code cell, install the necessary libraries with the following code snippets (differences are bolded).

*CPU + GPU*

``` highlight
import sys

if sys.platform in ['linux', 'win32']: # Linux or Windows
    ! -m pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
else: # Mac
    print("PyTorch 1.9 MacOS Binaries do not support CUDA, install from source instead")

! -m pip install onnxruntime-gpu onnx onnxconverter_common==1.8.1 pillow
```

*OpenVINO*

``` highlight
import sys

if sys.platform in ['linux', 'win32']: # Linux or Windows
    ! -m pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
else: # Mac
    print("PyTorch 1.9 MacOS Binaries do not support CUDA, install from source instead")

! -m pip install onnxruntime-openvino onnx onnxconverter_common==1.8.1 pillow

import openvino.utils as utils
utils.add_openvino_libs_to_path()
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#resnet-50-demo) ResNet-50 Demo

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#environment-setup) Environment Setup

Import necessary libraries to get models and run inference.

``` highlight
from torchvision import models, datasets, transforms as T
import torch
from PIL import Image
import numpy as np
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#load-and-export-pre-trained-resnet-50-model-to-onnx) Load and Export Pre-trained ResNet-50 model to ONNX

Download a pretrained ResNet-50 model from PyTorch and export to ONNX format.

``` highlight
resnet50 = models.resnet50(pretrained=True)

# Download ImageNet labels
!curl -o imagenet_classes.txt https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt

# Read the categories
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]

# Export the model to ONNX
image_height = 224
image_width = 224
x = torch.randn(1, 3, image_height, image_width, requires_grad=True)
torch_out = resnet50(x)
torch.onnx.export(resnet50,                     # model being run
                  x,                            # model input (or a tuple for multiple inputs)
                  "resnet50.onnx",              # where to save the model (can be a file or file-like object)
                  export_params=True,           # store the trained parameter weights inside the model file
                  opset_version=12,             # the ONNX version to export the model to
                  do_constant_folding=True,     # whether to execute constant folding for optimization
                  input_names = ['input'],      # the model's input names
                  output_names = ['output'])    # the model's output names
```

Sample Output:

``` highlight
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 10472 100 10472 0 0 50581 0 --:--:-- --:--:-- --:--:-- 50834
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#set-up-pre-processing-for-inference) Set up Pre-Processing for Inference

Create preprocessing for the image (ex. cat.jpg) you want to use the model to inference on.

``` highlight
# Pre-processing for ResNet-50 Inferencing, from https://pytorch.org/hub/pytorch_vision_resnet/
resnet50.eval()  
filename = 'cat.jpg' # change to your filename

input_image = Image.open(filename)
preprocess = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

# move the input and model to GPU for speed if available
print("GPU Availability: ", torch.cuda.is_available())
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    resnet50.to('cuda')
```

Sample Output:

``` highlight
GPU Availability: False
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-resnet-50-onnx-model-with-onnx-runtime) Inference ResNet-50 ONNX Model with ONNX Runtime

Inference the model with ONNX Runtime by selecting the appropriate Execution Provider for the environment. If your environment uses CPU, uncomment CPUExecutionProvider, if the environment uses NVIDIA CUDA, uncomment CUDAExecutionProvider, and if the environment uses OpenVINOExecutionProvider, uncomment OpenVINOExecutionProvider -- commenting out the other `onnxruntime.InferenceSession` lines of code.

``` highlight
# Inference with ONNX Runtime
import onnxruntime
from onnx import numpy_helper
import time

session_fp32 = onnxruntime.InferenceSession("resnet50.onnx", providers=['CPUExecutionProvider'])
# session_fp32 = onnxruntime.InferenceSession("resnet50.onnx", providers=['CUDAExecutionProvider'])
# session_fp32 = onnxruntime.InferenceSession("resnet50.onnx", providers=['OpenVINOExecutionProvider'])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

latency = []
def run_sample(session, image_file, categories, inputs):
    start = time.time()
    input_arr = inputs.cpu().detach().numpy()
    ort_outputs = session.run([], )[0]
    latency.append(time.time() - start)
    output = ort_outputs.flatten()
    output = softmax(output) # this is optional
    top5_catid = np.argsort(-output)[:5]
    for catid in top5_catid:
        print(categories[catid], output[catid])
    return ort_outputs

ort_output = run_sample(session_fp32, 'cat.jpg', categories, input_batch)
print("ONNX Runtime CPU/GPU/OpenVINO Inference time =  ms".format(format(sum(latency) * 1000 / len(latency), '.2f')))
```

Sample output:

``` highlight
Egyptian cat 0.78605634
tabby 0.117310025
tiger cat 0.020089425
Siamese cat 0.011728076
plastic bag 0.0052174763
ONNX Runtime CPU Inference time = 32.34 ms
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#comparison-with-pytorch) Comparison with PyTorch

Use PyTorch to benchmark against ONNX Runtime CPU and GPU accuracy and latency.

``` highlight
# Inference with OpenVINO
from openvino.runtime import Core

ie = Core()
onnx_model_path = "./resnet50.onnx"
model_onnx = ie.read_model(model=onnx_model_path)
compiled_model_onnx = ie.compile_model(model=model_onnx, device_name="CPU")

# inference
output_layer = next(iter(compiled_model_onnx.outputs))

latency = []
input_arr = input_batch.detach().numpy()
inputs = 
start = time.time()
request = compiled_model_onnx.create_infer_request()
output = request.infer(inputs=inputs)

outputs = request.get_output_tensor(output_layer.index).data
latency.append(time.time() - start)

print("OpenVINO CPU Inference time =  ms".format(format(sum(latency) * 1000 / len(latency), '.2f')))

print("***** Verifying correctness *****")
for i in range(2):
    print('OpenVINO and ONNX Runtime output  are close:'.format(i), np.allclose(ort_output, outputs, rtol=1e-05, atol=1e-04))
```

Sample output:

``` highlight
Egyptian cat 0.7820879
tabby 0.113261245
tiger cat 0.020114701
Siamese cat 0.012514038
plastic bag 0.0056432663
OpenVINO CPU Inference time = 31.83 ms
***** Verifying correctness *****
PyTorch and ONNX Runtime output 0 are close: True
PyTorch and ONNX Runtime output 1 are close: True
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#comparison-with-openvino) Comparison with OpenVINO

Use OpenVINO to benchmark against ONNX Runtime OpenVINO accuracy and latency.

``` highlight
# Inference with OpenVINO
from openvino.runtime import Core

ie = Core()
onnx_model_path = "./resnet50.onnx"
model_onnx = ie.read_model(model=onnx_model_path)
compiled_model_onnx = ie.compile_model(model=model_onnx, device_name="CPU")

# inference
output_layer = next(iter(compiled_model_onnx.outputs))

latency = []
input_arr = input_batch.detach().numpy()
inputs = 
start = time.time()
request = compiled_model_onnx.create_infer_request()
output = request.infer(inputs=inputs)

outputs = request.get_output_tensor(output_layer.index).data
latency.append(time.time() - start)

print("OpenVINO CPU Inference time =  ms".format(format(sum(latency) * 1000 / len(latency), '.2f')))

print("***** Verifying correctness *****")
for i in range(2):
    print('OpenVINO and ONNX Runtime output  are close:'.format(i), np.allclose(ort_output, outputs, rtol=1e-05, atol=1e-04))
```

Sample output:

``` highlight
Egyptian cat 0.7820879
tabby 0.113261245
tiger cat 0.020114701
Siamese cat 0.012514038
plastic bag 0.0056432663
OpenVINO CPU Inference time = 31.83 ms
***** Verifying correctness *****
PyTorch and ONNX Runtime output 0 are close: True
PyTorch and ONNX Runtime output 1 are close: True
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#conclusion) Conclusion

We've demonstrated that ONNX Runtime is an effective way to run your PyTorch or ONNX model on CPU, NVIDIA CUDA (GPU), and Intel OpenVINO (Mobile). ONNX Runtime enables deployment to more types of hardware that can be found on [Execution Providers](https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html). We'd love to hear your feedback by participating in our ONNX Runtime [Github repo](https://github.com/microsoft/onnxruntime).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#video-demonstration) Video Demonstration

Watch the video [here](https://www.youtube.com/embed/sbc3Bmv2Kwo?feature=oembed) for more explanation on ResNet-50 Deployment and Flexible Inferencing with the step by step guide.