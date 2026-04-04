# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/fuyu.md

# Fuyu

## Overview

The Fuyu model was created by [ADEPT](https://www.adept.ai/blog/fuyu-8b), and authored by Rohan Bavishi, Erich Elsen, Curtis Hawthorne, Maxwell Nye, Augustus Odena, Arushi Somani, Sağnak Taşırlar.

The authors introduced Fuyu-8B, a decoder-only multimodal model based on the classic transformers architecture, with query and key normalization. A linear encoder is added to create multimodal embeddings from image inputs.

By treating image tokens like text tokens and using a special image-newline character, the model knows when an image line ends. Image positional embeddings are removed. This avoids the need for different training phases for various image resolutions. With 8 billion parameters and licensed under CC-BY-NC, Fuyu-8B is notable for its ability to handle both text and images, its impressive context size of 16K, and its overall performance.

The `Fuyu` models were trained using `bfloat16`, but the original inference uses `float16` The checkpoints uploaded on the hub use `dtype = 'float16'` which will be
used by the `AutoModel` API to cast the checkpoints from `torch.float32` to `torch.float16`.

The `dtype` of the online weights is mostly irrelevant, unless you are using `dtype="auto"` when initializing a model using `model = AutoModelForCausalLM.from_pretrained("path", dtype = "auto")`. The reason is that the model will first be downloaded ( using the `dtype` of the checkpoints online) then it will be cast to the default `dtype` of `torch` (becomes `torch.float32`). Users should specify the `dtype` they want, and if they don't it will be `torch.float32`.

Finetuning the model in `float16` is not recommended and known to produce `nan`, as such the model should be fine-tuned in `bfloat16`.

Tips:

- To convert the model, you need to clone the original repository using `git clone https://github.com/persimmon-ai-labs/adept-inference`, then get the checkpoints:

```bash
git clone https://github.com/persimmon-ai-labs/adept-inference
wget path/to/fuyu-8b-model-weights.tar
tar -xvf fuyu-8b-model-weights.tar
python src/transformers/models/fuyu/convert_fuyu_weights_to_hf.py  --input_dir /path/to/downloaded/fuyu/weights/ --output_dir /output/path \
    --pt_model_path /path/to/fuyu_8b_release/iter_0001251/mp_rank_00/model_optim_rng.pt
    --ada_lib_path /path/to/adept-inference
```

For the chat model:

```bash
wget https://axtkn4xl5cip.objectstorage.us-phoenix-1.oci.customer-oci.com/n/axtkn4xl5cip/b/adept-public-data/o/8b_chat_model_release.tar
tar -xvf 8b_base_model_release.tar
```

Then, model can be loaded via:

```py
from transformers import FuyuConfig, FuyuForCausalLM
model_config = FuyuConfig()
model = FuyuForCausalLM(model_config).from_pretrained('/output/path')
```

Inputs need to be passed through a specific Processor to have the correct formats.
A processor requires an image_processor and a tokenizer. Hence, inputs can be loaded via:

```py
from PIL import Image
from transformers import AutoTokenizer
from transformers.models.fuyu.processing_fuyu import FuyuProcessor
from transformers.models.fuyu.image_processing_fuyu_fast import FuyuImageProcessorFast

tokenizer = AutoTokenizer.from_pretrained('adept-hf-collab/fuyu-8b')
image_processor = FuyuImageProcessorFast()

processor = FuyuProcessor(image_processor=image_processor, tokenizer=tokenizer)
text_prompt = "Generate a coco-style caption.\\n"

bus_image_url = "https://huggingface.co/datasets/hf-internal-testing/fixtures-captioning/resolve/main/bus.png"
bus_image_pil = Image.open(io.BytesIO(requests.get(bus_image_url).content))
inputs_to_model = processor(images=bus_image_pil, text=text_prompt)

```

This model was contributed by [Molbap](https://huggingface.co/Molbap).
The original code can be found [here](https://github.com/persimmon-ai-labs/adept-inference).

- Fuyu uses a `sentencepiece` based tokenizer, with a `Unigram` model. It supports bytefallback, which is only available in `tokenizers==0.14.0` for the fast tokenizer.
The `LlamaTokenizer` is used as it is a standard wrapper around sentencepiece.

- The authors suggest to use the following prompt for image captioning: `f"Generate a coco-style caption.\\n"`

## FuyuConfig[[transformers.FuyuConfig]]

#### transformers.FuyuConfig[[transformers.FuyuConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/configuration_fuyu.py#L25)

This is the configuration class to store the configuration of a [FuyuForCausalLM](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuForCausalLM). It is used to instantiate an
Fuyu model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the
[adept/fuyu-8b](https://huggingface.co/adept/fuyu-8b).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import FuyuConfig

>>> # Initializing a Fuyu fuyu-7b style configuration
>>> configuration = FuyuConfig()
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 262144) : Vocabulary size of the Fuyu model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [FuyuForCausalLM](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuForCausalLM)

hidden_size (`int`, *optional*, defaults to 4096) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 16384) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 36) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 64) : Number of attention heads for each attention layer in the Transformer encoder.

