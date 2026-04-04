# Source: https://docs.wandb.ai/weave/reference/python-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# weave

> Browse the complete Python SDK reference documentation for W&B Weave, including all modules and classes.

export const SourceLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="source-link">
    Source
  </a>;

# API Overview

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/agent/agent.py#L17" />

## <kbd>class</kbd> `Agent`

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `model_name`: `<class 'str'>`
* `temperature`: `<class 'float'>`
* `system_message`: `<class 'str'>`
* `tools`: `list[typing.Any]`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L23" />

### <kbd>method</kbd> `step`

```python  theme={null}
step(state: AgentState) → AgentState
```

Run a step of the agent.

**Args:**

* <b>`state`</b>: The current state of the environment.
* <b>`action`</b>: The action to take.
  **Returns:**
  The new state of the environment.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/agent/agent.py#L12" />

## <kbd>class</kbd> `AgentState`

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `history`: `list[typing.Any]`

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server/interface/builtin_object_classes/annotation_spec.py#L12" />

## <kbd>class</kbd> `AnnotationSpec`

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `field_schema`: `dict[str, typing.Any]`
* `unique_among_creators`: `<class 'bool'>`
* `op_scope`: `list[str] | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server/interface/builtin_object_classes/annotation_spec.py#L47" />

### <kbd>classmethod</kbd> `preprocess_field_schema`

```python  theme={null}
preprocess_field_schema(data: dict[str, Any]) → dict[str, Any]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server/interface/builtin_object_classes/annotation_spec.py#L92" />

### <kbd>classmethod</kbd> `validate_field_schema`

```python  theme={null}
validate_field_schema(schema: dict[str, Any]) → dict[str, Any]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server/interface/builtin_object_classes/annotation_spec.py#L103" />

### <kbd>method</kbd> `value_is_valid`

```python  theme={null}
value_is_valid(payload: Any) → bool
```

Validates a payload against this annotation spec's schema.

**Args:**

* <b>`payload`</b>: The data to validate against the schema
  **Returns:**

* <b>`bool`</b>:  True if validation succeeds, False otherwise

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/Audio/audio.py#L81" />

## <kbd>class</kbd> `Audio`

A class representing audio data in a supported format (wav or mp3).

This class handles audio data storage and provides methods for loading from different sources and exporting to files.

**Attributes:**

* <b>`format`</b>:  The audio format (currently supports 'wav' or 'mp3')
* <b>`data`</b>:  The raw audio data as bytes

**Args:**

* <b>`data`</b>: The audio data (bytes or base64 encoded string)

* <b>`format`</b>: The audio format ('wav' or 'mp3')

* <b>`validate_base64`</b>: Whether to attempt base64 decoding of the input data
  **Raises:**

* <b>`ValueError`</b>:  If audio data is empty or format is not supported

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/Audio/audio.py#L106" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(
    data: 'bytes',
    format: 'SUPPORTED_FORMATS_TYPE',
    validate_base64: 'bool' = True
) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/Audio/audio.py#L174" />

### <kbd>method</kbd> `export`

```python  theme={null}
export(path: 'str | bytes | Path | PathLike') → None
```

Export audio data to a file.

**Args:**

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/Audio/audio.py#L121" />

### <kbd>classmethod</kbd> `from_data`

```python  theme={null}
from_data(data: 'str | bytes', format: 'str') → Self
```

Create an Audio object from raw data and specified format.

* <b>`path`</b>: Path where the audio file should be written
  **Args:**

* <b>`data`</b>: Audio data as bytes or base64 encoded string

* <b>`format`</b>: Audio format ('wav' or 'mp3')
  **Returns:**

* <b>`Audio`</b>:  A new Audio instance

**Raises:**

* <b>`ValueError`</b>:  If format is not supported

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/Audio/audio.py#L146" />

### <kbd>classmethod</kbd> `from_path`

```python  theme={null}
from_path(path: 'str | bytes | Path | PathLike') → Self
```

Create an Audio object from a file path.

**Args:**

* <b>`path`</b>: Path to an audio file (must have .wav or .mp3 extension)
  **Returns:**

* <b>`Audio`</b>:  A new Audio instance loaded from the file

**Raises:**

* <b>`ValueError`</b>:  If file doesn't exist or has unsupported extension

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L42" />

## <kbd>class</kbd> `Content`

A class to represent content from various sources, resolving them to a unified byte-oriented representation with associated metadata.

This class must be instantiated using one of its classmethods:

* from\_path()
* from\_bytes()
* from\_text()
* from\_url()
* from\_base64()
* from\_data\_url()

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L87" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(*args: 'Any', **kwargs: 'Any') → None
```

Direct initialization is disabled. Please use a classmethod like `Content.from_path()` to create an instance.

**Pydantic Fields:**

* `data`: `<class 'bytes'>`
* `size`: `<class 'int'>`
* `mimetype`: `<class 'str'>`
* `digest`: `<class 'str'>`
* `filename`: `<class 'str'>`
* `content_type`: `typing.Literal['bytes', 'text', 'base64', 'file', 'url', 'data_url', 'data_url:base64', 'data_url:encoding', 'data_url:encoding:base64']`
* `input_type`: `<class 'str'>`
* `encoding`: `<class 'str'>`
* `metadata`: `dict[str, typing.Any] | None`
* `extension`: `str | None`

***

#### <kbd>property</kbd> art

#### <kbd>property</kbd> ref

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L531" />

### <kbd>method</kbd> `as_string`

```python  theme={null}
as_string() → str
```

Display the data as a string. Bytes are decoded using the `encoding` attribute If base64, the data will be re-encoded to base64 bytes then decoded to an ASCII string

**Returns:**
str.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L246" />

### <kbd>classmethod</kbd> `from_base64`

```python  theme={null}
from_base64(
    b64_data: 'str | bytes',
    extension: 'str | None' = None,
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None
) → Self
```

Initializes Content from a base64 encoded string or bytes.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L156" />

### <kbd>classmethod</kbd> `from_bytes`

```python  theme={null}
from_bytes(
    data: 'bytes',
    extension: 'str | None' = None,
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None,
    encoding: 'str' = 'utf-8'
) → Self
```

Initializes Content from raw bytes.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L345" />

### <kbd>classmethod</kbd> `from_data_url`

```python  theme={null}
from_data_url(url: 'str', metadata: 'dict[str, Any] | None' = None) → Self
```

Initializes Content from a data URL.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L297" />

### <kbd>classmethod</kbd> `from_path`

```python  theme={null}
from_path(
    path: 'str | Path',
    encoding: 'str' = 'utf-8',
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None
) → Self
```

Initializes Content from a local file path.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L197" />

### <kbd>classmethod</kbd> `from_text`

```python  theme={null}
from_text(
    text: 'str',
    extension: 'str | None' = None,
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None,
    encoding: 'str' = 'utf-8'
) → Self
```

Initializes Content from a string of text.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L387" />

### <kbd>classmethod</kbd> `from_url`

```python  theme={null}
from_url(
    url: 'str',
    headers: 'dict[str, Any] | None' = None,
    timeout: 'int | None' = 30,
    metadata: 'dict[str, Any] | None' = None
) → Self
```

Initializes Content by fetching bytes from an HTTP(S) URL.

