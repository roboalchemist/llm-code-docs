# Source: https://docs.kedro.org/en/stable/api/pipeline/kedro.pipeline.Pipeline/index.md

## kedro.pipeline.pipeline

A `Pipeline` is a collection of `Node` objects which can be executed as a Directed Acyclic Graph, sequentially or in parallel. The `Pipeline` class offers quick access to input dependencies, produced outputs and execution order.

### CircularDependencyError

Bases: `Exception`

Raised when it is not possible to provide a topological execution order for nodes, due to a circular dependency existing in the node definition.

### ConfirmNotUniqueError

Bases: `Exception`

Raised when two or more nodes that are part of the same pipeline attempt to confirm the same dataset.

### OutputNotUniqueError

Bases: `Exception`

Raised when two or more nodes that are part of the same pipeline produce outputs with the same name.

### Pipeline

```
Pipeline(nodes, *, inputs=None, outputs=None, parameters=None, tags=None, namespace=None, prefix_datasets_with_namespace=True)
```

A `Pipeline` defined as a collection of `Node` objects. This class treats nodes as part of a graph representation and provides inputs, outputs and execution order.

Parameters:

- **`nodes`** (`Iterable[Node | Pipeline] | Pipeline`) – The iterable of nodes the Pipeline will be made of. If you provide pipelines among the list of nodes, those pipelines will be expanded and all their nodes will become part of this new pipeline.
- **`inputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of input names to be exposed as connection points to other pipelines upstream. This is optional; if not provided, the pipeline inputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed input names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current input names will be mapped to new names. Must only refer to the pipeline's free inputs.
- **`outputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of names to be exposed as connection points to other pipelines downstream. This is optional; if not provided, the pipeline outputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed output names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current output names will be mapped to new names. Can refer to both the pipeline's free outputs, as well as intermediate results that need to be exposed.
- **`parameters`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of parameters to namespace. When str or set[str] are provided, the listed parameter names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current parameter names will be mapped to new names. The parameters can be specified without the params: prefix.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to all the pipeline nodes.
- **`namespace`** (`str | None`, default: `None` ) – A prefix to give to all dataset names, except those explicitly named with the inputs/outputs arguments, and parameter references (params: and parameters).
- **`prefix_datasets_with_namespace`** (`bool`, default: `True` ) – A flag to specify if the inputs, outputs, and parameters of the nodes should be prefixed with the namespace. It is set to True by default. It is useful to turn off when namespacing is used for grouping nodes for deployment purposes.

Raises:

- `ValueError` – When an empty list of nodes is provided, or when not all nodes have unique names.
- `CircularDependencyError` – When visiting all the nodes is not possible due to the existence of a circular dependency.
- `OutputNotUniqueError` – When multiple Node instances produce the same output.
- `ConfirmNotUniqueError` – When multiple Node instances attempt to confirm the same dataset.
- `PipelineError` – When inputs, outputs or parameters are incorrectly specified, or they do not exist on the original pipeline.

Example:

```
from kedro.pipeline import Pipeline
from kedro.pipeline import node

# In the following scenario first_ds and second_ds
# are datasets provided by io. Pipeline will pass these
# datasets to first_node function and provides the result
# to the second_node as input.


def first_node(first_ds, second_ds):
    return dict(third_ds=first_ds + second_ds)


def second_node(third_ds):
    return third_ds


pipeline = Pipeline(
    [
        node(first_node, ["first_ds", "second_ds"], ["third_ds"]),
        node(second_node, dict(third_ds="third_ds"), "fourth_ds"),
    ]
)

pipeline.describe()
```

Source code in `kedro/pipeline/pipeline.py`

