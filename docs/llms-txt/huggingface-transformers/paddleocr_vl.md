# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/paddleocr_vl.md

# PaddleOCR-VL

## Overview

**Huggingface Hub**: [PaddleOCR-VL](https://huggingface.co/collections/PaddlePaddle/paddleocr-vl) | **Github Repo**: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

**Official Website**: [Baidu AI Studio](https://aistudio.baidu.com/paddleocr) | **arXiv**: [Technical Report](https://huggingface.co/papers/2510.14528)

**PaddleOCR-VL** is a SOTA and resource-efficient model tailored for document parsing. Its core component is PaddleOCR-VL-0.9B, a compact yet powerful vision-language model (VLM) that integrates a NaViT-style dynamic resolution visual encoder with the ERNIE-4.5-0.3B language model to enable accurate element recognition. This innovative model efficiently supports 109 languages and excels in recognizing complex elements (e.g., text, tables, formulas, and charts), while maintaining minimal resource consumption. Through comprehensive evaluations on widely used public benchmarks and in-house benchmarks, PaddleOCR-VL achieves SOTA performance in both page-level document parsing and element-level recognition. It significantly outperforms existing solutions, exhibits strong competitiveness against top-tier VLMs, and delivers fast inference speeds. These strengths make it highly suitable for practical deployment in real-world scenarios.

### **Core Features**

1. **Compact yet Powerful VLM Architecture:** We present a novel vision-language model that is specifically designed for resource-efficient inference, achieving outstanding performance in element recognition. By integrating a NaViT-style dynamic high-resolution visual encoder with the lightweight ERNIE-4.5-0.3B language model, we significantly enhance the model’s recognition capabilities and decoding efficiency. This integration maintains high accuracy while reducing computational demands, making it well-suited for efficient and practical document processing applications.

2. **SOTA Performance on Document Parsing:** PaddleOCR-VL achieves state-of-the-art performance in both page-level document parsing and element-level recognition. It significantly outperforms existing pipeline-based solutions and exhibiting strong competitiveness against leading vision-language models (VLMs) in document parsing. Moreover, it excels in recognizing complex document elements, such as text, tables, formulas, and charts, making it suitable for a wide range of challenging content types, including handwritten text and historical documents. This makes it highly versatile and suitable for a wide range of document types and scenarios.

3. **Multilingual Support:** PaddleOCR-VL Supports 109 languages, covering major global languages, including but not limited to Chinese, English, Japanese, Latin, and Korean, as well as languages with different scripts and structures, such as Russian (Cyrillic script), Arabic, Hindi (Devanagari script), and Thai. This broad language coverage substantially enhances the applicability of our system to multilingual and globalized document processing scenarios.

### **Model Architecture**

## Usage

### Usage tips

> [!IMPORTANT]
> We currently recommend using the [PaddleOCR official method for inference](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html), as it is faster and supports page-level document parsing.
> The example code below only supports element-level recognition.

We have four types of element-level recognition:

- Text recognition, indicated by the prompt `OCR:`.
- Formula recognition, indicated by the prompt `Formula Recognition:`.
- Table recognition, indicated by the prompt `Table Recognition:`.
- Chart recognition, indicated by the prompt `Chart Recognition:`.

The following examples are all based on text recognition, with the prompt `OCR:`.

### Single input inference

The example below demonstrates how to generate text with PaddleOCRVL using [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel).

```py
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="PaddlePaddle/PaddleOCR-VL", dtype="bfloat16")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/ocr_demo2.jpg"},
            {"type": "text", "text": "OCR:"},
        ]
    }
]
result = pipe(text=messages)
print(result[0]["generated_text"])
```

```py
from transformers import AutoProcessor, AutoModelForImageTextToText

model = AutoModelForImageTextToText.from_pretrained("PaddlePaddle/PaddleOCR-VL", dtype="bfloat16")
processor = AutoProcessor.from_pretrained("PaddlePaddle/PaddleOCR-VL")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/ocr_demo2.jpg"},
            {"type": "text", "text": "OCR:"},
        ]
    }
]
inputs = processor.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=100)
result = processor.decode(outputs[0][inputs["input_ids"].shape[-1]:-1])
print(result)
```

### Batched inference

PaddleOCRVL also supports batched inference. We advise users to use `padding_side="left"` when computing batched generation as it leads to more accurate results. Here is how you can do it with PaddleOCRVL using [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel):

```py
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="PaddlePaddle/PaddleOCR-VL", dtype="bfloat16")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/ocr_demo2.jpg"},
            {"type": "text", "text": "OCR:"},
        ]
    }
]
result = pipe(text=[messages, messages])
print(result[0][0]["generated_text"])
print(result[1][0]["generated_text"])
```

```py
from transformers import AutoProcessor, AutoModelForImageTextToText

model = AutoModelForImageTextToText.from_pretrained("PaddlePaddle/PaddleOCR-VL", dtype="bfloat16")
processor = AutoProcessor.from_pretrained("PaddlePaddle/PaddleOCR-VL")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/ocr_demo2.jpg"},
            {"type": "text", "text": "OCR:"},
        ]
    }
]
batch_messages = [messages, messages]
inputs = processor.apply_chat_template(
	batch_messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
    padding=True,
    padding_side='left',
).to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=100)
generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
result = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(result)
```

### Using Flash Attention 2

Flash Attention 2 is an even faster, optimized version of the previous optimization, please refer to the [FlashAttention](https://huggingface.co/docs/transformers/perf_infer_gpu_one#flashattention).

For example:

```shell
pip install flash-attn --no-build-isolation
```

```python
from transformers import AutoModelForImageTextToText
model = AutoModelForImageTextToText.from_pretrained("PaddlePaddle/PaddleOCR-VL", dtype="bfloat16", attn_implementation="flash_attention_2")
```

## PaddleOCRVLForConditionalGeneration[[transformers.PaddleOCRVLForConditionalGeneration]]

#### transformers.PaddleOCRVLForConditionalGeneration[[transformers.PaddleOCRVLForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1335)

forwardtransformers.PaddleOCRVLForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1372[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [PaddleOCRVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessorFast). See [PaddleOCRVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([PaddleOCRVLProcessor](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLProcessor) uses
  [PaddleOCRVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessorFast) for processing images).
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.paddleocr_vl.modeling_paddleocr_vl.PaddleOCRVLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.paddleocr_vl.modeling_paddleocr_vl.PaddleOCRVLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.
The [PaddleOCRVLForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, PaddleOCRVLForConditionalGeneration

>>> model = PaddleOCRVLForConditionalGeneration.from_pretrained("PaddlePaddle/PaddleOCR-VL", dtype="bfloat16")
>>> processor = AutoProcessor.from_pretrained("PaddlePaddle/PaddleOCR-VL")

>>> messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/ocr_demo.jpg",
            },
            {"type": "text", "text": "OCR:"},
        ],
    }
]

>>> inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

>>> # Generate
>>> generated_ids = model.generate(**inputs, max_new_tokens=1024)
>>> generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
>>> output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
>>> print(output_text)
```

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

pixel_values (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [PaddleOCRVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessorFast). See [PaddleOCRVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([PaddleOCRVLProcessor](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLProcessor) uses [PaddleOCRVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessorFast) for processing images).

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

rope_deltas (`torch.LongTensor` of shape `(batch_size, )`, *optional*) : The rope index difference between sequence length and multimodal rope.

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

logits_to_keep (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

**Returns:**

``transformers.models.paddleocr_vl.modeling_paddleocr_vl.PaddleOCRVLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.paddleocr_vl.modeling_paddleocr_vl.PaddleOCRVLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.
#### get_image_features[[transformers.PaddleOCRVLForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1357)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, PaddleOCRVLForConditionalGeneration

>>> model = PaddleOCRVLForConditionalGeneration.from_pretrained("PaddlePaddle/PaddleOCR-VL")
>>> processor = AutoProcessor.from_pretrained("PaddlePaddle/PaddleOCR-VL")

>>> messages = [
...     {
...         "role": "user", "content": [
...             {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"},
...             {"type": "text", "text": "Where is the cat standing?"},
...         ]
...     },
... ]

>>> inputs = processor.apply_chat_template(
...     messages,
...     tokenize=True,
...     return_dict=True,
...     return_tensors="pt",
...     add_generation_prompt=True
... )
>>> # Generate
>>> generate_ids = model.generate(**inputs)
>>> processor.batch_decode(generate_ids, skip_special_tokens=True)[0]
```

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

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

## PaddleOCRVLConfig[[transformers.PaddleOCRVLConfig]]

#### transformers.PaddleOCRVLConfig[[transformers.PaddleOCRVLConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/configuration_paddleocr_vl.py#L256)

This is the configuration class to store the configuration of a [PaddleOCRVLForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLForConditionalGeneration). It is used to instantiate a
PaddleOCRVL model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
PaddleOCRVL [PaddlePaddle/PaddleOCR-VL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PaddleOCRVLForConditionalGeneration, PaddleOCRVLConfig

>>> # Initializing a PaddleOCRVL style configuration
>>> configuration = PaddleOCRVLConfig()

>>> # Initializing a model from the PaddleOCRVL style configuration
>>> model = PaddleOCRVLForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[PreTrainedConfig, dict]`, *optional*, defaults to `PaddleOCRTextConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[PreTrainedConfig, dict]`,  *optional*, defaults to `PaddleOCRVisionConfig`) : The config object or dictionary of the vision backbone.

image_token_id (`int`, *optional*, defaults to 100295) : The image token index to encode the image prompt.

video_token_id (`int`, *optional*, defaults to 100296) : The video token index to encode the image prompt.

vision_start_token_id (`int`, *optional*, defaults to 101305) : The token index to denote start of vision input.

vision_end_token_id (`int`, *optional*, defaults to 101306) : The token index to denote end of vision input.

tie_word_embeddings (`bool`, *optional*, defaults to `True`) : Whether the model's input and output word embeddings should be tied.

## PaddleOCRVisionConfig[[transformers.PaddleOCRVisionConfig]]

#### transformers.PaddleOCRVisionConfig[[transformers.PaddleOCRVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/configuration_paddleocr_vl.py#L33)

This is the configuration class to store the configuration of a [PaddleOCRVisionModel](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVisionModel). It is used to instantiate a
PaddleOCRVL vision encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the vision encoder of the PaddleOCRVL
[PaddlePaddle/PaddleOCRVL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import PaddleOCRVisionConfig, PaddleOCRVisionModel

>>> # Initializing a PaddleOCRVisionConfig with PaddlePaddle/PaddleOCR-VL style configuration
>>> configuration = PaddleOCRVisionConfig()

>>> # Initializing a PaddleOCRVisionModel (with random weights) from the PaddlePaddle/PaddleOCR-VL style configuration
>>> model = PaddleOCRVisionModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1152) : Dimensionality of the encoder layers and the pooler layer.

intermediate_size (`int`, *optional*, defaults to 4304) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_hidden_layers (`int`, *optional*, defaults to 27) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : Number of channels in the input images.

image_size (`int`, *optional*, defaults to 384) : The size (resolution) of each image.

patch_size (`int`, *optional*, defaults to 14) : The size (resolution) of each patch.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu_pytorch_tanh"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` `"quick_gelu"` are supported.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

spatial_merge_size (`int`, *optional*, defaults to 2) : The size used for merging spatial dimensions.

## PaddleOCRTextConfig[[transformers.PaddleOCRTextConfig]]

#### transformers.PaddleOCRTextConfig[[transformers.PaddleOCRTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/configuration_paddleocr_vl.py#L117)

This is the configuration class to store the configuration of a [PaddleOCRTextModel](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRTextModel). It is used to instantiate an Ernie 4.5
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the Ernie 4.5 0.3B.
e.g. [baidu/ERNIE-4.5-0.3B-PT](https://huggingface.co/baidu/ERNIE-4.5-0.3B-PT)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PaddleOCRTextModel, PaddleOCRTextConfig

>>> # Initializing a PaddleOCRText 0.3B style configuration
>>> configuration = PaddleOCRTextConfig()

>>> # Initializing a model from the 0.3B style configuration
>>> model = PaddleOCRTextModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 103424) : Vocabulary size of the Ernie 4.5 model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [PaddleOCRTextModel](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRTextModel)

hidden_size (`int`, *optional*, defaults to 1024) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 3072) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 18) : Number of hidden layers in the Transformer decoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer decoder.

num_key_value_heads (`int`, *optional*, defaults to 2) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `num_attention_heads`.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 131072) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions.