Downloads the content, infers mimetype/extension from headers, URL path, and data, and constructs a Content object from the resulting bytes.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L97" />

### <kbd>classmethod</kbd> `model_validate`

```python  theme={null}
model_validate(
    obj: 'Any',
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) → Self
```

Override model\_validate to handle Content reconstruction from dict.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L139" />

### <kbd>classmethod</kbd> `model_validate_json`

```python  theme={null}
model_validate_json(
    json_data: 'str | bytes | bytearray',
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) → Self
```

Override model\_validate\_json to handle Content reconstruction from JSON.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L541" />

### <kbd>method</kbd> `open`

```python  theme={null}
open() → bool
```

Open the file using the operating system's default application.

This method uses the platform-specific mechanism to open the file with the default application associated with the file's type.

**Returns:**

* <b>`bool`</b>:  True if the file was successfully opened, False otherwise.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L571" />

### <kbd>method</kbd> `save`

```python  theme={null}
save(dest: 'str | Path') → None
```

Copy the file to the specified destination path. Updates the filename and the path of the content to reflect the last saved copy.

**Args:**

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L523" />

### <kbd>method</kbd> `serialize_data`

```python  theme={null}
serialize_data(data: 'bytes') → str
```

When dumping model in json mode

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_wrappers/Content/content.py#L498" />

### <kbd>method</kbd> `to_data_url`

```python  theme={null}
to_data_url(use_base64: 'bool' = True) → str
```

Constructs a data URL from the content.

* <b>`dest`</b>: Destination path where the file will be copied to (string or pathlib.Path)  The destination path can be a file or a directory.  If dest has no file extension (e.g. .txt), destination will be considered a directory.
  **Args:**

* <b>`use_base64`</b>: If True, the data will be base64 encoded.  Otherwise, it will be percent-encoded. Defaults to True.
  **Returns:**
  A data URL string.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L26" />

## <kbd>class</kbd> `Dataset`

Dataset object with easy saving and automatic versioning.

**Examples:**

```python  theme={null}
# Create a dataset
dataset = Dataset(name='grammar', rows=[
     {'id': '0', 'sentence': "He no likes ice cream.", 'correction': "He doesn't like ice cream."},
     {'id': '1', 'sentence': "She goed to the store.", 'correction': "She went to the store."},
     {'id': '2', 'sentence': "They plays video games all day.", 'correction': "They play video games all day."}
])

# Publish the dataset
weave.publish(dataset)

# Retrieve the dataset
dataset_ref = weave.ref('grammar').get()

# Access a specific example
example_label = dataset_ref.rows[2]['sentence']
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `rows`: `trace.table.Table | trace.vals.WeaveTable`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L129" />

### <kbd>method</kbd> `add_rows`

```python  theme={null}
add_rows(rows: Iterable[dict]) → Dataset
```

Create a new dataset version by appending rows to the existing dataset.

This is useful for adding examples to large datasets without having to load the entire dataset into memory.

**Args:**

* <b>`rows`</b>: The rows to add to the dataset.
  **Returns:**
  The updated dataset.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L173" />

### <kbd>classmethod</kbd> `convert_to_table`

```python  theme={null}
convert_to_table(rows: Any) → Table | WeaveTable
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L61" />

### <kbd>classmethod</kbd> `from_calls`

```python  theme={null}
from_calls(calls: Iterable[Call]) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L71" />

### <kbd>classmethod</kbd> `from_hf`

```python  theme={null}
from_hf(
    hf_dataset: Union[ForwardRef('HFDataset'), ForwardRef('HFDatasetDict')]
) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L52" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L66" />

### <kbd>classmethod</kbd> `from_pandas`

```python  theme={null}
from_pandas(df: 'DataFrame') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L220" />

### <kbd>method</kbd> `select`

```python  theme={null}
select(indices: Iterable[int]) → Self
```

Select rows from the dataset based on the provided indices.

**Args:**

* <b>`indices`</b>: An iterable of integer indices specifying which rows to select.
  **Returns:**
  A new Dataset object containing only the selected rows.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L115" />

### <kbd>method</kbd> `to_hf`

```python  theme={null}
to_hf() → HFDataset
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/dataset/dataset.py#L107" />

### <kbd>method</kbd> `to_pandas`

```python  theme={null}
to_pandas() → DataFrame
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L192" />

## <kbd>class</kbd> `EasyPrompt`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L200" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(
    content: str | dict | list | None = None,
    role: str | None = None,
    dedent: bool = False,
    **kwargs: Any
) → None
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `data`: `<class 'list'>`
* `config`: `<class 'dict'>`
* `requirements`: `<class 'dict'>`

***

#### <kbd>property</kbd> as\_str

Join all messages into a single string.

***

#### <kbd>property</kbd> is\_bound

***

#### <kbd>property</kbd> messages

#### <kbd>property</kbd> placeholders

***

#### <kbd>property</kbd> system\_message

Join all messages into a system prompt message.

***

#### <kbd>property</kbd> system\_prompt

Join all messages into a system prompt object.

***

#### <kbd>property</kbd> unbound\_placeholders

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L230" />

### <kbd>method</kbd> `append`

```python  theme={null}
append(item: Any, role: str | None = None, dedent: bool = False) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L484" />

### <kbd>method</kbd> `as_dict`

```python  theme={null}
as_dict() → dict[str, Any]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L481" />

### <kbd>method</kbd> `as_pydantic_dict`

```python  theme={null}
as_pydantic_dict() → dict[str, Any]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L321" />

### <kbd>method</kbd> `bind`

```python  theme={null}
bind(*args: Any, **kwargs: Any) → Prompt
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L341" />

### <kbd>method</kbd> `bind_rows`

```python  theme={null}
bind_rows(dataset: list[dict] | Any) → list['Prompt']
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L442" />

### <kbd>method</kbd> `config_table`

```python  theme={null}
config_table(title: str | None = None) → Table
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L411" />

### <kbd>method</kbd> `configure`

```python  theme={null}
configure(config: dict | None = None, **kwargs: Any) → Prompt
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L522" />

### <kbd>method</kbd> `dump`

```python  theme={null}
dump(fp: <class 'IO'>) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L525" />

### <kbd>method</kbd> `dump_file`

```python  theme={null}
dump_file(filepath: str | Path) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L84" />

### <kbd>method</kbd> `format`

```python  theme={null}
format(**kwargs: Any) → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L491" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L506" />

### <kbd>classmethod</kbd> `load`

```python  theme={null}
load(fp: <class 'IO'>) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L516" />

### <kbd>classmethod</kbd> `load_file`

```python  theme={null}
load_file(filepath: str | Path) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L422" />

### <kbd>method</kbd> `messages_table`

```python  theme={null}
messages_table(title: str | None = None) → Table
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L450" />

### <kbd>method</kbd> `print`

```python  theme={null}
print() → str
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L417" />

### <kbd>method</kbd> `publish`

```python  theme={null}
publish(name: str | None = None) → ObjectRef
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L407" />

### <kbd>method</kbd> `require`

```python  theme={null}
require(param_name: str, **kwargs: Any) → Prompt
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L535" />

### <kbd>method</kbd> `run`

```python  theme={null}
run() → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L298" />

### <kbd>method</kbd> `validate_requirement`