````
def __init__(  # noqa: PLR0913
    self,
    nodes: Iterable[Node | Pipeline] | Pipeline,
    *,
    inputs: str | set[str] | dict[str, str] | None = None,
    outputs: str | set[str] | dict[str, str] | None = None,
    parameters: str | set[str] | dict[str, str] | None = None,
    tags: str | Iterable[str] | None = None,
    namespace: str | None = None,
    prefix_datasets_with_namespace: bool = True,
):
    """Initialise ``Pipeline`` with a list of ``Node`` instances.

    Args:
        nodes: The iterable of nodes the ``Pipeline`` will be made of. If you
            provide pipelines among the list of nodes, those pipelines will
            be expanded and all their nodes will become part of this
            new pipeline.
        inputs: A name or collection of input names to be exposed as connection points
            to other pipelines upstream. This is optional; if not provided, the
            pipeline inputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed input names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current input names will be
            mapped to new names.
            Must only refer to the pipeline's free inputs.
        outputs: A name or collection of names to be exposed as connection points
            to other pipelines downstream. This is optional; if not provided, the
            pipeline outputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed output names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current output names will be
            mapped to new names.
            Can refer to both the pipeline's free outputs, as well as
            intermediate results that need to be exposed.
        parameters: A name or collection of parameters to namespace.
            When str or set[str] are provided, the listed parameter names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current parameter names will be
            mapped to new names.
            The parameters can be specified without the `params:` prefix.
        tags: Optional set of tags to be applied to all the pipeline nodes.
        namespace: A prefix to give to all dataset names,
            except those explicitly named with the `inputs`/`outputs`
            arguments, and parameter references (`params:` and `parameters`).
        prefix_datasets_with_namespace: A flag to specify if the inputs, outputs, and parameters of the nodes
            should be prefixed with the namespace. It is set to True by default. It is
            useful to turn off when namespacing is used for grouping nodes for deployment purposes.

    Raises:
        ValueError:
            When an empty list of nodes is provided, or when not all
            nodes have unique names.
        CircularDependencyError:
            When visiting all the nodes is not
            possible due to the existence of a circular dependency.
        OutputNotUniqueError:
            When multiple ``Node`` instances produce the same output.
        ConfirmNotUniqueError:
            When multiple ``Node`` instances attempt to confirm the same
            dataset.
        PipelineError: When inputs, outputs or parameters are incorrectly
            specified, or they do not exist on the original pipeline.
    Example:
    ``` python
    from kedro.pipeline import Pipeline
    from kedro.pipeline import node

    # In the following scenario first_ds and second_ds
    # are datasets provided by io. Pipeline will pass these
    # datasets to first_node function and provides the result
    # to the second_node as input.


    def first_node(first_ds, second_ds):
        return dict(third_ds=first_ds + second_ds)


    def second_node(third_ds):
        return third_ds


    pipeline = Pipeline(
        [
            node(first_node, ["first_ds", "second_ds"], ["third_ds"]),
            node(second_node, dict(third_ds="third_ds"), "fourth_ds"),
        ]
    )

    pipeline.describe()
    ```
    """
    if isinstance(nodes, Pipeline):
        nodes = nodes.nodes

    if any([inputs, outputs, parameters, namespace]):
        nodes = self._map_nodes(
            nodes=nodes,
            inputs=inputs,
            outputs=outputs,
            parameters=parameters,
            tags=tags,
            namespace=namespace,
            prefix_datasets_with_namespace=prefix_datasets_with_namespace,
        )

    if nodes is None:
        raise ValueError(
            "'nodes' argument of 'Pipeline' is None. It must be an "
            "iterable of nodes and/or pipelines instead."
        )
    nodes_list = list(nodes)  # in case it's a generator
    _validate_duplicate_nodes(nodes_list)

    nodes_chain = list(
        chain.from_iterable(
            [[n] if isinstance(n, Node) else n.nodes for n in nodes_list]
        )
    )
    _validate_transcoded_inputs_outputs(nodes_chain)
    _tags = set(_to_list(tags))

    if _tags:
        tagged_nodes = [n.tag(_tags) for n in nodes_chain]
    else:
        tagged_nodes = nodes_chain

    self._nodes_by_name = {node.name: node for node in tagged_nodes}
    _validate_unique_outputs(tagged_nodes)
    _validate_unique_confirms(tagged_nodes)

    # input -> nodes with input
    self._nodes_by_input: dict[str, set[Node]] = defaultdict(set)
    for node in tagged_nodes:
        for input_ in node.inputs:
            self._nodes_by_input[_strip_transcoding(input_)].add(node)

    # output -> node with output
    self._nodes_by_output: dict[str, Node] = {}
    for node in tagged_nodes:
        for output in node.outputs:
            self._nodes_by_output[_strip_transcoding(output)] = node

    self._nodes = tagged_nodes
    self._toposorter = TopologicalSorter(self.node_dependencies)

    # test for circular dependencies without executing the toposort for efficiency
    try:
        self._toposorter.prepare()
    except CycleError as exc:
        loop = list(set(exc.args[1]))
        message = f"Circular dependencies exist among the following {len(loop)} item(s): {loop}"
        raise CircularDependencyError(message) from exc

    self._toposorted_nodes: list[Node] = []
    self._toposorted_groups: list[list[Node]] = []
    if any(n.namespace for n in self._nodes):
        self._validate_namespaces()
````

#### grouped_nodes

```
grouped_nodes
```

Return a list of the pipeline nodes in topologically ordered groups, i.e. if node A needs to be run before node B, it will appear in an earlier group.

Returns:

- `list[list[Node]]` – The pipeline nodes in topologically ordered groups.

#### node_dependencies

```
node_dependencies
```

