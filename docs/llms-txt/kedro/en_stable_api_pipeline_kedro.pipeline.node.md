# Source: https://docs.kedro.org/en/stable/api/pipeline/kedro.pipeline.node/index.md

## kedro.pipeline.node

This module provides user-friendly functions for creating nodes as parts of Kedro pipelines.

### GroupedNodes

```
GroupedNodes(name, type, nodes=list(), dependencies=list())
```

Represents a logical group of nodes, typically by namespace or a custom grouping. A group can also consist of a single node. This is used to support deployment—for example, by executing the entire group in a single container run.

### Node

```
Node(func, inputs, outputs, *, name=None, tags=None, confirms=None, namespace=None, preview_fn=None)
```

`Node` is an auxiliary class facilitating the operations required to run user-provided functions as part of Kedro pipelines.

Parameters:

- **`func`** (`Callable`) – A function that corresponds to the node logic. The function should have at least one input or output.
- **`inputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as inputs to the function. The number of names should match the number of arguments in the definition of the provided function. When dict[str, str] is provided, variable names will be mapped to function argument names.
- **`outputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as outputs of the function. The number of names should match the number of outputs returned by the provided function. When dict[str, str] is provided, variable names will be mapped to the named outputs the function returns.
- **`name`** (`str | None`, default: `None` ) – Optional node name to be used when displaying the node in logs or any other visualisations. Valid node name must contain only letters, digits, hyphens, underscores and/or fullstops.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to the node. Valid node tag must contain only letters, digits, hyphens, underscores and/or fullstops.
- **`confirms`** (`str | list[str] | None`, default: `None` ) – Optional name or the list of the names of the datasets that should be confirmed. This will result in calling confirm() method of the corresponding dataset instance. Specified dataset names do not necessarily need to be present in the node inputs or outputs.
- **`namespace`** (`str | None`, default: `None` ) – Optional node namespace.
- **`preview_fn`** (`Callable[..., PreviewPayload] | None`, default: `None` ) – Optional preview function that returns one of the valid preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview). This is an experimental feature.

Raises:

- `ValueError` – Raised in the following cases: a) When the provided arguments do not conform to the format suggested by the type hint of the argument. b) When the node produces multiple outputs with the same name. c) When an input has the same name as an output. d) When the given node name violates the requirements: it must contain only letters, digits, hyphens, underscores and/or fullstops.

Source code in `kedro/pipeline/node.py`

