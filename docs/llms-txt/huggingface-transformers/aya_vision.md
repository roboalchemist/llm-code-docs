# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/aya_vision.md

# Aya Vision

[Aya Vision](https://huggingface.co/papers/2505.08751) is a family of open-weight multimodal vision-language models from Cohere Labs. It is trained with a synthetic annotation framework that generates high-quality multilingual image captions, improving Aya Vision's generated responses. In addition, a cross-modal model merging technique is used to prevent the model from losing its text capabilities after adding vision capabilities. The model combines a CommandR-7B language model with a SigLIP vision encoder.

You can find all the original Aya Vision checkpoints under the [Aya Vision](https://huggingface.co/collections/CohereLabs/cohere-labs-aya-vision-67c4ccd395ca064308ee1484) collection.

> [!TIP]
> This model was contributed by [saurabhdash](https://huggingface.co/saurabhdash) and [yonigozlan](https://huggingface.co/yonigozlan).
>
> Click on the Aya Vision models in the right sidebar for more examples of how to apply Aya Vision to different image-to-text tasks.

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```python
from transformers import pipeline

pipe = pipeline(model="CohereLabs/aya-vision-8b", task="image-text-to-text", device_map="auto")

# Format message with the aya-vision chat template
messages = [
    {"role": "user",
     "content": [
       {"type": "image", "url": "https://media.istockphoto.com/id/458012057/photo/istanbul-turkey.jpg?s=612x612&w=0&k=20&c=qogAOVvkpfUyqLUMr_XJQyq-HkACXyYUSZbKhBlPrxo="},
        {"type": "text", "text": "Bu resimde hangi anıt gösterilmektedir?"},
    ]},
    ]
outputs = pipe(text=messages, max_new_tokens=300, return_full_text=False)

print(outputs)
```

```python
# pip install 'git+https://github.com/huggingface/transformers.git@v4.49.0-Aya Vision'
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "CohereLabs/aya-vision-8b"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, device_map="auto", dtype=torch.float16
)

# Format message with the aya-vision chat template
messages = [
    {"role": "user",
     "content": [
       {"type": "image", "url": "https://pbs.twimg.com/media/Fx7YvfQWYAIp6rZ?format=jpg&name=medium"},
        {"type": "text", "text": "चित्र में लिखा पाठ क्या कहता है?"},
    ]},
    ]

inputs = processor.apply_chat_template(
    messages, padding=True, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
).to(model.device)

gen_tokens = model.generate(
    **inputs,
    max_new_tokens=300,
    do_sample=True,
    temperature=0.3,
)

print(processor.tokenizer.decode(gen_tokens[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

Quantization reduces the memory footprint of large models by representing weights at lower precision. Refer to the [Quantization](../quantization/overview) overview for supported backends.

The example below uses [bitsandbytes](../quantization/bitsandbytes) to only quantize the weights to 4-bits.

```python
import torch
from transformers import (
    AutoProcessor,
    AutoModelForImageTextToText,
    BitsAndBytesConfig
)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

processor = AutoProcessor.from_pretrained("CohereLabs/aya-vision-32b", use_fast=True)
model = AutoModelForImageTextToText.from_pretrained(
    "CohereLabs/aya-vision-32b",
    quantization_config=bnb_config,
    device_map="auto"
)

inputs = processor.apply_chat_template(
    [
    {"role": "user", "content": [
        {"type": "image", "url": "https://huggingface.co/roschmid/dog-races/resolve/main/images/Border_Collie.jpg"},
        {"type": "text",  "text":"Describe what you see."}
    ]}
    ],
    padding=True,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt"
).to(model.device)

generated = model.generate(**inputs, max_new_tokens=50)
print(processor.tokenizer.decode(generated[0], skip_special_tokens=True))
```

## Notes

- Images are represented with the `` tag in the chat template.

- Use the [apply_chat_template()](/docs/transformers/v5.0.0/en/main_classes/processors#transformers.ProcessorMixin.apply_chat_template) method to correctly format inputs.

- The example below demonstrates inference with multiple images.
  
    ```py
    import torch
    from transformers import AutoProcessor, AutoModelForImageTextToText
        
    processor = AutoProcessor.from_pretrained("CohereForAI/aya-vision-8b")
    model = AutoModelForImageTextToText.from_pretrained(
        "CohereForAI/aya-vision-8b", device_map="auto", dtype=torch.float16
    )
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg",
                },
                {
                    "type": "image",
                    "url": "https://thumbs.dreamstime.com/b/golden-gate-bridge-san-francisco-purple-flowers-california-echium-candicans-36805947.jpg",
                },
                {
                    "type": "text",
                    "text": "These images depict two different landmarks. Can you identify them?",
                },
            ],
        },
    ]
    
    inputs = processor.apply_chat_template(
        messages, padding=True, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
    ).to(model.device)
    
    gen_tokens = model.generate(
        **inputs, 
        max_new_tokens=300, 
        do_sample=True, 
        temperature=0.3,
    )
    
    gen_text = processor.tokenizer.decode(gen_tokens[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    print(gen_text)
    ```

- The example below demonstrates inference with batched inputs.
  
    ```py
    import torch
    from transformers import AutoProcessor, AutoModelForImageTextToText
        
    processor = AutoProcessor.from_pretrained(model_id)
    model = AutoModelForImageTextToText.from_pretrained(
        "CohereForAI/aya-vision-8b", device_map="auto", dtype=torch.float16
    )
    
    batch_messages = [
        [
            {
                "role": "user",
                "content": [
                    {"type": "image", "url": "https://llava-vl.github.io/static/images/view.jpg"},
                    {"type": "text", "text": "Write a haiku for this image"},
                ],
            },
        ],
        [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg",
                    },
                    {
                        "type": "image",
                        "url": "https://thumbs.dreamstime.com/b/golden-gate-bridge-san-francisco-purple-flowers-california-echium-candicans-36805947.jpg",
                    },
                    {
                        "type": "text",
                        "text": "These images depict two different landmarks. Can you identify them?",
                    },
                ],
            },
        ],
    ]
    
    batch_inputs = processor.apply_chat_template(
        batch_messages, 
        padding=True, 
        add_generation_prompt=True, 
        tokenize=True, 
        return_dict=True, 
        return_tensors="pt"
    ).to(model.device)
    
    batch_outputs = model.generate(
        **batch_inputs,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.3,
    )
    
    for i, output in enumerate(batch_outputs):
        response = processor.tokenizer.decode(
            output[batch_inputs.input_ids.shape[1]:], 
            skip_special_tokens=True
        )
        print(f"Response {i+1}:\n{response}\n")
    ```

## AyaVisionProcessor[[transformers.AyaVisionProcessor]]

#### transformers.AyaVisionProcessor[[transformers.AyaVisionProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/processing_aya_vision.py#L39)

Constructs a AyaVisionProcessor which wraps a image processor and a tokenizer into a single processor.

[AyaVisionProcessor](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionProcessor) offers all the functionalities of [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) and [CohereTokenizer](/docs/transformers/v5.0.0/en/model_doc/cohere#transformers.CohereTokenizer). See the
[~GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) and [~CohereTokenizer](/docs/transformers/v5.0.0/en/model_doc/cohere#transformers.CohereTokenizer) for more information.

__call__transformers.AyaVisionProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/processing_aya_vision.py#L117[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.aya_vision.processing_aya_vision.AyaVisionProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`, *optional*) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **text** (`Union[str, list, list]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.

**Parameters:**

image_processor (`GotOcr2ImageProcessorFast`) : The image processor is a required input.

tokenizer (`CohereTokenizer`) : The tokenizer is a required input.

patch_size (`int`, *optional*, defaults to 28) : The size of image patches for tokenization.

img_size (`int`, *optional*, defaults to 364) : The size of the image to be tokenized. This should correspond to the size given to the image processor.

image_token (`str`, *optional*, defaults to `""`) : The token to be used to represent an image in the text.

downsample_factor (`int`, *optional*, defaults to 1) : The factor by which to scale the patch size.

start_of_img_token (`str`, *optional*, defaults to `""`) : The token to be used to represent the start of an image in the text.

end_of_img_token (`str`, *optional*, defaults to `""`) : The token to be used to represent the end of an image in the text.

img_patch_token (`str`, *optional*, defaults to `""`) : The token to be used to represent an image patch in the text.

img_line_break_token (`str`, *optional*, defaults to `""`) : The token to be used to represent a line break in the text.

tile_token (`str`, *optional*, defaults to `"TILE"`) : The token to be used to represent an image patch in the text.

tile_global_token (`str`, *optional*, defaults to `"TILE_GLOBAL"`) : The token to be used to represent the cover image in the text.

chat_template (`str`) : A Jinja template to convert lists of messages in a chat into a tokenizable string.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.

## AyaVisionConfig[[transformers.AyaVisionConfig]]

#### transformers.AyaVisionConfig[[transformers.AyaVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/configuration_aya_vision.py#L24)

This is the configuration class to store the configuration of a [AyaVisionForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionForConditionalGeneration). It is used to instantiate an
AyaVision model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of AyaVision.
e.g. [CohereForAI/aya-vision-8b](https://huggingface.co/CohereForAI/aya-vision-8b)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SiglipVisionConfig`) : The config object or dictionary of the vision backbone.

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `Cohere2Config`) : The config object or dictionary of the text backbone.

