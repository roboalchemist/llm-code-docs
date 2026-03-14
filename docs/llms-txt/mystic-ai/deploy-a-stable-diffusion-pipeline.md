# Source: https://docs.mystic.ai/docs/deploy-a-stable-diffusion-pipeline.md

# Deploy Stable Diffusion

How to deploy a pre-trained HugginFace stable diffusion pipeline to Mystic.

HuggingFace (HF) provides a really simple way to use some of the best models from the open-source ML sphere. In this guide, we'll build out a pipeline around a HF `diffusers` model. The logic followed here can be replicated for almost *any* of the \~500,000 models available on HF. We selected `[runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)` out of the [many available ](https://huggingface.co/models?pipeline_tag=text-to-image\&sort=trending\&search=stable+diffusion) pre-trained stable diffusion HF pipelines.

The `runwayml/stable-diffusion-v1-5` pipeline is a Text-to-Image model based on the Stable Diffusion technique, which is a method used for generating images from textual descriptions. It's a powerful tool that has been used in a variety of applications, from AI art generation to creating images from QR codes. The Stable Diffusion technique is a type of generative model that works by simulating a diffusion process. This process starts with a random noise image and gradually transforms it into an image that resembles the input text. The model learns to control this diffusion process to generate high-quality images that match the input text as closely as possible.

The `runwayml/stable-diffusion-v1-5` pipeline is one of the most popular Stable Diffusion models on Hugging Face. It has been used in a wide range of projects, such as the HuggingGPT, QR code AI art generator, ControlNet, and many others. This popularity is due to the high quality of the images it generates and its ease of use.

**NOTE: This is a walkthrough, so many of the below code snippets are mere chunks of a larger script. If you're skimming or just want to see code, then skip to the conclusion where you'll find the complete script.**

# Getting started with HuggingFace `diffusers`

Once you've installed `diffusers`, it's really simple to initialise a model and start running inference on it. We'll use a [pre-trained stable diffusion model](https://huggingface.co/runwayml/stable-diffusion-v1-5).\
It is a text to image model, which means it will take in an input sentence/prompt like *A photo of an astronaut riding a horse on mars*, and output an image related to the input prompt.\
HuggingFace makes it *very* easy to load any pre-trained stable diffusion pipeline and to use it in inference, by interfacing with the `StableDiffusionPipeline` module.

> 🚧 A HuggingFace `pipeline` is not the same as a Mystic `pipeline`
>
> Both HuggingFace and Mystic use the same word 'pipeline' to mean 'a set of processing steps which convert an input to an output'. Later in this guide, we're going to embed this model within a Mystic 'pipeline'.

Getting started using `runwayml/stable-diffusion-v1-5` for inference, is as simple as:

```python
from diffusers import StableDiffusionPipeline
from PIL.Image import Image

MODEL_ID = "runwayml/stable-diffusion-v1-5"

# Load the HF pipeline
model = StableDiffusionPipeline.from_pretrained(MODEL_ID)

# The input prompt
prompt = "A photo of an astronaut riding a horse on mars"

# Generate an image from the prompt
output_image: Image = model(prompt).images[0]

# Save the image to a local file
image.save("astronaut_rides_horse.png")

```

Running the Python script will take a while but you should eventually see an image saved to a local file.\
What just happened here? We instantiated a pre-trained HF pipeline, and just by passing a prompt string we made a prediction, which returned a list of `PIL` images. We then saved the first image to a local file.

Internally, the HF pipeline assembles the model on CPU, downloads the `runwayml/stable-diffusion-v1-5` weights, and then loads them into the model. **If you have a GPU attached**, you can ensure the prediction takes place on your GPU instead, by creating a `torch.device` and moving the model (tensor) *to* that device:

```python
...
import torch

# Create a GPU device if it is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the HF pipeline
sd_pipeline = StableDiffusionPipeline.from_pretrained(MODEL_ID).to(
    device
)
...

```

Here we're taking advantage of the neat `.to()` method provided by PyTorch to send models, inputs, and other data to specific devices.

# Building a pipeline container

Now that we have a HF model working for local inference, it's time to start laying the ground to offload that work to Mystic. In order for our Python code to run on the Mystic servers, we will need to package it into a deployable unit and upload it. This is achieved by creating a docker image of our pipeline, with the help of the Mystic SDK.\
But before creating this image, let's actually write out the source code for the pipeline.

## The core model

In order to organise our code, we will create a wrapper class around the HF model.\
In this class we'll define how the HF model should be loaded, how the inputs and outputs to the model should be processed and of course, the inference method itself.\
Create a `sd_pipeline.py` file with the following code:

```python Python
import typing as t
from pathlib import Path

from PIL.Image import Image
from pipeline import File, Pipeline, Variable, entity, pipe
from pipeline.objects.graph import InputField, InputSchema

HF_MODEL_ID = "runwayml/stable-diffusion-v1-5"


class ModelKwargs(InputSchema):
    num_images_per_prompt: int = InputField(
        title="num_images_per_prompt",
        description="The number of images to generate per prompt.",
        default=1,
        optional=True,
    )
    height: int = InputField(
        title="height",
        description="The height in pixels of the generated image.",
        default=512,
        optional=True,
        multiple_of=64,
        ge=64,
    )
    width: int = InputField(
        title="width",
        description="The width in pixels of the generated image.",
        default=512,
        optional=True,
        multiple_of=64,
        ge=64,
    )
    num_inference_steps: int = InputField(
        title="num_inference_steps",
        description=(
            "The number of denoising steps. More denoising steps "
            "usually lead to a higher quality image at the expense "
            "of slower inference."
        ),
        default=50,
        optional=True,
    )


@entity
class StableDiffusionModel:
    def __init__(self) -> None:
        self.model = None
        self.device = None

    @pipe(run_once=True, on_startup=True)
    def load(self) -> None:
        """
        Load the HF model into memory"""
        import torch
        from diffusers import StableDiffusionPipeline

        device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
        self.model = StableDiffusionPipeline.from_pretrained(HF_MODEL_ID)
        self.model.to(device)

    @pipe
    def predict(self, prompt: str, model_kwargs: ModelKwargs) -> t.List[Image]:
        """
        Generates a list of PIL images.
        """
        return self.model(prompt=prompt, **model_kwargs.to_dict()).images

    @pipe
    def postprocess(self, images: t.List[Image]) -> t.List[File]:
        """
        Creates a list of Files from the `PIL` images.
        """
        output_images = []
        for i, image in enumerate(images):
            path = Path(f"/tmp/sd/image-{i}.jpg")
            path.parent.mkdir(parents=True, exist_ok=True)
            image.save(str(path))
            output_images.append(File(path=path, allow_out_of_context_creation=True))
        return output_images
```

OK that may seem like a bit of a mouthful, but most of the code here is actually pretty straight-forward.

### Input model kwargs

