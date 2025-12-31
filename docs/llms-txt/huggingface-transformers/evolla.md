# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/evolla.md

# Evolla

## Overview

The Evolla model was proposed in [Decoding the Molecular Language of Proteins with Evolla](https://doi.org/10.1101/2025.01.05.630192) by [Zhou et al.](https://doi.org/10.1101/2025.01.05.630192).

Evolla is an advanced 80-billion-parameter protein-language generative model designed to decode the molecular language of proteins. It integrates information from protein sequences, structures, and user queries to generate precise and contextually nuanced insights into protein function. Trained on an unprecedented AI-generated dataset of 546 million protein question-answer pairs and 150 billion word tokens, Evolla significantly advances research in proteomics and functional genomics, providing expert-level insights and shedding light on the molecular logic encoded in proteins.

The abstract from the paper is the following:

*Proteins, nature's intricate molecular machines, are the products of billions of years of evolution and play fundamental roles in sustaining life. Yet, deciphering their molecular language - that is, understanding how protein sequences and structures encode and determine biological functions - remains a corner-stone challenge in modern biology. Here, we introduce Evolla, an 80 billion frontier protein-language generative model designed to decode the molecular language of proteins. By integrating information from protein sequences, structures, and user queries, Evolla generates precise and contextually nuanced insights into protein function. A key innovation of Evolla lies in its training on an unprecedented AI-generated dataset: 546 million protein question-answer pairs and 150 billion word tokens, designed to reflect the immense complexity and functional diversity of proteins. Post-pretraining, Evolla integrates Direct Preference Optimization (DPO) to refine the model based on preference signals and Retrieval-Augmented Generation (RAG) for external knowledge incorporation, improving response quality and relevance. To evaluate its performance, we propose a novel framework, Instructional Response Space (IRS), demonstrating that Evolla delivers expert-level insights, advancing research in proteomics and functional genomics while shedding light on the molecular logic encoded in proteins. The online demo is available at http://www.chat-protein.com/.*

Examples:

```python
processor = EvollaProcessor.from_pretrained("westlake-repl/Evolla-10B-DPO-hf")
model = EvollaForProteinText2Text.from_pretrained("westlake-repl/Evolla-10B-DPO-hf")
# aa_seq should have same length as foldseek
protein_inputs = [
    {
        
        "aa_seq": "MATGGRRG...",
        "foldseek": "###lqpfd...", # hashtag means the low-confidence foldseek tokens
    },
    {
        "aa_seq": "MLPGLALL...",
        "foldseek": "dfwwkwad...",
    }
]
message_list = [
    [
        {
            "role": "system",
            "content": "You are an AI expert that can answer any questions about protein.",
        },
        {"role": "user", "content": "What is the function of this protein?"},
    ],
    [
        {
            "role": "system",
            "content": "You are an AI expert that can answer any questions about protein.",
        },
        {"role": "user", "content": "What is the function of this protein?"},
    ]
]
input_dict = processor(
    protein_inputs, messages_list, return_tensors="pt", text_max_length=512, protein_max_length=1024
)
with torch.no_grad():
    generated_ids = hf_model.generate(**input_dict)
generated_texts = processor.batch_decode(
    generated_ids, skip_special_tokens=True
)
```

Tips:

- This model was contributed by [Xibin Bayes Zhou](https://huggingface.co/XibinBayesZhou).
- The original code can be found [here](https://github.com/westlake-repl/Evolla).

## EvollaConfig[[transformers.EvollaConfig]]

#### transformers.EvollaConfig[[transformers.EvollaConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/configuration_evolla.py#L102)

This is the configuration class to store the configuration of a [EvollaModel](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaModel). It is used to instantiate an
Evolla model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the Evolla-10B.

e.g. [westlake-repl/Evolla-10B-hf](https://huggingface.co/westlake-repl/Evolla-10B-hf)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import EvollaModel, EvollaConfig

>>> # Initializing a Evolla evolla-10b style configuration
>>> configuration = EvollaConfig()

>>> # Initializing a model from the evolla-10b style configuration
>>> model = EvollaModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

protein_encoder_config (`dict`, *optional*) : Dictionary of configuration options used to initialize `SaProtConfig`.

vocab_size (`int`, *optional*, defaults to 128256) : Vocabulary size of the Evolla llama model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [EvollaModel](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaModel).

hidden_size (`int`, *optional*, defaults to 4096) : Dimensionality of the llama layers and the pooler layer.

intermediate_size (`int`, *optional*, defaults to 14336) : Dimensionality of the intermediate layers in the llama model.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the llama model.

num_attention_heads (`int`, *optional*, defaults to 32) : Number of attention heads for each attention layer in the llama model.

num_key_value_heads (`int`, *optional*, defaults to 8) : Number of key-value pairs for each attention layer in the llama model.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the llama model. If string, `"gelu"`, `"relu"`, `"selu"` and `"silu"` are supported.

max_position_embeddings (`int`, *optional*, defaults to 8192) : The maximum sequence length that this model might ever be used with. Typically set this to something large just in case (e.g., 512 or 1024 or 2048).

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon value for the RMS-norm layer in the llama model.

rope_parameters (`float`, *optional*) : The scaling factor for the RoPE layer in the llama model.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use bias in the attention layer.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention layer.

mlp_bias (`bool`, *optional*, defaults to `False`) : Whether to use bias in the MLP layer.

aligner_ffn_mult (`int`, *optional*, defaults to 4) : The FFN multiplier for the aligner layer.

aligner_enable_bias (`bool`, *optional*, defaults to `True`) : Whether to use bias in the aligner layer.

aligner_attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1) : The dropout ratio for the attention probabilities in the aligner layer.

aligner_num_add_layers (`int`, *optional*, defaults to 8) : The number of additional layers for the aligner layer.

resampler_depth (`int`, *optional*, defaults to 6) : The depth of the resampler layer in the llama model.

resampler_dim_head (`int`, *optional*, defaults to 64) : The dimension of the heads in the resampler layer in the llama model.

resampler_heads (`int`, *optional*, defaults to 8) : The number of heads in the resampler layer in the llama model.

resampler_num_latents (`int`, *optional*, defaults to 64) : The number of latents in the resampler layer in the llama model.

resampler_ff_mult (`int`, *optional*, defaults to 4) : The FFN multiplier for the resampler layer.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

pad_token_id (`int`, *optional*) : The id of the *padding* token.

bos_token_id (`int`, *optional*, defaults to 128000) : The id of the *beginning-of-sequence* token.

eos_token_id (`int`, *optional*, defaults to 128009) : The id of the *end-of-sequence* token.

use_cache (`bool`, *optional*, defaults to `False`) : Whether or not the model should return the last key/values attentions (not used by all models).

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether or not to tie the input and output word embeddings.

## EvollaModel[[transformers.EvollaModel]]

#### transformers.EvollaModel[[transformers.EvollaModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/modeling_evolla.py#L1271)

forwardtransformers.EvollaModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/modeling_evolla.py#L1299[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "protein_input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "protein_attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "structure_feats", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "msa_feats", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "structure_batch_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "msa_batch_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
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
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **protein_input_ids** (`torch.LongTensor`, *optional*) --
  The input IDs for the protein sequence in structure-aware tokens. Should be of shape `(batch_size, protein_seq_length)` and type `torch.LongTensor`.
- **protein_attention_mask** (`torch.Tensor`, *optional*) --
  The attention mask for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.Tensor`.
- **structure_feats** (`torch.FloatTensor`, *optional*) --
  The input IDs for purely structure-based features. Should be of shape `(batch_size, structure_seq_length, structure_feat_dim)` and type `torch.FloatTensor`. Dummy input for now.
- **msa_feats** (`torch.FloatTensor`, *optional*) --
  The input IDs for purely MSA-based features. Should be of shape `(batch_size, msa_seq_length, msa_feat_dim)` and type `torch.FloatTensor`. Dummy input for now.
- **structure_batch_mask** (`torch.Tensor`, *optional*) --
  The batch mask to decide which protein sequences are purely structure-based. Should be of shape `(batch_size)` and type `torch.Tensor`. Should be paired with `structure_feats`. Dummpy input for now.
- **msa_batch_mask** (`torch.Tensor`, *optional*) --
  The batch mask to decide which protein sequences are purely MSA-based. Should be of shape `(batch_size)` and type `torch.Tensor`. Should be paired with `msa_feats`. Dummpy input for now.0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [EvollaModel](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

protein_input_ids (`torch.LongTensor`, *optional*) : The input IDs for the protein sequence in structure-aware tokens. Should be of shape `(batch_size, protein_seq_length)` and type `torch.LongTensor`.

protein_attention_mask (`torch.Tensor`, *optional*) : The attention mask for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.Tensor`.

structure_feats (`torch.FloatTensor`, *optional*) : The input IDs for purely structure-based features. Should be of shape `(batch_size, structure_seq_length, structure_feat_dim)` and type `torch.FloatTensor`. Dummy input for now.

msa_feats (`torch.FloatTensor`, *optional*) : The input IDs for purely MSA-based features. Should be of shape `(batch_size, msa_seq_length, msa_feat_dim)` and type `torch.FloatTensor`. Dummy input for now.

structure_batch_mask (`torch.Tensor`, *optional*) : The batch mask to decide which protein sequences are purely structure-based. Should be of shape `(batch_size)` and type `torch.Tensor`. Should be paired with `structure_feats`. Dummpy input for now.

msa_batch_mask (`torch.Tensor`, *optional*) : The batch mask to decide which protein sequences are purely MSA-based. Should be of shape `(batch_size)` and type `torch.Tensor`. Should be paired with `msa_feats`. Dummpy input for now.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## EvollaForProteinText2Text[[transformers.EvollaForProteinText2Text]]

#### transformers.EvollaForProteinText2Text[[transformers.EvollaForProteinText2Text]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/modeling_evolla.py#L1400)

forwardtransformers.EvollaForProteinText2Text.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/modeling_evolla.py#L1415[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "protein_input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "protein_attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **protein_input_ids** (`torch.LongTensor`, *optional*) --
  The input IDs for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.LongTensor`.
- **protein_attention_mask** (`torch.Tensor`, *optional*) --
  The attention mask for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.Tensor`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0
The [EvollaForProteinText2Text](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaForProteinText2Text) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import EvollaProcessor, EvollaForProteinText2Text
>>> model = EvollaForProteinText2Text.from_pretrained("westlake/Evolla-10B-hf")
>>> processor = EvollaProcessor.from_pretrained("westlake/Evolla-10B-hf")

>>> protein_information = {
    "aa_seq": "your amino acid sequence",
    "foldseek": "your foldseek sequence",
}
>>> question = "What is the function of this protein?"
>>> message = [
    {"role": "system", "content": "You are an AI expert that can answer any questions about protein."},
    {"role": "user", "content": question},
]

>>> inputs = processor(proteins=[protein_information], messages_list=[message], return_tensors="pt", padding="longest")
>>> outputs = model.generate(**inputs)

>>> print(processor.batch_decode(outputs, skip_special_tokens=True))
```

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

protein_input_ids (`torch.LongTensor`, *optional*) : The input IDs for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.LongTensor`.

protein_attention_mask (`torch.Tensor`, *optional*) : The attention mask for the protein sequence. Should be of shape `(batch_size, protein_seq_length)` and type `torch.Tensor`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

logits_to_keep (`Union[int, torch.Tensor]`, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

## EvollaProcessor[[transformers.EvollaProcessor]]

#### transformers.EvollaProcessor[[transformers.EvollaProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/processing_evolla.py#L30)

Constructs a EVOLLA processor which wraps a LLama tokenizer and SaProt tokenizer (EsmTokenizer) into a single processor.

[EvollaProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaProcessor) offers all the functionalities of [EsmTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/esm#transformers.EsmTokenizer) and [LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer). See the
docstring of [__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/evolla#transformers.EvollaProcessor.__call__) and `decode()` for more information.

__call__transformers.EvollaProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/evolla/processing_evolla.py#L97[{"name": "proteins", "val": ": typing.Union[list[dict], dict, NoneType] = None"}, {"name": "messages_list", "val": ": typing.Union[list[list[dict]], list[dict], NoneType] = None"}, {"name": "protein_max_length", "val": ": typing.Optional[int] = None"}, {"name": "text_max_length", "val": ": typing.Optional[int] = None"}, {"name": "**kwargs", "val": ""}]- **proteins** (`Union[List[dict], dict]`) --
  A list of dictionaries or a single dictionary containing the following keys:
  - `"aa_seq"` (`str`) -- The amino acid sequence of the protein.
  - `"foldseek"` (`str`) -- The foldseek string of the protein.
- **messages_list** (`Union[List[List[dict]], List[dict]]`) --
  A list of lists of dictionaries or a list of dictionaries containing the following keys:
  - `"role"` (`str`) -- The role of the message.
  - `"content"` (`str`) -- The content of the message.
- **protein_max_length** (`int`, *optional*, defaults to 1024) --
  The maximum length of the sequence to be generated.
- **text_max_length** (`int`, *optional*, defaults to 512) --
  The maximum length of the text.0a dict with following keys- `protein_input_ids` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The input IDs for the protein sequence.
- `protein_attention_mask` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The attention mask for the protein sequence.
- `text_input_ids` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The input IDs for the text sequence.
- `text_attention_mask` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The attention mask for the text sequence.
This method takes batched or non-batched proteins and messages_list and converts them into format that can be used by
the model.

**Parameters:**

protein_tokenizer (`EsmTokenizer`) : An instance of [EsmTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/esm#transformers.EsmTokenizer). The protein tokenizer is a required input.

tokenizer (`LlamaTokenizerFast`, *optional*) : An instance of [LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer). The tokenizer is a required input.

protein_max_length (`int`, *optional*, defaults to 1024) : The maximum length of the sequence to be generated.

text_max_length (`int`, *optional*, defaults to 512) : The maximum length of the text to be generated.

**Returns:**

`a dict with following keys`

- `protein_input_ids` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The input IDs for the protein sequence.
- `protein_attention_mask` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The attention mask for the protein sequence.
- `text_input_ids` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The input IDs for the text sequence.
- `text_attention_mask` (`torch.Tensor` of shape `(batch_size, sequence_length)`) -- The attention mask for the text sequence.