All dependencies of nodes where the first Node has a direct dependency on the second Node.

Returns:

- `dict[Node, set[Node]]` – Dictionary where keys are nodes and values are sets made up of
- `dict[Node, set[Node]]` – their parent nodes. Independent nodes have this as empty sets.

#### nodes

```
nodes
```

Return a list of the pipeline nodes in topological order, i.e. if node A needs to be run before node B, it will appear earlier in the list.

Returns:

- `list[Node]` – The list of all pipeline nodes in topological order.

#### __repr__

```
__repr__()
```

Pipeline ([node1, ..., node10 ...], name='pipeline_name')

Source code in `kedro/pipeline/pipeline.py`

```
def __repr__(self) -> str:  # pragma: no cover
    """Pipeline ([node1, ..., node10 ...], name='pipeline_name')"""
    max_nodes_to_display = 10

    nodes_reprs = [repr(node) for node in self.nodes[:max_nodes_to_display]]
    if len(self.nodes) > max_nodes_to_display:
        nodes_reprs.append("...")
    sep = ",\n"
    nodes_reprs_str = f"[\n{sep.join(nodes_reprs)}\n]" if nodes_reprs else "[]"
    constructor_repr = f"({nodes_reprs_str})"
    return f"{self.__class__.__name__}{constructor_repr}"
```

#### all_inputs

```
all_inputs()
```

All inputs for all nodes in the pipeline.

Returns:

- `set[str]` – All node input names as a Set.

Source code in `kedro/pipeline/pipeline.py`

```
def all_inputs(self) -> set[str]:
    """All inputs for all nodes in the pipeline.

    Returns:
        All node input names as a Set.

    """
    return set.union(set(), *(node.inputs for node in self._nodes))
```

#### all_outputs

```
all_outputs()
```

All outputs of all nodes in the pipeline.

Returns:

- `set[str]` – All node outputs.

Source code in `kedro/pipeline/pipeline.py`

```
def all_outputs(self) -> set[str]:
    """All outputs of all nodes in the pipeline.

    Returns:
        All node outputs.

    """
    return set.union(set(), *(node.outputs for node in self._nodes))
```

#### datasets

```
datasets()
```

The names of all datasets used by the `Pipeline`, including inputs and outputs.

Returns:

- `set[str]` – The set of all pipeline datasets.

Source code in `kedro/pipeline/pipeline.py`

```
def datasets(self) -> set[str]:
    """The names of all datasets used by the ``Pipeline``,
    including inputs and outputs.

    Returns:
        The set of all pipeline datasets.

    """
    return self.all_outputs() | self.all_inputs()
```

#### describe

```
describe(names_only=True)
```

Obtain the order of execution and expected free input variables in a loggable pre-formatted string. The order of nodes matches the order of execution given by the topological sort.

Parameters:

- **`names_only`** (`bool`, default: `True` ) – The flag to describe names_only pipeline with just node names.

Example:

```
pipeline = Pipeline([...])

logger = logging.getLogger(__name__)

logger.info(pipeline.describe())
```

After invocation the following will be printed as an info level log statement: ::

```
#### Pipeline execution order ####
Inputs: C, D

func1([C]) -> [A]
func2([D]) -> [B]
func3([A, D]) -> [E]

Outputs: B, E
##################################
```

Returns:

- `str` – The pipeline description as a formatted string.

Source code in `kedro/pipeline/pipeline.py`

````
def describe(self, names_only: bool = True) -> str:
    """Obtain the order of execution and expected free input variables in
    a loggable pre-formatted string. The order of nodes matches the order
    of execution given by the topological sort.

    Args:
        names_only: The flag to describe names_only pipeline with just
            node names.

    Example:
    ``` python
    pipeline = Pipeline([...])

    logger = logging.getLogger(__name__)

    logger.info(pipeline.describe())
    ```

    After invocation the following will be printed as an info level log
    statement:
    ::

        #### Pipeline execution order ####
        Inputs: C, D

        func1([C]) -> [A]
        func2([D]) -> [B]
        func3([A, D]) -> [E]

        Outputs: B, E
        ##################################

    Returns:
        The pipeline description as a formatted string.

    """

    def set_to_string(set_of_strings: set[str]) -> str:
        """Convert set to a string but return 'None' in case of an empty
        set.
        """
        return ", ".join(sorted(set_of_strings)) if set_of_strings else "None"

    nodes_as_string = "\n".join(
        node.name if names_only else str(node) for node in self.nodes
    )

    str_representation = (
        "#### Pipeline execution order ####\n"
        "Inputs: {0}\n\n"
        "{1}\n\n"
        "Outputs: {2}\n"
        "##################################"
    )

    return str_representation.format(
        set_to_string(self.inputs()), nodes_as_string, set_to_string(self.outputs())
    )
