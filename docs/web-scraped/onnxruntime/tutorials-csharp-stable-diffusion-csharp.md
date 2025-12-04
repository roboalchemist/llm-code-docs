# Source: https://onnxruntime.ai/docs/tutorials/csharp/stable-diffusion-csharp.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-stable-diffusion-with-c-and-onnx-runtime) Inference Stable Diffusion with C# and ONNX Runtime 

In this tutorial we will learn how to do inferencing for the popular Stable Diffusion deep learning model in C#. Stable Diffusion models take a text prompt and create an image that represents the text. See the example below:

``` highlight
"make a picture of green tree with flowers around it and a red sky" 
```

  --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  ![Image of browser inferencing on sample images.](../../../images/sample-output-stablediff.png)   ![Image of browser inferencing on sample images.](../../../images/stablediff-example-image.png)
  --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Prerequisites](#prerequisites)
- [Use Hugging Face to download the Stable Diffusion models](#use-hugging-face-to-download-the-stable-diffusion-models)
- [Understanding the model in Python with Diffusers from Hugging Face](#understanding-the-model-in-python-with-diffusers-from-hugging-face)
- [Inference with C#](#inference-with-c)
- [Main Function](#main-function)
- [Tokenization with ONNX Runtime Extensions](#tokenization-with-onnx-runtime-extensions)
- [Text embedding with the CLIP text encoder model](#text-embedding-with-the-clip-text-encoder-model)
- [The Inference Loop: UNet model, Timesteps and LMS Scheduler](#the-inference-loop-unet-model-timesteps-and-lms-scheduler)
  - [Scheduler](#scheduler)
  - [Timesteps](#timesteps)
  - [Latents](#latents)
  - [Inference Loop](#inference-loop)
- [Postprocess the `output` with the VAEDecoder](#postprocess-the-output-with-the-vaedecoder)
- [Conclusion](#conclusion)
- [Resources](#resources)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

This tutorial can be run locally or in the cloud by leveraging Azure Machine Learning compute.

- [Download the Source Code from GitHub](https://github.com/cassiebreviu/StableDiffusion)

To run locally:

- [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/Download)

- A GPU enabled machine with CUDA or DirectML on Windows

  - Configure CUDA EP. Follow [this tutorial to configure CUDA and cuDNN for GPU with ONNX Runtime and C# on Windows 11](https://onnxruntime.ai/docs/tutorials/csharp/csharp-gpu.html)
  - Windows comes with DirectML support. No additional configuration is needed. Be sure to clone the [`direct-ML-EP`](https://github.com/cassiebreviu/StableDiffusion/tree/direct-ML-EP) branch of this repo if you choose this option.
  - This was built on a GTX 3070 and it has not been tested on anything smaller.

To run in the cloud with Azure Machine Learning:

- [Azure Subscription](https://azure.microsoft.com/free/)
- [Azure Machine Learning Resource](https://azure.microsoft.com/services/machine-learning/)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#use-hugging-face-to-download-the-stable-diffusion-models) Use Hugging Face to download the Stable Diffusion models

The Hugging Face site has a great library of open source models. We will leverage and download the [ONNX Stable Diffusion models from Hugging Face](https://huggingface.co/models?sort=downloads&search=Stable+Diffusion).

- [Stable Diffusion Models v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4/tree/onnx)

Once you have selected a model version repo, click `Files and Versions`, then select the `ONNX` branch. If there isn't an ONNX model branch available, use the `main` branch and convert it to ONNX. See the [ONNX conversion tutorial for PyTorch](https://learn.microsoft.com/windows/ai/windows-ml/tutorials/pytorch-convert-model) for more information.

- Clone the repo:

  :::: 
  ::: highlight
  ``` highlight
  git lfs install
  git clone https://huggingface.co/CompVis/stable-diffusion-v1-4 -b onnx
  ```
  :::
  ::::
- Copy the folders with the ONNX files to the C# project folder `\StableDiffusion\StableDiffusion`. The folders to copy are: `unet`, `vae_decoder`, `text_encoder`, `safety_checker`.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#understanding-the-model-in-python-with-diffusers-from-hugging-face) Understanding the model in Python with Diffusers from Hugging Face

When taking a prebuilt model and operationalizing it, its useful to take a moment and understand the models in this pipeline. This code is based on the Hugging Face Diffusers Library and Blog. If you want to learn more about how it works [check out this amazing blog post](https://huggingface.co/blog/stable_diffusion) for more details!

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-with-c) Inference with C#

Now lets start to breakdown how to inference in C#! The `unet` model takes the text embedding of the user prompt created by the [CLIP model](https://huggingface.co/docs/transformers/model_doc/clip) that connects text and image. The latent noisy image is created as a starting point. The scheduler algorithm and the `unet` model work together to denoise the image to create an image that represents the text prompt. Lets look at the code.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#main-function) Main Function

The main function sets the prompt, number of inference steps, and the guidance scale. It then calls the `UNet.Inference` function to run the inference.

The properties that need to be set are:

- `prompt` - The text prompt to use for the image
- `num_inference_steps` - The number of steps to run inference for. The more steps the longer it will take to run the inference loop but the image quality should improve.
- `guidance_scale` - The scale for the classifier-free guidance. The higher the number the more it will try to look like the prompt but the image quality may suffer.
- `batch_size` - The number of images to create
- `height` - The height of the image. Default is 512 and must be a multiple of 8.
- `width` - The width of the image. Default is 512 and must be a multiple of 8.

*\* NOTE: Check out the [Hugging Face Blog](https://huggingface.co/blog/stable_diffusion) for more details.*

``` highlight
//Default args
var prompt = "make a picture of green tree with flowers around it and a red sky";
// Number of steps
var num_inference_steps = 10;

// Scale for classifier-free guidance
var guidance_scale = 7.5;
//num of images requested
var batch_size = 1;
// Load the tokenizer and text encoder to tokenize and encodethe text.
var textTokenized = TextProcessing.TokenizeText(prompt);
var textPromptEmbeddings = TextProcessing.TextEncode(textTokenized).ToArray();
// Create uncond_input of blank tokens
var uncondInputTokens = TextProcessing.CreateUncondInput();
var uncondEmbedding = TextProcessing.TextEncode(uncondInputTokens).ToArray();
// Concat textEmeddings and uncondEmbedding
DenseTensor<float> textEmbeddings = new DenseTensor<float>(ne[] );
for (var i = 0; i < textPromptEmbeddings.Length; i++)

var height = 512;
var width = 512;
// Inference Stable Diff
var image = UNet.Inference(num_inference_steps, textEmbeddings,guidance_scale, batch_size, height, width);
// If image failed or was unsafe it will return null.
if( image == null )

```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenization-with-onnx-runtime-extensions) Tokenization with ONNX Runtime Extensions

The `TextProcessing` class has the functions to tokenize the text prompt and encoded it with the [CLIP model](https://huggingface.co/docs/transformers/model_doc/clip) text encoder.

Instead of reimplementing the CLIP tokenizer in C#, we can leverage the cross-platform CLIP tokenizer implementation in [ONNX Runtime Extensions](https://github.com/microsoft/onnxruntime-extensions). The ONNX Runtime Extensions has a `custom_op_cliptok.onnx` file tokenizer that is used to tokenize the text prompt. The tokenizer is a simple tokenizer that splits the text into words and then converts the words into tokens.

- Text Prompt: a sentence or phrase that represents the image you want to create.

  :::: 
  ::: highlight
  ``` highlight
  make a picture of green tree with flowers aroundit and a red sky
  ```
  :::
  ::::

- Text Tokenization: The text prompt is tokenized into a list of tokens. Each token id is a number that represents a word in the sentence, then its filled with a blank token to create the `maxLength` of 77 tokens. The token ids are then converted to a tensor of shape (1,77).

- Below is the code to tokenize the text prompt with ONNX Runtime Extensions.

``` highlight
public static int[] TokenizeText(string text)
);
            inputTensor.StringTensorSetElementAt(text.AsSpan(), 0);

            var inputs = new Dictionary<string, OrtValue>
            
            };

            // Run session and send the input data in to get inference output. 
            using var runOptions = new RunOptions();
            using var tokens = tokenizeSession.Run(runOptions, inputs, tokenizeSession.OutputNames);

            var inputIds = tokens[0].GetTensorDataAsSpan<long>();

            // Cast inputIds to Int32
            var InputIdsInt = new int[inputIds.Length];
            for(int i = 0; i < inputIds.Length; i++)
            

            Console.WriteLine(String.Join(" ", InputIdsInt));

            var modelMaxLength = 77;
            // Pad array with 49407 until length is modelMaxLength
            if (InputIdsInt.Length < modelMaxLength)
            
            return InputIdsInt;
}
```

``` highlight
tensor([[49406,  1078,   320,  1674,   539,  1901,  2677,   593,  4023,  1630,
           585,   537,   320,   736,  2390, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407,
         49407, 49407, 49407, 49407, 49407, 49407, 49407]])
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#text-embedding-with-the-clip-text-encoder-model) Text embedding with the CLIP text encoder model

The tokens are sent to the text encoder model and converted into a tensor of shape (1, 77, 768) where the first dimension is the batch size, the second dimension is the number of tokens and the third dimension is the embedding size. The text encoder is a [OpenAI CLIP](https://openai.com/research/clip) model that connects text to images.

The text encoder creates the text embedding which is trained to encode the text prompt into a vector that is used to guide the image generation. The text embedding is then concatenated with the uncond embedding to create the text embeddings that is sent to the unet model for inferencing.

- Text Embedding: A vector of numbers that represents the text prompt created from the tokenization result. The text embedding is created by the `text_encoder` model.

``` highlight
        public static float[] TextEncoder(int[] tokenizedInput)
        );

            var textEncoderOnnxPath = Directory.GetCurrentDirectory().ToString() + ("\\text_encoder\\model.onnx");

            using var encodeSession = new InferenceSession(textEncoderOnnxPath);

            // Pre-allocate the output so it goes to a managed buffer
            // we know the shape
            var lastHiddenState = new float[1 * 77 * 768];
            using var outputOrtValue = OrtValue.CreateTensorValueFromMemory<float>(lastHiddenState, new long[] );

            string[] input_names = ;
            OrtValue[] inputs = ;

            string[] output_names = ;
            OrtValue[] outputs = ;

            // Run inference.
            using var runOptions = new RunOptions();
            encodeSession.Run(runOptions, input_names, inputs, output_names, outputs);

            return lastHiddenState;
        }
```

``` highlight
torch.Size([1, 77, 768])
tensor([[[-0.3884,  0.0229, -0.0522,  ..., -0.4899, -0.3066,  0.0675],
         [ 0.0520, -0.6046,  1.9268,  ..., -0.3985,  0.9645, -0.4424],
         [-0.8027, -0.4533,  1.7525,  ..., -1.0365,  0.6296,  1.0712],
         ...,
         [-0.6833,  0.3571, -1.1353,  ..., -1.4067,  0.0142,  0.3566],
         [-0.7049,  0.3517, -1.1524,  ..., -1.4381,  0.0090,  0.3777],
         [-0.6155,  0.4283, -1.1282,  ..., -1.4256, -0.0285,  0.3206]]],
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#the-inference-loop-unet-model-timesteps-and-lms-scheduler) The Inference Loop: UNet model, Timesteps and LMS Scheduler

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#scheduler) Scheduler

The scheduler algorithm and the `unet` model work together to denoise the image to create an image that represents the text prompt. There are different scheduler algorithms that can be used, to learn more about them [check out this blog from Hugging Face](https://huggingface.co/docs/diffusers/using-diffusers/schedulers). In this example we will use the \`LMSDiscreteScheduler, which was created based on the HuggingFace [scheduling_lms_discrete.py](https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_lms_discrete.py).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#timesteps) Timesteps

The inference loop is the main loop that runs the scheduler algorithm and the `unet` model. The loop runs for the number of `timesteps` which are calculated by the scheduler algorithm based on the number of inference steps and other parameters.

For this example we have 10 inference steps which calculated the following timesteps:

``` highlight
// Get path to model to create inference session.
var modelPath = Directory.GetCurrentDirectory().ToString() + ("\\unet\\model.onnx");
var scheduler = new LMSDiscreteScheduler();
var timesteps = scheduler.SetTimesteps(numInferenceSteps);
```

``` highlight
tensor([999., 888., 777., 666., 555., 444., 333., 222., 111.,   0.])
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#latents) Latents

The `latents` is the noisy image tensor that is used in the model input. It is created using the `GenerateLatentSample` function to create a random tensor of shape (1,4,64,64). The `seed` can be set to a random number or a fixed number. If the `seed` is set to a fixed number the same latent tensor will be used each time. This is useful for debugging or if you want to create the same image each time.

``` highlight
var seed = new Random().Next();
var latents = GenerateLatentSample(batchSize, height, width,seed, scheduler.InitNoiseSigma);
```

![Image of browser inferencing on sample images.](../../../images/latents-noise-example.png)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-loop) Inference Loop

For each inference step the latent image is duplicated to create the tensor shape of (2,4,64,64), it is then scaled and inferenced with the unet model. The output tensors (2,4,64,64) are split and guidance is applied. The resulting tensor is then sent into the `LMSDiscreteScheduler` step as part of the denoising process and the resulting tensor from the scheduler step is returned and the loop completes again until the `num_inference_steps` is reached.

``` highlight
var modelPath = Directory.GetCurrentDirectory().ToString() + ("\\unet\\model.onnx");
var scheduler = new LMSDiscreteScheduler();
var timesteps = scheduler.SetTimesteps(numInferenceSteps);

var seed = new Random().Next();
var latents = GenerateLatentSample(batchSize, height, width, seed, scheduler.InitNoiseSigma);

// Create Inference Session
using var options = new SessionOptions();
using var unetSession = new InferenceSession(modelPath, options);

var latentInputShape = new int[] ;
var splitTensorsShape = new int[] ;

for (int t = 0; t < timesteps.Length; t++)

```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#postprocess-the-output-with-the-vaedecoder) Postprocess the `output` with the VAEDecoder

After the inference loop is complete, the resulting tensor is scaled and then sent to the `vae_decoder` model to decode the image. Lastly the decoded image tensor is converted to an image and saved to disc.

``` highlight
public static Tensor<float> Decoder(List<NamedOnnxValue> input)

public static Image<Rgba32> ConvertToImage(Tensor<float> output, int width = 512, int height = 512, string imageName = "sample")

    }
    result.Save($@"C:/code/StableDiffusion/.png");
    return result;
}
```

The result image:

![image](/images/sample-output-stablediff.png)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#conclusion) Conclusion

This is a high level overview of how to run Stable Diffusion in C#. It covered the main concepts and provided examples on how to implement it. To get the full code, check out the [Stable Diffusion C# Sample](https://github.com/cassiebreviu/StableDiffusion).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#resources) Resources

- [Stable Diffusion C# Sample Source Code](https://github.com/cassiebreviu/StableDiffusion)
- [C# API Doc](https://onnxruntime.ai/docs/api/csharp/api)
- [Get Started with C# in ONNX Runtime](https://onnxruntime.ai/docs/get-started/with-csharp.html)
- [Hugging Face Stable Diffusion Blog](https://huggingface.co/blog/stable_diffusion)