hidden_act (`str` or `function`, *optional*, defaults to `"relu2"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 16384) : The maximum sequence length that this model might ever be used with.

image_size (`int`, *optional*, defaults to 300) : The input image size.

patch_size (`int`, *optional*, defaults to 30) : The input vision transformer encoding patch size.

num_channels (`int`, *optional*, defaults to 3) : The input image number of channels.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

layer_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`. Whether to tie weight embeddings

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie input and output embeddings.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

qk_layernorm (`bool`, *optional*, defaults to `True`) : Whether or not to normalize the Queries and Keys after projecting the hidden states

hidden_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio after applying the MLP to the hidden states.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio after computing the attention scores.

pad_token_id (`int`, *optional*) : The id of the *padding* token.

bos_token_id (`int`, *optional*, defaults to 1) : The id of the *beginning-of-sequence* token.

eos_token_id (`Union[int, list[int]]`, *optional*, defaults to 2) : The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.

image_token_id (`int`, *optional*, defaults to 71011) : The id of the image placeholder token.

text_config (`dict`, *optional*) : Dictionary of configuration options used to initialize the `language```Aut`.

## FuyuModel[[transformers.FuyuModel]]

#### transformers.FuyuModel[[transformers.FuyuModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L51)

The Fuyu model which consists of a vision backbone and a language model, without a language modeling head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.FuyuModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L153[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "image_patches", "val": ": torch.Tensor | None = None"}, {"name": "image_patches_indices", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **image_patches** (`torch.FloatTensor` of shape `(batch_size, num_total_patches, patch_size_ x patch_size x num_channels)`, *optional*) --
  Image patches to be used as continuous embeddings. The patches are flattened and then projected to the
  hidden size of the model.
- **image_patches_indices** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Tensor of indices of the image patches in the input_ids tensor.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [FuyuModel](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
#### gather_continuous_embeddings[[transformers.FuyuModel.gather_continuous_embeddings]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L73)

This function places the continuous_embeddings into the word_embeddings at the locations
indicated by image_patch_input_indices. Different batch elements can have different numbers of continuous
embeddings.

**Parameters:**

word_embeddings (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) : Tensor of word embeddings.

continuous_embeddings (`torch.FloatTensor` of shape `(batch_size, num_patches, hidden_size)`) : Tensor of continuous embeddings. The length of the list is the batch size. Each entry is shape [num_image_embeddings, hidden], and num_image_embeddings needs to match the number of non-negative indices in image_patch_input_indices for that batch element.

image_patch_input_indices (`torch.LongTensor` of shape `(batch_size, sequence_length)`) : Tensor of indices of the image patches in the input_ids tensor.
#### get_image_features[[transformers.FuyuModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L117)

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **pooler_output** (`torch.FloatTensor` of shape `(batch_size, hidden_size)`) -- Last layer hidden-state of the first token of the sequence (classification token) after further processing
  through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
  the classification token after processing through a linear layer and a tanh activation function. The linear
  layer weights are trained from the next sentence prediction (classification) objective during pretraining.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
#### get_placeholder_mask[[transformers.FuyuModel.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L129)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.

## FuyuForCausalLM[[transformers.FuyuForCausalLM]]

#### transformers.FuyuForCausalLM[[transformers.FuyuForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L233)

Fuyu Model with a language modeling head on top for causal language model conditioned on image patches and text.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.FuyuForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/modeling_fuyu.py#L253[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "image_patches", "val": ": torch.Tensor | None = None"}, {"name": "image_patches_indices", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "labels", "val": ": torch.Tensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "logits_to_keep", "val": ": int | None = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **image_patches** (`torch.FloatTensor` of shape `(batch_size, num_total_patches, patch_size_ x patch_size x num_channels)`, *optional*) --
  Image patches to be used as continuous embeddings. The patches are flattened and then projected to the
  hidden size of the model.
- **image_patches_indices** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Tensor of indices of the image patches in the input_ids tensor.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.text_config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.text_config.vocab_size]`.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **logits_to_keep** (`int`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [FuyuForCausalLM](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import FuyuProcessor, FuyuForCausalLM
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> processor = FuyuProcessor.from_pretrained("adept/fuyu-8b")
>>> model = FuyuForCausalLM.from_pretrained("adept/fuyu-8b")

>>> url = "https://huggingface.co/datasets/hf-internal-testing/fixtures-captioning/resolve/main/bus.png"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))
>>> prompt = "Generate a coco-style caption.\n"

>>> inputs = processor(images=image, text=prompt, return_tensors="pt")
>>> outputs = model(**inputs)

>>> generated_ids = model.generate(**inputs, max_new_tokens=7)
>>> generation_text = processor.batch_decode(generated_ids[:, -7:], skip_special_tokens=True)
>>> print(generation_text[0])
A blue bus parked on the side of a road.
```

**Parameters:**

config ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([FuyuConfig](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## FuyuImageProcessor[[transformers.FuyuImageProcessor]]

#### transformers.FuyuImageProcessor[[transformers.FuyuImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/image_processing_fuyu.py#L197)

This class should handle the image processing part before the main FuyuForCausalLM. In particular, it should
handle:

- Processing Images:
  Taking a batch of images as input. If the images are variable-sized, it resizes them based on the desired patch
  dimensions. The image output is always img_h, img_w of (1080, 1920)

  Then, it patches up these images using the patchify_image function.

- Creating Image Input IDs:
  For each patch, a placeholder ID is given to identify where these patches belong in a token sequence. For
  variable-sized images, each line of patches is terminated with a newline ID.

- Image Patch Indices:
  For each image patch, the code maintains an index where these patches should be inserted in a token stream.

__call__transformers.FuyuImageProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/image_processing_utils.py#L48[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ImagesKwargs]"}]
Preprocess an image or a batch of images.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image to `size`.

size (`dict[str, int]`, *optional*, defaults to `{"height" : 1080, "width": 1920}`): Dictionary in the format `{"height": int, "width": int}` specifying the size of the output image.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`) : `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BILINEAR`.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the image to `size`.