````

#### filter

```
filter(tags=None, from_nodes=None, to_nodes=None, node_names=None, from_inputs=None, to_outputs=None, node_namespaces=None)
```

Creates a new `Pipeline` object with the nodes that meet all of the specified filtering conditions.

The new pipeline object is the intersection of pipelines that meet each filtering condition. This is distinct from chaining multiple filters together.

Parameters:

- **`tags`** (`Iterable[str] | None`, default: `None` ) – A list of node tags which should be used to lookup the nodes of the new Pipeline.
- **`from_nodes`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be used as a starting point of the new Pipeline.
- **`to_nodes`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be used as an end point of the new Pipeline.
- **`node_names`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be selected for the new Pipeline.
- **`from_inputs`** (`Iterable[str] | None`, default: `None` ) – A list of inputs which should be used as a starting point of the new Pipeline
- **`to_outputs`** (`Iterable[str] | None`, default: `None` ) – A list of outputs which should be the final outputs of the new Pipeline.
- **`node_namespaces`** (`Iterable[str] | None`, default: `None` ) – A list of node namespaces which should be used to select nodes in the new Pipeline.

Returns:

- `Pipeline` – A new Pipeline object with nodes that meet all of the specified filtering conditions.

Raises:

- `ValueError` – The filtered Pipeline has no nodes.

Example:

```
pipeline = Pipeline(
    [
        node(func, "A", "B", name="node1"),
        node(func, "B", "C", name="node2"),
        node(func, "C", "D", name="node3"),
    ]
)
pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
# Gives a new pipeline object containing node1 and node3.
```

Source code in `kedro/pipeline/pipeline.py`

````
def filter(  # noqa: PLR0913
    self,
    tags: Iterable[str] | None = None,
    from_nodes: Iterable[str] | None = None,
    to_nodes: Iterable[str] | None = None,
    node_names: Iterable[str] | None = None,
    from_inputs: Iterable[str] | None = None,
    to_outputs: Iterable[str] | None = None,
    node_namespaces: Iterable[str] | None = None,
) -> Pipeline:
    """Creates a new ``Pipeline`` object with the nodes that meet all of the
    specified filtering conditions.

    The new pipeline object is the intersection of pipelines that meet each
    filtering condition. This is distinct from chaining multiple filters together.

    Args:
        tags: A list of node tags which should be used to lookup
            the nodes of the new ``Pipeline``.
        from_nodes: A list of node names which should be used as a
            starting point of the new ``Pipeline``.
        to_nodes:  A list of node names which should be used as an
            end point of the new ``Pipeline``.
        node_names: A list of node names which should be selected for the
            new ``Pipeline``.
        from_inputs: A list of inputs which should be used as a starting point
            of the new ``Pipeline``
        to_outputs: A list of outputs which should be the final outputs of
            the new ``Pipeline``.
        node_namespaces: A list of node namespaces which should be used to select
            nodes in the new ``Pipeline``.

    Returns:
        A new ``Pipeline`` object with nodes that meet all of the specified
            filtering conditions.

    Raises:
        ValueError: The filtered ``Pipeline`` has no nodes.

    Example:
    ``` python
    pipeline = Pipeline(
        [
            node(func, "A", "B", name="node1"),
            node(func, "B", "C", name="node2"),
            node(func, "C", "D", name="node3"),
        ]
    )
    pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
    # Gives a new pipeline object containing node1 and node3.
    ```
    """

    filter_methods = {
        self.only_nodes_with_tags: tags,
        self.from_nodes: from_nodes,
        self.to_nodes: to_nodes,
        self.only_nodes: node_names,
        self.from_inputs: from_inputs,
        self.to_outputs: to_outputs,
        self.only_nodes_with_namespaces: [node_namespaces]
        if node_namespaces
        else None,
    }

    subset_pipelines = {
        filter_method(*filter_args)  # type: ignore
        for filter_method, filter_args in filter_methods.items()
        if filter_args
    }

    # Intersect all the pipelines subsets. We apply each filter to the original
    # pipeline object (self) rather than incrementally chaining filter methods
    # together. Hence, the order of filtering does not affect the outcome, and the
    # resultant pipeline is unambiguously defined.
    # If this were not the case then, for example,
    # pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
    # would give different outcomes depending on the order of filter methods:
    # only_nodes and then from_inputs would give node1, while only_nodes and then
    # from_inputs would give node1 and node3.
    filtered_pipeline = Pipeline(self._nodes)
    for subset_pipeline in subset_pipelines:
        filtered_pipeline &= subset_pipeline

    if not filtered_pipeline.nodes:
        raise ValueError(
            "Pipeline contains no nodes after applying all provided filters. "
            "Please ensure that at least one pipeline with nodes has been defined."
        )
    return filtered_pipeline
