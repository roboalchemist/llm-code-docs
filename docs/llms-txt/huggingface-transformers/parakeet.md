# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/parakeet.md

# Parakeet

## Overview

Parakeet models, [introduced by NVIDIA NeMo](https://developer.nvidia.com/blog/pushing-the-boundaries-of-speech-recognition-with-nemo-parakeet-asr-models/), are models that combine a [Fast Conformer](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html#fast-conformer) encoder with connectionist temporal classification (CTC), recurrent neural network transducer (RNNT) or token and duration transducer (TDT) decoder for automatic speech recognition.

**Model Architecture**

- **Fast Conformer Encoder**: A linearly scalable Conformer architecture that processes mel-spectrogram features and reduces sequence length through subsampling. This is more efficient version of the Conformer Encoder found in [FastSpeech2Conformer](./fastspeech2_conformer) (see [ParakeetEncoder](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetEncoder) for the encoder implementation and details).
- [**ParakeetForCTC**](#parakeetforctc): a Fast Conformer Encoder + a CTC decoder
  - **CTC Decoder**: Simple but effective decoder consisting of:
    - 1D convolution projection from encoder hidden size to vocabulary size (for optimal NeMo compatibility).
    - CTC loss computation for training.
    - Greedy CTC decoding for inference.

The original implementation can be found in [NVIDIA NeMo](https://github.com/NVIDIA/NeMo).
Model checkpoints are to be found under [the NVIDIA organization](https://huggingface.co/nvidia/models?search=parakeet).

This model was contributed by [Nithin Rao Koluguri](https://huggingface.co/nithinraok), [Eustache Le Bihan](https://huggingface.co/eustlb) and [Eric Bezzam](https://huggingface.co/bezzam).

## Usage

### Basic usage

```py
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="nvidia/parakeet-ctc-1.1b")
out = pipe("https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3")
print(out)
```

```py
from transformers import AutoModelForCTC, AutoProcessor
from datasets import load_dataset, Audio
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained("nvidia/parakeet-ctc-1.1b")
model = AutoModelForCTC.from_pretrained("nvidia/parakeet-ctc-1.1b", dtype="auto", device_map=device)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))
speech_samples = [el['array'] for el in ds["audio"][:5]]

inputs = processor(speech_samples, sampling_rate=processor.feature_extractor.sampling_rate)
inputs.to(model.device, dtype=model.dtype)
outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))
```

### Making The Model Go Brrr

Parakeet supports full-graph compilation with CUDA graphs! This optimization is most effective when you know the maximum audio length you want to transcribe. The key idea is using static input shapes to avoid recompilation. For example, if you know your audio will be under 30 seconds, you can use the processor to pad all inputs to 30 seconds, preparing consistent input features and attention masks. See the example below!

```python
from transformers import AutoModelForCTC, AutoProcessor
from datasets import load_dataset, Audio
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained("nvidia/parakeet-ctc-1.1b")
model = AutoModelForCTC.from_pretrained("nvidia/parakeet-ctc-1.1b", dtype="auto", device_map=device)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))
speech_samples = [el['array'] for el in ds["audio"][:5]]

# Compile the generate method with fullgraph and CUDA graphs
model.generate = torch.compile(model.generate, fullgraph=True, mode="reduce-overhead")

# let's define processor kwargs to pad to 30 seconds
processor_kwargs = {
    "padding": "max_length",
    "max_length": 30 * processor.feature_extractor.sampling_rate,
}

# Define a timing context using CUDA events
class TimerContext:
    def __init__(self, name="Execution"):
        self.name = name
        self.start_event = None
        self.end_event = None
        
    def __enter__(self):
        # Use CUDA events for more accurate GPU timing
        self.start_event = torch.cuda.Event(enable_timing=True)
        self.end_event = torch.cuda.Event(enable_timing=True)
        self.start_event.record()
        return self

    def __exit__(self, *args):
        self.end_event.record()
        torch.cuda.synchronize()
        elapsed_time = self.start_event.elapsed_time(self.end_event) / 1000.0
        print(f"{self.name} time: {elapsed_time:.4f} seconds")

inputs = processor(speech_samples[0], **processor_kwargs)
inputs.to(device, dtype=model.dtype)
print("\n" + "="*50)
print("First generation - compiling...")
# Generate with the compiled model
with TimerContext("First generation"):
    outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))

inputs = processor(speech_samples[1], **processor_kwargs)
inputs.to(device, dtype=model.dtype)
print("\n" + "="*50)
print("Second generation - recording CUDA graphs...")
with TimerContext("Second generation"):
    outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))

inputs = processor(speech_samples[2], **processor_kwargs)
inputs.to(device, dtype=model.dtype)
print("\n" + "="*50)
print("Third generation - fast !!!")
with TimerContext("Third generation"):
    outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))

inputs = processor(speech_samples[3], **processor_kwargs)
inputs.to(device, dtype=model.dtype)
print("\n" + "="*50)
print("Fourth generation - still fast !!!")
with TimerContext("Fourth generation"):
    outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))
```

### Training

```python
from transformers import AutoModelForCTC, AutoProcessor
from datasets import load_dataset, Audio
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained("nvidia/parakeet-ctc-1.1b")
model = AutoModelForCTC.from_pretrained("nvidia/parakeet-ctc-1.1b", dtype="auto", device_map=device)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))
speech_samples = [el['array'] for el in ds["audio"][:5]]
text_samples = [el for el in ds["text"][:5]]

# passing `text` to the processor will prepare inputs' `labels` key
inputs = processor(audio=speech_samples, text=text_samples, sampling_rate=processor.feature_extractor.sampling_rate)
inputs.to(device, dtype=model.dtype)

outputs = model(**inputs)
outputs.loss.backward()
```

## ParakeetTokenizer[[transformers.ParakeetTokenizer]]

#### transformers.ParakeetTokenizer[[transformers.ParakeetTokenizer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/tokenization_parakeet.py#L20)

Inherits all methods from [PreTrainedTokenizerFast](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend). Users should refer to this superclass for more information regarding those methods,
except for `_decode` which is overridden to adapt it to CTC decoding:
1. Group consecutive tokens
2. Filter out the blank token

## ParakeetFeatureExtractor[[transformers.ParakeetFeatureExtractor]]

#### transformers.ParakeetFeatureExtractor[[transformers.ParakeetFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/feature_extraction_parakeet.py#L36)

Constructs a Parakeet feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

This class extracts mel-filter bank features from raw speech using a custom numpy implementation of the `Short Time
Fourier Transform` which should match pytorch's `torch.stft` equivalent.

__call__transformers.ParakeetFeatureExtractor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/feature_extraction_parakeet.py#L127[{"name": "raw_speech", "val": ": numpy.ndarray | list[float] | list[numpy.ndarray] | list[list[float]]"}, {"name": "truncation", "val": ": bool = False"}, {"name": "pad_to_multiple_of", "val": ": int | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "return_attention_mask", "val": ": bool | None = None"}, {"name": "padding", "val": ": str | None = 'longest'"}, {"name": "max_length", "val": ": int | None = None"}, {"name": "sampling_rate", "val": ": int | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "device", "val": ": str | None = 'cpu'"}, {"name": "return_token_timestamps", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **raw_speech** (`np.ndarray`, `list[float]`, `list[np.ndarray]`, `list[list[float]]`) --
  The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
  values, a list of numpy arrays or a list of list of float values. Must be mono channel audio, not
  stereo, i.e. single float per timestep.
- **truncation** (`bool`, *optional*, default to `True`) --
  Activates truncation to cut input sequences longer than *max_length* to *max_length*.
- **pad_to_multiple_of** (`int`, *optional*, defaults to None) --
  If set will pad the sequence to a multiple of the provided value.

  This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
  `>= 7.5` (Volta), or on TPUs which benefit from having sequence lengths be a multiple of 128.
- **return_attention_mask** (`bool`, *optional*) --
  Whether to return the attention mask. If left to the default, will return the attention mask according
  to the specific feature_extractor's default.

  [What are attention masks?](../glossary#attention-mask)

  

  For Parakeet models, `attention_mask` should always be passed for batched inference, to avoid subtle
  bugs.

  

- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors instead of list of python integers. Acceptable values are:

  - `'tf'`: Return TensorFlow `tf.constant` objects.
  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return Numpy `np.ndarray` objects.
- **sampling_rate** (`int`, *optional*) --
  The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
  `sampling_rate` at the forward call to prevent silent errors and allow automatic speech recognition
  pipeline.
- **padding_value** (`float`, *optional*, defaults to 0.0) --
  The value that is used to fill the padding values / vectors.
- **do_normalize** (`bool`, *optional*, defaults to `False`) --
  Whether or not to zero-mean unit-variance normalize the input. Normalizing can help to significantly
  improve the performance of the model.
- **device** (`str`, *optional*, defaults to `'cpu'`) --
  Specifies the device for computation of the log-mel spectrogram of audio signals in the
  `_torch_extract_fbank_features` method. (e.g., "cpu", "cuda")
- **return_token_timestamps** (`bool`, *optional*, defaults to `None`) --
  Deprecated. Use `return_attention_mask` instead from which the number of frames can be inferred.

  Whether or not to return the number of frames of the input raw_speech.
  These num_frames can be used by the model to compute word level timestamps.0

Main method to featurize and prepare for the model one or several sequence(s). Implementation uses PyTorch for
the STFT computation if available, otherwise a slower NumPy based one.

**Parameters:**

feature_size (`int`, *optional*, defaults to 80) : The feature dimension of the extracted features.

sampling_rate (`int`, *optional*, defaults to 16000) : The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).

hop_length (`int`, *optional*, defaults to 160) : Length of the overlapping windows for the STFT used to obtain the Mel Frequency coefficients.

n_fft (`int`, *optional*, defaults to 512) : Size of the Fourier transform.

win_length (`int`, *optional*, defaults to 400) : The window length for the STFT computation.

preemphasis (`float`, *optional*, defaults to 0.97) : A preemphasis filter coefficient. 0.0 means no preemphasis filter.

padding_value (`float`, *optional*, defaults to 0.0) : Padding value used to pad the audio. Should correspond to silences.

## ParakeetProcessor[[transformers.ParakeetProcessor]]

#### transformers.ParakeetProcessor[[transformers.ParakeetProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/processing_parakeet.py#L41)

Constructs a ParakeetProcessor which wraps a feature extractor and a tokenizer into a single processor.

[ParakeetProcessor](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetProcessor) offers all the functionalities of `feature_extractor_class` and `tokenizer_class`. See the
`~feature_extractor_class` and `~tokenizer_class` for more information.

__call__transformers.ParakeetProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/processing_parakeet.py#L45[{"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor']]"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "sampling_rate", "val": ": int | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.parakeet.processing_parakeet.ParakeetProcessorKwargs]"}]- **audio** (`Union[numpy.ndarray, torch.Tensor, collections.abc.Sequence, collections.abc.Sequence]`) --
  The audio or batch of audios to be prepared. Each audio can be a NumPy array or PyTorch tensor.
  In case of a NumPy array/PyTorch tensor, each audio should be of shape (C, T), where C is a number of channels,
  and T is the sample length of the audio.
- **text** (`Union[str, list, list]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **sampling_rate** (`int`, *optional*) --
  The sampling rate of the input audio in Hz. This should match the sampling rate expected by the feature
  extractor (defaults to 16000 Hz). If provided, it will be validated against the processor's expected
  sampling rate, and an error will be raised if they don't match. If not provided, a warning will be
  issued and the default sampling rate will be assumed.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0

**Parameters:**

feature_extractor (`feature_extractor_class`) : The feature extractor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.
#### batch_decode[[transformers.ParakeetProcessor.batch_decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L1593)

This method forwards all its arguments to PreTrainedTokenizer's [batch_decode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.
#### decode[[transformers.ParakeetProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L1602)

This method forwards all its arguments to PreTrainedTokenizer's [decode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.

## ParakeetEncoderConfig[[transformers.ParakeetEncoderConfig]]

#### transformers.ParakeetEncoderConfig[[transformers.ParakeetEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/configuration_parakeet.py#L23)

This is the configuration class to store the configuration of a [ParakeetEncoder](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetEncoder). It is used to instantiate a
`ParakeetEncoder` model according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import ParakeetEncoderModel, ParakeetEncoderConfig

>>> # Initializing a `ParakeetEncoder` configuration
>>> configuration = ParakeetEncoderConfig()

>>> # Initializing a model from the configuration
>>> model = ParakeetEncoderModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

This configuration class is based on the ParakeetEncoder architecture from NVIDIA NeMo. You can find more details
and pre-trained models at [nvidia/parakeet-ctc-1.1b](https://huggingface.co/nvidia/parakeet-ctc-1.1b).

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimension of the layers and the hidden states.

num_hidden_layers (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

intermediate_size (`int`, *optional*, defaults to 4096) : Dimension of the "intermediate" (often named feed-forward) layer in the Transformer encoder.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the encoder and pooler.

attention_bias (`bool`, *optional*, defaults to `True`) : Whether to use bias in the attention layers.

convolution_bias (`bool`, *optional*, defaults to `True`) : Whether to use bias in convolutions of the conformer's convolution module.

conv_kernel_size (`int`, *optional*, defaults to 9) : The kernel size of the convolution layers in the Conformer block.

subsampling_factor (`int`, *optional*, defaults to 8) : The factor by which the input sequence is subsampled.

subsampling_conv_channels (`int`, *optional*, defaults to 256) : The number of channels in the subsampling convolution layers.

num_mel_bins (`int`, *optional*, defaults to 80) : Number of mel features.

subsampling_conv_kernel_size (`int`, *optional*, defaults to 3) : The kernel size of the subsampling convolution layers.

subsampling_conv_stride (`int`, *optional*, defaults to 2) : The stride of the subsampling convolution layers.

dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for all fully connected layers in the embeddings, encoder, and pooler.

dropout_positions (`float`, *optional*, defaults to 0.0) : The dropout ratio for the positions in the input sequence.

layerdrop (`float`, *optional*, defaults to 0.1) : The dropout ratio for the layers in the encoder.

activation_dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for activations inside the fully connected layer.

attention_dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for the attention layers.

max_position_embeddings (`int`, *optional*, defaults to 5000) : The maximum sequence length that this model might ever be used with.

scale_input (`bool`, *optional*, defaults to `True`) : Whether to scale the input embeddings.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## ParakeetCTCConfig[[transformers.ParakeetCTCConfig]]

#### transformers.ParakeetCTCConfig[[transformers.ParakeetCTCConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/configuration_parakeet.py#L152)

This is the configuration class to store the configuration of a [ParakeetForCTC](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetForCTC). It is used to instantiate a
Parakeet CTC model according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import ParakeetForCTC, ParakeetCTCConfig

>>> # Initializing a Parakeet configuration
>>> configuration = ParakeetCTCConfig()

>>> # Initializing a model from the configuration
>>> model = ParakeetForCTC(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

This configuration class is based on the Parakeet CTC architecture from NVIDIA NeMo. You can find more details
and pre-trained models at [nvidia/parakeet-ctc-1.1b](https://huggingface.co/nvidia/parakeet-ctc-1.1b).

from_encoder_configtransformers.ParakeetCTCConfig.from_encoder_confighttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/configuration_parakeet.py#L220[{"name": "encoder_config", "val": ": ParakeetEncoderConfig"}, {"name": "**kwargs", "val": ""}][ParakeetCTCConfig](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetCTCConfig)An instance of a configuration object

Instantiate a [ParakeetCTCConfig](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetCTCConfig) (or a derived class) from parakeet encoder model configuration.

**Parameters:**

vocab_size (`int`, *optional*, defaults to 1025) : Vocabulary size of the model.

ctc_loss_reduction (`str`, *optional*, defaults to `"mean"`) : Specifies the reduction to apply to the output of `torch.nn.CTCLoss`. Only relevant when training an instance of [ParakeetForCTC](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetForCTC).

ctc_zero_infinity (`bool`, *optional*, defaults to `True`) : Whether to zero infinite losses and the associated gradients of `torch.nn.CTCLoss`. Infinite losses mainly occur when the inputs are too short to be aligned to the targets. Only relevant when training an instance of [ParakeetForCTC](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetForCTC).

encoder_config (`Union[dict, ParakeetEncoderConfig]`, *optional*) : The config object or dictionary of the encoder.

pad_token_id (`int`, *optional*, defaults to 1024) : Padding token id. Also used as blank token id.

**Returns:**

`[ParakeetCTCConfig](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetCTCConfig)`

An instance of a configuration object

## ParakeetEncoder[[transformers.ParakeetEncoder]]

#### transformers.ParakeetEncoder[[transformers.ParakeetEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/modeling_parakeet.py#L549)

The Parakeet Encoder model, based on the [Fast Conformer architecture](https://huggingface.co/papers/2305.05084).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ParakeetEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/modeling_parakeet.py#L572[{"name": "input_features", "val": ": Tensor"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "output_attention_mask", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`torch.Tensor` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  `feature_extractor_class`. See `feature_extractor_class.__call__` for details (`processor_class` uses
  `feature_extractor_class` for processing audios).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **output_attention_mask** (`bool`, *optional*) --
  Whether to return the output attention mask.0[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [ParakeetEncoder](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetEncoder) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, ParakeetEncoder
>>> from datasets import load_dataset, Audio

>>> model_id = "nvidia/parakeet-ctc-1.1b"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> encoder = ParakeetEncoder.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"])
>>> encoder_outputs = encoder(**inputs)

>>> print(encoder_outputs.last_hidden_state.shape)
```

**Parameters:**

config ([ParakeetEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetEncoderConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## ParakeetForCTC[[transformers.ParakeetForCTC]]

#### transformers.ParakeetForCTC[[transformers.ParakeetForCTC]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/modeling_parakeet.py#L674)

Parakeet Encoder with a Connectionist Temporal Classification (CTC) head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ParakeetForCTC.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/modeling_parakeet.py#L685[{"name": "input_features", "val": ": Tensor"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "labels", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`torch.Tensor` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  `feature_extractor_class`. See `feature_extractor_class.__call__` for details (`processor_class` uses
  `feature_extractor_class` for processing audios).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **labels** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.0[transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [ParakeetForCTC](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetForCTC) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, ParakeetForCTC
>>> from datasets import load_dataset, Audio

>>> model_id = "nvidia/parakeet-ctc-1.1b"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = ParakeetForCTC.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"], text=ds[0]["text"])
>>> outputs = model(**inputs)

>>> print(outputs.loss)
```

**Parameters:**

config ([ParakeetCTCConfig](/docs/transformers/v5.0.0/en/model_doc/parakeet#transformers.ParakeetCTCConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
#### generate[[transformers.ParakeetForCTC.generate]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/parakeet/modeling_parakeet.py#L758)

Example:

```python
>>> from transformers import AutoProcessor, ParakeetForCTC
>>> from datasets import load_dataset, Audio

>>> model_id = "nvidia/parakeet-ctc-1.1b"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = ParakeetForCTC.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"], text=ds[0]["text"])
>>> predicted_ids = model.generate(**inputs)
>>> transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

>>> print(transcription)
```

