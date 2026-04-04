# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html

Title: Triton Inference Server In-Process Python API [BETA] — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html

Markdown Content:
Starting with release 24.01 Triton Inference Server will include a Python package enabling developers to embed Triton Inference Server instances in their Python applications. The in-process Python API is designed to match the functionality of the in-process C API while providing a higher level abstraction. At its core the API relies on a 1:1 python binding of the C API and provides all the flexibility and power of the C API with a simpler to use interface.

> [!Note] As the API is in BETA please expect some changes as we test out different features and get feedback. All feedback is weclome and we look forward to hearing from you!

| [Requirements](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#requirements) | [Installation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#installation) | [Hello World](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#hello-world) | [Stable Diffusion](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#stable-diffusion) | [Ray Serve Deployment](https://github.com/triton-inference-server/tutorials/blob/main/Triton_Inference_Server_Python_API/examples/rayserve) |

Requirements[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#requirements "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following instructions require a linux system with Docker installed. For CUDA support, make sure your CUDA driver meets the requirements in “NVIDIA Driver” section of Deep Learning Framework support matrix: https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html

Installation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#installation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The tutorial and Python API package are designed to be installed and run within the `nvcr.io/nvidia/tritonserver:24.08-py3` docker image.

A set of convenience scripts are provided to create a docker image based on the `nvcr.io/nvidia/tritonserver:24.08-py3` image with the Python API installed plus additional dependencies required for the examples.

### Triton Inference Server 24.08 + Python API[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#triton-inference-server-24-08-python-api "Link to this heading")

#### Clone Repository[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#clone-repository "Link to this heading")

git clone https://github.com/triton-inference-server/tutorials.git
cd tutorials/Triton_Inference_Server_Python_API

#### Build `triton-python-api:r24.08` Image[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#build-triton-python-api-r24-08-image "Link to this heading")

./build.sh

#### Supported Backends[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#supported-backends "Link to this heading")

The built image includes all the backends shipped by default in the tritonserver `nvcr.io/nvidia/tritonserver:24.08-py3` container.

dali  fil  identity  onnxruntime  openvino  python  pytorch  repeat  square  tensorflow  tensorrt

#### Included Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#included-models "Link to this heading")

The `default` build includes an `identity` model that can be used for exercising basic operations including sending input tensors of different data types. The `identity` model copies provided inputs of `shape [-1, -1]` to outputs of shape `[-1, -1]`. Inputs are named `data_type_input` and outputs are named `data_type_output` (e.g. `string_input`, `string_output`, `fp16_input`, `fp16_output`).

Hello World[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#hello-world "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Start `triton-python-api:r24.08` Container[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#start-triton-python-api-r24-08-container "Link to this heading")

The following command starts a container and volume mounts the current directory as `workspace`.

./run.sh

### Enter Python Shell[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#enter-python-shell "Link to this heading")

python3

### Create and Start a Server Instance[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#create-and-start-a-server-instance "Link to this heading")

import tritonserver

server = tritonserver.Server(model_repository="/workspace/identity-models")
server.start()

### List Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#list-models "Link to this heading")

server.models()

#### Example Output[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#example-output "Link to this heading")

`server.models()` returns a dictionary of the available models with their current state.

{('identity', 1): {'name': 'identity', 'version': 1, 'state': 'READY'}}

### Send an Inference Request[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#send-an-inference-request "Link to this heading")

model = server.model("identity")
responses = model.infer(inputs={"string_input":[["hello world!"]]})

### Iterate through Responses[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#iterate-through-responses "Link to this heading")

`model.infer()` returns an iterator that can be used to process the results of an inference request.

for response in responses:
    print(response.outputs["string_output"].to_string_array())

#### Example Output[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id1 "Link to this heading")

[['hello world!']]

Stable Diffusion[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#stable-diffusion "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This example is based on the [Popular_Models_Guide/StableDiffusion](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion) tutorial.

### Build `triton-python-api:r24.08-diffusion` Image and Stable Diffusion Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#build-triton-python-api-r24-08-diffusion-image-and-stable-diffusion-models "Link to this heading")

Please note the following command will take many minutes depending on your hardware configuration and network connection.

 ./build.sh --framework diffusion --build-models

### Supported Backends[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id2 "Link to this heading")

The built image includes all the backends shipped by default in the tritonserver `nvcr.io/nvidia/tritonserver:24.08-py3` container.

dali  fil  identity  onnxruntime  openvino  python  pytorch  repeat  square  tensorflow  tensorrt

### Included Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id3 "Link to this heading")

The `diffusion` build includes a `stable_diffustion` pipeline that takes a text prompt and returns a generated image. For more details on the models and pipeline please see the [Popular_Models_Guide/StableDiffusion](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion) tutorial.

### Start Container[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#start-container "Link to this heading")

The following command starts a container and volume mounts the current directory as `workspace`.

./run.sh --framework diffusion

### Enter Python Shell[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id4 "Link to this heading")

python3

### Create and Start a Server Instance[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id5 "Link to this heading")

import tritonserver
import numpy
from PIL import Image

server = tritonserver.Server(model_repository="/workspace/diffusion-models")
server.start()

### List Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id6 "Link to this heading")

server.models()

#### Example Output[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id7 "Link to this heading")

{('stable_diffusion_1_5', 1): {'name': 'stable_diffusion_1_5', 'version': 1, 'state': 'READY'}, ('stable_diffusion_xl', 1): {'name': 'stable_diffusion_xl', 'version': 1, 'state': 'READY'}}

### Send an Inference Request[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id8 "Link to this heading")

model = server.model("stable_diffusion_xl")
responses = model.infer(inputs={"prompt":[["butterfly in new york, realistic, 4k, photograph"]]})

### Iterate through Responses and save image[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#iterate-through-responses-and-save-image "Link to this heading")

for response in responses:
	generated_image = numpy.from_dlpack(response.outputs["generated_image"])
	generated_image = generated_image.squeeze().astype(numpy.uint8)
	image_ = Image.fromarray(generated_image)
	image_.save("sample_generated_image.jpg")

#### Example Output[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html#id9 "Link to this heading")

![Image 1: sample_generated_image](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_images/sample_generated_image.jpg)
