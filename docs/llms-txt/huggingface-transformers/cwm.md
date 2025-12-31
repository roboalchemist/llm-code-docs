# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/cwm.md

# Code World Model (CWM)

## Overview

The Code World Model (CWM) model was proposed in [CWM: An Open-Weights LLM for Research on Code
Generation with World Models](https://ai.facebook.com/research/publications/cwm) by Meta FAIR CodeGen Team.
CWM is an LLM for code generation and reasoning about code that has, in particular, been trained
to better represent and reason about how code and commands affect the state of a program or system.
Specifically, we mid-trained CWM on a large number of observation-action trajectories from Python
execution traces and agentic interactions in containerized environments. We post-trained with
extensive multi-task RL in verifiable coding, math, and multi-turn software engineering environments.

The abstract from the paper is the following:

> *We release Code World Model (CWM), a 32-billion-parameter open-weights LLM, to advance research
on code generation with world models. To improve code understanding beyond what can be learned
from training on static code alone, we mid-train CWM on a large amount of observation-action
trajectories from Python interpreter and agentic Docker environments, and perform extensive multi-
task reasoning RL in verifiable coding, math, and multi-turn software engineering environments. With
CWM, we provide a strong testbed for researchers to explore the opportunities world modeling affords
for improving code generation with reasoning and planning in computational environments. We
present first steps of how world models can benefit agentic coding, enable step-by-step simulation of
Python code execution, and show early results of how reasoning can benefit from the latter. CWM is
a dense, decoder-only LLM trained with a context size of up to 131 k tokens. Independent of its world
modeling capabilities, CWM offers strong performance on general coding and math tasks: it reaches
pass@1 scores of 65.8 % on SWE-bench Verified (with test-time scaling), 68.9 % on LiveCodeBench,
96.6 % on Math-500, and 76.0 % on AIME 2024. To support further research on code world modeling,
we release model checkpoints after mid-training, SFT, and RL.*

Tips:

CWM requires a dedicated system prompt to function optimally during inference. Without proper prompt
configuration, CWM's output quality may be significantly degraded. The following serves as the default
system prompt for reasoning tasks. For agentic workflows, append the relevant tool specifications
after this base prompt. Checkout the original code repository for more details.

```text
You are a helpful AI assistant. You always reason before responding, using the following format:

your internal reasoning

your external response
```

This model was contributed by [Meta FAIR CodeGen Team](https://huggingface.co/facebook).
The original code can be found [here](https://github.com/facebookresearch/cwm).

## Usage examples

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'facebook/cwm'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto"
)

system_prompt = """
You are a helpful AI assistant. You always reason before responding, using the following format:

your internal reasoning

your external response
""".strip()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Write a haiku about recursion in programming."}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True, # Switches between thinking and non-thinking modes. Default is True.
    preserve_previous_think=True, # Switches between keeping thinking blocks from previous messages or not. Default is True.
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()
print(tokenizer.decode(output_ids))
```

Produces the following output:

    Okay, I need to write a haiku about recursion in programming. Let's start by recalling what recursion is. Recursion is a programming technique where a function calls itself in its own definition, often used to solve problems that can be broken down into smaller, similar sub-problems.

    A haiku is a three-line poem with a syllable count of 5-7-5. So, I need to capture the essence of recursion in a concise and poetic way. Let's think about the key elements of recursion: the function calling itself, the base case that stops the recursion, and the idea of breaking down problems into smaller parts.

    Maybe I can use imagery related to mirrors or reflections, since recursion often involves a function reflecting or repeating itself. Alternatively, I could use natural imagery like a spiral or a tree, which suggests self-similar patterns.

    Let me try to come up with some ideas. For example, "Function calls itself" could be a starting point. But how to make that into a haiku? Maybe something like:

    Function calls itself
    Base case stops the endless loop
    Spiral of code

    Hmm, that's a start. But maybe I can make it more poetic. Let's think about the idea of a function calling itself as a kind of infinite loop, but with a base case that stops it. That's like a spiral that unwinds at the center.

    Another angle: recursion is often used for problems that have a recursive structure, like tree traversals or factorial calculations. Maybe I can use a natural image to represent that.

    How about:

    Branches split again
    Leaves unfold in endless dance
    Roots hold the base case

    That's a bit more poetic. The branches splitting represent the recursive calls, the leaves unfolding could represent the processing of each sub-problem, and the roots holding the base case are what stops the recursion.

    Alternatively, maybe something simpler:

    Mirror within mirror
    Reflections infinite deep
    Base case breaks the glass

    This uses the mirror metaphor to represent the function calling itself, with the base case being the point where the recursion stops, breaking the infinite reflection.

    I think I like the mirror idea better. Let me refine that:

    Mirror within mirror
    Infinite reflections dance
    Base case shatters glass

    Yes, that seems to capture the idea of recursion well. The mirror represents the function calling itself, the infinite reflections are the recursive calls, and the base case shattering the glass is what stops the recursion.

    Let me check the syllable count:

    Mirror within mirror (5 syllables: Mir-ror-with-in-mir-ror)
    Infinite reflections dance (7 syllables: In-fi-nite-ref-lec-tions-dance)
    Base case shatters glass (5 syllables: Base-case-shat-ters-glass)

    Yes, that fits the 5-7-5 structure. I think that's a good haiku about recursion.
    
    Mirror within mirror
    Infinite reflections dance
    Base case shatters glass

## CwmConfig[[transformers.CwmConfig]]

#### transformers.CwmConfig[[transformers.CwmConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/configuration_cwm.py#L27)

Configuration for Code World Model (CWM).
This is an inherited Llama3-compatible configuration with layer-interleaved
sliding-window attention. Configures a `CwmModel`. Designed to yield a configuration mirroring the model in the
[facebook/cwm](https://huggingface.co/facebook/cwm) architecture by default. Other models include:
- [facebook/cwm-sft](https://huggingface.co/facebook/cwm-sft)
- [facebook/cwm-pretrain](https://huggingface.co/facebook/cwm-pretrain)

**Parameters:**

vocab_size (`int`, *optional*, defaults to 128256) : Vocabulary size of the CWM model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [CwmModel](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmModel)

hidden_size (`int`, *optional*, defaults to 6144) : Dimension of the hidden representations

intermediate_size (`int`, *optional*, defaults to 21504) : Dimension of the MLP representations

num_hidden_layers (`int`, *optional*, defaults to 64) : Number of hidden layers in the Transformer decoder

num_attention_heads (`int`, *optional*, defaults to 48) : Number of attention heads for each attention layer in the Transformer decoder

num_key_value_heads (`int`, *optional*, defaults to 8) : This is the number of key_value heads that should be used to implement Grouped Query Attention (GQA). If it is not specified, will default to `num_attention_heads`.

head_dim (`int`, *optional*, defaults to 128) : The attention head dimension.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 131072) : The maximum sequence length that this model might ever be used with. CWM's attention allows sequence lengths up to 131072 tokens.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

pad_token_id (`int`, *optional*) : Padding token id.

eos_token_id (`int` or `list[int]`, *optional*, defaults to `[128001, 128008, 128009]`) : The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.

bos_token_id (`int`, *optional*, defaults to 128000) : The id of the *beginning-of-sequence* token.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie weight embeddings

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

pretraining_tp (`int`, *optional*, defaults to 1) : Tensor parallelism degree used during pretraining. See [this document](https://huggingface.co/docs/transformers/parallelism) and [this issue](https://github.com/pytorch/pytorch/issues/76232).

mlp_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in up_proj, down_proj and gate_proj layers in the MLP layers.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

sliding_window (`int`, *optional*, defaults to 8192) : Sliding window attention window size.

layer_types (`List[str]`, *optional*) : List of layer types for each layer. Each element should be either "full_attention" or "sliding_attention". If not specified, will default to alternating pattern based on the provided window pattern.

## CwmPreTrainedModel[[transformers.CwmPreTrainedModel]]

#### transformers.CwmPreTrainedModel[[transformers.CwmPreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/modeling_cwm.py#L330)

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

_forward_unimplementedtransformers.CwmPreTrainedModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/torch/nn/modules/module.py#L388[{"name": "*input", "val": ": typing.Any"}]
Define the computation performed at every call.

Should be overridden by all subclasses.

Although the recipe for forward pass needs to be defined within
this function, one should call the `Module` instance afterwards
instead of this since the former takes care of running the
registered hooks while the latter silently ignores them.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## CwmModel[[transformers.CwmModel]]

#### transformers.CwmModel[[transformers.CwmModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/modeling_cwm.py#L353)

The bare Cwm Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.CwmModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/modeling_cwm.py#L372[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).0`transformers.models.cwm.modeling_cwm.CwmModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.cwm.modeling_cwm.CwmModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([CwmConfig](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmConfig)) and inputs.
The [CwmModel](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([CwmConfig](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.cwm.modeling_cwm.CwmModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.cwm.modeling_cwm.CwmModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([CwmConfig](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmConfig)) and inputs.

## CwmForCausalLM[[transformers.CwmForCausalLM]]

#### transformers.CwmForCausalLM[[transformers.CwmForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/modeling_cwm.py#L441)

The Cwm Model for causal language modeling.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.CwmForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/cwm/modeling_cwm.py#L455[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([CwmConfig](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [CwmForCausalLM](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoTokenizer, CwmForCausalLM

>>> model = CwmForCausalLM.from_pretrained("meta-cwm/Cwm-2-7b-hf")
>>> tokenizer = AutoTokenizer.from_pretrained("meta-cwm/Cwm-2-7b-hf")

>>> prompt = "Hey, are you conscious? Can you talk to me?"
>>> inputs = tokenizer(prompt, return_tensors="pt")

>>> # Generate
>>> generate_ids = model.generate(inputs.input_ids, max_length=30)
>>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
"Hey, are you conscious? Can you talk to me?\nI'm not conscious, but I can talk to you."
```

**Parameters:**

config ([CwmForCausalLM](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([CwmConfig](/docs/transformers/v5.0.0rc1/en/model_doc/cwm#transformers.CwmConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