````

#### from_inputs

```
from_inputs(*inputs)
```

Create a new `Pipeline` object with the nodes which depend directly or transitively on the provided inputs. If provided a name, but no format, for a transcoded input, it includes all the nodes that use inputs with that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*inputs`** (`str`, default: `()` ) – A list of inputs which should be used as a starting point of the new Pipeline

Raises:

- `ValueError` – Raised when any of the given inputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the current one such that only nodes depending directly or transitively on the provided inputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def from_inputs(self, *inputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly or transitively on the provided inputs.
    If provided a name, but no format, for a transcoded input, it
    includes all the nodes that use inputs with that name, otherwise it
    matches to the fully-qualified name only (i.e. name@format).

    Args:
        *inputs: A list of inputs which should be used as a starting point
            of the new ``Pipeline``

    Raises:
        ValueError: Raised when any of the given inputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes depending
            directly or transitively on the provided inputs are being
            copied.

    """
    starting = set(inputs)
    result: set[Node] = set()
    next_nodes = self._get_nodes_with_inputs_transcode_compatible(starting)

    while next_nodes:
        result |= next_nodes
        outputs = set(chain.from_iterable(node.outputs for node in next_nodes))
        starting = outputs

        next_nodes = set(
            chain.from_iterable(
                self._nodes_by_input[_strip_transcoding(input_)]
                for input_ in starting
            )
        )

    return Pipeline(result)
```

#### from_nodes

```
from_nodes(*node_names)
```

Create a new `Pipeline` object with the nodes which depend directly or transitively on the provided nodes.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – A list of node_names which should be used as a starting point of the new Pipeline.

Raises: ValueError: Raised when any of the given names do not exist in the `Pipeline` object. Returns: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes depending directly or transitively on the provided nodes are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def from_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly or transitively on the provided nodes.

    Args:
        *node_names: A list of node_names which should be used as a
            starting point of the new ``Pipeline``.
    Raises:
        ValueError: Raised when any of the given names do not exist in the
            ``Pipeline`` object.
    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of
            the current one such that only nodes depending directly or
            transitively on the provided nodes are being copied.

    """

    res = self.only_nodes(*node_names)
    res += self.from_inputs(*map(_strip_transcoding, res.all_outputs()))
    return res
```

#### group_nodes_by

```
group_nodes_by(group_by='namespace')
```

Return a list of grouped nodes based on the specified strategy.

Parameters:

- **`group_by`** (`str | None`, default: `'namespace'` ) – Strategy for grouping. Supported values:
  - "namespace": Groups nodes by their top-level namespace.
  - None or "none": No grouping, each node is its own group.

Returns:

- `list[GroupedNodes]` – A list of GroupedNodes instances.

Source code in `kedro/pipeline/pipeline.py`

```
def group_nodes_by(
    self,
    group_by: str | None = "namespace",
) -> list[GroupedNodes]:
    """Return a list of grouped nodes based on the specified strategy.

    Args:
        group_by: Strategy for grouping. Supported values:
            - "namespace": Groups nodes by their top-level namespace.
            - None or "none": No grouping, each node is its own group.

    Returns:
        A list of GroupedNodes instances.
    """
    if group_by is None or group_by.lower() == "none":
        return self._group_by_none()
    if group_by.lower() == "namespace":
        return self._group_by_namespace()
    raise ValueError(f"Unsupported group_by strategy: {group_by}")
```

#### inputs

```
inputs()
```

The names of free inputs that must be provided at runtime so that the pipeline is runnable. Does not include intermediate inputs which are produced and consumed by the inner pipeline nodes. Resolves transcoded names where necessary.

Returns:

- `set[str]` – The set of free input names needed by the pipeline.

Source code in `kedro/pipeline/pipeline.py`

```
def inputs(self) -> set[str]:
    """The names of free inputs that must be provided at runtime so that
    the pipeline is runnable. Does not include intermediate inputs which
    are produced and consumed by the inner pipeline nodes. Resolves
    transcoded names where necessary.

    Returns:
        The set of free input names needed by the pipeline.

    """
    return self._remove_intermediates(self.all_inputs())
```

#### only_nodes

```
only_nodes(*node_names)
```

Create a new `Pipeline` which will contain only the specified nodes by name.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – One or more node names. The returned Pipeline will only contain these nodes.

Raises:

- `ValueError` – When some invalid node name is given.

Returns:

- `Pipeline` – A new Pipeline, containing only nodes.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` which will contain only the specified
    nodes by name.

    Args:
        *node_names: One or more node names. The returned ``Pipeline``
            will only contain these nodes.

    Raises:
        ValueError: When some invalid node name is given.

    Returns:
        A new ``Pipeline``, containing only ``nodes``.

    """
    unregistered_nodes = set(node_names) - set(self._nodes_by_name.keys())
    if unregistered_nodes:
        # check if unregistered nodes are available under namespace
        namespaces = []
        for unregistered_node in unregistered_nodes:
            namespaces.extend(
                [
                    node_name
                    for node_name in self._nodes_by_name.keys()
                    if node_name.endswith(f".{unregistered_node}")
                ]
            )
        if namespaces:
            raise ValueError(
                f"Pipeline does not contain nodes named {list(unregistered_nodes)}. "
                f"Did you mean: {namespaces}?"
            )
        raise ValueError(
            f"Pipeline does not contain nodes named {list(unregistered_nodes)}."
        )

    nodes = [self._nodes_by_name[name] for name in node_names]
    return Pipeline(nodes)