padding_value (`float`, *optional*, defaults to 1.0) : The value to pad the image with.

padding_mode (`str`, *optional*, defaults to `"constant"`) : The padding mode to use when padding the image.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image.

image_mean (`float`, *optional*, defaults to 0.5) : The mean to use when normalizing the image.

image_std (`float`, *optional*, defaults to 0.5) : The standard deviation to use when normalizing the image.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image.

rescale_factor (`float`, *optional*, defaults to `1 / 255`) : The factor to use when rescaling the image.

patch_size (`dict[str, int]`, *optional*, defaults to `{"height" : 30, "width": 30}`): Dictionary in the format `{"height": int, "width": int}` specifying the size of the patches.

## FuyuImageProcessor[[transformers.FuyuImageProcessorFast]]

#### transformers.FuyuImageProcessorFast[[transformers.FuyuImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/image_processing_fuyu_fast.py#L50)

Constructs a fast Fuyu image processor.

__call__transformers.FuyuImageProcessorFast.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/image_processing_utils.py#L48[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ImagesKwargs]"}]
Preprocess an image or a batch of images.

## FuyuProcessor[[transformers.FuyuProcessor]]

#### transformers.FuyuProcessor[[transformers.FuyuProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/processing_fuyu.py#L336)

Constructs a FuyuProcessor which wraps a image processor and a tokenizer into a single processor.

[FuyuProcessor](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuProcessor) offers all the functionalities of [FuyuImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessorFast) and `tokenizer_class`. See the
[~FuyuImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessorFast) and `~tokenizer_class` for more information.

__call__transformers.FuyuProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/fuyu/processing_fuyu.py#L484[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.fuyu.processing_fuyu.FuyuProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`, *optional*) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **text** (`Union[str, list]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0`FuyuBatchEncoding`A `FuyuBatchEncoding` with the following fields:

- **input_ids** -- Tensor of token ids to be fed to a model. Returned when `text` is not `None`.
- **image_patches** -- List of Tensor of image patches. Returned when `images` is not `None`.
- **image_patches_indices** -- Tensor of indices where patch embeddings have to be inserted by the model.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model when
  `return_attention_mask=True`.

**Parameters:**

image_processor (`FuyuImageProcessorFast`) : The image processor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

**Returns:**

``FuyuBatchEncoding``

A `FuyuBatchEncoding` with the following fields:

- **input_ids** -- Tensor of token ids to be fed to a model. Returned when `text` is not `None`.
- **image_patches** -- List of Tensor of image patches. Returned when `images` is not `None`.
- **image_patches_indices** -- Tensor of indices where patch embeddings have to be inserted by the model.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model when
  `return_attention_mask=True`.

