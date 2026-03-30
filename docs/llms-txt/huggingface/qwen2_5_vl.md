# Source: https://huggingface.co/docs/transformers/v5.3.0/model_doc/qwen2_5_vl.md

# Qwen2.5-VL

[Qwen2.5-VL](https://huggingface.co/papers/2502.13923) is a multimodal vision-language model, available in 3B, 7B, and 72B parameters, pretrained on 4.1T tokens. The model introduces window attention in the ViT encoder to accelerate training and inference, dynamic FPS sampling on the spatial and temporal dimensions for better video understanding across different sampling rates, and an upgraded MRoPE (multi-resolutional rotary positional encoding) mechanism to better capture and learn temporal dynamics.

You can find all the original Qwen2.5-VL checkpoints under the [Qwen2.5-VL](https://huggingface.co/collections/Qwen/qwen25-vl-6795ffac22b334a837c0f9a5) collection.

> [!TIP]
> Click on the Qwen2.5-VL models in the right sidebar for more examples of how to apply Qwen2.5-VL to different vision and language tasks.

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.3.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoModel) class.

```py
import torch
from transformers import pipeline
pipe = pipeline(
    task="image-text-to-text",
    model="Qwen/Qwen2.5-VL-7B-Instruct",
    device=0,
    dtype=torch.bfloat16
)
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
            },
            { "type": "text", "text": "Describe this image."},
        ]
    }
]
pipe(text=messages,max_new_tokens=20, return_full_text=False)

```

```py
import torch
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-7B-Instruct",
    dtype=torch.float16,
    device_map="auto",
    attn_implementation="sdpa"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
messages = [
    {
        "role":"user",
        "content":[
            {
                "type":"image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
            },
            {
                "type":"text",
                "text":"Describe this image."
            }
        ]
    }

]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
       generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```

Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the [Quantization](../quantization/overview) overview for more available quantization backends.

The example below uses [torchao](../quantization/torchao) to only quantize the weights to int4.

```python
import torch
from transformers import TorchAoConfig, Qwen2_5_VLForConditionalGeneration, AutoProcessor

quantization_config = TorchAoConfig("int4_weight_only", group_size=128)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-7B-Instruct",
    dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=quantization_config
)

```

## Notes

- Use Qwen2.5-VL for video inputs by setting `"type": "video"` as shown below.

    ```python
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "video", "path": "/path/to/video.mp4"},
                {"type": "text", "text": "What happened in the video?"},
            ],
        }
    ]
    
    inputs = processor.apply_chat_template(
        conversation,
        fps=1,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device)
    
    # Inference: Generation of the output
    output_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
    output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(output_text)
    ```

- Use Qwen2.5-VL for a mixed batch of inputs (images, videos, text). Add labels when handling multiple images or videos for better reference
 as show below.

    ```python
    import torch
    from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
    
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2.5-VL-7B-Instruct",
        dtype=torch.float16,
        device_map="auto",
        attn_implementation="sdpa"
    )
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "image"}, 
                {"type": "text", "text": "Hello, how are you?"}
            ]
        },
        {
            "role": "assistant",
            "content": "I'm doing well, thank you for asking. How can I assist you today?"
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe these images and video?"}, 
                {"type": "image"}, 
                {"type": "image"}, 
                {"type": "video"}, 
                {"type": "text", "text": "These are from my vacation."}
            ]
        },
        {
            "role": "assistant",
            "content": "I'd be happy to describe the images and video for you. Could you please provide more context about your vacation?"
        },
        {
            "role": "user",
            "content": "It was a trip to the mountains. Can you see the details in the images and video?"
        }
    ]
    
    # default:
    prompt_without_id = processor.apply_chat_template(conversation, add_generation_prompt=True)
    # Excepted output: 'system\nYou are a helpful assistant.\nuser\nHello, how are you?\nassistant\nI'm doing well, thank you for asking. How can I assist you today?\nuser\nCan you describe these images and video?These are from my vacation.\nassistant\nI'd be happy to describe the images and video for you. Could you please provide more context about your vacation?\nuser\nIt was a trip to the mountains. Can you see the details in the images and video?\nassistant\n'
    
    
    # add ids
    prompt_with_id = processor.apply_chat_template(conversation, add_generation_prompt=True, add_vision_id=True)
    # Excepted output: 'system\nYou are a helpful assistant.\nuser\nPicture 1: Hello, how are you?\nassistant\nI'm doing well, thank you for asking. How can I assist you today?\nuser\nCan you describe these images and video?Picture 2: Picture 3: Video 1: These are from my vacation.\nassistant\nI'd be happy to describe the images and video for you. Could you please provide more context about your vacation?\nuser\nIt was a trip to the mountains. Can you see the details in the images and video?\nassistant\n'
    ```

- Use the `min_pixels` and `max_pixels` parameters in [AutoProcessor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoProcessor) to set the resolution.

    ```python
    min_pixels = 224*224
    max_pixels = 2048*2048
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)
    ```

    Higher resolution can require more compute whereas reducing the resolution can save memory as follows:

    ```python
    min_pixels = 256*28*28
    max_pixels = 1024*28*28 
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)
    ```

## Qwen2_5_VLConfig[[transformers.Qwen2_5_VLConfig]]

#### transformers.Qwen2_5_VLConfig[[transformers.Qwen2_5_VLConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/configuration_qwen2_5_vl.py#L244)

This is the configuration class to store the configuration of a [Qwen2_5_VLModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLModel). It is used to instantiate a
Qwen2-VL model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
Qwen2-VL-7B-Instruct [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import Qwen2_5_VLForConditionalGeneration, Qwen2_5_VLConfig

>>> # Initializing a Qwen2_5_VL style configuration
>>> configuration = Qwen2_5_VLConfig()

>>> # Initializing a model from the Qwen2-VL-7B style configuration
>>> model = Qwen2_5_VLForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[PreTrainedConfig, dict]`, *optional*, defaults to `Qwen2_5_VLTextConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[PreTrainedConfig, dict]`,  *optional*, defaults to `Qwen2_5_VLVisionConfig`) : The config object or dictionary of the vision backbone.

image_token_id (`int`, *optional*, defaults to 151655) : The image token index to encode the image prompt.

video_token_id (`int`, *optional*, defaults to 151656) : The video token index to encode the image prompt.

vision_start_token_id (`int`, *optional*, defaults to 151652) : The token index to denote start of vision input.

vision_end_token_id (`int`, *optional*, defaults to 151653) : The token index to denote end of vision input.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether the model's input and output word embeddings should be tied.

## Qwen2_5_VLTextConfig[[transformers.Qwen2_5_VLTextConfig]]

#### transformers.Qwen2_5_VLTextConfig[[transformers.Qwen2_5_VLTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/configuration_qwen2_5_vl.py#L71)

This is the configuration class to store the configuration of a [Qwen2_5_VLTextModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLTextModel). It is used to instantiate a
Qwen2-VL model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
Qwen2-VL-7B-Instruct [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import Qwen2_5_VLTextModel, Qwen2_5_VLConfig

>>> # Initializing a Qwen2_5_VL style configuration
>>> configuration = Qwen2_5_VLConfig()

>>> # Initializing a model from the Qwen2-VL-7B style configuration
>>> model = Qwen2_5_VLTextModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 152064) : Vocabulary size of the Qwen2_5_VL model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [Qwen2_5_VLModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLModel)

hidden_size (`int`, *optional*, defaults to 8192) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 29568) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 80) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 64) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 8) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `32`.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 32768) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

use_sliding_window (`bool`, *optional*, defaults to `False`) : Whether to use sliding window attention.

sliding_window (`int`, *optional*, defaults to 4096) : Sliding window attention (SWA) window size. If not specified, will default to `4096`.

max_window_layers (`int`, *optional*, defaults to 80) : The number of layers using full attention. The first `max_window_layers` layers will use full attention, while any additional layer afterwards will use SWA (Sliding Window Attention).

layer_types (`list`, *optional*) : Attention pattern for each layer.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

bos_token_id (`int`, *optional*, defaults to 151643) : The id of the _beginning-of-stream_ token.

eos_token_id (`int`, *optional*, defaults to 151645) : The id of the _end-of-stream_ token.

pad_token_id (`int`, *optional*) : The id of the _padding_ token.

## Qwen2_5_VLProcessor[[transformers.Qwen2_5_VLProcessor]]

#### transformers.Qwen2_5_VLProcessor[[transformers.Qwen2_5_VLProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/processing_qwen2_5_vl.py#L47)

Constructs a Qwen2_5_VLProcessor which wraps a image processor, a tokenizer, and a video processor into a single processor.

[Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) offers all the functionalities of [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast), [Qwen2Tokenizer](/docs/transformers/v5.3.0/en/model_doc/qwen2#transformers.Qwen2Tokenizer), and [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor). See the
[~Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast), [~Qwen2Tokenizer](/docs/transformers/v5.3.0/en/model_doc/qwen2#transformers.Qwen2Tokenizer), and [~Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor) for more information.

__call__transformers.Qwen2_5_VLProcessor.__call__https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/processing_qwen2_5_vl.py#L63[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.qwen2_5_vl.processing_qwen2_5_vl.Qwen2_5_VLProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list[PIL.Image.Image], list[numpy.ndarray], list[torch.Tensor]]`, *optional*) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **text** (`Union[str, list[str], list[list[str]]]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **videos** (`Union[list[PIL.Image.Image], numpy.ndarray, torch.Tensor, list[numpy.ndarray], list[torch.Tensor], list[list[PIL.Image.Image]], list[list[numpy.ndarray]], list[list[torch.Tensor]], ~video_utils.URL, list[~video_utils.URL], list[list[~video_utils.URL]], ~video_utils.Path, list[~video_utils.Path], list[list[~video_utils.Path]]]`, *optional*) --
  Video to preprocess. Expects a single or batch of videos with pixel values ranging from 0 to 255. If
  passing in videos with pixel values between 0 and 1, set `do_rescale=False`.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.3.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.
- ****kwargs** ([ProcessingKwargs](/docs/transformers/v5.3.0/en/main_classes/processors#transformers.ProcessingKwargs), *optional*) --
  Additional processing options for each modality (text, images, videos, audio). Model-specific parameters
  are listed above; see the TypedDict class for the complete list of supported arguments.0[BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of videos to be fed to a model. Returned when `videos` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.
- **video_grid_thw** -- List of video 3D grid in LLM. Returned when `videos` is not `None`.
- **second_per_grid_ts** -- List of video seconds per time grid. Returned when `videos` is not `None`.

**Parameters:**

image_processor (`Qwen2VLImageProcessorFast`) : The image processor is a required input.

tokenizer (`Qwen2Tokenizer`) : The tokenizer is a required input.

video_processor (`Qwen2VLVideoProcessor`) : The video processor is a required input.

chat_template (`str`) : A Jinja template to convert lists of messages in a chat into a tokenizable string.

**Returns:**

`[BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of videos to be fed to a model. Returned when `videos` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.
- **video_grid_thw** -- List of video 3D grid in LLM. Returned when `videos` is not `None`.
- **second_per_grid_ts** -- List of video seconds per time grid. Returned when `videos` is not `None`.

## Qwen2_5_VLTextModel[[transformers.Qwen2_5_VLTextModel]]

#### transformers.Qwen2_5_VLTextModel[[transformers.Qwen2_5_VLTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L841)

The bare Qwen2 5 Vl Text Model outputting raw hidden-states without any specific head on to.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen2_5_VLTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L863[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
  Whether or not to return a [ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
The [Qwen2_5_VLTextModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

**Parameters:**

config ([Qwen2_5_VLTextConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLTextConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.

## Qwen2_5_VLModel[[transformers.Qwen2_5_VLModel]]

#### transformers.Qwen2_5_VLModel[[transformers.Qwen2_5_VLModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L998)

The bare Qwen2 5 Vl Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen2_5_VLModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1318[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "second_per_grid_ts", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
  Whether or not to return a [ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast). See [Qwen2VLImageProcessorFast.__call__()](/docs/transformers/v5.3.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses
  [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast) for processing images).
- **pixel_values_videos** (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor). See [Qwen2VLVideoProcessor.__call__()](/docs/transformers/v5.3.0/en/model_doc/pe_video#transformers.PeVideoVideoProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses
  [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor) for processing videos).
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **video_grid_thw** (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) --
  The temporal, height and width of feature shape of each video in LLM.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens matching each modality. For example text (0), image (1), video (2).
  Multimodal token type ids can be obtained using [AutoProcessor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoProcessor). See [ProcessorMixin.__call__()](/docs/transformers/v5.3.0/en/model_doc/vilt#transformers.ViltProcessor.__call__) for details.

- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **second_per_grid_ts** (`torch.Tensor` of shape `(num_videos)`, *optional*) --
  The time interval (in seconds) for each grid along the temporal dimension in the 3D position IDs.0`Qwen2_5_VLModelOutputWithPast` or `tuple(torch.FloatTensor)`A `Qwen2_5_VLModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
The [Qwen2_5_VLModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.

**Parameters:**

config ([Qwen2_5_VLModel](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``Qwen2_5_VLModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `Qwen2_5_VLModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
#### get_video_features[[transformers.Qwen2_5_VLModel.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1188)

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

**Parameters:**

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input videos.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
#### get_image_features[[transformers.Qwen2_5_VLModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1210)

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

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.

## Qwen2_5_VLForConditionalGeneration[[transformers.Qwen2_5_VLForConditionalGeneration]]

#### transformers.Qwen2_5_VLForConditionalGeneration[[transformers.Qwen2_5_VLForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1441)

forwardtransformers.Qwen2_5_VLForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1495[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "second_per_grid_ts", "val": ": torch.Tensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast). See [Qwen2VLImageProcessorFast.__call__()](/docs/transformers/v5.3.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses
  [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast) for processing images).
- **pixel_values_videos** (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor). See [Qwen2VLVideoProcessor.__call__()](/docs/transformers/v5.3.0/en/model_doc/pe_video#transformers.PeVideoVideoProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses
  [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor) for processing videos).
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **video_grid_thw** (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) --
  The temporal, height and width of feature shape of each video in LLM.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens matching each modality. For example text (0), image (1), video (2).
  Multimodal token type ids can be obtained using [AutoProcessor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoProcessor). See [ProcessorMixin.__call__()](/docs/transformers/v5.3.0/en/model_doc/vilt#transformers.ViltProcessor.__call__) for details.

- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **second_per_grid_ts** (`torch.Tensor` of shape `(num_videos)`, *optional*) --
  The time interval (in seconds) for each grid along the temporal dimension in the 3D position IDs.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`Qwen2_5_VLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `Qwen2_5_VLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
The [Qwen2_5_VLForConditionalGeneration](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.

Example:

```python
>>> from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

>>> model = Qwen2_5_VLForConditionalGeneration.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
>>> processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

>>> messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
            },
            {"type": "text", "text": "Describe the image."},
        ],
    }
]

>>> inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)

>>> # Generate
>>> generated_ids = model.generate(**inputs, max_new_tokens=1024)
>>> generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
>>> output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
>>> print(output_text)
```

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

output_attentions (`bool`, *optional*) : Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned tensors for more detail.

output_hidden_states (`bool`, *optional*) : Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for more detail.

pixel_values (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast). See [Qwen2VLImageProcessorFast.__call__()](/docs/transformers/v5.3.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses [Qwen2VLImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessorFast) for processing images).

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) : The tensors corresponding to the input video. Pixel values for videos can be obtained using [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor). See [Qwen2VLVideoProcessor.__call__()](/docs/transformers/v5.3.0/en/model_doc/pe_video#transformers.PeVideoVideoProcessor.__call__) for details ([Qwen2_5_VLProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLProcessor) uses [Qwen2VLVideoProcessor](/docs/transformers/v5.3.0/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor) for processing videos).

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

rope_deltas (`torch.LongTensor` of shape `(batch_size, )`, *optional*) : The rope index difference between sequence length and multimodal rope.

mm_token_type_ids (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens matching each modality. For example text (0), image (1), video (2). Multimodal token type ids can be obtained using [AutoProcessor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoProcessor). See [ProcessorMixin.__call__()](/docs/transformers/v5.3.0/en/model_doc/vilt#transformers.ViltProcessor.__call__) for details. 

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

second_per_grid_ts (`torch.Tensor` of shape `(num_videos)`, *optional*) : The time interval (in seconds) for each grid along the temporal dimension in the 3D position IDs.

logits_to_keep (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

**Returns:**

``Qwen2_5_VLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `Qwen2_5_VLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
#### get_video_features[[transformers.Qwen2_5_VLForConditionalGeneration.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1463)

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

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

>>> model = Qwen2_5_VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
>>> processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

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

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input videos.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.
#### get_image_features[[transformers.Qwen2_5_VLForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py#L1480)

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

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

>>> model = Qwen2_5_VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
>>> processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

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

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen2_5_VLConfig](/docs/transformers/v5.3.0/en/model_doc/qwen2_5_vl#transformers.Qwen2_5_VLConfig)) and inputs.