```

#### only_nodes_with_inputs

```
only_nodes_with_inputs(*inputs)
```

Create a new `Pipeline` object with the nodes which depend directly on the provided inputs. If provided a name, but no format, for a transcoded input, it includes all the nodes that use inputs with that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*inputs`** (`str`, default: `()` ) – A list of inputs which should be used as a starting point of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given inputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the current one such that only nodes depending directly on the provided inputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_inputs(self, *inputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly on the provided inputs.
    If provided a name, but no format, for a transcoded input, it
    includes all the nodes that use inputs with that name, otherwise it
    matches to the fully-qualified name only (i.e. name@format).

    Args:
        *inputs: A list of inputs which should be used as a starting
            point of the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given inputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes depending
            directly on the provided inputs are being copied.

    """
    starting = set(inputs)
    nodes = self._get_nodes_with_inputs_transcode_compatible(starting)

    return Pipeline(nodes)
```

#### only_nodes_with_namespaces

```
only_nodes_with_namespaces(node_namespaces)
```

Creates a new `Pipeline` containing only nodes with the specified namespaces.

Parameters:

- **`node_namespaces`** (`list[str]`) – A list of node namespaces.

Raises:

- `ValueError` – When pipeline contains no nodes with the specified namespaces.

Returns:

- `Pipeline` – A new Pipeline containing nodes with the specified namespaces.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_namespaces(self, node_namespaces: list[str]) -> Pipeline:
    """Creates a new ``Pipeline`` containing only nodes with the specified
    namespaces.

    Args:
        node_namespaces: A list of node namespaces.

    Raises:
        ValueError: When pipeline contains no nodes with the specified namespaces.

    Returns:
        A new ``Pipeline`` containing nodes with the specified namespaces.
    """
    nodes = []
    unmatched_namespaces = []  # Track namespaces that don't match any nodes

    for node_namespace in node_namespaces:
        matching_nodes = []
        for n in self._nodes:
            if n.namespace and (
                n.namespace == node_namespace
                or n.namespace.startswith(f"{node_namespace}.")
            ):
                matching_nodes.append(n)

        if not matching_nodes:
            unmatched_namespaces.append(node_namespace)
        nodes.extend(matching_nodes)

    if unmatched_namespaces:
        raise ValueError(
            f"Pipeline does not contain nodes with the following namespaces: {unmatched_namespaces}"
        )

    return Pipeline(nodes)
```

#### only_nodes_with_outputs

```
only_nodes_with_outputs(*outputs)
```

Create a new `Pipeline` object with the nodes which are directly required to produce the provided outputs. If provided a name, but no format, for a transcoded dataset, it includes all the nodes that output to that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*outputs`** (`str`, default: `()` ) – A list of outputs which should be the final outputs of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given outputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the
- `Pipeline` – current one such that only nodes which are directly required to
- `Pipeline` – produce the provided outputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_outputs(self, *outputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which are directly
    required to produce the provided outputs.
    If provided a name, but no format, for a transcoded dataset, it
    includes all the nodes that output to that name, otherwise it matches
    to the fully-qualified name only (i.e. name@format).

    Args:
        *outputs: A list of outputs which should be the final outputs
            of the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given outputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
        current one such that only nodes which are directly required to
        produce the provided outputs are being copied.
    """
    starting = set(outputs)
    nodes = self._get_nodes_with_outputs_transcode_compatible(starting)

    return Pipeline(nodes)
```

#### only_nodes_with_tags

```
only_nodes_with_tags(*tags)
```

Creates a new `Pipeline` object with the nodes which contain *any* of the provided tags. The resulting `Pipeline` is empty if no tags are provided.

Parameters:

- **`*tags`** (`str`, default: `()` ) – A list of node tags which should be used to lookup the nodes of the new Pipeline.

Returns: Pipeline: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes containing *any* of the tags provided are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_tags(self, *tags: str) -> Pipeline:
    """Creates a new ``Pipeline`` object with the nodes which contain *any*
    of the provided tags. The resulting ``Pipeline`` is empty if no tags
    are provided.

    Args:
        *tags: A list of node tags which should be used to lookup
            the nodes of the new ``Pipeline``.
    Returns:
        Pipeline: A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes containing *any*
            of the tags provided are being copied.
    """
    unique_tags = set(tags)
    nodes = [node for node in self._nodes if unique_tags & node.tags]
    return Pipeline(nodes)
```

#### outputs

```
outputs()
```

The names of outputs produced when the whole pipeline is run. Does not include intermediate outputs that are consumed by other pipeline nodes. Resolves transcoded names where necessary.

Returns:

- `set[str]` – The set of final pipeline outputs.

Source code in `kedro/pipeline/pipeline.py`

```
def outputs(self) -> set[str]:
    """The names of outputs produced when the whole pipeline is run.
    Does not include intermediate outputs that are consumed by
    other pipeline nodes. Resolves transcoded names where necessary.

    Returns:
        The set of final pipeline outputs.

    """
    return self._remove_intermediates(self.all_outputs())
```

#### tag

```
tag(tags)
```

Tags all the nodes in the pipeline.

Parameters:

- **`tags`** (`str | Iterable[str]`) – The tags to be added to the nodes.

Returns:

- `Pipeline` – New Pipeline object with nodes tagged.

Source code in `kedro/pipeline/pipeline.py`

```
def tag(self, tags: str | Iterable[str]) -> Pipeline:
    """Tags all the nodes in the pipeline.

    Args:
        tags: The tags to be added to the nodes.

    Returns:
        New ``Pipeline`` object with nodes tagged.
    """
    nodes = [n.tag(tags) for n in self._nodes]
    return Pipeline(nodes)
```

#### to_json

```
to_json()
```

Return a json representation of the pipeline.

Source code in `kedro/pipeline/pipeline.py`

```
def to_json(self) -> str:
    """Return a json representation of the pipeline."""
    transformed = [
        {
            "name": n.name,
            "inputs": list(n.inputs),
            "outputs": list(n.outputs),
            "tags": list(n.tags),
        }
        for n in self._nodes
    ]
    pipeline_versioned = {
        "kedro_version": kedro.__version__,
        "pipeline": transformed,
    }

    return json.dumps(pipeline_versioned)
```

#### to_nodes

```
to_nodes(*node_names)
```

Create a new `Pipeline` object with the nodes required directly or transitively by the provided nodes.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – A list of node_names which should be used as an end point of the new Pipeline.

Raises: ValueError: Raised when any of the given names do not exist in the `Pipeline` object. Returns: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes required directly or transitively by the provided nodes are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def to_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes required directly
    or transitively by the provided nodes.

    Args:
        *node_names: A list of node_names which should be used as an
            end point of the new ``Pipeline``.
    Raises:
        ValueError: Raised when any of the given names do not exist in the
            ``Pipeline`` object.
    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
            current one such that only nodes required directly or
            transitively by the provided nodes are being copied.

    """

    res = self.only_nodes(*node_names)
    res += self.to_outputs(*map(_strip_transcoding, res.all_inputs()))
    return res
```

#### to_outputs

```
to_outputs(*outputs)
```

Create a new `Pipeline` object with the nodes which are directly or transitively required to produce the provided outputs. If provided a name, but no format, for a transcoded dataset, it includes all the nodes that output to that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*outputs`** (`str`, default: `()` ) – A list of outputs which should be the final outputs of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given outputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the
- `Pipeline` – current one such that only nodes which are directly or transitively
- `Pipeline` – required to produce the provided outputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def to_outputs(self, *outputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which are directly
    or transitively required to produce the provided outputs.
    If provided a name, but no format, for a transcoded dataset, it
    includes all the nodes that output to that name, otherwise it matches
    to the fully-qualified name only (i.e. name@format).

    Args:
        *outputs: A list of outputs which should be the final outputs of
            the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given outputs do not exist in the
            ``Pipeline`` object.


    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
        current one such that only nodes which are directly or transitively
        required to produce the provided outputs are being copied.

    """
    starting = set(outputs)
    result: set[Node] = set()
    next_nodes = self._get_nodes_with_outputs_transcode_compatible(starting)

    while next_nodes:
        result |= next_nodes
        inputs = set(chain.from_iterable(node.inputs for node in next_nodes))
        starting = inputs

        next_nodes = {
            self._nodes_by_output[_strip_transcoding(output)]
            for output in starting
            if _strip_transcoding(output) in self._nodes_by_output
        }

    return Pipeline(result)
```

### PipelineError

Bases: `Exception`

Raised when a pipeline is not adapted and integrated appropriately using the helper.

### pipeline

```
pipeline(nodes, *, inputs=None, outputs=None, parameters=None, tags=None, namespace=None, prefix_datasets_with_namespace=True)
```

Create a `Pipeline` from a collection of nodes and/or `Pipeline`\\s.

Parameters:

- **`nodes`** (`Iterable[Node | Pipeline] | Pipeline`) – The nodes the Pipeline will be made of. If you provide pipelines among the list of nodes, those pipelines will be expanded and all their nodes will become part of this new pipeline.
- **`inputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of input names to be exposed as connection points to other pipelines upstream. This is optional; if not provided, the pipeline inputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed input names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current input names will be mapped to new names. Must only refer to the pipeline's free inputs.
- **`outputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of names to be exposed as connection points to other pipelines downstream. This is optional; if not provided, the pipeline outputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed output names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current output names will be mapped to new names. Can refer to both the pipeline's free outputs, as well as intermediate results that need to be exposed.
- **`parameters`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of parameters to namespace. When str or set[str] are provided, the listed parameter names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current parameter names will be mapped to new names. The parameters can be specified without the params: prefix.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to all the pipeline nodes.
- **`namespace`** (`str | None`, default: `None` ) – A prefix to give to all dataset names, except those explicitly named with the inputs/outputs arguments, and parameter references (params: and parameters).
- **`prefix_datasets_with_namespace`** (`bool`, default: `True` ) – A flag to specify if the inputs and outputs of the nodes should be prefixed with the namespace. It is set to True by default. It is useful to turn off when namespacing is used for grouping nodes for deployment purposes.

Raises:

- `PipelineError` – When inputs, outputs or parameters are incorrectly specified, or they do not exist on the original pipeline.
- `ValueError` – When underlying pipeline nodes inputs/outputs are not any of the expected types (str, dict, list, or None).

Returns:

- `Pipeline` – A new Pipeline object.

Source code in `kedro/pipeline/pipeline.py`

```
def pipeline(  # noqa: PLR0913
    nodes: Iterable[Node | Pipeline] | Pipeline,
    *,
    inputs: str | set[str] | dict[str, str] | None = None,
    outputs: str | set[str] | dict[str, str] | None = None,
    parameters: str | set[str] | dict[str, str] | None = None,
    tags: str | Iterable[str] | None = None,
    namespace: str | None = None,
    prefix_datasets_with_namespace: bool = True,
) -> Pipeline:
    r"""Create a ``Pipeline`` from a collection of nodes and/or ``Pipeline``\s.

    Args:
        nodes: The nodes the ``Pipeline`` will be made of. If you
            provide pipelines among the list of nodes, those pipelines will
            be expanded and all their nodes will become part of this
            new pipeline.
        inputs: A name or collection of input names to be exposed as connection points
            to other pipelines upstream. This is optional; if not provided, the
            pipeline inputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed input names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current input names will be
            mapped to new names.
            Must only refer to the pipeline's free inputs.
        outputs: A name or collection of names to be exposed as connection points
            to other pipelines downstream. This is optional; if not provided, the
            pipeline outputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed output names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current output names will be
            mapped to new names.
            Can refer to both the pipeline's free outputs, as well as
            intermediate results that need to be exposed.
        parameters: A name or collection of parameters to namespace.
            When str or set[str] are provided, the listed parameter names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current parameter names will be
            mapped to new names.
            The parameters can be specified without the `params:` prefix.
        tags: Optional set of tags to be applied to all the pipeline nodes.
        namespace: A prefix to give to all dataset names,
            except those explicitly named with the `inputs`/`outputs`
            arguments, and parameter references (`params:` and `parameters`).
        prefix_datasets_with_namespace: A flag to specify if the inputs and outputs of the nodes
                should be prefixed with the namespace. It is set to True by default. It is
                useful to turn off when namespacing is used for grouping nodes for deployment purposes.

    Raises:
        PipelineError: When inputs, outputs or parameters are incorrectly
            specified, or they do not exist on the original pipeline.
        ValueError: When underlying pipeline nodes inputs/outputs are not
            any of the expected types (str, dict, list, or None).

    Returns:
        A new ``Pipeline`` object.
    """

    return Pipeline(
        nodes=nodes,
        inputs=inputs,
        outputs=outputs,
        parameters=parameters,
        tags=tags,
        namespace=namespace,
        prefix_datasets_with_namespace=prefix_datasets_with_namespace,
    )
```
