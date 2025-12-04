# Source: https://onnxruntime.ai/docs/genai/api/python.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python-api) Python API

*Note: this API is in preview and is subject to change.*

- [Install and import](#install-and-import)
- [Model class](#model-class)
  - [Load a model](#load-a-model)
    - [Properties](#properties)
    - [Methods](#methods)
- [Config class](#config-class)
  - [Methods](#methods-1)
- [GeneratorParams class](#generatorparams-class)
  - [Methods](#methods-2)
- [Generator class](#generator-class)
  - [Methods](#methods-3)
- [Tokenizer class](#tokenizer-class)
  - [Methods](#methods-4)
- [TokenizerStream class](#tokenizerstream-class)
  - [Methods](#methods-5)
- [NamedTensors class](#namedtensors-class)
  - [Methods](#methods-6)
- [Tensor class](#tensor-class)
  - [Methods](#methods-7)
- [Adapters class](#adapters-class)
  - [Methods](#methods-8)
- [MultiModalProcessor class](#multimodalprocessor-class)
  - [Methods](#methods-9)
- [Images class](#images-class)
- [Audios class](#audios-class)
- [Utility functions](#utility-functions)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-and-import) Install and import

The Python API is delivered by the onnxruntime-genai Python package.

``` highlight
pip install onnxruntime-genai
```

``` highlight
import onnxruntime_genai
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#model-class) Model class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#load-a-model) Load a model

``` highlight
onnxruntime_genai.Model(config_path: str) -> Model
onnxruntime_genai.Model(config: onnxruntime_genai.Config) -> Model
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#properties) Properties

- `type`: Returns the model type as a string.

  :::: 
  ::: highlight
  ``` highlight
  model = onnxruntime_genai.Model("config.json")
  print(model.type)
  ```
  :::
  ::::

- `device_type`: Returns the device type as a string.

  :::: 
  ::: highlight
  ``` highlight
  print(model.device_type)
  ```
  :::
  ::::

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods) Methods

- `create_multimodal_processor() -> MultiModalProcessor`

  :::: 
  ::: highlight
  ``` highlight
  processor = model.create_multimodal_processor()
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#config-class) Config class

``` highlight
onnxruntime_genai.Config(config_path: str) -> Config
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-1) Methods

- `append_provider(provider: str)`

  :::: 
  ::: highlight
  ``` highlight
  config = onnxruntime_genai.Config("config.json")
  config.append_provider("CUDAExecutionProvider")
  ```
  :::
  ::::

- `set_provider_option(option: str, value: str)`

  :::: 
  ::: highlight
  ``` highlight
  config.set_provider_option("device_id", "0")
  ```
  :::
  ::::

- `clear_providers()`

  :::: 
  ::: highlight
  ``` highlight
  config.clear_providers()
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generatorparams-class) GeneratorParams class

``` highlight
onnxruntime_genai.GeneratorParams(model: Model) -> GeneratorParams
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-2) Methods

- `set_inputs(named_tensors: NamedTensors)`

  :::: 
  ::: highlight
  ``` highlight
  params = onnxruntime_genai.GeneratorParams(model)
  named_tensors = onnxruntime_genai.NamedTensors()
  params.set_inputs(named_tensors)
  ```
  :::
  ::::

- `set_model_input(name: str, value: numpy.ndarray)`

  :::: 
  ::: highlight
  ``` highlight
  import numpy as np
  params.set_model_input("input_ids", np.array([1, 2, 3], dtype=np.int32))
  ```
  :::
  ::::

- `try_graph_capture_with_max_batch_size(max_batch_size: int)`

  :::: 
  ::: highlight
  ``` highlight
  params.try_graph_capture_with_max_batch_size(8)
  ```
  :::
  ::::

- `set_search_options(**options)`

  :::: 
  ::: highlight
  ``` highlight
  params.set_search_options(temperature=0.7, top_p=0.9)
  ```
  :::
  ::::

- `set_guidance(type: str, data: str)`

  :::: 
  ::: highlight
  ``` highlight
  params.set_guidance("prefix", "Once upon a time")
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generator-class) Generator class

``` highlight
onnxruntime_genai.Generator(model: Model, params: GeneratorParams) -> Generator
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-3) Methods

- `is_done() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  generator = onnxruntime_genai.Generator(model, params)
  done = generator.is_done()
  ```
  :::
  ::::

- `get_output(name: str) -> numpy.ndarray`

  :::: 
  ::: highlight
  ``` highlight
  output = generator.get_output("output_ids")
  ```
  :::
  ::::

- `append_tokens(tokens: numpy.ndarray[int32])`

  :::: 
  ::: highlight
  ``` highlight
  generator.append_tokens(np.array([4, 5], dtype=np.int32))
  ```
  :::
  ::::

- `append_tokens(tokens: onnxruntime_genai.Tensor)`

  :::: 
  ::: highlight
  ``` highlight
  tensor = onnxruntime_genai.Tensor(np.array([4, 5], dtype=np.int32))
  generator.append_tokens(tensor)
  ```
  :::
  ::::

- `get_logits() -> numpy.ndarray[float32]`

  :::: 
  ::: highlight
  ``` highlight
  logits = generator.get_logits()
  ```
  :::
  ::::

- `set_logits(new_logits: numpy.ndarray[float32])`

  :::: 
  ::: highlight
  ``` highlight
  generator.set_logits(np.zeros_like(logits))
  ```
  :::
  ::::

- `generate_next_token()`

  :::: 
  ::: highlight
  ``` highlight
  generator.generate_next_token()
  ```
  :::
  ::::

- `rewind_to(new_length: int)`

  :::: 
  ::: highlight
  ``` highlight
  generator.rewind_to(2)
  ```
  :::
  ::::

- `get_next_tokens() -> numpy.ndarray[int32]`

  :::: 
  ::: highlight
  ``` highlight
  next_tokens = generator.get_next_tokens()
  ```
  :::
  ::::

- `get_sequence(index: int) -> numpy.ndarray[int32]`

  :::: 
  ::: highlight
  ``` highlight
  sequence = generator.get_sequence(0)
  ```
  :::
  ::::

- `set_active_adapter(adapters: onnxruntime_genai.Adapters, adapter_name: str)`

  :::: 
  ::: highlight
  ``` highlight
  adapters = onnxruntime_genai.Adapters(model)
  generator.set_active_adapter(adapters, "adapter_name")
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenizer-class) Tokenizer class

``` highlight
onnxruntime_genai.Tokenizer(model: Model) -> Tokenizer
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-4) Methods

- `encode(text: str) -> numpy.ndarray[int32]`

  :::: 
  ::: highlight
  ``` highlight
  tokenizer = onnxruntime_genai.Tokenizer(model)
  tokens = tokenizer.encode("Hello world")
  ```
  :::
  ::::

- `to_token_id(text: str) -> int`

  :::: 
  ::: highlight
  ``` highlight
  token_id = tokenizer.to_token_id("Hello")
  ```
  :::
  ::::

- `decode(tokens: numpy.ndarray[int32]) -> str`

  :::: 
  ::: highlight
  ``` highlight
  text = tokenizer.decode(tokens)
  ```
  :::
  ::::

- `apply_chat_template(template_str: str, messages: str, tools: str = None, add_generation_prompt: bool = False) -> str`

  :::: 
  ::: highlight
  ``` highlight
  chat = tokenizer.apply_chat_template(": ", messages="Hi!", add_generation_prompt=True)
  ```
  :::
  ::::

- `encode_batch(texts: list[str]) -> onnxruntime_genai.Tensor`

  :::: 
  ::: highlight
  ``` highlight
  batch_tensor = tokenizer.encode_batch(["Hello", "World"])
  ```
  :::
  ::::

- `decode_batch(tokens: onnxruntime_genai.Tensor) -> list[str]`

  :::: 
  ::: highlight
  ``` highlight
  texts = tokenizer.decode_batch(batch_tensor)
  ```
  :::
  ::::

- `create_stream() -> TokenizerStream`

  :::: 
  ::: highlight
  ``` highlight
  stream = tokenizer.create_stream()
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenizerstream-class) TokenizerStream class

``` highlight
onnxruntime_genai.TokenizerStream(tokenizer: Tokenizer) -> TokenizerStream
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-5) Methods

- `decode(token: int32) -> str`

  :::: 
  ::: highlight
  ``` highlight
  token_str = stream.decode(123)
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#namedtensors-class) NamedTensors class

``` highlight
onnxruntime_genai.NamedTensors() -> NamedTensors
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-6) Methods

- `__getitem__(name: str) -> onnxruntime_genai.Tensor`

  :::: 
  ::: highlight
  ``` highlight
  tensor = named_tensors["input_ids"]
  ```
  :::
  ::::

- `__setitem__(name: str, value: numpy.ndarray or onnxruntime_genai.Tensor)`

  :::: 
  ::: highlight
  ``` highlight
  named_tensors["input_ids"] = np.array([1, 2, 3], dtype=np.int32)
  ```
  :::
  ::::

- `__contains__(name: str) -> bool`

  :::: 
  ::: highlight
  ``` highlight
  exists = "input_ids" in named_tensors
  ```
  :::
  ::::

- `__delitem__(name: str)`

  :::: 
  ::: highlight
  ``` highlight
  del named_tensors["input_ids"]
  ```
  :::
  ::::

- `__len__() -> int`

  :::: 
  ::: highlight
  ``` highlight
  length = len(named_tensors)
  ```
  :::
  ::::

- `keys() -> list[str]`

  :::: 
  ::: highlight
  ``` highlight
  keys = named_tensors.keys()
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tensor-class) Tensor class

``` highlight
onnxruntime_genai.Tensor(array: numpy.ndarray) -> Tensor
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-7) Methods

- `shape() -> list[int]`

  :::: 
  ::: highlight
  ``` highlight
  tensor = onnxruntime_genai.Tensor(np.array([1, 2, 3]))
  print(tensor.shape())
  ```
  :::
  ::::

- `type() -> int`

  :::: 
  ::: highlight
  ``` highlight
  print(tensor.type())
  ```
  :::
  ::::

- `data() -> memoryview`

  :::: 
  ::: highlight
  ``` highlight
  data = tensor.data()
  ```
  :::
  ::::

- `as_numpy() -> numpy.ndarray`

  :::: 
  ::: highlight
  ``` highlight
  arr = tensor.as_numpy()
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#adapters-class) Adapters class

``` highlight
onnxruntime_genai.Adapters(model: Model) -> Adapters
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-8) Methods

- `unload(adapter_name: str)`

  :::: 
  ::: highlight
  ``` highlight
  adapters.unload("adapter_name")
  ```
  :::
  ::::

- `load(file: str, name: str)`

  :::: 
  ::: highlight
  ``` highlight
  adapters.load("adapter_file.bin", "adapter_name")
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#multimodalprocessor-class) MultiModalProcessor class

``` highlight
onnxruntime_genai.MultiModalProcessor(model: Model) -> MultiModalProcessor
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#methods-9) Methods

- `__call__(prompt: str = None, images: Images = None, audios: Audios = None) -> onnxruntime_genai.Tensor`

  :::: 
  ::: highlight
  ``` highlight
  result = processor(prompt="Describe this image", images=onnxruntime_genai.Images.open("image.png"))
  ```
  :::
  ::::

- `create_stream() -> TokenizerStream`

  :::: 
  ::: highlight
  ``` highlight
  stream = processor.create_stream()
  ```
  :::
  ::::

- `decode(tokens: numpy.ndarray[int32]) -> str`

  :::: 
  ::: highlight
  ``` highlight
  text = processor.decode(tokens)
  ```
  :::
  ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#images-class) Images class

``` highlight
onnxruntime_genai.Images.open(*image_paths: str) -> Images
onnxruntime_genai.Images.open_bytes(*image_datas: bytes) -> Images
```

``` highlight
images = onnxruntime_genai.Images.open("image1.png", "image2.jpg")
with open("image1.png", "rb") as f:
    images_bytes = onnxruntime_genai.Images.open_bytes(f.read())
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#audios-class) Audios class

``` highlight
onnxruntime_genai.Audios.open(*audio_paths: str) -> Audios
onnxruntime_genai.Audios.open_bytes(*audio_datas: bytes) -> Audios
```

``` highlight
audios = onnxruntime_genai.Audios.open("audio1.wav")
with open("audio1.wav", "rb") as f:
    audios_bytes = onnxruntime_genai.Audios.open_bytes(f.read())
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#utility-functions) Utility functions

- `onnxruntime_genai.set_log_options(**options)`

  :::: 
  ::: highlight
  ``` highlight
  onnxruntime_genai.set_log_options(verbose=True)
  ```
  :::
  ::::

- `onnxruntime_genai.is_cuda_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_cuda_available())
  ```
  :::
  ::::

- `onnxruntime_genai.is_dml_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_dml_available())
  ```
  :::
  ::::

- `onnxruntime_genai.is_rocm_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_rocm_available())
  ```
  :::
  ::::

- `onnxruntime_genai.is_webgpu_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_webgpu_available())
  ```
  :::
  ::::

- `onnxruntime_genai.is_qnn_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_qnn_available())
  ```
  :::
  ::::

- `onnxruntime_genai.is_openvino_available() -> bool`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.is_openvino_available())
  ```
  :::
  ::::

- `onnxruntime_genai.set_current_gpu_device_id(device_id: int)`

  :::: 
  ::: highlight
  ``` highlight
  onnxruntime_genai.set_current_gpu_device_id(0)
  ```
  :::
  ::::

- `onnxruntime_genai.get_current_gpu_device_id() -> int`

  :::: 
  ::: highlight
  ``` highlight
  print(onnxruntime_genai.get_current_gpu_device_id())
  ```
  :::
  ::::