```python  theme={null}
validate_requirement(key: str, value: Any) → list
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L315" />

### <kbd>method</kbd> `validate_requirements`

```python  theme={null}
validate_requirements(values: dict[str, Any]) → list
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L434" />

### <kbd>method</kbd> `values_table`

```python  theme={null}
values_table(title: str | None = None) → Table
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L61" />

## <kbd>class</kbd> `Evaluation`

Sets up an evaluation which includes a set of scorers and a dataset.

Calling evaluation.evaluate(model) will pass in rows from a dataset into a model matching  the names of the columns of the dataset to the argument names in model.predict.

Then it will call all of the scorers and save the results in weave.

If you want to preprocess the rows from the dataset you can pass in a function to preprocess\_model\_input.

**Examples:**

```python  theme={null}
# Collect your examples
examples = [
     {"question": "What is the capital of France?", "expected": "Paris"},
     {"question": "Who wrote 'To Kill a Mockingbird'?", "expected": "Harper Lee"},
     {"question": "What is the square root of 64?", "expected": "8"},
]

# Define any custom scoring function
@weave.op
def match_score1(expected: str, model_output: dict) -> dict:
     # Here is where you'd define the logic to score the model output
     return {'match': expected == model_output['generated_text']}

@weave.op
def function_to_evaluate(question: str):
     # here's where you would add your LLM call and return the output
     return  {'generated_text': 'Paris'}

# Score your examples using scoring functions
evaluation = Evaluation(
     dataset=examples, scorers=[match_score1]
)

# Start tracking the evaluation
weave.init('intro-example')
# Run the evaluation
asyncio.run(evaluation.evaluate(function_to_evaluate))
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `dataset`: `<class 'dataset.dataset.Dataset'>`
* `scorers`: `list[typing.Annotated[trace.op_protocol.Op | flow.scorer.Scorer, BeforeValidator(func=<function cast_to_scorer at 0x110ab76a0>, json_schema_input_type=PydanticUndefined)]] | None`
* `preprocess_model_input`: `collections.abc.Callable[[dict], dict] | None`
* `trials`: `<class 'int'>`
* `metadata`: `dict[str, typing.Any] | None`
* `evaluation_name`: `str | collections.abc.Callable[trace.call.Call, str] | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L282" />

### <kbd>method</kbd> `evaluate`

```python  theme={null}
evaluate(model: Op | Model) → dict
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L119" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L240" />

### <kbd>method</kbd> `get_eval_results`

```python  theme={null}
get_eval_results(model: Op | Model) → EvaluationResults
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L293" />

### <kbd>method</kbd> `get_evaluate_calls`

```python  theme={null}
get_evaluate_calls() → PaginatedIterator[CallSchema, WeaveObject]
```

Retrieve all evaluation calls that used this Evaluation object.

Note that this returns a CallsIter instead of a single call because it's possible to have multiple evaluation calls for a single evaluation (e.g. if you run the same evaluation multiple times).

**Returns:**

* <b>`CallsIter`</b>:  An iterator over Call objects representing evaluation runs.

**Raises:**

* <b>`ValueError`</b>:  If the evaluation has no ref (hasn't been saved/run yet).

**Examples:**

```python  theme={null}
evaluation = Evaluation(dataset=examples, scorers=[scorer])
await evaluation.evaluate(model)  # Run evaluation first
calls = evaluation.get_evaluate_calls()
for call in calls:
     print(f"Evaluation run: {call.id} at {call.started_at}")
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L329" />

### <kbd>method</kbd> `get_score_calls`

```python  theme={null}
get_score_calls() → dict[str, list[Call]]
```

Retrieve scorer calls for each evaluation run, grouped by trace ID.

**Returns:**

* <b>`dict[str, list[Call]]`</b>:  A dictionary mapping trace IDs to lists of scorer Call objects.  Each trace ID represents one evaluation run, and the list contains all scorer  calls executed during that run.

**Examples:**

```python  theme={null}
evaluation = Evaluation(dataset=examples, scorers=[accuracy_scorer, f1_scorer])
await evaluation.evaluate(model)
score_calls = evaluation.get_score_calls()
for trace_id, calls in score_calls.items():
     print(f"Trace {trace_id}: {len(calls)} scorer calls")
     for call in calls:
         scorer_name = call.summary.get("weave", {}).get("trace_name")
         print(f"  Scorer: {scorer_name}, Output: {call.output}")
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval.py#L368" />

### <kbd>method</kbd> `get_scores`

```python  theme={null}
get_scores() → dict[str, dict[str, list[Any]]]
```

Extract and organize scorer outputs from evaluation runs.

**Returns:**

* <b>`dict[str, dict[str, list[Any]]]`</b>:  A nested dictionary structure where:
  * First level keys are trace IDs (evaluation runs)
  * Second level keys are scorer names
  * Values are lists of scorer outputs for that run and scorer

**Examples:**

```python  theme={null}
evaluation = Evaluation(dataset=examples, scorers=[accuracy_scorer, f1_scorer])
await evaluation.evaluate(model)
scores = evaluation.get_scores()
# Access scores by trace and scorer
for trace_id, trace_scores in scores.items():
         print(f"Evaluation run {trace_id}:")
         for scorer_name, outputs in trace_scores.items():
             print(f"  {scorer_name}: {outputs}")
```

Expected output:

```
{
     "trace_123": {
     "accuracy_scorer": [{"accuracy": 0.85}],
     "f1_scorer": [{"f1": 0.78}]
     }
}
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_model_construction.py#L160" />

### <kbd>method</kbd> `model_post_init`

```python  theme={null}
model_post_init(_Evaluation__context: Any) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L177" />

### <kbd>method</kbd> `predict_and_score`

```python  theme={null}
predict_and_score(model: Op | Model, example: dict) → dict
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L217" />

### <kbd>method</kbd> `summarize`

```python  theme={null}
summarize(eval_table: EvaluationResults) → dict
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L597" />

## <kbd>class</kbd> `EvaluationLogger`

This class provides an imperative interface for logging evaluations.

An evaluation is started automatically when the first prediction is logged using the `log_prediction` method, and finished when the `log_summary` method is called.

Each time you log a prediction, you will get back a `ScoreLogger` object. You can use this object to log scores and metadata for that specific prediction. For more information, see the `ScoreLogger` class.

Basic usage - log predictions with inputs and outputs directly:

```python  theme={null}
ev = EvaluationLogger()

# Log predictions with known inputs/outputs
pred = ev.log_prediction(inputs={'q': 'Hello'}, outputs={'a': 'Hi there!'})
pred.log_score("correctness", 0.9)

# Finish the evaluation
ev.log_summary({"avg_score": 0.9})
```

Advanced usage - use context manager for dynamic outputs and nested operations:

```python  theme={null}
ev = EvaluationLogger()

# Use context manager when you need to capture nested operations
with ev.log_prediction(inputs={'q': 'Hello'}) as pred:
     # Any operations here (like LLM calls) automatically become
     # children of the predict call
     response = your_llm_call(...)
     pred.output = response.content
     pred.log_score("correctness", 0.9)

# Finish the evaluation
ev.log_summary({"avg_score": 0.9})
```

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L639" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(
    name: 'str | None' = None,
    model: 'Model | dict | str | None' = None,
    dataset: 'Dataset | list[dict] | str | None' = None,
    eval_attributes: 'dict[str, Any] | None' = None,
    scorers: 'list[str] | None' = None
) → None
```