```
def __init__(  # noqa: PLR0913, PLR0912
    self,
    func: Callable,
    inputs: str | list[str] | dict[str, str] | None,
    outputs: str | list[str] | dict[str, str] | None,
    *,
    name: str | None = None,
    tags: str | Iterable[str] | None = None,
    confirms: str | list[str] | None = None,
    namespace: str | None = None,
    preview_fn: Callable[..., PreviewPayload] | None = None,
):
    """Create a node in the pipeline by providing a function to be called
    along with variable names for inputs and/or outputs.

    Args:
        func: A function that corresponds to the node logic.
            The function should have at least one input or output.
        inputs: The name or the list of the names of variables used as
            inputs to the function. The number of names should match
            the number of arguments in the definition of the provided
            function. When dict[str, str] is provided, variable names
            will be mapped to function argument names.
        outputs: The name or the list of the names of variables used
            as outputs of the function. The number of names should match
            the number of outputs returned by the provided function.
            When dict[str, str] is provided, variable names will be mapped
            to the named outputs the function returns.
        name: Optional node name to be used when displaying the node in
            logs or any other visualisations. Valid node name must contain
            only letters, digits, hyphens, underscores and/or fullstops.
        tags: Optional set of tags to be applied to the node. Valid node tag must
            contain only letters, digits, hyphens, underscores and/or fullstops.
        confirms: Optional name or the list of the names of the datasets
            that should be confirmed. This will result in calling
            ``confirm()`` method of the corresponding dataset instance.
            Specified dataset names do not necessarily need to be present
            in the node ``inputs`` or ``outputs``.
        namespace: Optional node namespace.
        preview_fn: Optional preview function that returns one of the valid
            preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview).
            This is an experimental feature.

    Raises:
        ValueError: Raised in the following cases:
            a) When the provided arguments do not conform to
            the format suggested by the type hint of the argument.
            b) When the node produces multiple outputs with the same name.
            c) When an input has the same name as an output.
            d) When the given node name violates the requirements:
            it must contain only letters, digits, hyphens, underscores
            and/or fullstops.

    """
    if not callable(func):
        raise ValueError(
            _node_error_message(
                f"first argument must be a function, not '{type(func).__name__}'."
            )
        )

    if inputs and not isinstance(inputs, (list | dict | str)):
        raise ValueError(
            _node_error_message(
                f"'inputs' type must be one of [String, List, Dict, None], "
                f"not '{type(inputs).__name__}'."
            )
        )

    for _input in _to_list(inputs):
        if not isinstance(_input, str):
            raise ValueError(
                _node_error_message(
                    f"names of variables used as inputs to the function "
                    f"must be of 'String' type, but {_input} from {inputs} "
                    f"is '{type(_input)}'."
                )
            )
        _node_dataset_name_validation(_input, namespace)

    if outputs and not isinstance(outputs, (list | dict | str)):
        raise ValueError(
            _node_error_message(
                f"'outputs' type must be one of [String, List, Dict, None], "
                f"not '{type(outputs).__name__}'."
            )
        )

    for _output in _to_list(outputs):
        if not isinstance(_output, str):
            raise ValueError(
                _node_error_message(
                    f"names of variables used as outputs of the function "
                    f"must be of 'String' type, but {_output} from {outputs} "
                    f"is '{type(_output)}'."
                )
            )
        _node_dataset_name_validation(_output, namespace)

    if not inputs and not outputs:
        raise ValueError(
            _node_error_message("it must have some 'inputs' or 'outputs'.")
        )

    self._validate_inputs(func, inputs)

    self._func = func
    self._inputs = inputs
    # The type of _outputs is picked up as possibly being None, however the checks above prevent that
    # ever being the case. Mypy doesn't get that though, so it complains about the assignment of outputs to
    # _outputs with different types.
    self._outputs: str | list[str] | dict[str, str] = outputs  # type: ignore[assignment]
    if name and not re.match(r"[\w\.-]+$", name):
        raise ValueError(
            f"'{name}' is not a valid node name. It must contain only "
            f"letters, digits, hyphens, underscores and/or fullstops."
        )
    self._name = name
    self._namespace = namespace
    self._tags = set(_to_list(tags))
    for tag in self._tags:
        if not re.match(r"[\w\.-]+$", tag):
            raise ValueError(
                f"'{tag}' is not a valid node tag. It must contain only "
                f"letters, digits, hyphens, underscores and/or fullstops."
            )

    self._validate_unique_outputs()
    self._validate_inputs_dif_than_outputs()
    self._confirms = confirms

    if preview_fn:
        if not callable(preview_fn):
            raise ValueError(
                _node_error_message(
                    f"preview_fn must be a function, not '{type(preview_fn).__name__}'."
                )
            )
        if not getattr(Node, "__preview_fn_warned__", False):
            warn(
                "The 'preview_fn' feature is experimental and may change in future versions.",
                category=KedroExperimentalWarning,
                stacklevel=2,
            )
            setattr(Node, "__preview_fn_warned__", True)

    self._preview_fn = preview_fn
```

#### confirms

```
confirms
```

Return dataset names to confirm as a list.

Returns:

- `list[str]` – Dataset names to confirm as a list.

#### func

```
func
```

Exposes the underlying function of the node.

Returns:

- `Callable` – Return the underlying function of the node.

#### inputs

```
inputs
```

Return node inputs as a list, in the order required to bind them properly to the node's function.

Returns:

- `list[str]` – Node input names as a list.

#### name

```
name
```

Node's name.

Returns:

- `str` – Node's name if provided or the name of its function.

#### namespace

```
namespace
```

Node's namespace.

Returns:

- `str | None` – String representing node's namespace, typically from outer to inner scopes.

#### namespace_prefixes

```
namespace_prefixes
```

Return all hierarchical prefixes of the node's namespace.

Returns:

- `list[str]` – A list of namespace prefixes, from shortest to longest.
- `list[str]` – For example, a namespace 'a.b.c' would return ['a', 'a.b', 'a.b.c'].
- `list[str]` – If the node has no namespace, returns an empty list.

#### outputs

```
outputs
```

Return node outputs as a list preserving the original order if possible.

Returns:

- `list[str]` – Node output names as a list.

#### short_name

```
short_name
```

Node's name.

Returns:

- `str` – Returns a short, user-friendly name that is not guaranteed to be unique.
- `str` – The namespace is stripped out of the node name.

#### tags

```
tags
```

Return the tags assigned to the node.

Returns:

- `set[str]` – Return the set of all assigned tags to the node.

#### preview

```
preview()
```

Execute the preview function if available and validate its return type.

Returns:

- `PreviewPayload | None` – A preview payload (one of TextPreview, MermaidPreview, ImagePreview, or CustomPreview) if preview_fn is set, None otherwise.

Raises:

- `ValueError` – If the preview function does not return one of the valid preview types.

Examples:

```
from kedro.pipeline.preview_contract import (
    MermaidPreview,
    ImagePreview,
)

# Define your preview methods


# Example 1: Mermaid diagram
def preview_pipeline_flow() -> MermaidPreview:
    steps = ["Load", "Validate", "Transform", "Save"]
    mermaid = "graph LR\n"
    for i, step in enumerate(steps):
        if i < len(steps) - 1:
            mermaid += f"    {step} --> {steps[i+1]}\n"

    return MermaidPreview(content=mermaid)


# Example 2: Image preview (URL or data URI)
def preview_image() -> ImagePreview:
    return ImagePreview(
        content="https://example.com/chart.png",
        # or use data URI: "data:image/png;base64,iVBORw0KGgo..."
    )


# Define your node which uses the preview_fn
my_node = node(
    func=process_data,
    inputs="raw_data",
    outputs="processed_data",
    preview_fn=your_preview_function,
)

# Receive the preview payload
payload = my_node.preview()

# Serialize for frontend/API use:
json_dict = payload.to_dict()  # Returns JSONObject
```

Source code in `kedro/pipeline/node.py`

````
def preview(self) -> PreviewPayload | None:
    """Execute the preview function if available and validate its return type.

    Returns:
        A preview payload (one of TextPreview, MermaidPreview, ImagePreview,
            or CustomPreview) if preview_fn is set, None otherwise.

    Raises:
        ValueError: If the preview function does not return one of the valid
            preview types.

    Examples:
        ```python
        from kedro.pipeline.preview_contract import (
            MermaidPreview,
            ImagePreview,
        )

        # Define your preview methods


        # Example 1: Mermaid diagram
        def preview_pipeline_flow() -> MermaidPreview:
            steps = ["Load", "Validate", "Transform", "Save"]
            mermaid = "graph LR\\n"
            for i, step in enumerate(steps):
                if i < len(steps) - 1:
                    mermaid += f"    {step} --> {steps[i+1]}\\n"

            return MermaidPreview(content=mermaid)


        # Example 2: Image preview (URL or data URI)
        def preview_image() -> ImagePreview:
            return ImagePreview(
                content="https://example.com/chart.png",
                # or use data URI: "data:image/png;base64,iVBORw0KGgo..."
            )


        # Define your node which uses the preview_fn
        my_node = node(
            func=process_data,
            inputs="raw_data",
            outputs="processed_data",
            preview_fn=your_preview_function,
        )

        # Receive the preview payload
        payload = my_node.preview()

        # Serialize for frontend/API use:
        json_dict = payload.to_dict()  # Returns JSONObject
        ```
    """
    if not self._preview_fn:
        return None

    result = self._preview_fn()

    # Import the specific preview classes for isinstance check
    from kedro.pipeline.preview_contract import (
        CustomPreview,
        ImagePreview,
        MermaidPreview,
        TextPreview,
    )

    valid_types = (
        TextPreview,
        MermaidPreview,
        ImagePreview,
        CustomPreview,
    )

    if not isinstance(result, valid_types):
        raise ValueError(
            f"preview_fn must return one of the valid preview types "
            f"(TextPreview, MermaidPreview, ImagePreview, or CustomPreview), "
            f"but got '{type(result).__name__}' instead."
        )

    return result