vision_feature_select_strategy (`str`, *optional*, defaults to `"full"`) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`. If `"default"`, the CLS token is removed from the vision features. If `"full"`, the full vision features are used.

vision_feature_layer (`int`, *optional*, defaults to -1) : The index of the layer to select the vision feature.

downsample_factor (`int`, *optional*, defaults to 2) : The downsample factor to apply to the vision features.

adapter_layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon value used for layer normalization in the adapter.

image_token_index (`int`, *optional*, defaults to 255036) : The image token index to encode the image prompt.

tie_word_embeddings (`bool`, *optional*, defaults to `True`) : Whether to tie weight embeddings.

## AyaVisionModel[[transformers.AyaVisionModel]]

#### transformers.AyaVisionModel[[transformers.AyaVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L163)

The AyaVision model which consists of a vision backbone and a language model, without a language modeling head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.AyaVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L244[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "vision_feature_layer", "val": ": int | list[int] | None = None"}, {"name": "vision_feature_select_strategy", "val": ": str | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast). See [GotOcr2ImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([AyaVisionProcessor](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionProcessor) uses
  [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) for processing images).
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
- **vision_feature_layer** (`Union[int, list]`, *optional*) --
  The index of the layer to select the vision feature. If multiple indices are provided,
  the vision feature of the corresponding indices will be concatenated to form the
  vision features.
- **vision_feature_select_strategy** (`str`, *optional*) --
  The feature selection strategy used to select the vision feature from the vision backbone.
  Can be one of `"default"` or `"full"`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0`transformers.models.aya_vision.modeling_aya_vision.AyaVisionModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.aya_vision.modeling_aya_vision.AyaVisionModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [AyaVisionModel](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.aya_vision.modeling_aya_vision.AyaVisionModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.aya_vision.modeling_aya_vision.AyaVisionModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
#### get_image_features[[transformers.AyaVisionModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L182)

Obtains image last hidden states from the vision tower and apply multimodal projection.

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast). See [GotOcr2ImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([AyaVisionProcessor](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionProcessor) uses [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) for processing images).

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`.

output_hidden_states (`bool`, *optional*) : Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for more detail.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

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
#### get_placeholder_mask[[transformers.AyaVisionModel.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L220)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.

## AyaVisionForConditionalGeneration[[transformers.AyaVisionForConditionalGeneration]]

#### transformers.AyaVisionForConditionalGeneration[[transformers.AyaVisionForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L303)

The AYA_VISION model which consists of a vision backbone and a language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.AyaVisionForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L342[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "vision_feature_layer", "val": ": int | list[int] | None = None"}, {"name": "vision_feature_select_strategy", "val": ": str | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "image_sizes", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast). See [GotOcr2ImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([AyaVisionProcessor](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionProcessor) uses
  [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) for processing images).
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
- **vision_feature_layer** (`Union[int, list]`, *optional*) --
  The index of the layer to select the vision feature. If multiple indices are provided,
  the vision feature of the corresponding indices will be concatenated to form the
  vision features.
- **vision_feature_select_strategy** (`str`, *optional*) --
  The feature selection strategy used to select the vision feature from the vision backbone.
  Can be one of `"default"` or `"full"`.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).
- **image_sizes** (`torch.Tensor` of shape `(batch_size, 2)`, *optional*) --
  The sizes of the images in the batch, being (height, width) for each image.0`transformers.models.aya_vision.modeling_aya_vision.AyaVisionCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.aya_vision.modeling_aya_vision.AyaVisionCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

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
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [AyaVisionForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, AyaVisionForConditionalGeneration
>>> import torch

>>> torch_device = "cuda:0"
>>> processor = AutoProcessor.from_pretrained("CohereForAI/aya-vision-8b", use_fast=True)
>>> model = AyaVisionForConditionalGeneration.from_pretrained("CohereForAI/aya-vision-8b", device_map=torch_device)

>>> messages = [
...     {
...         "role": "user",
...         "content": [
...             {
...                 "type": "image",
...                 "url": "https://pbs.twimg.com/media/Fx7YvfQWYAIp6rZ?format=jpg&name=medium",
...             },
...             {"type": "text", "text": "चित्र में लिखा पाठ क्या कहता है?"},
...         ],
...     }
... ]

>>> inputs = processor.apply_chat_template(
...     messages, padding=True, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt", device=torch_device
... ).to(model.device)

>>> gen_tokens = model.generate(**inputs, max_new_tokens=300, do_sample=True, temperature=0.3)
>>> processor.tokenizer.decode(gen_tokens[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
```

**Parameters:**

config ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.aya_vision.modeling_aya_vision.AyaVisionCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.aya_vision.modeling_aya_vision.AyaVisionCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

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
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
#### get_image_features[[transformers.AyaVisionForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/aya_vision/modeling_aya_vision.py#L327)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, AyaVisionForConditionalGeneration

>>> model = AyaVisionForConditionalGeneration.from_pretrained("CohereForAI/aya-vision-8b")
>>> processor = AutoProcessor.from_pretrained("CohereForAI/aya-vision-8b")

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

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast). See [GotOcr2ImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([AyaVisionProcessor](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionProcessor) uses [GotOcr2ImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/got_ocr2#transformers.GotOcr2ImageProcessorFast) for processing images).

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AyaVisionConfig](/docs/transformers/v5.0.0/en/model_doc/aya_vision#transformers.AyaVisionConfig)) and inputs.

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