***

#### <kbd>property</kbd> attributes

***

#### <kbd>property</kbd> ui\_url

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L1019" />

### <kbd>method</kbd> `fail`

```python  theme={null}
fail(exception: 'BaseException') → None
```

Convenience method to fail the evaluation with an exception.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L1003" />

### <kbd>method</kbd> `finish`

```python  theme={null}
finish(exception: 'BaseException | None' = None) → None
```

Clean up the evaluation resources explicitly without logging a summary.

Ensures all prediction calls and the main evaluation call are finalized. This is automatically called if the logger is used as a context manager.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L863" />

### <kbd>method</kbd> `log_example`

```python  theme={null}
log_example(
    inputs: 'dict[str, Any]',
    output: 'Any',
    scores: 'dict[str, ScoreType]'
) → None
```

Log a complete example with inputs, output, and scores.

This is a convenience method that combines log\_prediction and log\_score for when you have all the data upfront.

**Args:**

* <b>`inputs`</b>: The input data for the prediction
* <b>`output`</b>: The output value
* <b>`scores`</b>: Dictionary mapping scorer names to score values
  **Example:**

```python  theme={null}
ev = EvaluationLogger()
ev.log_example(
    inputs={'q': 'What is 2+2?'},
    output='4',
    scores={'correctness': 1.0, 'fluency': 0.9}
)
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L791" />

### <kbd>method</kbd> `log_prediction`

```python  theme={null}
log_prediction(inputs: 'dict[str, Any]', output: 'Any' = None) → ScoreLogger
```

Log a prediction to the Evaluation.

Returns a ScoreLogger that can be used directly or as a context manager.

**Args:**

* <b>`inputs`</b>: The input data for the prediction
* <b>`output`</b>: The output value. Defaults to None. Can be set later using pred.output.
  **Returns:**
  ScoreLogger for logging scores and optionally finishing the prediction.

Example (direct):

* <b>`pred = ev.log_prediction({'q'`</b>:  '...'}, output="answer") pred.log\_score("correctness", 0.9) pred.finish()

Example (context manager):

* <b>`with ev.log_prediction({'q'`</b>:  '...'}) as pred:  response = model(...)  pred.output = response  pred.log\_score("correctness", 0.9) # Automatically calls finish() on exit

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L902" />

### <kbd>method</kbd> `log_summary`

```python  theme={null}
log_summary(summary: 'dict | None' = None, auto_summarize: 'bool' = True) → None
```

Log a summary dict to the Evaluation.

This will calculate the summary, call the summarize op, and then finalize the evaluation, meaning no more predictions or scores can be logged.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/evaluation/eval_imperative.py#L951" />

### <kbd>method</kbd> `set_view`

```python  theme={null}
set_view(
    name: 'str',
    content: 'Content | str',
    extension: 'str | None' = None,
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None,
    encoding: 'str' = 'utf-8'
) → None
```

Attach a view to the evaluation's main call summary under `weave.views`.

Saves the provided content as an object in the project and writes its reference URI under `summary.weave.views.<name>` for the evaluation's `evaluate` call. String inputs are wrapped as text content using `Content.from_text` with the provided extension or mimetype.

**Args:**

* <b>`name`</b>: The view name to display, used as the key under `summary.weave.views`.
* <b>`content`</b>: A `weave.Content` instance or string to serialize.
* <b>`extension`</b>: Optional file extension for string content inputs.
* <b>`mimetype`</b>: Optional MIME type for string content inputs.
* <b>`metadata`</b>: Optional metadata attached to newly created `Content`.
* <b>`encoding`</b>: Text encoding for string content inputs.
  **Returns:**
  None

**Examples:**
` import weave`

> > > ev = weave.EvaluationLogger()
> > > ev.set\_view("report", "# Report", extension="md")

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/File/file.py#L30" />

## <kbd>class</kbd> `File`

A class representing a file with path, mimetype, and size information.

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/File/file.py#L34" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(path: 'str | Path', mimetype: 'str | None' = None)
```

Initialize a File object.

**Args:**

***

#### <kbd>property</kbd> filename

Get the filename of the file.

* <b>`path`</b>: Path to the file (string or pathlib.Path)

* <b>`mimetype`</b>: Optional MIME type of the file - will be inferred from extension if not provided
  **Returns:**

* <b>`str`</b>:  The name of the file without the directory path.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/File/file.py#L60" />

### <kbd>method</kbd> `open`

```python  theme={null}
open() → bool
```

Open the file using the operating system's default application.

This method uses the platform-specific mechanism to open the file with the default application associated with the file's type.

**Returns:**

* <b>`bool`</b>:  True if the file was successfully opened, False otherwise.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/type_handlers/File/file.py#L81" />

### <kbd>method</kbd> `save`

```python  theme={null}
save(dest: 'str | Path') → None
```

Copy the file to the specified destination path.

**Args:**

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/rich/markdown.py#L512" />

## <kbd>class</kbd> `Markdown`

A Markdown renderable.

* <b>`dest`</b>: Destination path where the file will be copied to (string or pathlib.Path)  The destination path can be a file or a directory.
  **Args:**

* <b>`markup`</b> (str):  A string containing markdown.

* <b>`code_theme`</b> (str, optional):  Pygments theme for code blocks. Defaults to "monokai". See [https://pygments.org/styles/](https://pygments.org/styles/) for code themes.

* <b>`justify`</b> (JustifyMethod, optional):  Justify value for paragraphs. Defaults to None.

* <b>`style`</b> (Union\[str, Style], optional):  Optional style to apply to markdown.

* <b>`hyperlinks`</b> (bool, optional):  Enable hyperlinks. Defaults to `True`.

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/rich/markdown.py#L548" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(
    markup: 'str',
    code_theme: 'str' = 'monokai',
    justify: 'JustifyMethod | None' = None,
    style: 'str | Style' = 'none',
    hyperlinks: 'bool' = True,
    inline_code_lexer: 'str | None' = None,
    inline_code_theme: 'str | None' = None
) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L164" />

## <kbd>class</kbd> `MessagesPrompt`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L168" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(messages: list[dict])
```

* <b>`inline_code_lexer`</b>: (str, optional): Lexer to use if inline code highlighting is  enabled. Defaults to None.

* <b>`inline_code_theme`</b>: (Optional\[str], optional): Pygments theme for inline code  highlighting, or None for no highlighting. Defaults to None.
  **Pydantic Fields:**

* `name`: `str | None`

* `description`: `str | None`

* `ref`: `trace.refs.ObjectRef | None`

* `messages`: `list[dict]`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L180" />

### <kbd>method</kbd> `format`

```python  theme={null}
format(**kwargs: Any) → list
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L172" />

### <kbd>method</kbd> `format_message`

```python  theme={null}
format_message(message: dict, **kwargs: Any) → dict
```

Format a single message by replacing template variables.

This method delegates to the standalone format\_message\_with\_template\_vars function for the actual formatting logic.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L183" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/model.py#L25" />

## <kbd>class</kbd> `Model`

Intended to capture a combination of code and data the operates on an input. For example it might call an LLM with a prompt to make a prediction or generate text.

When you change the attributes or the code that defines your model, these changes will be logged and the version will be updated. This ensures that you can compare the predictions across different versions of your model. Use this to iterate on prompts or to try the latest LLM and compare predictions across different settings

**Examples:**

```python  theme={null}
class YourModel(Model):
     attribute1: str
     attribute2: int

     @weave.op
     def predict(self, input_data: str) -> dict:
         # Model logic goes here
         prediction = self.attribute1 + ' ' + input_data
         return {'pred': prediction}
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/model.py#L51" />

### <kbd>method</kbd> `get_infer_method`

```python  theme={null}
get_infer_method() → Callable
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/monitor.py#L12" />

## <kbd>class</kbd> `Monitor`

Sets up a monitor to score incoming calls automatically.

**Examples:**

```python  theme={null}
import weave
from weave.scorers import ValidJSONScorer

json_scorer = ValidJSONScorer()

my_monitor = weave.Monitor(
     name="my-monitor",
     description="This is a test monitor",
     sampling_rate=0.5,
     op_names=["my_op"],
     query={
         "$expr": {
             "$gt": [
                 {
                         "$getField": "started_at"
                     },
                     {
                         "$literal": 1742540400
                     }
                 ]
             }
         }
     },
     scorers=[json_scorer],
)

my_monitor.activate()
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `sampling_rate`: `<class 'float'>`
* `scorers`: `list[flow.scorer.Scorer]`
* `op_names`: `list[str]`
* `query`: `trace_server.interface.query.Query | None`
* `active`: `<class 'bool'>`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/monitor.py#L54" />

### <kbd>method</kbd> `activate`

```python  theme={null}
activate() → ObjectRef
```

Activates the monitor.

**Returns:**
The ref to the monitor.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/monitor.py#L64" />

### <kbd>method</kbd> `deactivate`

```python  theme={null}
deactivate() → ObjectRef
```

Deactivates the monitor.

**Returns:**
The ref to the monitor.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/monitor.py#L74" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/object/obj.py#L75" />

## <kbd>class</kbd> `Object`

Base class for Weave objects that can be tracked and versioned.

This class extends Pydantic's BaseModel to provide Weave-specific functionality for object tracking, referencing, and serialization. Objects can have names, descriptions, and references that allow them to be stored and retrieved from the Weave system.

**Attributes:**

* <b>`name`</b> (Optional\[str]):  A human-readable name for the object.
* <b>`description`</b> (Optional\[str]):  A description of what the object represents.
* <b>`ref`</b> (Optional\[ObjectRef]):  A reference to the object in the Weave system.

**Examples:**

```python  theme={null}
# Create a simple object
obj = Object(name="my_object", description="A test object")

# Create an object from a URI
obj = Object.from_uri("weave:///entity/project/object:digest")
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/object/obj.py#L114" />

### <kbd>classmethod</kbd> `from_uri`

```python  theme={null}
from_uri(uri: str, objectify: bool = True) → Self
```

Create an object instance from a Weave URI.

**Args:**

* <b>`uri`</b> (str):  The Weave URI pointing to the object.
* <b>`objectify`</b> (bool):  Whether to objectify the result. Defaults to True.

**Returns:**

* <b>`Self`</b>:  An instance of the class created from the URI.

**Raises:**

* <b>`NotImplementedError`</b>:  If the class doesn't implement the required  methods for deserialization.

**Examples:**

```python  theme={null}
obj = MyObject.from_uri("weave:///entity/project/object:digest")
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/object/obj.py#L140" />

### <kbd>classmethod</kbd> `handle_relocatable_object`

```python  theme={null}
handle_relocatable_object(
    v: Any,
    handler: ValidatorFunctionWrapHandler,
    info: ValidationInfo
) → Any
```

Handle validation of relocatable objects including ObjectRef and WeaveObject.

This validator handles special cases where the input is an ObjectRef or WeaveObject that needs to be properly converted to a standard Object instance. It ensures that references are preserved and that ignored types are handled correctly during the validation process.

**Args:**

* <b>`v`</b> (Any):  The value to validate.
* <b>`handler`</b> (ValidatorFunctionWrapHandler):  The standard pydantic validation handler.
* <b>`info`</b> (ValidationInfo):  Validation context information.

**Returns:**

* <b>`Any`</b>:  The validated object instance.

**Examples:**
This method is called automatically during object creation and validation. It handles cases like: \`\`\`python

# When an ObjectRef is passed

obj = MyObject(some\_object\_ref)

# When a WeaveObject is passed

obj = MyObject(some\_weave\_object)

````

---

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L159" />

## <kbd>class</kbd> `ObjectRef`
ObjectRef(entity: 'str', project: 'str', name: 'str', _digest: 'str | Future[str]', _extra: 'tuple[str | Future[str], ...]' = ()) 

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/../../../../weave/trace/refs/__init__" />

### <kbd>method</kbd> `__init__`

```python
__init__(
entity: 'str',
project: 'str',
name: 'str',
_digest: 'str | Future[str]',
_extra: 'tuple[str | Future[str], ]' = ()
) → None
````

***

#### <kbd>property</kbd> digest

***

#### <kbd>property</kbd> extra

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L167" />

### <kbd>method</kbd> `as_param_dict`

```python  theme={null}
as_param_dict() → dict
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L258" />

### <kbd>method</kbd> `delete`

```python  theme={null}
delete() → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L214" />

### <kbd>method</kbd> `get`

```python  theme={null}
get(objectify: 'bool' = True) → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L242" />

### <kbd>method</kbd> `is_descended_from`

```python  theme={null}
is_descended_from(potential_ancestor: 'ObjectRef') → bool
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L70" />

### <kbd>method</kbd> `maybe_parse_uri`

```python  theme={null}
maybe_parse_uri(s: 'str') → AnyRef | None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L265" />

### <kbd>method</kbd> `parse_uri`

```python  theme={null}
parse_uri(uri: 'str') → ObjectRef
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L208" />

### <kbd>method</kbd> `uri`

```python  theme={null}
uri() → str
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L149" />

### <kbd>method</kbd> `with_attr`

```python  theme={null}
with_attr(attr: 'str') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L141" />

### <kbd>method</kbd> `with_extra`

```python  theme={null}
with_extra(extra: 'tuple[str | Future[str], ]') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L152" />

### <kbd>method</kbd> `with_index`

```python  theme={null}
with_index(index: 'int') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L155" />

### <kbd>method</kbd> `with_item`

```python  theme={null}
with_item(item_digest: 'str | Future[str]') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/refs.py#L146" />

### <kbd>method</kbd> `with_key`

```python  theme={null}
with_key(key: 'str') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L83" />

## <kbd>class</kbd> `Prompt`

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L84" />

### <kbd>method</kbd> `format`

```python  theme={null}
format(**kwargs: Any) → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L493" />

## <kbd>class</kbd> `SavedView`

A fluent-style class for working with SavedView objects.

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L499" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(view_type: 'str' = 'traces', label: 'str' = 'SavedView') → None
```

***

#### <kbd>property</kbd> entity

***

#### <kbd>property</kbd> label

***

#### <kbd>property</kbd> project

***

#### <kbd>property</kbd> view\_type

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L623" />

### <kbd>method</kbd> `add_column`

```python  theme={null}
add_column(path: 'str | ObjectPath', label: 'str | None' = None) → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L632" />

### <kbd>method</kbd> `add_columns`

```python  theme={null}
add_columns(*columns: 'str') → SavedView
```

Convenience method for adding multiple columns to the grid.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L524" />

### <kbd>method</kbd> `add_filter`

```python  theme={null}
add_filter(
    field: 'str',
    operator: 'str',
    value: 'Any | None' = None
) → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L598" />

### <kbd>method</kbd> `add_sort`

```python  theme={null}
add_sort(field: 'str', direction: 'SortDirection') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L663" />

### <kbd>method</kbd> `column_index`

```python  theme={null}
column_index(path: 'int | str | ObjectPath') → int
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L578" />

### <kbd>method</kbd> `filter_op`

```python  theme={null}
filter_op(op_name: 'str | None') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L848" />

### <kbd>method</kbd> `get_calls`

```python  theme={null}
get_calls(
    limit: 'int | None' = None,
    offset: 'int | None' = None,
    include_costs: 'bool' = False,
    include_feedback: 'bool' = False,
    all_columns: 'bool' = False
) → CallsIter
```

Get calls matching this saved view's filters and settings.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L906" />

### <kbd>method</kbd> `get_known_columns`

```python  theme={null}
get_known_columns(num_calls_to_query: 'int | None' = None) → list[str]
```

Get the set of columns that are known to exist.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L916" />

### <kbd>method</kbd> `get_table_columns`

```python  theme={null}
get_table_columns() → list[TableColumn]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L617" />

### <kbd>method</kbd> `hide_column`

```python  theme={null}
hide_column(col_name: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L638" />

### <kbd>method</kbd> `insert_column`

```python  theme={null}
insert_column(
    idx: 'int',
    path: 'str | ObjectPath',
    label: 'str | None' = None
) → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L976" />

### <kbd>classmethod</kbd> `load`

```python  theme={null}
load(ref: 'str') → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L741" />

### <kbd>method</kbd> `page_size`

```python  theme={null}
page_size(page_size: 'int') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L711" />

### <kbd>method</kbd> `pin_column_left`

```python  theme={null}
pin_column_left(col_name: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L721" />

### <kbd>method</kbd> `pin_column_right`

```python  theme={null}
pin_column_right(col_name: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L683" />

### <kbd>method</kbd> `remove_column`

```python  theme={null}
remove_column(path: 'int | str | ObjectPath') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L702" />

### <kbd>method</kbd> `remove_columns`

```python  theme={null}
remove_columns(*columns: 'str') → SavedView
```

Remove columns from the saved view.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L547" />

### <kbd>method</kbd> `remove_filter`

```python  theme={null}
remove_filter(index_or_field: 'int | str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L562" />

### <kbd>method</kbd> `remove_filters`

```python  theme={null}
remove_filters() → SavedView
```

Remove all filters from the saved view.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L520" />

### <kbd>method</kbd> `rename`

```python  theme={null}
rename(label: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L677" />

### <kbd>method</kbd> `rename_column`

```python  theme={null}
rename_column(path: 'int | str | ObjectPath', label: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L833" />

### <kbd>method</kbd> `save`

```python  theme={null}
save() → SavedView
```

Publish the saved view to the server.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L657" />

### <kbd>method</kbd> `set_columns`

```python  theme={null}
set_columns(*columns: 'str') → SavedView
```

Set the columns to be displayed in the grid.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L611" />

### <kbd>method</kbd> `show_column`

```python  theme={null}
show_column(col_name: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L605" />

### <kbd>method</kbd> `sort_by`

```python  theme={null}
sort_by(field: 'str', direction: 'SortDirection') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L889" />

### <kbd>method</kbd> `to_grid`

```python  theme={null}
to_grid(limit: 'int | None' = None) → Grid
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L770" />

### <kbd>method</kbd> `to_rich_table_str`

```python  theme={null}
to_rich_table_str() → str
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L753" />

### <kbd>method</kbd> `ui_url`

```python  theme={null}
ui_url() → str | None
```

URL to show this saved view in the UI.

Note this is the "result" page with traces etc, not the URL for the view object.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/saved_view.py#L731" />

### <kbd>method</kbd> `unpin_column`

```python  theme={null}
unpin_column(col_name: 'str') → SavedView
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/scorer.py#L30" />

## <kbd>class</kbd> `Scorer`

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `column_map`: `dict[str, str] | None`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/scorer.py#L48" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/flow/scorer.py#L36" />

### <kbd>method</kbd> `model_post_init`

```python  theme={null}
model_post_init(_Scorer__context: Any) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L40" />

### <kbd>method</kbd> `score`

```python  theme={null}
score(output: Any, **kwargs: Any) → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L44" />

### <kbd>method</kbd> `summarize`

```python  theme={null}
summarize(score_rows: list) → dict | None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L88" />

## <kbd>class</kbd> `StringPrompt`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L92" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(content: str)
```

**Pydantic Fields:**

* `name`: `str | None`
* `description`: `str | None`
* `ref`: `trace.refs.ObjectRef | None`
* `content`: `<class 'str'>`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L96" />

### <kbd>method</kbd> `format`

```python  theme={null}
format(**kwargs: Any) → str
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/prompt/prompt.py#L99" />

### <kbd>classmethod</kbd> `from_obj`

```python  theme={null}
from_obj(obj: WeaveObject) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/table.py#L9" />

## <kbd>class</kbd> `Table`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/table.py#L12" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(rows: 'list[dict]') → None
```

***

#### <kbd>property</kbd> rows

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/table.py#L50" />

### <kbd>method</kbd> `append`

```python  theme={null}
append(row: 'dict') → None
```

Add a row to the table.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/table.py#L56" />

### <kbd>method</kbd> `pop`

```python  theme={null}
pop(index: 'int') → None
```

Remove a row at the given index from the table.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L100" />

## <kbd>class</kbd> `ContextAwareThread`

A Thread that runs functions with the context of the caller.

This is a drop-in replacement for threading.Thread that ensures calls behave as expected inside the thread.  Weave requires certain contextvars to be set (see call\_context.py), but new threads do not automatically copy context from the parent, which can cause the call context to be lost -- not good!  This class automates contextvar copying so using this thread "just works" as the user probably expects.

You can achieve the same effect without this class by instead writing:

```python  theme={null}
def run_with_context(func, *args, **kwargs):
     context = copy_context()
     def wrapper():
         context.run(func, *args, **kwargs)
     return wrapper

thread = threading.Thread(target=run_with_context(your_func, *args, **kwargs))
thread.start()
```

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L124" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(*args: 'Any', **kwargs: 'Any') → None
```

***

#### <kbd>property</kbd> daemon

A boolean value indicating whether this thread is a daemon thread.

This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.

The entire Python program exits when only daemon threads are left.

***

#### <kbd>property</kbd> ident

Thread identifier of this thread or None if it has not been started.

This is a nonzero integer. See the get\_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.

***

#### <kbd>property</kbd> name

A string used for identification purposes only.

It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.

***

#### <kbd>property</kbd> native\_id

Native integral thread ID of this thread, or None if it has not been started.

This is a non-negative integer. See the get\_native\_id() function. This represents the Thread ID as reported by the kernel.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L128" />

### <kbd>method</kbd> `run`

```python  theme={null}
run() → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L309" />

## <kbd>class</kbd> `ThreadContext`

Context object providing access to current thread and turn information.

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L312" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(thread_id: 'str | None')
```

Initialize ThreadContext with the specified thread\_id.

**Args:**

***

#### <kbd>property</kbd> thread\_id

Get the thread\_id for this context.

* <b>`thread_id`</b>: The thread identifier for this context, or None if disabled.
  **Returns:**
  The thread identifier, or None if thread tracking is disabled.

***

#### <kbd>property</kbd> turn\_id

Get the current turn\_id from the active context.

**Returns:**
The current turn\_id if set, None otherwise.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L40" />

## <kbd>class</kbd> `ContextAwareThreadPoolExecutor`

A ThreadPoolExecutor that runs functions with the context of the caller.

This is a drop-in replacement for concurrent.futures.ThreadPoolExecutor that ensures weave calls behave as expected inside the executor.  Weave requires certain contextvars to be set (see call\_context.py), but new threads do not automatically copy context from the parent, which can cause the call context to be lost -- not good!  This class automates contextvar copying so using this executor "just works" as the user probably expects.

You can achieve the same effect without this class by instead writing:

```python  theme={null}
with concurrent.futures.ThreadPoolExecutor() as executor:
     contexts = [copy_context() for _ in range(len(vals))]

     def _wrapped_fn(*args):
         return contexts.pop().run(fn, *args)

     executor.map(_wrapped_fn, vals)
```

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L63" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(*args: 'Any', **kwargs: 'Any') → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L72" />

### <kbd>method</kbd> `map`

```python  theme={null}
map(
    fn: 'Callable',
    *iterables: 'Iterable[Any]',
    timeout: 'float | None' = None,
    chunksize: 'int' = 1
) → Iterator
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/util.py#L68" />

### <kbd>method</kbd> `submit`

```python  theme={null}
submit(fn: 'Callable', *args: 'Any', **kwargs: 'Any') → Any
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L1388" />

### <kbd>function</kbd> `as_op`

```python  theme={null}
as_op(fn: 'Callable[P, R]') → Op[P, R]
```

Given a @weave.op decorated function, return its Op.

@weave.op decorated functions are instances of Op already, so this function should be a no-op at runtime. But you can use it to satisfy type checkers if you need to access OpDef attributes in a typesafe way.

**Args:**

* <b>`fn`</b>: A weave.op decorated function.
  **Returns:**
  The Op of the function.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/../../../../weave/trace/api/attributes#L236" />

### <kbd>function</kbd> `attributes`

```python  theme={null}
attributes(attributes: 'dict[str, Any]') → Iterator
```

Context manager for setting attributes on a call.

**Example:**

```python  theme={null}
with weave.attributes({'env': 'production'}):
     print(my_function.call("World"))
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L386" />

### <kbd>function</kbd> `finish`

```python  theme={null}
finish() → None
```

Stops logging to weave.

Following finish, calls of weave.op decorated functions will no longer be logged. You will need to run weave.init() again to resume logging.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L210" />

### <kbd>function</kbd> `get`

```python  theme={null}
get(uri: 'str | ObjectRef') → Any
```

A convenience function for getting an object from a URI.

Many objects logged by Weave are automatically registered with the Weave server. This function allows you to retrieve those objects by their URI.

**Args:**

* <b>`uri`</b>: A fully-qualified weave ref URI.
  **Returns:**
  The object.

**Example:**

```python  theme={null}
weave.init("weave_get_example")
dataset = weave.Dataset(rows=[{"a": 1, "b": 2}])
ref = weave.publish(dataset)

dataset2 = weave.get(ref)  # same as dataset!
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L114" />

### <kbd>function</kbd> `get_client`

```python  theme={null}
get_client() → WeaveClient | None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/context/call_context.py#L118" />

### <kbd>function</kbd> `get_current_call`

```python  theme={null}
get_current_call() → Call | None
```

Get the Call object for the currently executing Op, within that Op.

**Returns:**
The Call object for the currently executing Op, or  None if tracking has not been initialized or this method is  invoked outside an Op.

**Note:**

> The returned Call's `attributes` dictionary becomes immutable once the call starts. Use :func:`weave.attributes` to set call metadata before invoking an Op. The `summary` field may be updated while the Op executes and will be merged with computed summary information when the call finishes.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L43" />

### <kbd>function</kbd> `init`

```python  theme={null}
init(
    project_name: 'str',
    settings: 'UserSettings | dict[str, Any] | None' = None,
    autopatch_settings: 'AutopatchSettings | None' = None,
    global_postprocess_inputs: 'PostprocessInputsFunc | None' = None,
    global_postprocess_output: 'PostprocessOutputFunc | None' = None,
    global_attributes: 'dict[str, Any] | None' = None
) → WeaveClient
```

Initialize weave tracking, logging to a wandb project.

Logging is initialized globally, so you do not need to keep a reference to the return value of init.

Following init, calls of weave.op decorated functions will be logged to the specified project.

**Args:**

NOTE: Global postprocessing settings are applied to all ops after each op's own postprocessing.  The order is always: 1. Op-specific postprocessing 2. Global postprocessing

* <b>`project_name`</b>: The name of the Weights & Biases team and project to log to. If you don't  specify a team, your default entity is used. To find or update your default entity, refer to [User Settings](https://docs.wandb.ai/guides/models/app/settings-page/user-settings/#default-team) in the W\&B Models documentation.
* <b>`settings`</b>: Configuration for the Weave client generally.
* <b>`autopatch_settings`</b>: (Deprecated) Configuration for autopatch integrations. Use explicit patching instead.
* <b>`global_postprocess_inputs`</b>: A function that will be applied to all inputs of all ops.
* <b>`global_postprocess_output`</b>: A function that will be applied to all outputs of all ops.
* <b>`global_attributes`</b>: A dictionary of attributes that will be applied to all traces.
  **Returns:**
  A Weave client.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/log_call.py#L18" />

### <kbd>function</kbd> `log_call`

```python  theme={null}
log_call(
    op: 'str',
    inputs: 'dict[str, Any]',
    output: 'Any',
    parent: 'Call | None' = None,
    attributes: 'dict[str, Any] | None' = None,
    display_name: 'str | Callable[[Call], str] | None' = None,
    use_stack: 'bool' = True,
    exception: 'BaseException | None' = None
) → Call
```

Log a call directly to Weave without using the decorator pattern.

This function provides an imperative API for logging operations to Weave, useful when you want to log calls after they've already been executed or when the decorator pattern isn't suitable for your use case.

**Args:**

* <b>`op`</b> (str):  The operation name to log. This will be used as the op\_name  for the call. Anonymous operations (strings not referring to published  ops) are supported.
* <b>`inputs`</b> (dict\[str, Any]):  A dictionary of input parameters for the operation.
* <b>`output`</b> (Any):  The output/result of the operation.
* <b>`parent`</b> (Call | None):  Optional parent call to nest this call under.  If not provided, the call will be a root-level call (or nested under  the current call context if one exists). Defaults to None.
* <b>`attributes`</b> (dict\[str, Any] | None):  Optional metadata to attach to the call.  These are frozen once the call is created. Defaults to None.
* <b>`display_name`</b> (str | Callable\[\[Call], str] | None):  Optional display name  for the call in the UI. Can be a string or a callable that takes the  call and returns a string. Defaults to None.
* <b>`use_stack`</b> (bool):  Whether to push the call onto the runtime stack. When True,  the call will be available in the call context and can be accessed via  weave.require\_current\_call(). When False, the call is logged but not  added to the call stack. Defaults to True.
* <b>`exception`</b> (BaseException | None):  Optional exception to log if the operation  failed. Defaults to None.

**Returns:**

* <b>`Call`</b>:  The created and finished Call object with full trace information.

**Examples:**
Basic usage:

````python  theme={null}
import weave
    >>> weave.init('my-project')
    >>> call = weave.log_call(
    ...     op="my_function",
    ...     inputs={"x": 5, "y": 10},
    ...     output=15
    ... )

    Logging with attributes and display name:
    >>> call = weave.log_call(
    ...     op="process_data",
    ...     inputs={"data": [1, 2, 3]},
    ...     output={"mean": 2.0},
    ...     attributes={"version": "1.0", "env": "prod"},
    ...     display_name="Data Processing"
    ... )

    Logging a failed operation:
    >>> try:
    ...     result = risky_operation()
    ... except Exception as e:
    ...     call = weave.log_call(
    ...         op="risky_operation",
    ...         inputs={},
    ...         output=None,
    ...         exception=e
    ...     )

    Nesting calls:
    >>> parent_call = weave.log_call("parent", {"input": 1}, 2)
    >>> child_call = weave.log_call(
    ...     "child",
    ...     {"input": 2},
    ...     4,
    ...     parent=parent_call
    ... )

    Logging without adding to call stack:
    >>> call = weave.log_call(
    ...     op="background_task",
    ...     inputs={"task_id": 123},
    ...     output="completed",
    ...     use_stack=False  # Don't push to call stack
    ... )

---

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/op.py#L1202" />

### <kbd>function</kbd> `op`

```python
op(
    func: 'Callable[P, R] | None' = None,
    name: 'str | None' = None,
    call_display_name: 'str | CallDisplayNameFunc | None' = None,
    postprocess_inputs: 'PostprocessInputsFunc | None' = None,
    postprocess_output: 'PostprocessOutputFunc | None' = None,
    tracing_sample_rate: 'float' = 1.0,
    enable_code_capture: 'bool' = True,
    accumulator: 'Callable[[Any | None, Any], Any] | None' = None,
    kind: 'OpKind | None' = None,
    color: 'OpColor | None' = None
) → Callable[[Callable[P, R]], Op[P, R]] | Op[P, R]
````

A decorator to weave op-ify a function or method. Works for both sync and async. Automatically detects iterator functions and applies appropriate behavior.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L118" />

### <kbd>function</kbd> `publish`

```python  theme={null}
publish(obj: 'Any', name: 'str | None' = None) → ObjectRef
```

Save and version a Python object.

Weave creates a new version of the object if the object's name already exists and its content hash does not match the latest version of that object.

**Args:**

* <b>`obj`</b>: The object to save and version.
* <b>`name`</b>: The name to save the object under.
  **Returns:**
  A Weave Ref to the saved object.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L181" />

### <kbd>function</kbd> `ref`

```python  theme={null}
ref(location: 'str') → ObjectRef
```

Creates a Ref to an existing Weave object. This does not directly retrieve the object but allows you to pass it to other Weave API functions.

**Args:**

* <b>`location`</b>: A Weave Ref URI, or if `weave.init()` has been called, `name:version` or `name`. If no version is provided, `latest` is used.
  **Returns:**
  A Weave Ref to the object.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/context/call_context.py#L69" />

### <kbd>function</kbd> `require_current_call`

```python  theme={null}
require_current_call() → Call
```

Get the Call object for the currently executing Op, within that Op.

This allows you to access attributes of the Call such as its id or feedback while it is running.

```python  theme={null}
@weave.op
def hello(name: str) -> None:
     print(f"Hello {name}!")
     current_call = weave.require_current_call()
     print(current_call.id)
```

It is also possible to access a Call after the Op has returned.

If you have the Call's id, perhaps from the UI, you can use the `get_call` method on the `WeaveClient` returned from `weave.init` to retrieve the Call object.

```python  theme={null}
client = weave.init("<project>")
mycall = client.get_call("<call_id>")
```

Alternately, after defining your Op you can use its `call` method. For example:

```python  theme={null}
@weave.op
def add(a: int, b: int) -> int:
     return a + b

result, call = add.call(1, 2)
print(call.id)
```

**Returns:**
The Call object for the currently executing Op

**Raises:**

* <b>`NoCurrentCallError`</b>:  If tracking has not been initialized or this method is  invoked outside an Op.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace/api.py#L256" />

### <kbd>function</kbd> `set_view`

```python  theme={null}
set_view(
    name: 'str',
    content: 'Content | str',
    extension: 'str | None' = None,
    mimetype: 'str | None' = None,
    metadata: 'dict[str, Any] | None' = None,
    encoding: 'str' = 'utf-8'
) → None
```

Attach a custom view to the current call summary at `_weave.views.<name>`.

**Args:**

* <b>`name`</b>: The view name (key under `summary._weave.views`).
* <b>`content`</b>: A `weave.Content` instance or raw string. Strings are wrapped via  `Content.from_text` using the supplied extension or mimetype.
* <b>`extension`</b>: Optional file extension to use when `content` is a string.
* <b>`mimetype`</b>: Optional MIME type to use when `content` is a string.
* <b>`metadata`</b>: Optional metadata to attach when creating `Content` from text.
* <b>`encoding`</b>: Text encoding to apply when creating `Content` from text.
  **Returns:**
  None

**Examples:**
` import weave`

> > > weave.init("proj")
> > > @weave.op
> > > ... def foo():
> > > ...     weave.set\_view("readme", "# Hello", extension="md")
> > > ...     return 1
> > > foo()

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/../../../../weave/trace/api/thread#L339" />

### <kbd>function</kbd> `thread`

```python  theme={null}
thread(
    thread_id: 'str | None | object' = <object object at 0x1105c49a0>
) → Iterator[ThreadContext]
```

Context manager for setting thread\_id on calls within the context.

**Examples:**

```python  theme={null}
# Auto-generate thread_id
with weave.thread() as t:
     print(f"Thread ID: {t.thread_id}")
     result = my_function("input")  # This call will have the auto-generated thread_id
     print(f"Current turn: {t.turn_id}")

# Explicit thread_id
with weave.thread("custom_thread") as t:
     result = my_function("input")  # This call will have thread_id="custom_thread"

# Disable threading
with weave.thread(None) as t:
     result = my_function("input")  # This call will have thread_id=None
```

**Args:**

* <b>`thread_id`</b>: The thread identifier to associate with calls in this context.  If not provided, a UUID v7 will be auto-generated.  If None, thread tracking will be disabled.
  **Yields:**

* <b>`ThreadContext`</b>:  An object providing access to thread\_id and current turn\_id.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/integrations/wandb/wandb.py#L9" />

### <kbd>function</kbd> `wandb_init_hook`

```python  theme={null}
wandb_init_hook() → None
```