````

#### run

```
run(inputs=None)
```

Run this node using the provided inputs and return its results in a dictionary.

Parameters:

- **`inputs`** (`dict[str, Any] | None`, default: `None` ) – Dictionary of inputs as specified at the creation of the node.

Raises:

- `ValueError` – In the following cases: a) The node function inputs are incompatible with the node input definition. Example 1: node definition input is a list of 2 DataFrames, whereas only 1 was provided or 2 different ones were provided. b) The node function outputs are incompatible with the node output definition. Example 1: node function definition is a dictionary, whereas function returns a list. Example 2: node definition output is a list of 5 strings, whereas the function returns a list of 4 objects.
- `Exception` – Any exception thrown during execution of the node.

Returns:

- `dict[str, Any]` – All produced node outputs are returned in a dictionary, where the
- `dict[str, Any]` – keys are defined by the node outputs.

Source code in `kedro/pipeline/node.py`

```
def run(self, inputs: dict[str, Any] | None = None) -> dict[str, Any]:
    """Run this node using the provided inputs and return its results
    in a dictionary.

    Args:
        inputs: Dictionary of inputs as specified at the creation of
            the node.

    Raises:
        ValueError: In the following cases:
            a) The node function inputs are incompatible with the node
            input definition.
            Example 1: node definition input is a list of 2
            DataFrames, whereas only 1 was provided or 2 different ones
            were provided.
            b) The node function outputs are incompatible with the node
            output definition.
            Example 1: node function definition is a dictionary,
            whereas function returns a list.
            Example 2: node definition output is a list of 5
            strings, whereas the function returns a list of 4 objects.
        Exception: Any exception thrown during execution of the node.

    Returns:
        All produced node outputs are returned in a dictionary, where the
        keys are defined by the node outputs.

    """
    self._logger.info("Running node: %s", str(self))

    outputs = None

    if not (inputs is None or isinstance(inputs, dict)):
        raise ValueError(
            f"Node.run() expects a dictionary or None, "
            f"but got {type(inputs)} instead"
        )

    try:
        inputs = {} if inputs is None else inputs
        if not self._inputs:
            outputs = self._run_with_no_inputs(inputs)
        elif isinstance(self._inputs, str):
            outputs = self._run_with_one_input(inputs, self._inputs)
        elif isinstance(self._inputs, list):
            outputs = self._run_with_list(inputs, self._inputs)
        elif isinstance(self._inputs, dict):
            outputs = self._run_with_dict(inputs, self._inputs)

        return self._outputs_to_dictionary(outputs)

    # purposely catch all exceptions
    except Exception as exc:
        self._logger.error(
            "Node %s failed with error: \n%s",
            str(self),
            str(exc),
            extra={"markup": True},
        )
        raise exc
```

#### tag

```
tag(tags)
```

Create a new `Node` which is an exact copy of the current one, but with more tags added to it.

Parameters:

- **`tags`** (`str | Iterable[str]`) – The tags to be added to the new node.

Returns:

- `Node` – A copy of the current Node object with the tags added.

Source code in `kedro/pipeline/node.py`

```
def tag(self, tags: str | Iterable[str]) -> Node:
    """Create a new ``Node`` which is an exact copy of the current one,
        but with more tags added to it.

    Args:
        tags: The tags to be added to the new node.

    Returns:
        A copy of the current ``Node`` object with the tags added.

    """
    return self._copy(tags=self.tags | set(_to_list(tags)))
```

### node

```
node(func, inputs, outputs, *, name=None, tags=None, confirms=None, namespace=None, preview_fn=None)
```

Create a node in the pipeline by providing a function to be called along with variable names for inputs and/or outputs.

Parameters:

- **`func`** (`Callable`) – A function that corresponds to the node logic. The function should have at least one input or output.
- **`inputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as inputs to the function. The number of names should match the number of arguments in the definition of the provided function. When dict[str, str] is provided, variable names will be mapped to function argument names.
- **`outputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as outputs to the function. The number of names should match the number of outputs returned by the provided function. When dict[str, str] is provided, variable names will be mapped to the named outputs the function returns.
- **`name`** (`str | None`, default: `None` ) – Optional node name to be used when displaying the node in logs or any other visualisations.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to the node.
- **`confirms`** (`str | list[str] | None`, default: `None` ) – Optional name or the list of the names of the datasets that should be confirmed. This will result in calling confirm() method of the corresponding dataset instance. Specified dataset names do not necessarily need to be present in the node inputs or outputs.
- **`namespace`** (`str | None`, default: `None` ) – Optional node namespace.
- **`preview_fn`** (`Callable[..., PreviewPayload] | None`, default: `None` ) – Optional preview function that returns one of the valid preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview). This is an experimental feature.

Returns:

- `Node` – A Node object with mapped inputs, outputs and function.

Example:

```
import pandas as pd
import numpy as np


def clean_data(cars: pd.DataFrame, boats: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return dict(cars_df=cars.dropna(), boats_df=boats.dropna())


def halve_dataframe(data: pd.DataFrame) -> List[pd.DataFrame]:
    return np.array_split(data, 2)


nodes = [
    node(
        clean_data,
        inputs=["cars2017", "boats2017"],
        outputs=dict(cars_df="clean_cars2017", boats_df="clean_boats2017"),
    ),
    node(halve_dataframe, "clean_cars2017", ["train_cars2017", "test_cars2017"]),
    node(
        halve_dataframe,
        dict(data="clean_boats2017"),
        ["train_boats2017", "test_boats2017"],
    ),
]
```

Source code in `kedro/pipeline/node.py`

````
def node(  # noqa: PLR0913
    func: Callable,
    inputs: str | list[str] | dict[str, str] | None,
    outputs: str | list[str] | dict[str, str] | None,
    *,
    name: str | None = None,
    tags: str | Iterable[str] | None = None,
    confirms: str | list[str] | None = None,
    namespace: str | None = None,
    preview_fn: Callable[..., PreviewPayload] | None = None,
) -> Node:
    """Create a node in the pipeline by providing a function to be called
    along with variable names for inputs and/or outputs.

    Args:
        func: A function that corresponds to the node logic. The function
            should have at least one input or output.
        inputs: The name or the list of the names of variables used as inputs
            to the function. The number of names should match the number of
            arguments in the definition of the provided function. When
            dict[str, str] is provided, variable names will be mapped to
            function argument names.
        outputs: The name or the list of the names of variables used as outputs
            to the function. The number of names should match the number of
            outputs returned by the provided function. When dict[str, str]
            is provided, variable names will be mapped to the named outputs the
            function returns.
        name: Optional node name to be used when displaying the node in logs or
            any other visualisations.
        tags: Optional set of tags to be applied to the node.
        confirms: Optional name or the list of the names of the datasets
            that should be confirmed. This will result in calling ``confirm()``
            method of the corresponding dataset instance. Specified dataset
            names do not necessarily need to be present in the node ``inputs``
            or ``outputs``.
        namespace: Optional node namespace.
        preview_fn: Optional preview function that returns one of the valid
            preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview).
            This is an experimental feature.

    Returns:
        A Node object with mapped inputs, outputs and function.

    Example:
    ``` python
    import pandas as pd
    import numpy as np


    def clean_data(cars: pd.DataFrame, boats: pd.DataFrame) -> dict[str, pd.DataFrame]:
        return dict(cars_df=cars.dropna(), boats_df=boats.dropna())


    def halve_dataframe(data: pd.DataFrame) -> List[pd.DataFrame]:
        return np.array_split(data, 2)


    nodes = [
        node(
            clean_data,
            inputs=["cars2017", "boats2017"],
            outputs=dict(cars_df="clean_cars2017", boats_df="clean_boats2017"),
        ),
        node(halve_dataframe, "clean_cars2017", ["train_cars2017", "test_cars2017"]),
        node(
            halve_dataframe,
            dict(data="clean_boats2017"),
            ["train_boats2017", "test_boats2017"],
        ),
    ]
    ```
    """
    return Node(
        func,
        inputs,
        outputs,
        name=name,
        tags=tags,
        confirms=confirms,
        namespace=namespace,
        preview_fn=preview_fn,
    )
````