First, notice that we have defined an `ModelKwargs` class which inherits from `InputSchema`. This is useful for passing additional runtime parameters to the model, in addition to the required `string` prompt input. Similar to how `pydantic` works, each `InputField` will be validated at runtime and a `HTTP 422` status code will be returned if the runtime inputs do not conform to the schema.\
There are a number of other optional keyword arguments we might want to supply to our model at inference. For instance, the number of images per prompt, the dimensions of the images and so on. You can [see all the available model parameters](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img#diffusers.StableDiffusionPipeline.__call__) for a HF stable diffusion pipeline. Feel free to include any additional ones in your own deployments. Notice further that the typical `pydantic` `Field` [constraints](https://docs.pydantic.dev/latest/concepts/fields/#numeric-constraints), such as `multiple_of` or `ge` are also available to you.

### `entity` and `pipe` decorators

Next, notice that the methods of the `entity` class have `pipe` decorators. These ensure that the actual runtime values of any `Variable`, `InputSchema` or `File` objects will be passed to these methods when we call them from within the pipeline graph (defined below), rather than the bare objects themselves.\
We've implemented the following methods:

* `load` handles the instantiation of the model and sending it to a GPU (more on this below).

* `predict` passes our inputs to the stable diffusion model and generates a list of `PIL` images.

* `postprocess` creates `File` objects from the generated `PIL` images. When `File` objects are are output from a pipeline, they will be uploaded to Mystic storage behind the scenes and an external URL will be returned in the output instead of the raw file bytes.

### Set the `load` function to run only on startup

One of the great features of a platform like Mystic is that it can *cache your models on GPU* so that you don't have to experience cold starts on every request.\
In a later section, we will be creating a blueprint for running the pipeline where the `load` method will be called.\
Every request to your pipeline's endpoint will follow this blueprint from top to bottom.\
However, we only want to execute the `load` method if the model is not already cached.

Thus we need to tell the blueprint to only call the `load` method once when the pipeline loads, and not again for the duration of the pipeline's time within GPU cache. Fortunately, there's a really easy way to do exactly that, and unlock all the performance benefits that it entails. Just tag the `pipe` decorator on the `load` method with the following two arguments:

```python
...
@pipe(run_once=True, on_startup=True)
def load(self) -> bool:
  ...
```

Now, even though we call `model.load()` within the pipeline, we can be sure it will only run when the pipeline caches, and not again. Inference should be *even* faster as a result!

> 📘 Your model stays cached until another replaces it
>
> Mystic automatically stores your model in GPU cache after it has been deployed, so that future inference requests can skip the cold start. It will remain cached until another pipeline 'kicks it off' so that the platform can serve all users fairly. However, if your traffic is regular and sufficiently high-volume then your pipeline will remain \~permanently cached while you only pay for inference time.

### Post-processing

You may have noticed that the images generated by the HF model are native Python `PIL` objects.\
Hence, we cannot return these directly from the pipeline as these are not natively JSON-serializable.\
We could, for instance `base64` encode these images and return that from the pipeline.\
However, we make use of the `File` object to ensure that the images are saved to `Mystic` storage.\
This ensures that your images are persisted and can be accessed any time through an external URL.\
All we need to do is output `File` objects from the pipeline and `Mystic` will automatically handle saving these files to storage under the hood any time your pipeline is run.

## The pipeline graph

Next we'll create a `pipeline` blueprint.\
This blueprint is essentially a computational graph representing a set of instructions for what should happen when a request is made to your inference endpoint.\
In the body of your request, you will typically be passing some payload, which includes e.g. `prompt`, `num_inference_steps` etc.\
This payload should then be passed as input variables to the pipeline at runtime and fed into operations, whose outputs are in turn fed into further operations until we arrive at the output of the pipeline itself.

To build the pipeline, you need to create a `Pipeline` object and use a **context manager**, as below:

```python Python
with Pipeline() as builder:
    # Define inputs to the pipeline
    prompt = Variable(
        str,
        title="prompt",
        description="The prompt to guide image generation",
        max_length=512,
    )
    model_kwargs = Variable(ModelKwargs)

    # Load the HF model
    model = StableDiffusionModel()
    model.load()

    # Pass the inputs to the model
    images: t.List[Image] = model.predict(prompt, model_kwargs)

    # Process the images to save to storage
    output: t.List[File] = model.postprocess(images)

    builder.output(output)

pipeline_graph = builder.get_pipeline()

```

Simply append the above code snippet to your `sd_pipeline.py` file.

* At the start, we define the input variables to the pipeline.\
  This tells the pipeline that it should expect 2 variables at runtime, a `str` (the prompt) and an `InputSchema` (model params).
* We then create a `StableDiffusionModel` instance and load the HF model into memory.
* The inputs are then passed to the model, which returns a list of `PIL` images.
* A post processing to ensure that the output files are saved to Mystic storage.

> 📘 Why is the syntax so strict?
>
> If you're unfamiliar with building computational graphs this syntax can be a bit alien and tricky to parse. The point is to create a *deterministic flow from input/s to output/s* so that Mystic servers can find optimisations and handle scaling correctly. In the end you'll acheive better performance.

You can add as many inputs and as many outputs to the pipeline as you like, so as your model grows, you can introduce a host of different arguments, data points, and return values.\
One thing you can't do within a pipeline, however, is use a 'raw' runtime value such as `42` or `True`.\
All runtime values should either be within a `Variable` or further down within the `model` class.

## Building the pipeline image

In order to easily generate a dockerfile for our pipeline, we can define a `pipeline.yaml` configuration file for the pipeline, which will be parsed automatically by the Mystic SDK to generate a dockerfile.

```yaml
runtime:
  container_commands:
    - apt-get update
    - apt-get install -y git
  python:
    version: "3.10"
    requirements:
      - pipeline-ai
      - diffusers==0.24.0
      - torch==2.1.1
      - transformers==4.35.2
      - accelerate==0.25.0
    cuda_version: "11.4"
accelerators:
  - "nvidia_t4"
accelerator_memory: null
pipeline_graph: sd_pipeline:pipeline_graph
pipeline_name: <YOUR_USERNAME>/stable-diffusion-v1.5
extras: {}
```

Here you can specify for instance, which base python version your pipeline should use as well as any python requirements, e.g. `diffusers`, `transformers` etc.. If your pipeline requires `apt` packages, such as `ffmpeg`, you can specify these should be installed in the `container_commands`. The `pipeline_graph` should point to the pipeline `Graph` object we defined previosuly, so the `pipeline_graph` object defined in `sd_pipeline.py`. Then for the `pipeline_name`, substitute \<YOUR\_USERNAME> by your Mystic username.\
To build the docker image of your pipeline, simply run

```Shell
pipeline container build
```

in the directory containing the `pipeline.yaml` file.

# Running the pipeline locally

The Mystic SDK can also be used locally to handle the execution of the pipeline, called a 'run'. So, a great way of debugging your pipeline before uploading it to Mystic is to run it locally! Of course, if you don't have a GPU attached then in some cases local runs will be too slow to be practical.\
To run a container of the image of the pipeline we just built, execute

```Shell
pipeline container up
```

Here, you should see all the startup logs appearing, for instance the model weights being downloaded from HF.\
The container comes with an out of the box mini frontend for testing out your model, available at `http://localhost:14300/play`.

# Running the pipeline on Mystic

> 📘 First login with our CLI
>
> We will be interacting with the Mystic API using the CLI and assume you have authenticated. For more information about how to authenticate using the CLI, see our [authentication guide](https://docs.mystic.ai/docs/login)

## Uploading the pipeline

Before we can run the model on Mystic, we need to **upload** it to the servers. Since a pipeline is effectively just a docker image, we need to push the image to the Mystic registry.\
Again, the CLI provides a neat command to handle all that:

```Shell
pipeline container push
```

> 🚧 You can't modify uploaded pipelines
>
> Once a pipeline has been uploaded to Mystic, it's considered immutable, which is to say it can't be updated or modified in any way, even if its a buggy pipeline. This means you have to upload a new pipeline every time you make a change.

## Running the pipeline

And now we run the pipeline, supplying a prompt input string and dictionary of type `InputKwargs`:

```python
from pipeline.cloud.pipelines import run_pipeline

run = run_pipeline(
    "<YOUR_PIPELINE_ID>",
    "A photo of an astronaut riding a horse on mars",
    {
        "num_images_per_prompt": 2,
        "num_inference_steps": 25,
    },
)

```

Internally this performs a POST request to the `/v4/runs` endpoint in our main API, so if you're building an app in a different language you don't need to worry about dropping the Mystic SDK.

The first time you run the pipeline, it may take up to a couple minutes because the pipeline won't be cached on our servers. Subsequent runs won't be subject to this cold start though and should be pretty speedy!

# Conclusion

In this guide, we saw how to interface with the HuggingFace `StableDiffusionPipeline` to very easily start generating local predictions on a pretrained stable-diffusion pipeline. We then packaged this HuggingFace pipeline into a single deployable docker image, getting our Python code in a form ready to be sent and executed on the `Mystic` servers. After uploading the pipeline to the cloud, we were quickly able to start running the pipeline remotely.

## Complete script

Below is the complete script for defining the pipeline

```python Python
import typing as t
from pathlib import Path

from PIL.Image import Image
from pipeline.cloud.pipelines import run_pipeline
from pipeline.objects.graph import InputField, InputSchema

from pipeline import File, Pipeline, Variable, entity, pipe

HF_MODEL_ID = "runwayml/stable-diffusion-v1-5"


class ModelKwargs(InputSchema):
    num_images_per_prompt: int | None = InputField(
        title="num_images_per_prompt",
        description="The number of images to generate per prompt.",
        default=1,
        optional=True,
    )
    height: int | None = InputField(
        title="height",
        description="The height in pixels of the generated image.",
        default=512,
        optional=True,
        multiple_of=64,
        ge=64,
    )
    width: int | None = InputField(
        title="width",
        description="The width in pixels of the generated image.",
        default=512,
        optional=True,
        multiple_of=64,
        ge=64,
    )
    num_inference_steps: int | None = InputField(
        title="num_inference_steps",
        description=(
            "The number of denoising steps. More denoising steps "
            "usually lead to a higher quality image at the expense "
            "of slower inference."
        ),
        default=50,
        optional=True,
    )


@entity
class StableDiffusionModel:
    def __init__(self) -> None:
        self.model = None
        self.device = None

    @pipe(run_once=True, on_startup=True)
    def load(self) -> None:
        """
        Load the HF model into memory"""
        import torch
        from diffusers import StableDiffusionPipeline

        device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
        self.model = StableDiffusionPipeline.from_pretrained(HF_MODEL_ID)
        self.model.to(device)

    @pipe
    def predict(self, prompt: str, model_kwargs: ModelKwargs) -> t.List[Image]:
        """
        Generates a list of PIL images.
        """
        return self.model(prompt=prompt, **model_kwargs.to_dict()).images

    @pipe
    def postprocess(self, images: t.List[Image]) -> t.List[File]:
        """
        Creates a list of Files from the `PIL` images.
        """
        output_images = []
        for i, image in enumerate(images):
            path = Path(f"/tmp/sd/image-{i}.jpg")
            path.parent.mkdir(parents=True, exist_ok=True)
            image.save(str(path))
            output_images.append(File(path=path, allow_out_of_context_creation=True))
        return output_images


with Pipeline() as builder:
    prompt = Variable(
        str,
        title="prompt",
        description="The prompt to guide image generation",
        max_length=512,
    )
    model_kwargs = Variable(ModelKwargs)

    model = StableDiffusionModel()
    model.load()

    images: t.List[Image] = model.predict(prompt, model_kwargs)

    output: t.List[File] = model.postprocess(images)

    builder.output(output)

pipeline_graph = builder.get_pipeline()


```