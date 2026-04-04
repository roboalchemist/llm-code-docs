# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/mamba2.md

# Mamba 2

[Mamba 2](https://huggingface.co/papers/2405.21060) is based on the state space duality (SSD) framework which connects structured state space models (SSMs) and attention variants. It uses a more efficient SSD algorithm that is 2-8x faster than Mamba and modifies the architecture to enable tensor parallelism and a grouped-value attention (GVA) head structure.

You can find all the original Mamba 2 checkpoints under the [State Space Models](https://huggingface.co/state-spaces) organization, but the examples shown below use [mistralai/Mamba-Codestral-7B-v0.1](https://huggingface.co/mistralai/Mamba-Codestral-7B-v0.1) because a Hugging Face implementation isn't supported yet for the original checkpoints.

Other Mamba 2-based architectures include [Bamba](./bamba), [FalconH1](./falcon_h1), and [Zamba2](./zamba2).

> [!TIP]
> This model was contributed by [ArthurZ](https://huggingface.co/ArthurZ).
> Click on the Mamba models in the right sidebar for more examples of how to apply Mamba to different language tasks.

The example below demonstrates how to generate text with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline), [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel), and from the command line.

```python
import torch
from transformers import pipeline

pipeline = pipeline(
    task="text-generation",
    model="mistralai/Mamba-Codestral-7B-v0.1",
    dtype=torch.bfloat16,
    device=0
)
pipeline("Plants create energy through a process known as")
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mamba-Codestral-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mamba-Codestral-7B-v0.1", dtype=torch.bfloat16, device_map="auto")
input_ids = tokenizer("Plants create energy through a process known as", return_tensors="pt").to(model.device)

output = model.generate(**input_ids)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

```bash
echo -e "Plants create energy through a process known as" | transformers run --task text-generation --model mistralai/Mamba-Codestral-7B-v0.1 --device 0
```

Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the [Quantization](../quantization/overview) overview for more available quantization backends.

The example below uses [torchao](../quantization/torchao) to only quantize the weights to 4-bit integers.

```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TorchAoConfig

quantization_config = TorchAoConfig("int4_weight_only", group_size=128)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mamba-Codestral-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mamba-Codestral-7B-v0.1", dtype=torch.bfloat16, quantization_config=quantization_config, device_map="auto")
input_ids = tokenizer("Plants create energy through a process known as", return_tensors="pt").to(model.device)

output = model.generate(**input_ids)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Notes

- Codestral Mamba has `groups=8` which are similar to the number of kv heads in an attention-based model.
- Codestral Mamba has two different forward passes, `torch_forward` or `cuda_kernels_forward`, and their results are expected to be slightly different.
  - `torch_forward` without compilation is 3-4x faster than `cuda_kernels_forward`.
  - `cuda_kernels_forward` uses the original CUDA kernels if they're available in your environment. It is slower during prefill because it requires a "warmup run" due to the higher CPU overhead (see [these](https://github.com/state-spaces/mamba/issues/389#issuecomment-2171755306) [comments](https://github.com/state-spaces/mamba/issues/355#issuecomment-2147597457) for more details).

- There are no positional embeddings in this model, but there is an `attention_mask` and a specific logic to mask out hidden states in two places in the case of batched generation (see this [comment](https://github.com/state-spaces/mamba/issues/66#issuecomment-1863563829) for more details). This (and the addition of the reimplemented Mamba 2 kernels) results in a slight discrepancy between batched and cached generation.

- The SSM algorithm heavily relies on tensor contractions, which have matmul equivalents but the order of operations is slightly different. This makes the difference greater at smaller precisions.

- Hidden states that correspond to padding tokens is shutdown in 2 places and is mostly tested with left-padding. Right-padding propagates noise down the line and is not guaranteed to yield satisfactory results. `tokenizer.padding_side = "left"` ensures you are using the correct padding side.

- The example below demonstrates how to fine-tune Mamba 2 with [PEFT](https://huggingface.co/docs/peft).

```python
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

model_id = "mistralai/Mamba-Codestral-7B-v0.1"
dataset = load_dataset("Abirate/english_quotes", split="train")
training_args = SFTConfig(dataset_text_field="quote", gradient_checkpointing=True, per_device_train_batch_size=4)
lora_config =  LoraConfig(target_modules=["x_proj", "embeddings", "in_proj", "out_proj"])
trainer = SFTTrainer(
    model=model_id,
    args=training_args,
    train_dataset=dataset,
    peft_config=lora_config,
)
trainer.train()
```

## Mamba2Config[[transformers.Mamba2Config]]

#### transformers.Mamba2Config[[transformers.Mamba2Config]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba2/configuration_mamba2.py#L25)

This is the configuration class to store the configuration of a [Mamba2Model](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Model). It is used to instantiate a MAMBA2
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the MAMBA2
[state-spaces/mamba2-2.8b](https://huggingface.co/state-spaces/mamba2-2.8b) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import Mamba2Config, Mamba2Model

>>> # Initializing a Mamba2 configuration
>>> configuration = Mamba2Config()

>>> # Initializing a model (with random weights) from the configuration
>>> model = Mamba2Model(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

num_heads (`int`, *optional*, defaults to 128) : Number of heads for the evolution matrices of mamba 2.

head_dim (`int`, *optional*, defaults to 64) : Dimension of each head.

vocab_size (`int`, *optional*, defaults to 32768) : Vocabulary size of the MAMBA2 model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [Mamba2Model](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Model).

hidden_size (`int`, *optional*, defaults to 4096) : Dimensionality of the embeddings and hidden states.

state_size (`int`, *optional*, defaults to 128) : shape of the state space latents.

num_hidden_layers (`int`, *optional*, defaults to 64) : Number of hidden layers in the model.

layer_norm_epsilon (`float`, *optional*, defaults to 1e-05) : The epsilon to use in the layer normalization layers.

pad_token_id (`int`, *optional*, defaults to 1) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 0) : The id of the beginning of sentence token in the vocabulary.

eos_token_id (`int`, *optional*, defaults to 2) : The id of the end of sentence token in the vocabulary.

expand (`int`, *optional*, defaults to 2) : Expanding factor used to determine the intermediate size.

conv_kernel (`int`, *optional*, defaults to 4) : Size of the convolution kernel.

n_groups (`int`, *optional*, defaults to 8) : Number of groups for the evolution matrices of mamba 2.

use_bias (`bool`, *optional*, defaults to `False`) : Whether or not to use bias in ["in_proj", "out_proj"] of the mixer block

use_conv_bias (`bool`, *optional*, defaults to `True`) : Whether or not to use bias in the convolution layer of the mixer block.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

initializer_range (`float`, *optional*, defaults to 0.1) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

residual_in_fp32 (`bool`, *optional*, defaults to `True`) : Whether or not residuals should be in `float32`. If set to `False` residuals will keep the same `dtype` as the rest of the model

time_step_rank (`Union[int,str]`, *optional*, defaults to `"auto"`) : Rank of the discretization projection matrix. `"auto"` means that it will default to `math.ceil(self.hidden_size / 16)`

time_step_min (`float`, *optional*, defaults to 0.001) : Minimum `time_step` used to bound `dt_proj.bias`.

time_step_max (`float`, *optional*, defaults to 0.1) : Maximum `time_step` used to bound `dt_proj.bias`.

time_step_floor (`float`, *optional*, defaults to 0.0001) : Minimum clamping value of the `dt_proj.bias` layer initialization.

time_step_limit (`tuple`, *optional*, defaults to `(0.0, inf)`) : Accepted range of time step values.

rescale_prenorm_residual (`bool`, *optional*, defaults to `False`) : Whether or not to rescale `out_proj` weights when initializing.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the cache should be used.

rms_norm (`bool`, *optional*, defaults to `True`) : Whether to use RMS norm or not.

chunk_size (`int`, *optional*, defaults to 256) : Size of the chunks that will comprise the sequence.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie word embeddings or not.

## Mamba2Model[[transformers.Mamba2Model]]

#### transformers.Mamba2Model[[transformers.Mamba2Model]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba2/modeling_mamba2.py#L817)

The bare Mamba2 Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Mamba2Model.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba2/modeling_mamba2.py#L842[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.LongTensor | None = None"}, {"name": "cache_params", "val": ": transformers.models.mamba2.modeling_mamba2.Mamba2Cache | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **inputs_embeds** (`torch.LongTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_params** (`Mamba2Cache`, *optional*) --
  If passed along, the model uses the previous state in all the blocks (which will give the output for the
  `input_ids` provided as if the model add `state_input_ids + input_ids` as context).
- **use_cache** (`bool`, *optional*) --
  If set to `True`, the `cache_params` is returned and can be used to quickly generate the next logits.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(batch_size,)`, *optional*) --
  The position of the current input in the cache. This is used to ensure that the cache is correctly updated.
  If `cache_params` is passed, `cache_position` should also be passed.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)0`transformers.models.mamba2.modeling_mamba2.Mamba2Output` or `tuple(torch.FloatTensor)`A `transformers.models.mamba2.modeling_mamba2.Mamba2Output` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Mamba2Config](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Config)) and inputs.

- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **cache_params** (`~models.mamba2.modeling_mamba2.Mamba2Cache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
The [Mamba2Model](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Model) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Mamba2Model](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Model)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.mamba2.modeling_mamba2.Mamba2Output` or `tuple(torch.FloatTensor)``

A `transformers.models.mamba2.modeling_mamba2.Mamba2Output` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Mamba2Config](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Config)) and inputs.

- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **cache_params** (`~models.mamba2.modeling_mamba2.Mamba2Cache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.

## Mamba2LMHeadModel[[transformers.Mamba2ForCausalLM]]

#### transformers.Mamba2ForCausalLM[[transformers.Mamba2ForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba2/modeling_mamba2.py#L932)

The MAMBA2 Model transformer with a language modeling head on top (linear layer with weights not tied to the input
embeddings).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Mamba2ForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba2/modeling_mamba2.py#L997[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "cache_params", "val": ": transformers.models.mamba2.modeling_mamba2.Mamba2Cache | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_params** (`Mamba2Cache`, *optional*) --
  If passed along, the model uses the previous state in all the blocks (which will give the output for the
  `input_ids` provided as if the model add `state_input_ids + input_ids` as context).
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
  `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
  are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, the `cache_params` is returned and can be used to quickly generate the next logits.
- **cache_position** (`torch.LongTensor` of shape `(batch_size,)`, *optional*) --
  The position of the current input in the cache. This is used to ensure that the cache is correctly updated.
  If `cache_params` is passed, `cache_position` should also be passed.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.mamba2.modeling_mamba2.Mamba2CausalLMOutput` or `tuple(torch.FloatTensor)`A `transformers.models.mamba2.modeling_mamba2.Mamba2CausalLMOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Mamba2Config](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Config)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **cache_params** (`~models.mamba2.modeling_mamba2.Mamba2Cache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
The [Mamba2ForCausalLM](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2ForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
```

**Parameters:**

config ([Mamba2ForCausalLM](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2ForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.mamba2.modeling_mamba2.Mamba2CausalLMOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.mamba2.modeling_mamba2.Mamba2CausalLMOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Mamba2Config](/docs/transformers/v5.0.0/en/model_doc/mamba2#transformers.Mamba2Config)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **cache_params** (`~models.mamba2.modeling_mamba2.Mamba2Cache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.

