# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/mamba.md

# Mamba

[Mamba](https://huggingface.co/papers/2312.00752) is a selective structured state space model (SSMs) designed to work around Transformers computational inefficiency when dealing with long sequences.  It is a completely attention-free architecture, and comprised of a combination of H3 and gated MLP blocks (Mamba block). Mamba's "content-based reasoning" allows it to focus on specific parts of an input depending on the current token. Mamba also uses a new hardware-aware parallel algorithm to compensate for the lack of convolutional operations. As a result, Mamba has fast inference and can scale to very long sequences.

You can find all the original Mamba checkpoints under the [State Space Models](https://huggingface.co/state-spaces) organization.

> [!TIP]
> This model was contributed by [Molbap](https://huggingface.co/Molbap) and [AntonV](https://huggingface.co/AntonV).
> Click on the Mamba models in the right sidebar for more examples of how to apply Mamba to different language tasks.

The example below demonstrates how to generate text with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline), [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel), and from the command line.

```py
import torch
from transformers import pipeline

pipeline = pipeline(
    task="text-generation",
    model="state-spaces/mamba-130m-hf",
    dtype=torch.float16,
    device=0
)
pipeline("Plants create energy through a process known as")
```

```py
import torch  
from transformers import AutoModelForCausalLM, AutoTokenizer  

tokenizer = AutoTokenizer.from_pretrained("state-spaces/mamba-130m-hf")
model = AutoModelForCausalLM.from_pretrained("state-spaces/mamba-130m-hf", dtype=torch.float16, device_map="auto",)  
input_ids = tokenizer("Plants create energy through a process known as", return_tensors="pt").to(model.device)  

output = model.generate(**input_ids)  
print(tokenizer.decode(output[0], skip_special_tokens=True)
```

```bash
echo -e "Plants create energy through a process known as" | transformers run --task text-generation --model state-spaces/mamba-130m-hf --device 0
```

Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the [Quantization](../quantization/overview) overview for more available quantization backends.

The example below uses [torchao](../quantization/torchao) to only quantize the weights to 4-bit integers.

```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TorchAoConfig
from torchao.quantization import Int4WeightOnlyConfig

quantization_config = Int4WeightOnlyConfig(group_size=128)
quantization_config = TorchAoConfig(quant_type=quant_config)
tokenizer = AutoTokenizer.from_pretrained("state-spaces/mamba-2.8b-hf")
model = AutoModelForCausalLM.from_pretrained("state-spaces/mamba-2.8b-hf", dtype=torch.bfloat16, quantization_config=quantization_config, device_map="auto",)
input_ids = tokenizer("Plants create energy through a process known as", return_tensors="pt").to(model.device)

output = model.generate(**input_ids)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Notes

- The current implementation uses the original CUDA kernels. The FlashAttention equivalent implementation is hosted in the [mamba-ssm](https://github.com/state-spaces/mamba) and [causal_conv1d](https://github.com/Dao-AILab/causal-conv1d) repositories. Make sure to install them if your hardware supports it!
- Mamba stacks `mixer` layers which are equivalent to `Attention` layers. You can find the main logic of Mamba in the `MambaMixer` class.
- The example below demonstrates how to fine-tune Mamba with [PEFT](https://huggingface.co/docs/peft).

  ```py
  from datasets import load_dataset
  from trl import SFTConfig, SFTTrainer
  from peft import LoraConfig

  model_id = "state-spaces/mamba-130m-hf"
  dataset = load_dataset("Abirate/english_quotes", split="train")
  training_args = SFTConfig(dataset_text_field="quote")
  lora_config =  LoraConfig(target_modules=["x_proj", "embeddings", "in_proj", "out_proj"])
  trainer = SFTTrainer(
      model=model_id,
      args=training_args,
      train_dataset=dataset,
      peft_config=lora_config,
  )
  trainer.train()
   ```

## MambaCache[[transformers.MambaCache]]

#### transformers.MambaCache[[transformers.MambaCache]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L48)

Cache for mamba model which does not have attention mechanism and key value states.

Example:

```python
>>> import torch
>>> from transformers import AutoTokenizer, MambaForCausalLM, MambaCache

>>> model = MambaForCausalLM.from_pretrained("state-spaces/mamba-130m-hf")
>>> tokenizer = AutoTokenizer.from_pretrained("state-spaces/mamba-130m-hf")

>>> inputs = tokenizer(text="My name is Mamba", return_tensors="pt")

>>> # Prepare a cache class and pass it to model's forward
>>> cache_params = MambaCache(config=model.config, max_batch_size=1, device=model.device, dtype=model.dtype)
>>> cache_position = torch.arange(len(inputs["input_ids"][0]), device=model.device)  # sequence length
>>> outputs = model(**inputs, cache_params=cache_params, cache_position=cache_position, use_cache=True)
>>> outputs.cache_params
```

update_conv_statetransformers.MambaCache.update_conv_statehttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L122[{"name": "layer_idx", "val": ": int"}, {"name": "new_conv_state", "val": ": Tensor"}, {"name": "cache_position", "val": ": LongTensor"}]

**Parameters:**

config (`PreTrainedConfig) : The configuration file defining the shape-related attributes required to initialize the static cache.

max_batch_size (`int`) : The maximum batch size with which the model will be used. Note that a new instance must be instantiated if a smaller batch size is used.

dtype (`torch.dtype`, *optional*, defaults to `torch.float16`) : The default `dtype` to use when initializing the layer.

device (`torch.device` or `str`, *optional*) : The device on which the cache should be initialized. Should be the same as the layer.
#### update_ssm_state[[transformers.MambaCache.update_ssm_state]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L139)
#### reset[[transformers.MambaCache.reset]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L144)

## MambaConfig[[transformers.MambaConfig]]

#### transformers.MambaConfig[[transformers.MambaConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/configuration_mamba.py#L25)

This is the configuration class to store the configuration of a [MambaModel](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaModel). It is used to instantiate a MAMBA
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the MAMBA
[state-spaces/mamba-2.8b](https://huggingface.co/state-spaces/mamba-2.8b) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import MambaConfig, MambaModel

>>> # Initializing a Mamba configuration
>>> configuration = MambaConfig()

>>> # Initializing a model (with random weights) from the configuration
>>> model = MambaModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 50280) : Vocabulary size of the MAMBA model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [MambaModel](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaModel).

hidden_size (`int`, *optional*, defaults to 768) : Dimensionality of the embeddings and hidden states.

state_size (`int`, *optional*, defaults to 16) : shape of the state space latents.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the model.

layer_norm_epsilon (`float`, *optional*, defaults to 1e-05) : The epsilon to use in the layer normalization layers.

pad_token_id (`int`, *optional*, defaults to 0) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 0) : The id of the beginning of sentence token in the vocabulary.

