# Hugging Face Optimum Documentation

Source: https://huggingface.co/docs/optimum/llms-full.txt

---

# Optimum

## Docs

- [Installation](https://huggingface.co/docs/optimum/main/installation.md)
- [🤗 Optimum Nvidia](https://huggingface.co/docs/optimum/main/nvidia_overview.md)
- [🤗 Optimum Furiosa](https://huggingface.co/docs/optimum/main/furiosa_overview.md)
- [🤗 Optimum](https://huggingface.co/docs/optimum/main/index.md)
- [Quick tour](https://huggingface.co/docs/optimum/main/quicktour.md)
- [🤗 Optimum notebooks](https://huggingface.co/docs/optimum/main/notebooks.md)
- [Normalized Configurations](https://huggingface.co/docs/optimum/main/utils/normalized_config.md)
- [Dummy Input Generators](https://huggingface.co/docs/optimum/main/utils/dummy_input_generators.md)
- [The Tasks Manager](https://huggingface.co/docs/optimum/main/exporters/task_manager.md)
- [Overview](https://huggingface.co/docs/optimum/main/exporters/overview.md)
- [Overview](https://huggingface.co/docs/optimum/main/torch_fx/overview.md)
- [Optimization](https://huggingface.co/docs/optimum/main/torch_fx/usage_guides/optimization.md)
- [Symbolic tracer](https://huggingface.co/docs/optimum/main/torch_fx/concept_guides/symbolic_tracer.md)
- [Optimization](https://huggingface.co/docs/optimum/main/torch_fx/package_reference/optimization.md)
- [Quantization](https://huggingface.co/docs/optimum/main/concept_guides/quantization.md)
- [Quantization](https://huggingface.co/docs/optimum/main/llm_quantization/usage_guides/quantization.md)

### Installation
https://huggingface.co/docs/optimum/main/installation.md

# Installation

🤗 Optimum can be installed using `pip` as follows:

```bash
python -m pip install optimum
```

If you'd like to use the accelerator-specific features of 🤗 Optimum, you can install the required dependencies according to the table below:

| Accelerator                                                                                                            | Installation                                                      |
|:-----------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| [ONNX Runtime](https://huggingface.co/docs/optimum/onnxruntime/overview)                                               | `pip install --upgrade --upgrade-strategy eager optimum[onnxruntime]`       |
| [OpenVINO](https://huggingface.co/docs/optimum/intel/index)                                                            | `pip install --upgrade --upgrade-strategy eager optimum[openvino]`          |
| [NVIDIA TensorRT-LLM](https://huggingface.co/docs/optimum/main/en/nvidia_overview)                                     | `docker run -it --gpus all --ipc host huggingface/optimum-nvidia`           |
| [AMD Instinct GPUs and Ryzen AI NPU](https://huggingface.co/docs/optimum/amd/index)                                    | `pip install --upgrade --upgrade-strategy eager optimum[amd]`               |
| [AWS Trainum & Inferentia](https://huggingface.co/docs/optimum-neuron/index)                                           | `pip install --upgrade --upgrade-strategy eager optimum[neuronx]`           |
| [Habana Gaudi Processor (HPU)](https://huggingface.co/docs/optimum/habana/index)                                       | `pip install --upgrade --upgrade-strategy eager optimum[habana]`            |
| [FuriosaAI](https://huggingface.co/docs/optimum/furiosa/index)                                                         | `pip install --upgrade --upgrade-strategy eager optimum[furiosa]`           |

The `--upgrade --upgrade-strategy eager` option is needed to ensure the different packages are upgraded to the latest possible version.

If you'd like to play with the examples or need the bleeding edge of the code and can't wait for a new release, you can install the base library from source as follows:

```bash
python -m pip install git+https://github.com/huggingface/optimum.git
```

For the accelerator-specific features, you can install them by appending `optimum[accelerator_type]` to the `pip` command, e.g.

```bash
python -m pip install optimum[onnxruntime]@git+https://github.com/huggingface/optimum.git
```

### 🤗 Optimum Nvidia
https://huggingface.co/docs/optimum/main/nvidia_overview.md

# 🤗 Optimum Nvidia

Find more information about 🤗 Optimum Nvidia [here](https://github.com/huggingface/optimum-nvidia).

### 🤗 Optimum Furiosa
https://huggingface.co/docs/optimum/main/furiosa_overview.md

# 🤗 Optimum Furiosa

Find more information about 🤗 Optimum Furiosa [here](https://github.com/huggingface/optimum-furiosa).

### 🤗 Optimum
https://huggingface.co/docs/optimum/main/index.md

# 🤗 Optimum

🤗 Optimum is an extension of [Transformers](https://huggingface.co/docs/transformers) that provides a set of performance optimization tools to train and run models on targeted hardware with maximum efficiency.

The AI ecosystem evolves quickly, and more and more specialized hardware along with their own optimizations are emerging every day.
As such, Optimum enables developers to efficiently use any of these platforms with the same ease inherent to Transformers.

🤗 Optimum is distributed as a collection of packages - check out the links below for an in-depth look at each one.

## Hardware partners

The packages below enable you to get the best of the 🤗 Hugging Face ecosystem on various types of devices.

  
    NVIDIA
      Accelerate inference with NVIDIA TensorRT-LLM on the NVIDIA platform
    
    AMD
      Enable performance optimizations for AMD Instinct GPUs and AMD Ryzen AI NPUs
    
    AWS Trainium/Inferentia
      Accelerate your training and inference workflows with AWS Trainium and AWS Inferentia
    
    Google TPUs
      Accelerate your training and inference workflows with Google TPUs
    
    Intel
      Optimize your model to speedup inference with OpenVINO
    
    Intel Gaudi
      Maximize training throughput and efficiency with Intel's Gaudi processor
    
    FuriosaAI
      Fast and efficient inference on FuriosaAI WARBOY
    
  

## Open-source integrations

🤗 Optimum also supports a variety of open-source frameworks to make model optimization very easy.

  
    ONNX Runtime
      Apply quantization and graph optimization to accelerate Transformers models training and inference with ONNX Runtime
    
    ExecuTorch
      PyTorch’s native solution to inference on the Edge via ExecuTorch
    
    Exporters
      Export your PyTorch model to different formats such as ONNX
    
    Torch FX
      Create and compose custom graph transformations to optimize PyTorch Transformers models with Torch FX

### Quick tour
https://huggingface.co/docs/optimum/main/quicktour.md

# Quick tour

This quick tour is intended for developers who are ready to dive into the code and see examples of how to integrate 🤗 Optimum into their model training and inference workflows.

## Accelerated inference

#### OpenVINO

To load a model and run inference with OpenVINO Runtime, you can just replace your `AutoModelForXxx` class with the corresponding `OVModelForXxx` class.
If you want to load a PyTorch checkpoint, set `export=True` to convert your model to the OpenVINO IR (Intermediate Representation).

```diff
- from transformers import AutoModelForSequenceClassification
+ from optimum.intel.openvino import OVModelForSequenceClassification
  from transformers import AutoTokenizer, pipeline

  # Download a tokenizer and model from the Hub and convert to OpenVINO format
  tokenizer = AutoTokenizer.from_pretrained(model_id)
  model_id = "distilbert-base-uncased-finetuned-sst-2-english"
- model = AutoModelForSequenceClassification.from_pretrained(model_id)
+ model = OVModelForSequenceClassification.from_pretrained(model_id, export=True)

  # Run inference!
  classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
  results = classifier("He's a dreadful magician.")
```

You can find more examples in the [documentation](https://huggingface.co/docs/optimum/intel/inference) and in the [examples](https://github.com/huggingface/optimum-intel/tree/main/examples/openvino).

#### ONNX Runtime

To accelerate inference with ONNX Runtime, 🤗 Optimum uses _configuration objects_ to define parameters for graph optimization and quantization. These objects are then used to instantiate dedicated _optimizers_ and _quantizers_.

Before applying quantization or optimization, first we need to load our model. To load a model and run inference with ONNX Runtime, you can just replace the canonical Transformers [`AutoModelForXxx`](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModel) class with the corresponding [`ORTModelForXxx`](https://huggingface.co/docs/optimum/onnxruntime/package_reference/modeling_ort#optimum.onnxruntime.ORTModel) class. If you want to load from a PyTorch checkpoint, set `export=True` to export your model to the ONNX format.

```python
>>> from optimum.onnxruntime import ORTModelForSequenceClassification
>>> from transformers import AutoTokenizer

>>> model_checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
>>> save_directory = "tmp/onnx/"

>>> # Load a model from transformers and export it to ONNX
>>> tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
>>> ort_model = ORTModelForSequenceClassification.from_pretrained(model_checkpoint, export=True)

>>> # Save the ONNX model and tokenizer
>>> ort_model.save_pretrained(save_directory)
>>> tokenizer.save_pretrained(save_directory)
```

Let's see now how we can apply dynamic quantization with ONNX Runtime:

```python
>>> from optimum.onnxruntime.configuration import AutoQuantizationConfig
>>> from optimum.onnxruntime import ORTQuantizer

>>> # Define the quantization methodology
>>> qconfig = AutoQuantizationConfig.arm64(is_static=False, per_channel=False)
>>> quantizer = ORTQuantizer.from_pretrained(ort_model)

>>> # Apply dynamic quantization on the model
>>> quantizer.quantize(save_dir=save_directory, quantization_config=qconfig)
```

In this example, we've quantized a model from the Hugging Face Hub, in the same manner we can quantize a model hosted locally by providing the path to the directory containing the model weights. The result from applying the `quantize()` method is a `model_quantized.onnx` file that can be used to run inference. Here's an example of how to load an ONNX Runtime model and generate predictions with it:

```python
>>> from optimum.onnxruntime import ORTModelForSequenceClassification
>>> from transformers import pipeline, AutoTokenizer

>>> model = ORTModelForSequenceClassification.from_pretrained(save_directory, file_name="model_quantized.onnx")
>>> tokenizer = AutoTokenizer.from_pretrained(save_directory)
>>> classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
>>> results = classifier("I love burritos!")
```

You can find more examples in the [documentation](https://huggingface.co/docs/optimum/onnxruntime/quickstart) and in the [examples](https://github.com/huggingface/optimum/tree/main/examples/onnxruntime).

## Accelerated training

#### Habana

To train transformers on Habana's Gaudi processors, 🤗 Optimum provides a `GaudiTrainer` that is very similar to the 🤗 Transformers [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer). Here is a simple example:

```diff
- from transformers import Trainer, TrainingArguments
+ from optimum.habana import GaudiTrainer, GaudiTrainingArguments

  # Download a pretrained model from the Hub
  model = AutoModelForXxx.from_pretrained("bert-base-uncased")

  # Define the training arguments
- training_args = TrainingArguments(
+ training_args = GaudiTrainingArguments(
      output_dir="path/to/save/folder/",
+     use_habana=True,
+     use_lazy_mode=True,
+     gaudi_config_name="Habana/bert-base-uncased",
      ...
  )

  # Initialize the trainer
- trainer = Trainer(
+ trainer = GaudiTrainer(
      model=model,
      args=training_args,
      train_dataset=train_dataset,
      ...
  )

  # Use Habana Gaudi processor for training!
  trainer.train()
```

You can find more examples in the [documentation](https://huggingface.co/docs/optimum/habana/quickstart) and in the [examples](https://github.com/huggingface/optimum-habana/tree/main/examples).

## Out of the box ONNX export

The Optimum library handles out of the box the ONNX export of Transformers and Diffusers models!

Exporting a model to ONNX is as simple as

```bash
optimum-cli export onnx --model gpt2 gpt2_onnx/
```

Check out the help for more options:

```bash
optimum-cli export onnx --help
```

Check out the [documentation](https://huggingface.co/docs/optimum/exporters/onnx/usage_guides/export_a_model) for more.

## `torch.fx` integration

Optimum integrates with `torch.fx`, providing as a one-liner several graph transformations. We aim at supporting a better management of [quantization](https://huggingface.co/docs/optimum/concept_guides/quantization) through `torch.fx`, both for quantization-aware training (QAT) and post-training quantization (PTQ).

Check out the [documentation](https://huggingface.co/docs/optimum/torch_fx/usage_guides/optimization) and [reference](https://huggingface.co/docs/optimum/torch_fx/package_reference/optimization) for more!

### 🤗 Optimum notebooks
https://huggingface.co/docs/optimum/main/notebooks.md

# 🤗 Optimum notebooks

You can find here a list of the notebooks associated with each accelerator in 🤗 Optimum.

## Optimum Habana

| Notebook                                                                                                                                                                               | Description                                                                                                                                                                       |  Colab                                                                                                                                                                                                          |        Studio Lab                                                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [How to use DeepSpeed to train models with billions of parameters on Habana Gaudi](https://github.com/huggingface/optimum-habana/blob/main/notebooks/AI_HW_Summit_2022.ipynb) | Show how to use DeepSpeed to pre-train/fine-tune the 1.6B-parameter GPT2-XL for causal language modeling on Habana Gaudi. |  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/optimum-habana/blob/main/notebooks/AI_HW_Summit_2022.ipynb) | [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/optimum-habana/blob/main/notebooks/AI_HW_Summit_2022.ipynb) |

## Optimum Intel

### OpenVINO

| Notebook                                                                                                                                                                               | Description                                                                                                                                                                       |                                     Colab                                                                                                                                                                                                          |        Studio Lab                                                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [How to run inference with OpenVINO](https://github.com/huggingface/optimum-intel/blob/main/notebooks/openvino/optimum_openvino_inference.ipynb) | Explains how to export your model to OpenVINO and run inference with OpenVINO Runtime on various tasks| [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/optimum-intel/blob/main/notebooks/openvino/optimum_openvino_inference.ipynb)| [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/optimum-intel/blob/main/notebooks/openvino/optimum_openvino_inference.ipynb)|
| [How to quantize a question answering model with NNCF](https://github.com/huggingface/optimum-intel/blob/main/notebooks/openvino/question_answering_quantization.ipynb) | Show how to apply post-training quantization on a question answering model using [NNCF](https://github.com/openvinotoolkit/nncf) and to accelerate inference with OpenVINO| [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/optimum-intel/blob/main/notebooks/openvino/question_answering_quantization.ipynb)| [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/optimum-intel/blob/main/notebooks/openvino/question_answering_quantization.ipynb)|

## Optimum ONNX Runtime

| Notebook                                                                                                                                                                    | Description                                                                                                                                    |                                                                        Colab                                                                                                                                                                                                          |        Studio Lab                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [How to quantize a model with ONNX Runtime for text classification](https://github.com/huggingface/notebooks/blob/main/examples/text_classification_quantization_ort.ipynb) | Show how to apply static and dynamic quantization on a model using [ONNX Runtime](https://github.com/microsoft/onnxruntime) for any GLUE task. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification_quantization_ort.ipynb) | [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/notebooks/blob/main/examples/text_classification_quantization_ort.ipynb) |
| [How to fine-tune a model for text classification with ONNX Runtime](https://github.com/huggingface/notebooks/blob/main/examples/text_classification_ort.ipynb)             | Show how to DistilBERT model on GLUE tasks using [ONNX Runtime](https://github.com/microsoft/onnxruntime).                                     | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification_ort.ipynb)          | [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/notebooks/blob/main/examples/text_classification_ort.ipynb) |
| [How to fine-tune a model for summarization with ONNX Runtime](https://github.com/huggingface/notebooks/blob/main/examples/summarization_ort.ipynb)                         | Show how to fine-tune a T5 model on the BBC news corpus.                                                                                       | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/summarization_ort.ipynb)                |                [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/notebooks/blob/main/examples/summarization_ort.ipynb) |
| [How to fine-tune DeBERTa for question-answering with ONNX Runtime](https://github.com/huggingface/notebooks/blob/main/examples/question_answering_ort.ipynb)                         | Show how to fine-tune a DeBERTa model on the squad.                                                                                       | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering_ort.ipynb)                |                [![Open in AWS Studio](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/notebooks/blob/main/examples/question_answering_ort.ipynb) |

### Normalized Configurations
https://huggingface.co/docs/optimum/main/utils/normalized_config.md

# Normalized Configurations

Model configuration classes in 🤗 Transformers are not standardized. Although Transformers implements an `attribute_map` attribute that mitigates the issue to some extent, it does not make it easy to reason on common configuration attributes in the code.
[NormalizedConfig](/docs/optimum/main/en/utils/normalized_config#optimum.utils.NormalizedConfig) classes try to fix that by allowing access to the configuration
attribute they wrap in a standardized way.

## Base class[[optimum.utils.NormalizedConfig]]

While it is possible to create `NormalizedConfig` subclasses for common use-cases, it is also possible to overwrite
the `original attribute name -> normalized attribute name` mapping directly using the
`with_args()` class method.

#### optimum.utils.NormalizedConfig[[optimum.utils.NormalizedConfig]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/normalized_config.py#L25)

Handles the normalization of `PretrainedConfig` attribute names, allowing to access attributes in a general way.

**Parameters:**

config (`PretrainedConfig`) : The config to normalize.

## Existing normalized configurations[[optimum.utils.NormalizedTextConfig]]

#### optimum.utils.NormalizedTextConfig[[optimum.utils.NormalizedTextConfig]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/normalized_config.py#L87)

#### optimum.utils.NormalizedSeq2SeqConfig[[optimum.utils.NormalizedSeq2SeqConfig]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/normalized_config.py#L99)

#### optimum.utils.NormalizedVisionConfig[[optimum.utils.NormalizedVisionConfig]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/normalized_config.py#L106)

#### optimum.utils.NormalizedTextAndVisionConfig[[optimum.utils.NormalizedTextAndVisionConfig]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/normalized_config.py#L125)

### Dummy Input Generators
https://huggingface.co/docs/optimum/main/utils/dummy_input_generators.md

# Dummy Input Generators

It is very common to have to generate dummy inputs to perform a task (tracing, exporting a model to some backend,
testing model outputs, etc). The goal of [DummyInputGenerator](/docs/optimum/main/en/utils/dummy_input_generators#optimum.utils.DummyInputGenerator) classes is to make this
generation easy and re-usable.

## Base class[[optimum.utils.DummyInputGenerator]]

#### optimum.utils.DummyInputGenerator[[optimum.utils.DummyInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L93)

Generates dummy inputs for the supported input names, in the requested framework.

concat_inputsoptimum.utils.DummyInputGenerator.concat_inputshttps://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L292[{"name": "inputs", "val": ""}, {"name": "dim", "val": ": int"}]- **inputs** --
  The list of tensors in a given framework to concatenate.
- **dim** (`int`) --
  The dimension along which to concatenate.0The tensor of the concatenation.

Concatenates inputs together.

**Parameters:**

inputs : The list of tensors in a given framework to concatenate.

dim (`int`) : The dimension along which to concatenate.

**Returns:**

The tensor of the concatenation.
#### constant_tensor[[optimum.utils.DummyInputGenerator.constant_tensor]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L245)

Generates a constant tensor.

**Parameters:**

shape (`List[int]`) : The shape of the constant tensor.

value (`Union[int, float]`, defaults to 1) : The value to fill the constant tensor with.

dtype (`Optional[Any]`, defaults to `None`) : The dtype of the constant tensor.

framework (`str`, defaults to `"pt"`) : The requested framework.

**Returns:**

A constant tensor in the requested framework.
#### generate[[optimum.utils.DummyInputGenerator.generate]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L114)

Generates the dummy input matching `input_name` for the requested framework.

**Parameters:**

input_name (`str`) : The name of the input to generate.

framework (`str`, defaults to `"pt"`) : The requested framework.

int_dtype (`str`, defaults to `"int64"`) : The dtypes of generated integer tensors.

float_dtype (`str`, defaults to `"fp32"`) : The dtypes of generated float tensors.

**Returns:**

A tensor in the requested framework of the input.
#### pad_input_on_dim[[optimum.utils.DummyInputGenerator.pad_input_on_dim]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L317)

Pads an input either to the desired length, or by a padding length.

**Parameters:**

input_ : The tensor to pad.

dim (`int`) : The dimension along which to pad.

desired_length (`Optional[int]`, defaults to `None`) : The desired length along the dimension after padding.

padding_length (`Optional[int]`, defaults to `None`) : The length to pad along the dimension.

value (`Union[int, float]`, defaults to 1) : The value to use for padding.

dtype (`Optional[Any]`, defaults to `None`) : The dtype of the padding.

**Returns:**

The padded tensor.
#### random_float_tensor[[optimum.utils.DummyInputGenerator.random_float_tensor]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L213)

Generates a tensor of random floats in the [min_value, max_value) range.

**Parameters:**

shape (`List[int]`) : The shape of the random tensor.

min_value (`float`, defaults to 0) : The minimum value allowed.

max_value (`float`, defaults to 1) : The maximum value allowed.

framework (`str`, defaults to `"pt"`) : The requested framework.

dtype (`str`, defaults to `"fp32"`) : The dtype of the generated float tensor. Could be "fp32", "fp16", "bf16".

**Returns:**

A random tensor in the requested framework.
#### random_int_tensor[[optimum.utils.DummyInputGenerator.random_int_tensor]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L134)

Generates a tensor of random integers in the [min_value, max_value) range.

**Parameters:**

shape (`List[int]`) : The shape of the random tensor.

max_value (`int`) : The maximum value allowed.

min_value (`int`, defaults to 0) : The minimum value allowed.

framework (`str`, defaults to `"pt"`) : The requested framework.

dtype (`str`, defaults to `"int64"`) : The dtype of the generated integer tensor. Could be "int64", "int32", "int8".

**Returns:**

A random tensor in the requested framework.
#### random_mask_tensor[[optimum.utils.DummyInputGenerator.random_mask_tensor]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L166)

Generates a mask tensor either right or left padded.

**Parameters:**

shape (`List[int]`) : The shape of the random tensor.

padding_side (`str`, defaults to "right") : The side on which the padding is applied.

framework (`str`, defaults to `"pt"`) : The requested framework.

dtype (`str`, defaults to `"int64"`) : The dtype of the generated integer tensor. Could be "int64", "int32", "int8".

**Returns:**

A random mask tensor either left padded or right padded in the requested framework.
#### supports_input[[optimum.utils.DummyInputGenerator.supports_input]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L100)

Checks whether the `DummyInputGenerator` supports the generation of the requested input.

**Parameters:**

input_name (`str`) : The name of the input to generate.

**Returns:**

``bool``

A boolean specifying whether the input is supported.

## Existing dummy input generators[[optimum.utils.DummyTextInputGenerator]]

#### optimum.utils.DummyTextInputGenerator[[optimum.utils.DummyTextInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L363)

Generates dummy encoder text inputs.

#### optimum.utils.DummyDecoderTextInputGenerator[[optimum.utils.DummyDecoderTextInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L519)

Generates dummy decoder text inputs.

#### optimum.utils.DummyPastKeyValuesGenerator[[optimum.utils.DummyPastKeyValuesGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L620)

Generates dummy past_key_values inputs.

#### optimum.utils.DummySeq2SeqPastKeyValuesGenerator[[optimum.utils.DummySeq2SeqPastKeyValuesGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L667)

Generates dummy past_key_values inputs for seq2seq architectures.

#### optimum.utils.DummyBboxInputGenerator[[optimum.utils.DummyBboxInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L755)

Generates dummy bbox inputs.

#### optimum.utils.DummyVisionInputGenerator[[optimum.utils.DummyVisionInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L795)

Generates dummy vision inputs.

#### optimum.utils.DummyAudioInputGenerator[[optimum.utils.DummyAudioInputGenerator]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/utils/input_generators.py#L883)

### The Tasks Manager
https://huggingface.co/docs/optimum/main/exporters/task_manager.md

# The Tasks Manager

Exporting a model from one framework to some format (also called backend here) involves specifying inputs and outputs information that the export function needs. The way `optimum.exporters` is structured for each backend is as follows:
- Configuration classes containing the information for each model to perform the export.
- Exporting functions using the proper configuration for the model to export.

The role of the [TasksManager](/docs/optimum/main/en/exporters/task_manager#optimum.exporters.tasks.TasksManager) is to be the main entry-point to load a model given a name and a task, and to get the proper configuration for a given (architecture, backend) couple. 
That way, there is a centralized place to register the `task -> model class` and `(architecture, backend) -> configuration` mappings. This allows the export functions to use this, and to rely on the various checks it provides.

## Task names

The tasks supported might depend on the backend, but here are the mappings between a task name and the auto class for PyTorch.

It is possible to know which tasks are supported for a model for a given backend, by doing:

```python
>>> from optimum.exporters.tasks import TasksManager

>>> model_type = "distilbert"
>>> # For instance, for the ONNX export.
>>> backend = "onnx"
>>> distilbert_tasks = list(TasksManager.get_supported_tasks_for_model_type(model_type, backend).keys())

>>> print(distilbert_tasks)
['default', 'fill-mask', 'text-classification', 'multiple-choice', 'token-classification', 'question-answering']
```

### PyTorch

#### Transformers

| Task                             | Auto Class                                                    |
|----------------------------------|---------------------------------------------------------------|
| `audio-classification`           | `AutoModelForAudioClassification`                             |
| `audio-frame-classification`     | `AutoModelForAudioFrameClassification`                        |
| `audio-xvector`                  | `AutoModelForAudioXVector`                                    |
| `automatic-speech-recognition`   | `AutoModelForSpeechSeq2Seq`, `AutoModelForCTC`                |
| `depth-estimation`               | `AutoModelForDepthEstimation`                                 |
| `feature-extraction`             | `AutoModel`                                                   |
| `fill-mask`                      | `AutoModelForMaskedLM`                                        |
| `image-classification`           | `AutoModelForImageClassification`                             |
| `image-to-image`                 | `AutoModelForImageToImage`                                    |
| `image-to-text`                  | `AutoModelForVision2Seq`, `AutoModel`                         |
| `image-text-to-text`             | `AutoModelForImageTextToText`                                 |
| `mask-generation`                | `AutoModel`                                                   |
| `masked-im`                      | `AutoModelForMaskedImageModeling`                             |
| `multiple-choice`                | `AutoModelForMultipleChoice`                                  |
| `object-detection`               | `AutoModelForObjectDetection`                                 |
| `question-answering`             | `AutoModelForQuestionAnswering`                               |
| `reinforcement-learning`         | `AutoModel`                                                   |
| `semantic-segmentation`          | `AutoModelForSemanticSegmentation`                            |
| `text-to-audio`                  | `AutoModelForTextToSpectrogram`, `AutoModelForTextToWaveform` |
| `text-generation`                | `AutoModelForCausalLM`                                        |
| `text2text-generation`           | `AutoModelForSeq2SeqLM`                                       |
| `text-classification`            | `AutoModelForSequenceClassification`                          |
| `token-classification`           | `AutoModelForTokenClassification`                             |
| `visual-question-answering`      | `AutoModelForVisualQuestionAnswering`                         |
| `zero-shot-image-classification` | `AutoModelForZeroShotImageClassification`                     |
| `zero-shot-object-detection`     | `AutoModelForZeroShotObjectDetection`                         |

#### Diffusers

| Task             | Auto Class                   |
|------------------|------------------------------|
| `text-to-image`  | `AutoPipelineForText2Image`  |
| `image-to-image` | `AutoPipelineForImage2Image` |
| `inpainting`     | `AutoPipelineForInpainting`  |

#### Sentence Transformers

| Task                  | Auto Class            |
|-----------------------|-----------------------|
| `feature-extraction`  | `SentenceTransformer` |
| `sentence-similarity` | `SentenceTransformer` |

## Reference[[optimum.exporters.tasks.TasksManager]]

#### optimum.exporters.tasks.TasksManager[[optimum.exporters.tasks.TasksManager]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L118)

Handles the `task name -> model class` and `architecture -> configuration` mappings.

create_registeroptimum.exporters.tasks.TasksManager.create_registerhttps://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L287[{"name": "backend", "val": ": str"}, {"name": "overwrite_existing", "val": ": bool = False"}]- **backend** (`str`) --
  The name of the backend that the register function will handle.
- **overwrite_existing** (`bool`, defaults to `False`) --
  Whether or not the register function is allowed to overwrite an already existing config.0`Callable[[str, Tuple[str, ...]], Callable[[Type], Type]]`A decorator taking the model type and a the
supported tasks.

Creates a register function for the specified backend.

Example:
```python
>>> register_for_new_backend = create_register("new-backend")

>>> @register_for_new_backend("bert", "text-classification", "token-classification")
>>> class BertNewBackendConfig(NewBackendConfig):
>>>     pass
```

**Parameters:**

backend (`str`) : The name of the backend that the register function will handle.

overwrite_existing (`bool`, defaults to `False`) : Whether or not the register function is allowed to overwrite an already existing config.

**Returns:**

``Callable[[str, Tuple[str, ...]], Callable[[Type], Type]]``

A decorator taking the model type and a the
supported tasks.
#### determine_framework[[optimum.exporters.tasks.TasksManager.determine_framework]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L579)

Determines the framework to use for the export.

The priority is in the following order:
1. User input via `framework`.
2. If local checkpoint is provided, use the same framework as the checkpoint.
3. If model repo, try to infer the framework from the cache if available, else from the Hub.
4. If could not infer, use available framework in environment, with priority given to PyTorch.

**Parameters:**

model_name_or_path (`Union[str, Path]`) : Can be either the model id of a model repo on the Hugging Face Hub, or a path to a local directory containing a model.

subfolder (`str`, *optional*, defaults to `""`) : In case the model files are located inside a subfolder of the model directory / repo on the Hugging Face Hub, you can specify the subfolder name here.

revision (`Optional[str]`,  defaults to `None`) : Revision is the specific model version to use. It can be a branch name, a tag name, or a commit id.

cache_dir (`Optional[str]`, *optional*) : Path to a directory in which a downloaded pretrained model weights have been cached if the standard cache should not be used.

token (`Optional[Union[bool,str]]`, defaults to `None`) : The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `huggingface-cli login` (stored in `huggingface_hub.constants.HF_TOKEN_PATH`).

**Returns:**

``str``

The framework to use for the export.
#### get_all_tasks[[optimum.exporters.tasks.TasksManager.get_all_tasks]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L1053)

Retrieves all the possible tasks.

**Returns:**

``List``

all the possible tasks.
#### get_exporter_config_constructor[[optimum.exporters.tasks.TasksManager.get_exporter_config_constructor]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L1226)

Gets the `ExportConfigConstructor` for a model (or alternatively for a model type) and task combination.

**Parameters:**

exporter (`str`) : The exporter to use.

model (`Optional[PreTrainedModel]`, defaults to `None`) : The instance of the model.

task (`str`, defaults to `"feature-extraction"`) : The task to retrieve the config for.

model_type (`Optional[str]`, defaults to `None`) : The model type to retrieve the config for.

model_name (`Optional[str]`, defaults to `None`) : The name attribute of the model object, only used for the exception message.

exporter_config_kwargs (`Optional[Dict[str, Any]]`, defaults to `None`) : Arguments that will be passed to the exporter config class when building the config constructor.

library_name (`Optional[str]`, defaults to `None`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers".

**Returns:**

``ExportConfigConstructor``

The `ExporterConfig` constructor for the requested backend.
#### get_model_class_for_task[[optimum.exporters.tasks.TasksManager.get_model_class_for_task]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L445)

Attempts to retrieve an AutoModel class from a task name.

**Parameters:**

task (`str`) : The task required.

framework (`str`, defaults to `"pt"`) : The framework to use for the export.

model_type (`Optional[str]`, defaults to `None`) : The model type to retrieve the model class for. Some architectures need a custom class to be loaded, and can not be loaded from auto class.

model_class_name (`Optional[str]`, defaults to `None`) : A model class name, allowing to override the default class that would be detected for the task. This parameter is useful for example for "automatic-speech-recognition", that may map to AutoModelForSpeechSeq2Seq or to AutoModelForCTC.

library (`str`, defaults to `transformers`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers".

**Returns:**

The AutoModel class corresponding to the task.
#### get_model_from_task[[optimum.exporters.tasks.TasksManager.get_model_from_task]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L1073)

Retrieves a model from its name and the task to be enabled.

**Parameters:**

task (`str`) : The task required.

model_name_or_path (`Union[str, Path]`) : Can be either the model id of a model repo on the Hugging Face Hub, or a path to a local directory containing a model.

subfolder (`str`, defaults to `""`) : In case the model files are located inside a subfolder of the model directory / repo on the Hugging Face Hub, you can specify the subfolder name here.

revision (`Optional[str]`, *optional*) : Revision is the specific model version to use. It can be a branch name, a tag name, or a commit id.

cache_dir (`Optional[str]`, *optional*) : Path to a directory in which a downloaded pretrained model weights have been cached if the standard cache should not be used.

token (`Optional[Union[bool,str]]`, defaults to `None`) : The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `huggingface-cli login` (stored in `huggingface_hub.constants.HF_TOKEN_PATH`).

framework (`Optional[str]`, *optional*) : The framework to use for the export. See `TasksManager.determine_framework` for the priority should none be provided.

torch_dtype (`Optional[torch.dtype]`, defaults to `None`) : Data type to load the model on. PyTorch-only argument.

device (`Optional[torch.device]`, defaults to `None`) : Device to initialize the model on. PyTorch-only argument. For PyTorch, defaults to "cpu".

library_name (`Optional[str]`, defaults to `None`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers". See `TasksManager.infer_library_from_model` for the priority should none be provided.

model_kwargs (`Dict[str, Any]`, *optional*) : Keyword arguments to pass to the model `.from_pretrained()` method.

library_name (`Optional[str]`, defaults to `None`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers". See `TasksManager.infer_library_from_model` for the priority should none be provided.

**Returns:**

The instance of the model.
#### get_supported_model_type_for_task[[optimum.exporters.tasks.TasksManager.get_supported_model_type_for_task]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L403)

Returns the list of supported architectures by the exporter for a given task. Transformers-specific.
#### get_supported_tasks_for_model_type[[optimum.exporters.tasks.TasksManager.get_supported_tasks_for_model_type]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L342)

Retrieves the `task -> exporter backend config constructors` map from the model type.

**Parameters:**

model_type (`str`) : The model type to retrieve the supported tasks for.

exporter (`str`) : The name of the exporter.

model_name (`Optional[str]`, defaults to `None`) : The name attribute of the model object, only used for the exception message.

library_name (`Optional[str]`, defaults to `None`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers".

**Returns:**

``Dict[str, ExportConfigConstructor]``

The mapping between the supported tasks and the backend config
constructors for the specified model type.
#### infer_library_from_model[[optimum.exporters.tasks.TasksManager.infer_library_from_model]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L956)

Infers the library from the model repo, model instance, or model class.

**Parameters:**

model (`Union[str, PreTrainedModel, DiffusionPipeline, Type]`) : The model to infer the task from. This can either be the name of a repo on the HuggingFace Hub, an instance of a model, or a model class.

subfolder (`str`, defaults to `""`) : In case the model files are located inside a subfolder of the model directory / repo on the Hugging Face Hub, you can specify the subfolder name here.

revision (`Optional[str]`, *optional*, defaults to `None`) : Revision is the specific model version to use. It can be a branch name, a tag name, or a commit id.

cache_dir (`Optional[str]`, *optional*) : Path to a directory in which a downloaded pretrained model weights have been cached if the standard cache should not be used.

token (`Optional[Union[bool,str]]`, defaults to `None`) : The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `huggingface-cli login` (stored in `huggingface_hub.constants.HF_TOKEN_PATH`).

**Returns:**

``str``

The library name automatically detected from the model repo, model instance, or model class.
#### infer_task_from_model[[optimum.exporters.tasks.TasksManager.infer_task_from_model]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L797)

Infers the task from the model repo, model instance, or model class.

**Parameters:**

model (`Union[str, PreTrainedModel, DiffusionPipeline, Type]`) : The model to infer the task from. This can either be the name of a repo on the HuggingFace Hub, an instance of a model, or a model class.

subfolder (`str`, *optional*, defaults to `""`) : In case the model files are located inside a subfolder of the model directory / repo on the Hugging Face Hub, you can specify the subfolder name here.

revision (`Optional[str]`,  defaults to `None`) : Revision is the specific model version to use. It can be a branch name, a tag name, or a commit id.

cache_dir (`Optional[str]`, *optional*) : Path to a directory in which a downloaded pretrained model weights have been cached if the standard cache should not be used.

token (`Optional[Union[bool,str]]`, defaults to `None`) : The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `huggingface-cli login` (stored in `huggingface_hub.constants.HF_TOKEN_PATH`).

library_name (`Optional[str]`, defaults to `None`) : The library name of the model. Can be any of "transformers", "timm", "diffusers", "sentence_transformers". See `TasksManager.infer_library_from_model` for the priority should none be provided.

**Returns:**

``str``

The task name automatically detected from the HF hub repo, model instance, or model class.
#### standardize_model_attributes[[optimum.exporters.tasks.TasksManager.standardize_model_attributes]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/exporters/tasks.py#L1002)

Updates the model for export. This function is suitable to make required changes to the models from different
libraries to follow transformers style.

**Parameters:**

model (`Union[PreTrainedModel, DiffusionPipeline]`) : The instance of the model.

### Overview
https://huggingface.co/docs/optimum/main/exporters/overview.md

# Overview

🤗 Optimum enables exporting models from PyTorch to different formats through its `exporters` module. For now, three exporting format are supported: ONNX (optimum-onnx), OpenVINO (optimum-intel), Neuron (optimum-neuron).

### Overview
https://huggingface.co/docs/optimum/main/torch_fx/overview.md

# Overview

🤗 Optimum provides an integration with Torch FX, a library for PyTorch that allows developers to implement custom transformations of their models that can be optimized for performance.

  
    How-to guides
      Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use 🤗 Optimum to solve real-world problems.
    
    Conceptual guides
      High-level explanations for building a better understanding about important topics such as quantization and graph optimization.
   
    Reference
      Technical descriptions of how the Torch FX classes and methods of 🤗 Optimum work.

### Optimization
https://huggingface.co/docs/optimum/main/torch_fx/usage_guides/optimization.md

# Optimization

The `optimum.fx.optimization` module provides a set of torch.fx graph transformations, along with classes and functions to write your own transformations and compose them.

## The transformation guide

In 🤗 Optimum, there are two kinds of transformations: reversible and non-reversible transformations.

### Write a non-reversible transformation

The most basic case of transformations is non-reversible transformations. Those transformations cannot be reversed, meaning that after applying them to a graph module, there is no way to get the original model back. To implement such transformations in 🤗 Optimum, it is very easy: you just need to subclass [Transformation](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation) and implement the [transform()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation.transform) method.

For instance, the following transformation changes all the multiplications to additions:

```python
>>> import operator
>>> from optimum.fx.optimization import Transformation

>>> class ChangeMulToAdd(Transformation):
...     def transform(self, graph_module):
...         for node in graph_module.graph.nodes:
...             if node.op == "call_function" and node.target == operator.mul:
...                 node.target = operator.add
...         return graph_module
```

After implementing it, your transformation can be used as a regular function:

```python
>>> from transformers import BertModel
>>> from transformers.utils.fx import symbolic_trace

>>> model = BertModel.from_pretrained("bert-base-uncased")
>>> traced = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "token_type_ids"],
... )

>>> transformation = ChangeMulToAdd()
>>> transformed_model = transformation(traced)
```

### Write a reversible transformation

A reversible transformation implements both the transformation and its reverse, allowing to retrieve the original model from the transformed one. To implement such transformation, you need to subclass [ReversibleTransformation](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.ReversibleTransformation) and implement the [transform()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation.transform) and [reverse()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.ReversibleTransformation.reverse) methods.

For instance, the following transformation is reversible:

```python
>>> import operator
>>> from optimum.fx.optimization import ReversibleTransformation

>>> class MulToMulTimesTwo(ReversibleTransformation):
...     def transform(self, graph_module):
...         for node in graph_module.graph.nodes:
...             if node.op == "call_function" and node.target == operator.mul:
...                 x, y = node.args
...                 node.args = (2 * x, y)
...         return graph_module
...
...     def reverse(self, graph_module):
...         for node in graph_module.graph.nodes:
...             if node.op == "call_function" and node.target == operator.mul:
...                 x, y = node.args
...                 node.args = (x / 2, y)
...         return graph_module
```

### Composing transformations together

As applying multiple transformations in chain is needed more often that not, [compose()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.compose) is provided. It is an utility function that allows you to create a transformation by chaining multiple other transformations.

```python
>>> from optimum.fx.optimization import compose
>>> composition = compose(MulToMulTimesTwo(), ChangeMulToAdd())
```

### Symbolic tracer
https://huggingface.co/docs/optimum/main/torch_fx/concept_guides/symbolic_tracer.md

# Symbolic tracer

In Torch FX, the symbolic tracer feeds dummy values through the code to record the underlying operations.

### Optimization
https://huggingface.co/docs/optimum/main/torch_fx/package_reference/optimization.md

# Optimization

## Transformation[[optimum.fx.optimization.Transformation]]

#### optimum.fx.optimization.Transformation[[optimum.fx.optimization.Transformation]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L85)

A torch.fx graph transformation.

It  must implement the [transform()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation.transform) method, and be used as a
callable.

__call__optimum.fx.optimization.Transformation.__call__https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L108[{"name": "graph_module", "val": ": GraphModule"}, {"name": "lint_and_recompile", "val": ": bool = True"}]- **graph_module** (`torch.fx.GraphModule`) --
  The module to transform.
- **lint_and_recompile** (`bool`, defaults to `True`) --
  Whether the transformed module should be linted and recompiled.
  This can be set to `False` when chaining transformations together to perform this operation only once.0`torch.fx.GraphModule`The transformed module.

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

**Returns:**

``torch.fx.GraphModule``

The transformed module.
#### get_transformed_nodes[[optimum.fx.optimization.Transformation.get_transformed_nodes]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L161)

**Parameters:**

graph_module (`torch.fx.GraphModule`) : The graph_module to get the nodes from.

**Returns:**

``List[torch.fx.Node]``

Gives the list of nodes that were transformed by the transformation.
#### mark_as_transformed[[optimum.fx.optimization.Transformation.mark_as_transformed]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L137)

Marks a node as transformed by this transformation.

**Parameters:**

node (`torch.fx.Node`) : The node to mark as transformed.
#### transform[[optimum.fx.optimization.Transformation.transform]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L95)

**Parameters:**

graph_module (`torch.fx.GraphModule`) : The module to transform.

**Returns:**

``torch.fx.GraphModule``

The transformed module.
#### transformed[[optimum.fx.optimization.Transformation.transformed]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L149)

**Parameters:**

node (`torch.fx.Node`) : The node to check.

**Returns:**

``bool``

Specifies whether the node was transformed by this transformation or not.

## Reversible transformation[[optimum.fx.optimization.ReversibleTransformation]]

#### optimum.fx.optimization.ReversibleTransformation[[optimum.fx.optimization.ReversibleTransformation]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L176)

A torch.fx graph transformation that is reversible.

It must implement the [transform()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation.transform) and
[reverse()](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.ReversibleTransformation.reverse) methods, and be used as a callable.

__call__optimum.fx.optimization.ReversibleTransformation.__call__https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L197[{"name": "graph_module", "val": ": GraphModule"}, {"name": "lint_and_recompile", "val": ": bool = True"}, {"name": "reverse", "val": ": bool = False"}]- **graph_module** (`torch.fx.GraphModule`) --
  The module to transform.
- **lint_and_recompile** (`bool`, defaults to `True`) --
  Whether the transformed module should be linted and recompiled.
  This can be set to `False` when chaining transformations together to perform this operation only once.
- **reverse** (`bool`, defaults to `False`) --
  If `True`, the reverse transformation is performed.0`torch.fx.GraphModule`The transformed module.

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

**Returns:**

``torch.fx.GraphModule``

The transformed module.
#### mark_as_restored[[optimum.fx.optimization.ReversibleTransformation.mark_as_restored]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L222)

Marks a node as restored back to its original state.

**Parameters:**

node (`torch.fx.Node`) : The node to mark as restored.
#### reverse[[optimum.fx.optimization.ReversibleTransformation.reverse]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L184)

**Parameters:**

graph_module (`torch.fx.GraphModule`) : The module to transform.

**Returns:**

``torch.fx.GraphModule``

The reverse transformed module.

#### optimum.fx.optimization.compose[[optimum.fx.optimization.compose]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L721)

Composes a list of transformations together.

Example:

```python
>>> from transformers import BertModel
>>> from transformers.utils.fx import symbolic_trace
>>> from optimum.fx.optimization import ChangeTrueDivToMulByInverse, MergeLinears, compose

>>> model = BertModel.from_pretrained("bert-base-uncased")
>>> traced = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "token_type_ids"],
... )
>>> composition = compose(ChangeTrueDivToMulByInverse(), MergeLinears())
>>> transformed_model = composition(traced)
```

**Parameters:**

args ([Transformation](/docs/optimum/main/en/torch_fx/package_reference/optimization#optimum.fx.optimization.Transformation)) : The transformations to compose together.

inplace (`bool`, defaults to `True`) : Whether the resulting transformation should be inplace, or create a new graph module.

**Returns:**

The composition transformation object.

### Transformations[[optimum.fx.optimization.MergeLinears]]

#### optimum.fx.optimization.MergeLinears[[optimum.fx.optimization.MergeLinears]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L237)

Transformation that merges linear layers that take the same input into one big linear layer.

Example:

```python
>>> from transformers import BertModel
>>> from transformers.utils.fx import symbolic_trace
>>> from optimum.fx.optimization import MergeLinears

>>> model = BertModel.from_pretrained("bert-base-uncased")
>>> traced = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "token_type_ids"],
... )
>>> transformation = MergeLinears()
>>> transformed_model = transformation(traced)
>>> restored_model = transformation(transformed_model, reverse=True)
```

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

#### optimum.fx.optimization.FuseBiasInLinear[[optimum.fx.optimization.FuseBiasInLinear]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L393)

Transformation that fuses the bias to the weight in torch.nn.Linear.

Example:

```python
>>> from transformers import BertModel
>>> from transformers.utils.fx import symbolic_trace
>>> from optimum.fx.optimization import FuseBiasInLinear

>>> model = BertModel.from_pretrained("bert-base-uncased")
>>> traced = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "token_type_ids"],
... )
>>> transformation = FuseBiasInLinear()
>>> transformed_model = transformation(traced)
>>> restored_model = transformation(transformed_model, reverse=True)
```

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

#### optimum.fx.optimization.ChangeTrueDivToMulByInverse[[optimum.fx.optimization.ChangeTrueDivToMulByInverse]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L447)

Transformation that changes truediv nodes to multiplication by the inverse nodes when the denominator is static.
For example, that is sometimes the case for the scaling factor in attention layers.

Example:

```python
>>> from transformers import BertModel
>>> from transformers.utils.fx import symbolic_trace
>>> from optimum.fx.optimization import ChangeTrueDivToMulByInverse

>>> model = BertModel.from_pretrained("bert-base-uncased")
>>> traced = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "token_type_ids"],
... )
>>> transformation = ChangeTrueDivToMulByInverse()
>>> transformed_model = transformation(traced)
>>> restored_model = transformation(transformed_model, reverse=True)
```

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

#### optimum.fx.optimization.FuseBatchNorm2dInConv2d[[optimum.fx.optimization.FuseBatchNorm2dInConv2d]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L478)

Transformation that fuses `nn.BatchNorm2d` following `nn.Conv2d` into a single `nn.Conv2d`.
The fusion will be done only if the convolution has the batch normalization as sole following node.

For example, fusion will not be done in the case

```
     Conv2d
     /   \
    /     \
ReLU   BatchNorm2d
```

Example:
```python
>>> from transformers.utils.fx import symbolic_trace
>>> from transformers import AutoModelForImageClassification

>>> from optimum.fx.optimization import FuseBatchNorm2dInConv2d

>>> model = AutoModelForImageClassification.from_pretrained("microsoft/resnet-50")
>>> model.eval()
>>> traced_model = symbolic_trace(
...     model,
...     input_names=["pixel_values"],
...     disable_check=True
... )

>>> transformation = FuseBatchNorm2dInConv2d()
>>> transformed_model = transformation(traced_model)
```

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

#### optimum.fx.optimization.FuseBatchNorm1dInLinear[[optimum.fx.optimization.FuseBatchNorm1dInLinear]]

[Source](https://github.com/huggingface/optimum/blob/main/optimum/fx/optimization/transformations.py#L561)

Transformation that fuses `nn.BatchNorm1d` following or preceding `nn.Linear` into a single `nn.Linear`.
The fusion will be done only if the linear layer has the batch normalization as sole following node, or the batch normalization
has the linear layer as sole following node.

For example, fusion will not be done in the case

```
     Linear
     /   \
    /     \
ReLU   BatchNorm1d
```

Example:
```python
>>> from transformers.utils.fx import symbolic_trace
>>> from transformers import AutoModel

>>> from optimum.fx.optimization import FuseBatchNorm1dInLinear

>>> model = AutoModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
>>> model.eval()
>>> traced_model = symbolic_trace(
...     model,
...     input_names=["input_ids", "attention_mask", "pixel_values"],
...     disable_check=True
... )

>>> transformation = FuseBatchNorm1dInLinear()
>>> transformed_model = transformation(traced_model)
```

**Parameters:**

preserves_computation (`bool`, defaults to `False`) : Whether the transformation preserves the graph computation or not. If `True`, the original and the transformed graph should produce the same outputs.

### Quantization
https://huggingface.co/docs/optimum/main/concept_guides/quantization.md

# Quantization

Quantization is a technique to reduce the computational and memory costs of running inference by representing the
weights and activations with low-precision data types like 8-bit integer (`int8`) instead of the usual 32-bit floating
point (`float32`).

Reducing the number of bits means the resulting model requires less memory storage, consumes less energy (in theory), and
operations like matrix multiplication can be performed much faster with integer arithmetic. It also allows to run models
on embedded devices, which sometimes only support integer data types.

## Theory

The basic idea behind quantization is quite easy: going from high-precision representation (usually the regular 32-bit
floating-point) for weights and activations to a lower precision data type. The most common lower precision data types
are:

- `float16`, accumulation data type `float16`
- `bfloat16`, accumulation data type `float32`
- `int16`, accumulation data type `int32`
- `int8`, accumulation data type `int32`

The accumulation data type specifies the type of the result of accumulating (adding, multiplying, etc) values of the
data type in question. For example, let's consider two `int8` values `A = 127`, `B = 127`, and let's define `C` as the
sum of `A` and `B`:

```
C = A + B
```

Here the result is much bigger than the biggest representable value in `int8`, which is `127`. Hence the need for a larger
precision data type to avoid a huge precision loss that would make the whole quantization process useless.

## Quantization

The two most common quantization cases are `float32 -> float16` and `float32 -> int8`.

### Quantization to `float16`

Performing quantization to go from `float32` to `float16` is quite straightforward since both data types follow the same
representation scheme. The questions to ask yourself when quantizing an operation to `float16` are:

- Does my operation have a `float16` implementation?
- Does my hardware support `float16`? For instance, Intel CPUs [have been supporting `float16` as a storage type, but
computation is done after converting to `float32`](https://scicomp.stackexchange.com/a/35193). Full support will come
in Cooper Lake and Sapphire Rapids.
- Is my operation sensitive to lower precision?
For instance the value of epsilon in `LayerNorm` is usually very small (~ `1e-12`), but the smallest representable value in
`float16` is ~ `6e-5`, this can cause `NaN` issues.  The same applies for big values.

### Quantization to `int8`

Performing quantization to go from `float32` to `int8` is more tricky. Only 256 values can be represented in `int8`,
while `float32` can represent a very wide range of values. The idea is to find the best way to project our range `[a, b]`
of `float32` values  to the `int8` space.

Let's consider a float `x` in `[a, b]`, then we can write the following quantization scheme, also called the *affine
quantization scheme*:

```
x = S * (x_q - Z)
```

where:

- `x_q` is the quantized `int8` value associated to `x`
- `S` and `Z` are the quantization parameters
  - `S` is the scale, and is a positive `float32`
  - `Z` is called the zero-point, it is the `int8` value corresponding to the value `0` in the `float32` realm. This is
  important to be able to represent exactly the value `0` because it is used everywhere throughout machine learning
  models.

The quantized value `x_q` of `x` in `[a, b]` can be computed as follows:

```
x_q = round(x/S + Z)
```

And `float32` values outside of the `[a, b]` range are clipped to the closest representable value, so for any
floating-point number `x`:

```
x_q = clip(round(x/S + Z), round(a/S + Z), round(b/S + Z))

```

Usually `round(a/S + Z)` corresponds to the smallest representable value in the considered data type, and `round(b/S + Z)`
to the biggest one. But this can vary, for instance when using a *symmetric quantization scheme* as you will see in the next
paragraph.

### Symmetric and affine quantization schemes

The equation above is called the *affine quantization scheme* because the mapping from `[a, b]` to `int8` is an affine one.

A common special case of this scheme is the *symmetric quantization scheme*, where we consider a symmetric range of float values `[-a, a]`.
In this case the integer space is usually `[-127, 127]`, meaning that the `-128` is opted out of the regular `[-128, 127]` signed `int8` range.
The reason being that having a symmetric range allows to have `Z = 0`. While one value out of the 256 representable
values is lost, it can provide a speedup since a lot of addition operations can be skipped.

**Note**: To learn how the quantization parameters `S` and `Z` are computed, you can read the
[Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://arxiv.org/abs/1712.05877)
paper, or [Lei Mao's blog post](https://leimao.github.io/article/Neural-Networks-Quantization) on the subject.

### Per-tensor and per-channel quantization

Depending on the accuracy / latency trade-off you are targeting you can play with the granularity of the quantization parameters:

- Quantization parameters can be computed on a *per-tensor* basis, meaning that one pair of `(S, Z)` will be used per
tensor.
- Quantization parameters can be computed on a *per-channel* basis, meaning that it is possible to store a pair of
`(S, Z)` per element along one of the dimensions of a tensor. For example for a tensor of shape `[N, C, H, W]`, having
*per-channel* quantization parameters for the second dimension would result in having `C` pairs of `(S, Z)`. While this
can give a better accuracy, it requires more memory.

### Calibration

The section above described how quantization from `float32` to `int8` works, but one question
remains: how is the `[a, b]` range of `float32` values determined? That is where calibration comes in to play.

Calibration is the step during quantization where the `float32` ranges are computed. For weights it is quite easy since
the actual range is known at *quantization-time*. But it is less clear for activations, and different approaches exist:

1. Post training **dynamic quantization**: the range for each activation is computed on the fly at *runtime*. While this
gives great results without too much work, it can be a bit slower than static quantization because of the overhead
introduced by computing the range each time.
It is also not an option on certain hardware.
2. Post training **static quantization**: the range for each activation is computed in advance at *quantization-time*,
typically by passing representative data through the model and recording the activation values. In practice, the steps are:
    1. Observers are put on activations to record their values.
    2. A certain number of forward passes on a calibration dataset is done (around `200` examples is enough).
    3. The ranges for each computation are computed according to some *calibration technique*.
3. **Quantization aware training**: the range for each activation is computed at *training-time*, following the same idea
than post training static quantization. But "fake quantize" operators are used instead of observers: they record
values just as observers do, but they also simulate the error induced by quantization to let the model adapt to it.

For both post training static quantization and quantization aware training, it is necessary to define calibration
techniques, the most common are:

- Min-max: the computed range is `[min observed value, max observed value]`, this works well with weights.
- Moving average min-max: the computed range is `[moving average min observed value, moving average max observed value]`,
this works well with activations.
- Histogram: records a histogram of values along with min and max values, then chooses according to some criterion:
  - Entropy: the range is computed as the one minimizing the error between the full-precision and the quantized data.
  - Mean Square Error: the range is computed as the one minimizing the mean square error between the full-precision and
  the quantized data.
  - Percentile: the range is computed using a given percentile value `p` on the observed values. The idea is to try to have
  `p%` of the observed values in the computed range. While this is possible when doing affine quantization, it is not always
  possible to exactly match that when doing symmetric quantization. You can check [how it is done in ONNX
  Runtime](https://github.com/microsoft/onnxruntime/blob/2cb12caf9317f1ded37f6db125cb03ba99320c40/onnxruntime/python/tools/quantization/calibrate.py#L698)
  for more details.

### Practical steps to follow to quantize a model to `int8`

To effectively quantize a model to `int8`, the steps to follow are:

1. Choose which operators to quantize. Good operators to quantize are the one dominating in terms of computation time,
for instance linear projections and matrix multiplications.
2. Try post-training dynamic quantization, if it is fast enough stop here, otherwise continue to step 3.
3. Try post-training static quantization which can be faster than dynamic quantization but often with a drop in terms of
accuracy. Apply observers to your models in places where you want to quantize.
4. Choose a calibration technique and perform it.
5. Convert the model to its quantized form: the observers are removed and the `float32` operators are converted to their `int8`
counterparts.
6. Evaluate the quantized model: is the accuracy good enough? If yes, stop here, otherwise start again at step 3 but
with quantization aware training this time.

## Energy efficiency in practice

The introduction above notes that quantization "consumes less energy (in theory)." Systematic benchmarking across
NVIDIA Ada Lovelace (RTX 4090D) and Blackwell (RTX 5090) architectures reveals that the relationship between
quantization and energy consumption is more nuanced in practice:

- **Large models (≥5B parameters)**: NF4 quantization achieves near-FP16 energy consumption with significant memory
savings — the expected benefit holds.
- **Small models (<3B parameters)**: NF4 quantization can *increase* energy consumption by 25–56% despite achieving
75% memory compression. The dequantization overhead exceeds the memory bandwidth savings at this scale.
- **INT8 mixed-precision**: The default `llm_int8_threshold=6.0` in `bitsandbytes` adds 17–33% energy overhead
compared to FP16, which is a justified cost for maintaining model accuracy.
- **Batch size effect**: Increasing batch size from 1 to 8–64 reduces per-token energy by 84–96%, often outweighing
the impact of precision choice.

These findings suggest that energy-optimal deployment depends on model size, precision format, batch size, and
hardware generation. Quantization remains beneficial for memory reduction, but its energy impact should be validated
empirically for each deployment scenario.

For detailed benchmarks and interactive visualizations, see the
[EcoCompute-AI toolkit](https://github.com/hongping-zh/ecocompute-ai) and
[interactive dashboard](https://hongping-zh.github.io/ecocompute-dynamic-eval/).
The full dataset is available on the [Hugging Face Hub](https://huggingface.co/datasets/hongpingzhang/ecocompute-energy-efficiency)
and archived on [Zenodo](https://zenodo.org/records/18900289).

## Supported tools to perform quantization in 🤗 Optimum

🤗 Optimum provides APIs to perform quantization using different tools for different targets:

- The `optimum.onnxruntime` package allows to
[quantize and run ONNX models](https://huggingface.co/docs/optimum/onnxruntime/usage_guides/quantization) using the
ONNX Runtime tool.
- The `optimum.intel` package enables to [quantize](https://huggingface.co/docs/optimum/intel/optimization_inc) 🤗 Transformers
models while respecting accuracy and latency constraints.
- The `optimum.fx` package provides wrappers around the
[PyTorch quantization functions](https://pytorch.org/docs/stable/quantization-support.html#torch-quantization-quantize-fx)
to allow graph-mode quantization of 🤗 Transformers models in PyTorch. This is a lower-level API compared to the two
mentioned above, giving more flexibility, but requiring more work on your end.
- The `optimum.gptq` package allows to [quantize and run LLM models](../llm_quantization/usage_guides/quantization) with GPTQ.

## Going further: How do machines represent numbers?

The section is not fundamental to understand the rest. It explains in brief how numbers are represented in computers.
Since quantization is about going from one representation to another, it can be useful to have some basics, but it is
definitely not mandatory.

The most fundamental unit of representation for computers is the bit. Everything in computers is represented as a
sequence of bits, including numbers. But the representation varies whether the numbers in question are integers or
real numbers.

#### Integer representation

Integers are usually represented with the following bit lengths: `8`, `16`, `32`, `64`. When representing integers, two cases
are considered:

1. Unsigned (positive) integers: they are simply represented as a sequence of bits. Each bit corresponds to a power
of two (from `0` to `n-1` where `n` is the bit-length), and the resulting number is the sum of those powers of two.

Example: `19` is represented as an unsigned int8 as `00010011` because :
```
19 = 0 x 2^7 + 0 x 2^6 + 0 x 2^5 + 1 x 2^4 + 0 x 2^3 + 0 x 2^2 + 1 x 2^1 + 1 x 2^0
```

2. Signed integers: it is less straightforward to represent signed integers, and multiple approaches exist, the most
common being the *two's complement*. For more information, you can check the
[Wikipedia page](https://en.wikipedia.org/wiki/Signed_number_representations) on the subject.

#### Real numbers representation

Real numbers are usually represented with the following bit lengths: `16`, `32`, `64`.
The two main ways of representing real numbers are:

1. Fixed-point: there are fixed number of digits reserved for representing the integer part and the fractional part.
2. Floating-point: the number of digits for representing the integer and the fractional parts can vary.

The floating-point representation can represent bigger ranges of values, and this is the one we will be focusing on
since it is the most commonly used. There are three components in the floating-point representation:

1. The sign bit: this is the bit specifying the sign of the number.
2. The exponent part
  - 5 bits in `float16`
  - 8 bits in `bfloat16`
  - 8 bits in `float32`
  - 11 bits in `float64`
2. The mantissa
  - 11 bits in `float16` (10 explicitly stored)
  - 8 bits in `bfloat16` (7 explicitly stored)
  - 24 bits in `float32` (23 explicitly stored)
  - 53 bits in `float64` (52 explicitly stored)

For more information on the bits allocation for each data type, check the nice illustration on the Wikipedia page about
the [bfloat16 floating-point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format).

For a real number `x` we have:

```
x = sign x mantissa x (2^exponent)
```

## References

- The
[Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://arxiv.org/abs/1712.05877) paper
- The [Basics of Quantization in Machine Learning (ML) for Beginners](https://iq.opengenus.org/basics-of-quantization-in-ml/)
blog post
- The [How to accelerate and compress neural networks with quantization](https://tivadardanka.com/blog/neural-networks-quantization)
blog post
- The Wikipedia pages on integers representation [here](https://en.wikipedia.org/wiki/Integer_(computer_science)) and
[here](https://en.wikipedia.org/wiki/Signed_number_representations)
- The Wikipedia pages on
  - [bfloat16 floating-point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
  - [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
  - [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
  - [Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)

### Quantization
https://huggingface.co/docs/optimum/main/llm_quantization/usage_guides/quantization.md

# Quantization

## AutoGPTQ Integration

🤗 Optimum collaborated with [AutoGPTQ library](https://github.com/PanQiWei/AutoGPTQ) to provide a simple API that apply GPTQ quantization on language models. With GPTQ quantization, you can quantize your favorite language model to 8, 4, 3 or even 2 bits. This comes without a big drop of performance and with faster inference speed. This is supported by most GPU hardwares.

If you want to quantize 🤗 Transformers models with GPTQ, follow this [documentation](https://huggingface.co/docs/transformers/main_classes/quantization).

To learn more about the quantization technique used in GPTQ, please refer to:
- the [GPTQ](https://arxiv.org/pdf/2210.17323.pdf) paper
- the [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ) library used as the backend

Note that the AutoGPTQ library provides more advanced usage (triton backend, fused attention, fused MLP) that are not integrated with Optimum. For now, we leverage only the CUDA kernel for GPTQ.

### Requirements

You need to have the following requirements installed to run the code below:

- AutoGPTQ library:
`pip install auto-gptq`

- Optimum library:
`pip install --upgrade optimum`

- Install latest `transformers` library from source:
`pip install --upgrade git+https://github.com/huggingface/transformers.git`

- Install latest `accelerate` library:
`pip install --upgrade accelerate`

### Load and quantize a model

The `GPTQQuantizer` class is used to quantize your model. In order to quantize your model, you need to provide a few arguments:
- the number of bits: `bits`
- the dataset used to calibrate the quantization: `dataset`
- the model sequence length used to process the dataset: `model_seqlen`
- the block name to quantize: `block_name_to_quantize`

With 🤗 Transformers integration, you don't need to pass the `block_name_to_quantize` and `model_seqlen` as we can retrieve them. However, for custom model, you need to specify them. Also, make sure that your model is converted to `torch.float16` before quantization.

```py
from transformers import AutoModelForCausalLM, AutoTokenizer
from optimum.gptq import GPTQQuantizer, load_quantized_model
import torch
model_name = "facebook/opt-125m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

quantizer = GPTQQuantizer(bits=4, dataset="c4", block_name_to_quantize = "model.decoder.layers", model_seqlen = 2048)
quantized_model = quantizer.quantize_model(model, tokenizer)
```

GPTQ quantization only works for text model for now. Furthermore, the quantization process can take a lot of time depending on one's hardware (175B model = 4 gpu hours using NVIDIA A100). Please check on the Hugging Face Hub if there is not already a GPTQ quantized version of the model you would like to quantize.

### Save the model

To save your model, use the save method from `GPTQQuantizer` class. It will create a folder with your model state dict along with the quantization config.
```python
save_folder = "/path/to/save_folder/"
quantizer.save(model,save_folder)
```

### Load quantized weights

You can load your quantized weights by using the `load_quantized_model()` function.
Through the Accelerate library, it is possible to load a model faster with a lower memory usage. The model needs to be initialized using empty weights, with weights loaded as a next step.
```python
from accelerate import init_empty_weights
with init_empty_weights():
    empty_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
empty_model.tie_weights()
quantized_model = load_quantized_model(empty_model, save_folder=save_folder, device_map="auto")
```

### Exllama kernels for faster inference

With the release of exllamav2 kernels, you can get faster inference speed compared to exllama kernels for 4-bit model. It is activated by default: `disable_exllamav2=False` in `load_quantized_model()`. In order to use these kernels, you need to have the entire model on gpus.

```py
from optimum.gptq import GPTQQuantizer, load_quantized_model
import torch

from accelerate import init_empty_weights
with init_empty_weights():
    empty_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
empty_model.tie_weights()
quantized_model = load_quantized_model(empty_model, save_folder=save_folder, device_map="auto")
```

If you wish to use exllama kernels, you will have to change the version by setting `exllama_config`:

```py
from optimum.gptq import GPTQQuantizer, load_quantized_model
import torch

from accelerate import init_empty_weights
with init_empty_weights():
    empty_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
empty_model.tie_weights()
quantized_model = load_quantized_model(empty_model, save_folder=save_folder, device_map="auto", exllama_config = {"version":1})
```

Note that only 4-bit models are supported with exllama/exllamav2 kernels for now. Furthermore, it is recommended to disable exllama/exllamav2 kernels when you are finetuning your model with peft.

You can find the benchmark of these kernels [here](https://github.com/huggingface/optimum/tree/main/tests/benchmark#gptq-benchmark)

#### Fine-tune a quantized model

With the official support of adapters in the Hugging Face ecosystem, you can fine-tune models that have been quantized with GPTQ.
Please have a look at [`peft`](https://github.com/huggingface/peft) library for more details.