pad_token_id (`int`, *optional*, defaults to 0) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 1) : Beginning of stream token id.

eos_token_id (`int`, *optional*, defaults to 2) : End of stream token id.

tie_word_embeddings (`bool`, *optional*, defaults to `True`) : Whether to tie weight embeddings

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

use_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in any of the projections including mlp and attention for example.

head_dim (`int`, *optional*, defaults to 128) : The attention head dimension. If None, it will default to hidden_size // num_attention_heads

## PaddleOCRTextModel[[transformers.PaddleOCRTextModel]]

#### transformers.PaddleOCRTextModel[[transformers.PaddleOCRTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L460)

The bare Paddleocr Vl Text Model outputting raw hidden-states without any specific head on to.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PaddleOCRTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L477[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [PaddleOCRTextModel](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([PaddleOCRTextConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRTextConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## PaddleOCRVisionModel[[transformers.PaddleOCRVisionModel]]

#### transformers.PaddleOCRVisionModel[[transformers.PaddleOCRVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L937)

forwardtransformers.PaddleOCRVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L954[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "cu_seqlens", "val": ": Tensor"}, {"name": "image_grid_thw", "val": ": list[tuple[int, int, int] | list[tuple[int, int, int]]] | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, sequence_length, image_channels, patch_size, patch_size)`) --
  The tensors corresponding to the input images.
- **cu_seqlens** (`torch.Tensor` of shape `(num_images + 1,)`) --
  The cumulative sequence lengths of each image or video feature.
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.0

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, sequence_length, image_channels, patch_size, patch_size)`) : The tensors corresponding to the input images.

cu_seqlens (`torch.Tensor` of shape `(num_images + 1,)`) : The cumulative sequence lengths of each image or video feature.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

## PaddleOCRVLImageProcessor[[transformers.PaddleOCRVLImageProcessor]]

#### transformers.PaddleOCRVLImageProcessor[[transformers.PaddleOCRVLImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/image_processing_paddleocr_vl.py#L107)

Constructs a PaddleOCRVL image processor that dynamically resizes images based on the original images.

get_number_of_image_patchestransformers.PaddleOCRVLImageProcessor.get_number_of_image_patcheshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/image_processing_paddleocr_vl.py#L476[{"name": "height", "val": ": int"}, {"name": "width", "val": ": int"}, {"name": "images_kwargs", "val": " = None"}]- **height** (`int`) --
  Height of the input image.
- **width** (`int`) --
  Width of the input image.
- **images_kwargs** (`dict`, *optional*) --
  Any kwargs to override defaults of the image processor.0`int`Number of image patches per image.

A utility that returns number of image patches for a given image size.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions.

size (`dict[str, int]`, *optional*) : Size of the image after resizing. `shortest_edge` and `longest_edge` keys must be present.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use when resizing the image.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image.

image_mean (`float` or `list[float]`, *optional*) : Mean to use if normalizing the image. This is a float or list of floats for each channel in the image.

image_std (`float` or `list[float]`, *optional*) : Standard deviation to use if normalizing the image. This is a float or list of floats for each channel in the image.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

min_pixels (`int`, *optional*, defaults to `384 * 384`) : The min pixels of the image to resize the image.

max_pixels (`int`, *optional*, defaults to `1536 * 1536`) : The max pixels of the image to resize the image.

patch_size (`int`, *optional*, defaults to 14) : The spatial patch size of the vision encoder.

temporal_patch_size (`int`, *optional*, defaults to 1) : The temporal patch size of the vision encoder.

merge_size (`int`, *optional*, defaults to 2) : The merge size of the vision encoder to llm encoder.

**Returns:**

``int``

Number of image patches per image.
#### preprocess[[transformers.PaddleOCRVLImageProcessor.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/image_processing_paddleocr_vl.py#L330)

**Parameters:**

images (`ImageInput`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the image.

size (`dict[str, int]`, *optional*, defaults to `self.size`) : Size of the image after resizing. Shortest edge of the image is resized to size["shortest_edge"], with the longest edge resized to keep the input aspect ratio.

resample (`int`, *optional*, defaults to `self.resample`) : Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the image.

rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the image.

image_mean (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) : Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.

image_std (`float` or `list[float]`, *optional*, defaults to `self.image_std`) : Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to `True`.

min_pixels (`int`, *optional*, defaults to `self.min_pixels`) : The min pixels of the image to resize the image.

max_pixels (`int`, *optional*, defaults to `self.max_pixels`) : The max pixels of the image to resize the image.

patch_size (`int`, *optional*, defaults to `self.patch_size`) : The spatial patch size of the vision encoder.

temporal_patch_size (`int`, *optional*, defaults to `self.temporal_patch_size`) : The temporal patch size of the vision encoder.

merge_size (`int`, *optional*, defaults to `self.merge_size`) : The merge size of the vision encoder to llm encoder.

do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`) : Whether to convert the image to RGB.

return_tensors (`str` or `TensorType`, *optional*) : The type of tensors to return. Can be one of: - Unset: Return a list of `np.ndarray`. - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`. - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input image.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

## PaddleOCRVLImageProcessorFast[[transformers.PaddleOCRVLImageProcessorFast]]

#### transformers.PaddleOCRVLImageProcessorFast[[transformers.PaddleOCRVLImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/image_processing_paddleocr_vl_fast.py#L70)

## PaddleOCRVLModel[[transformers.PaddleOCRVLModel]]

#### transformers.PaddleOCRVLModel[[transformers.PaddleOCRVLModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1032)

The bare Paddleocr Vl Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PaddleOCRVLModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1265[{"name": "input_ids", "val": ": LongTensor = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": list[torch.FloatTensor] | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ""}]

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*):
The temporal, height and width of feature shape of each image in LLM.
rope_deltas (`torch.LongTensor` of shape `(batch_size, )`, *optional*):
The rope index difference between sequence length and multimodal rope.

**Parameters:**

config ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.
#### get_image_features[[transformers.PaddleOCRVLModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1204)

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PaddleOCRVLConfig](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLConfig)) and inputs.

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
#### get_placeholder_mask[[transformers.PaddleOCRVLModel.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1241)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.
#### get_rope_index[[transformers.PaddleOCRVLModel.get_rope_index]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L1055)

Calculate the 3D rope index based on image and video's temporal, height and width in LLM.

Explanation:
Each embedding sequence contains vision embedding and text embedding or just contains text embedding.

For pure text embedding sequence, the rotary position embedding has no difference with modern LLMs.
Examples:
input_ids: [T T T T T], here T is for text.
temporal position_ids: [0, 1, 2, 3, 4]
height position_ids: [0, 1, 2, 3, 4]
width position_ids: [0, 1, 2, 3, 4]

For vision and text embedding sequence, we calculate 3D rotary position embedding for vision part
and 1D rotary position embedding for text part.
Examples:
Assume we have a video input with 3 temporal patches, 2 height patches and 2 width patches.
input_ids: [V V V V V V V V V V V V T T T T T], here V is for vision.
vision temporal position_ids: [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
vision height position_ids: [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
vision width position_ids: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
text temporal position_ids: [3, 4, 5, 6, 7]
text height position_ids: [3, 4, 5, 6, 7]
text width position_ids: [3, 4, 5, 6, 7]
Here we calculate the text start position_ids as the max vision position_ids plus 1.

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide it.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.

**Returns:**

position_ids (`torch.LongTensor` of shape `(3, batch_size, sequence_length)`)
mrope_position_deltas (`torch.Tensor` of shape `(batch_size)`)

## PaddleOCRVLProcessor[[transformers.PaddleOCRVLProcessor]]

#### transformers.PaddleOCRVLProcessor[[transformers.PaddleOCRVLProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/processing_paddleocr_vl.py#L40)

[PaddleOCRVLProcessor](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLProcessor) offers all the functionalities of [PaddleOCRVLImageProcessor](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessor) and `LLamaTokenizerFast`. See the
[__call__()](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLProcessor.__call__) and [decode()](/docs/transformers/v5.0.0/en/main_classes/processors#transformers.ProcessorMixin.decode) for more information.

__call__transformers.PaddleOCRVLProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/processing_paddleocr_vl.py#L60[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.paddleocr_vl.processing_paddleocr_vl.PaddleOCRVLProcessorKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`) --
  The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
  tensor. Both channels-first and channels-last formats are supported.
- **text** (`str`, `List[str]`, `List[List[str]]`) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
  `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:
  - `'tf'`: Return TensorFlow `tf.constant` objects.
  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.
  - `'jax'`: Return JAX `jnp.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.

**Parameters:**

image_processor ([PaddleOCRVLImageProcessor](/docs/transformers/v5.0.0/en/model_doc/paddleocr_vl#transformers.PaddleOCRVLImageProcessor), *optional*) : The image processor is a required input.

tokenizer (`LLamaTokenizerFast`, *optional*) : The tokenizer is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.

## PaddleOCRVisionTransformer[[transformers.PaddleOCRVisionTransformer]]

#### transformers.PaddleOCRVisionTransformer[[transformers.PaddleOCRVisionTransformer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L886)

forwardtransformers.PaddleOCRVisionTransformer.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/paddleocr_vl/modeling_paddleocr_vl.py#L898[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "cu_seqlens", "val": ": Tensor"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "image_grid_thw", "val": ": list[tuple[int, int, int] | list[tuple[int, int, int]]] | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, sequence_length, patch_size * patch_size * image_channels)`) --
  The tensors corresponding to the input images.
- **cu_seqlens** (`torch.Tensor` of shape `(num_images + 1,)`) --
  The cumulative sequence lengths of each image or video feature.
- **attention_mask** (`torch.Tensor`, *optional*) --
  The attention_mask used in forward function shape [batch_size X sequence_length] if not None.
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.0

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, sequence_length, patch_size * patch_size * image_channels)`) : The tensors corresponding to the input images.

cu_seqlens (`torch.Tensor` of shape `(num_images + 1,)`) : The cumulative sequence lengths of each image or video feature.

attention_mask (`torch.Tensor`, *optional*) : The attention_mask used in forward function shape [batch_size X sequence_length] if not None.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