eos_token_id (`int`, *optional*, defaults to 0) : The id of the end of sentence token in the vocabulary.

expand (`int`, *optional*, defaults to 2) : Expanding factor used to determine the intermediate size.

conv_kernel (`int`, *optional*, defaults to 4) : Size of the convolution kernel.

use_bias (`bool`, *optional*, defaults to `False`) : Whether or not to use bias in ["in_proj", "out_proj"] of the mixer block

use_conv_bias (`bool`, *optional*, defaults to `True`) : Whether or not to use bias in the convolution layer of the mixer block.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

initializer_range (`float`, *optional*, defaults to 0.1) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

residual_in_fp32 (`bool`, *optional*, defaults to `True`) : Whether or not residuals should be in `float32`. If set to `False` residuals will keep the same `dtype` as the rest of the model

time_step_rank (`Union[int,str]`, *optional*, defaults to `"auto"`) : Rank of the discretization projection matrix. `"auto"` means that it will default to `math.ceil(self.hidden_size / 16)`

time_step_scale (`float`, *optional*, defaults to 1.0) : Scale used used to scale `dt_proj.bias`.

time_step_min (`float`, *optional*, defaults to 0.001) : Minimum `time_step` used to bound `dt_proj.bias`.

time_step_max (`float`, *optional*, defaults to 0.1) : Maximum `time_step` used to bound `dt_proj.bias`.

time_step_init_scheme (`float`, *optional*, defaults to `"random"`) : Init scheme used for `dt_proj.weight`. Should be one of `["random","uniform"]`

time_step_floor (`float`, *optional*, defaults to 0.0001) : Minimum clamping value of the `dt_proj.bias` layer initialization.

rescale_prenorm_residual (`bool`, *optional*, defaults to `False`) : Whether or not to rescale `out_proj` weights when initializing.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the cache should be used.

use_mambapy (`bool`, *optional*, defaults to `False`) : Determines the fallback strategy during training if the CUDA-based official implementation of Mamba is not available. If `True`, the mamba.py implementation is used. If `False`, the naive and slower implementation is used. Consider switching to the naive version if memory is limited.

## MambaModel[[transformers.MambaModel]]

#### transformers.MambaModel[[transformers.MambaModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L597)

The bare Mamba Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.MambaModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L622[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.LongTensor | None = None"}, {"name": "cache_params", "val": ": transformers.models.mamba.modeling_mamba.MambaCache | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **inputs_embeds** (`torch.LongTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_params** (`MambaCache`, *optional*) --
  If passed along, the model uses the previous state in all the blocks (which will give the output for the
  `input_ids` provided as if the model add `state_input_ids + input_ids` as context).
- **use_cache** (`bool`, *optional*) --
  If set to `True`, the `cache_params` is returned and can be used to quickly generate the next logits.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)0`transformers.models.mamba.modeling_mamba.MambaOutput` or `tuple(torch.FloatTensor)`A `transformers.models.mamba.modeling_mamba.MambaOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MambaConfig](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **cache_params** (`~models.mamba.modeling_mamba.MambaCache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
The [MambaModel](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([MambaModel](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.mamba.modeling_mamba.MambaOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.mamba.modeling_mamba.MambaOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MambaConfig](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **cache_params** (`~models.mamba.modeling_mamba.MambaCache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.

## MambaLMHeadModel[[transformers.MambaForCausalLM]]

#### transformers.MambaForCausalLM[[transformers.MambaForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L709)

The MAMBA Model transformer with a language modeling head on top (linear layer with weights tied to the input
embeddings).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.MambaForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/mamba/modeling_mamba.py#L793[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "cache_params", "val": ": transformers.models.mamba.modeling_mamba.MambaCache | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.Tensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_params** (`MambaCache`, *optional*) --
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
- **cache_position** (`torch.Tensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.mamba.modeling_mamba.MambaCausalLMOutput` or `tuple(torch.FloatTensor)`A `transformers.models.mamba.modeling_mamba.MambaCausalLMOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MambaConfig](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **cache_params** (`~models.mamba.modeling_mamba.MambaCache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
The [MambaForCausalLM](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
```

**Parameters:**

config ([MambaForCausalLM](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.mamba.modeling_mamba.MambaCausalLMOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.mamba.modeling_mamba.MambaCausalLMOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MambaConfig](/docs/transformers/v5.0.0/en/model_doc/mamba#transformers.MambaConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **cache_params** (`~models.mamba.modeling_mamba.MambaCache | None.cache_params`, defaults to `None`) -- The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
  avoid providing the old `input_ids`.

  Includes both the State space model state matrices after the selective scan, and the Convolutional states
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.

