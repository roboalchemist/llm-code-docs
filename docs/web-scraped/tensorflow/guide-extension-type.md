# Source: https://www.tensorflow.org/guide/extension_type

Title: Extension types

URL Source: https://www.tensorflow.org/guide/extension_type

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/extension_type#main-content)

*   [Install](https://www.tensorflow.org/install)
*   [Learn](https://www.tensorflow.org/learn)
    *   [Tutorials](https://www.tensorflow.org/tutorials)
    *   [Guide](https://www.tensorflow.org/guide)
    *   [Migrate to TF2](https://www.tensorflow.org/guide/migrate)
    *   [TF 1 ↗](https://github.com/tensorflow/docs/tree/master/site/en/r1)

*   [API](https://www.tensorflow.org/api)
*   [Ecosystem](https://www.tensorflow.org/resources/models-datasets)
*   [Community](https://www.tensorflow.org/community)
*   [Why TensorFlow](https://www.tensorflow.org/about)
*   [GitHub](https://github.com/tensorflow)

*   [TensorFlow guide](https://www.tensorflow.org/guide)
*   TensorFlow basics

*   [Overview](https://www.tensorflow.org/guide/basics)
*   [Tensors](https://www.tensorflow.org/guide/tensor)
*   [Variables](https://www.tensorflow.org/guide/variable)
*   [Automatic differentiation](https://www.tensorflow.org/guide/autodiff)
*   [Graphs and functions](https://www.tensorflow.org/guide/intro_to_graphs)
*   [Modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)
*   [Training loops](https://www.tensorflow.org/guide/basic_training_loops)
*   Keras

*   [Overview](https://www.tensorflow.org/guide/keras)
*   [The Sequential model](https://www.tensorflow.org/guide/keras/sequential_model)
*   [The Functional API](https://www.tensorflow.org/guide/keras/functional_api)
*   [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods)
*   [Making new layers and models via subclassing](https://www.tensorflow.org/guide/keras/making_new_layers_and_models_via_subclassing)
*   [Serialization and saving](https://www.tensorflow.org/guide/keras/serialization_and_saving)
*   [Customizing Saving](https://www.tensorflow.org/guide/keras/customizing_saving_and_serialization)
*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers)
*   [Customizing what happens in fit()](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit)
*   [Writing a training loop from scratch](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns)
*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding)
*   [Writing your own callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks)
*   [Transfer learning & fine-tuning](https://www.tensorflow.org/guide/keras/transfer_learning)
*   [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training)
*   Build with Core

*   [Overview](https://www.tensorflow.org/guide/core)
*   [Quickstart for Core](https://www.tensorflow.org/guide/core/quickstart_core)
*   [Logistic regression](https://www.tensorflow.org/guide/core/logistic_regression_core)
*   [Multilayer perceptrons](https://www.tensorflow.org/guide/core/mlp_core)
*   [Matrix approximation](https://www.tensorflow.org/guide/core/matrix_core)
*   [Custom optimizers](https://www.tensorflow.org/guide/core/optimizers_core)
*   [DTensor with Core APIs](https://www.tensorflow.org/guide/core/distribution)
*   Tensor Flow in depth

*   [Tensor slicing](https://www.tensorflow.org/guide/tensor_slicing)
*   [Advanced autodiff](https://www.tensorflow.org/guide/advanced_autodiff)
*   [Ragged tensor](https://www.tensorflow.org/guide/ragged_tensor)
*   [Sparse tensor](https://www.tensorflow.org/guide/sparse_tensor)
*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)
*   [Num Py API](https://www.tensorflow.org/guide/tf_numpy)
*   [Num Py API Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)
*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)
*   [Thinking in Tensor Flow 2](https://www.tensorflow.org/guide/effective_tf2)
*   Customization

*   [Create an op](https://www.tensorflow.org/guide/create_op)
*   [Extension types](https://www.tensorflow.org/guide/extension_type)
*   Data input pipelines

*   [tf.data](https://www.tensorflow.org/guide/data)
*   [Optimize pipeline performance](https://www.tensorflow.org/guide/data_performance)
*   [Analyze pipeline performance](https://www.tensorflow.org/guide/data_performance_analysis)
*   Import and export

*   [Checkpoint](https://www.tensorflow.org/guide/checkpoint)
*   [Saved Model](https://www.tensorflow.org/guide/saved_model)
*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)
*   Accelerators

*   [Distributed training](https://www.tensorflow.org/guide/distributed_training)
*   [GPU](https://www.tensorflow.org/guide/gpu)
*   [TPU](https://www.tensorflow.org/guide/tpu)
*   Performance

*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)
*   [Profile Tensor Flow performance](https://www.tensorflow.org/guide/profiler)
*   [Optimize GPU Performance](https://www.tensorflow.org/guide/gpu_performance_analysis)
*   [Graph optimization](https://www.tensorflow.org/guide/graph_optimization)
*   [Mixed precision](https://www.tensorflow.org/guide/mixed_precision)
*   Model Garden

*   [Overview](https://www.tensorflow.org/tfmodels)
*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit)
*   [TFModels - NLP](https://www.tensorflow.org/tfmodels/nlp)
*   [Example: Image classification](https://www.tensorflow.org/tfmodels/vision/image_classification)
*   [Example: Object Detection](https://www.tensorflow.org/tfmodels/vision/object_detection)
*   [Example: Semantic Segmentation](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation)
*   [Example: Instance Segmentation](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)
*   Estimators

*   [Estimator overview](https://www.tensorflow.org/guide/estimator)
*   Appendix

*   [Version compatibility](https://www.tensorflow.org/guide/versions)

Extension types Stay organized with collections  Save and categorize content based on your preferences.
-------------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/extension_type#setup)
*   [Extension types](https://www.tensorflow.org/guide/extension_type#extension_types_2)
*   [Supported APIs](https://www.tensorflow.org/guide/extension_type#supported_apis)
*   [Requirements](https://www.tensorflow.org/guide/extension_type#requirements)
    *   [Field types](https://www.tensorflow.org/guide/extension_type#field_types)
    *   [Mutability](https://www.tensorflow.org/guide/extension_type#mutability)

*   [Functionality added by ExtensionType](https://www.tensorflow.org/guide/extension_type#functionality_added_by_extensiontype)
    *   [Constructor](https://www.tensorflow.org/guide/extension_type#constructor)
    *   [Printable representation](https://www.tensorflow.org/guide/extension_type#printable_representation)
    *   [Equality operators](https://www.tensorflow.org/guide/extension_type#equality_operators)
    *   [Validation method](https://www.tensorflow.org/guide/extension_type#validation_method)
    *   [Enforced immutability](https://www.tensorflow.org/guide/extension_type#enforced_immutability)
    *   [Nested TypeSpec](https://www.tensorflow.org/guide/extension_type#nested_typespec)

*   [Customizing ExtensionTypes](https://www.tensorflow.org/guide/extension_type#customizing_extensiontypes)
    *   [Overriding the default printable representation](https://www.tensorflow.org/guide/extension_type#overriding_the_default_printable_representation)
    *   [Defining methods](https://www.tensorflow.org/guide/extension_type#defining_methods)
    *   [Defining classmethods and staticmethods](https://www.tensorflow.org/guide/extension_type#defining_classmethods_and_staticmethods)
    *   [Defining properties](https://www.tensorflow.org/guide/extension_type#defining_properties)
    *   [Overriding the default constructor](https://www.tensorflow.org/guide/extension_type#overriding_the_default_constructor)
    *   [Overriding the default equality operator (__eq__)](https://www.tensorflow.org/guide/extension_type#overriding_the_default_equality_operator_eq_)
    *   [Using forward references](https://www.tensorflow.org/guide/extension_type#using_forward_references)
    *   [Defining subclasses](https://www.tensorflow.org/guide/extension_type#defining_subclasses)
    *   [Defining private fields](https://www.tensorflow.org/guide/extension_type#defining_private_fields)
    *   [Customizing the ExtensionType's TypeSpec](https://www.tensorflow.org/guide/extension_type#customizing_the_extensiontypes_typespec)

*   [Tensor API dispatch](https://www.tensorflow.org/guide/extension_type#tensor_api_dispatch)
    *   [Dispatch for a single API](https://www.tensorflow.org/guide/extension_type#dispatch_for_a_single_api)
    *   [Dispatch for all unary elementwise APIs](https://www.tensorflow.org/guide/extension_type#dispatch_for_all_unary_elementwise_apis)
    *   [Dispatch for binary all elementwise APIs](https://www.tensorflow.org/guide/extension_type#dispatch_for_binary_all_elementwise_apis)

*   [Batchable ExtensionTypes](https://www.tensorflow.org/guide/extension_type#batchable_extensiontypes)
    *   [BatchableExtensionType example: Network](https://www.tensorflow.org/guide/extension_type#batchableextensiontype_example_network)

*   [TensorFlow APIs that support ExtensionTypes](https://www.tensorflow.org/guide/extension_type#tensorflow_apis_that_support_extensiontypes)
    *   [@tf.function](https://www.tensorflow.org/guide/extension_type#tffunction)
    *   [Control flow operations](https://www.tensorflow.org/guide/extension_type#control_flow_operations)
    *   [Autograph control flow](https://www.tensorflow.org/guide/extension_type#autograph_control_flow)
    *   [Keras](https://www.tensorflow.org/guide/extension_type#keras)
    *   [SavedModel](https://www.tensorflow.org/guide/extension_type#savedmodel)
    *   [Datasets](https://www.tensorflow.org/guide/extension_type#datasets)

Setup
-----

```
!pip install -q tf_nightly
import tensorflow as tf
import numpy as np
from typing import Tuple, List, Mapping, Union, Optional
import tempfile
```

User-defined types can make projects more readable, modular, maintainable. However, most TensorFlow APIs have very limited support for user-defined Python types. This includes both high-level APIs (such as [Keras](https://www.tensorflow.org/guide/keras/overview), [tf.function](https://www.tensorflow.org/guide/function), [`tf.SavedModel`](https://www.tensorflow.org/guide/saved_model)) and lower-level APIs (such as [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop) and [`tf.concat`](https://www.tensorflow.org/api_docs/python/tf/concat)). TensorFlow **extension types** can be used to create user-defined object-oriented types that work seamlessly with TensorFlow's APIs. To create an extension type, simply define a Python class with [`tf.experimental.ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType) as its base, and use [type annotations](https://www.python.org/dev/peps/pep-0484/) to specify the type for each field.

```
class TensorGraph(tf.experimental.ExtensionType):
  """A collection of labeled nodes connected by weighted edges."""
  edge_weights: tf.Tensor               # shape=[num_nodes, num_nodes]
  node_labels: Mapping[str, tf.Tensor]  # shape=[num_nodes]; dtype=any

class MaskedTensor(tf.experimental.ExtensionType):
  """A tensor paired with a boolean mask, indicating which values are valid."""
  values: tf.Tensor
  mask: tf.Tensor       # shape=values.shape; false for missing/invalid values.

class CSRSparseMatrix(tf.experimental.ExtensionType):
  """Compressed sparse row matrix (https://en.wikipedia.org/wiki/Sparse_matrix)."""
  values: tf.Tensor     # shape=[num_nonzero]; dtype=any
  col_index: tf.Tensor  # shape=[num_nonzero]; dtype=int64
  row_index: tf.Tensor  # shape=[num_rows+1]; dtype=int64
```

The [`tf.experimental.ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType) base class works similarly to [`typing.NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple) and [`@dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass) from the standard Python library. In particular, it automatically adds a constructor and special methods (such as `__repr__` and `__eq__`) based on the field type annotations.

Typically, extension types tend to fall into one of two categories:

*   **_Data structures_**, which group together a collection of related values, and can provide useful operations based on those values. Data structures may be fairly general (such as the `TensorGraph` example above); or they may be highly customized to a specific model.

*   **_Tensor-like types_**, which specialize or extend the concept of "Tensor." Types in this category have a `rank`, a `shape`, and usually a `dtype`; and it makes sense to use them with Tensor operations (such as [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack), [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add), or [`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)). `MaskedTensor` and `CSRSparseMatrix` are examples of tensor-like types.

Supported APIs
--------------

Extension types are supported by the following TensorFlow APIs:

*   **Keras**: Extension types can be used as inputs and outputs for Keras `Models` and `Layers`.
*   **[`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)**: Extension types can be included in `Datasets`, and returned by dataset `Iterators`.
*   **TensorFlow Hub**: Extension types can be used as inputs and outputs for `tf.hub` modules.
*   **SavedModel**: Extension types can be used as inputs and outputs for `SavedModel` functions.
*   **[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)**: Extension types can be used as arguments and return values for functions wrapped with the [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) decorator.
*   **While loops**: Extension types can be used as loop variables in [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop), and can be used as arguments and return values for the while-loop's body.
*   **Conditionals**: Extension types can be conditionally selected using [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond) and [`tf.case`](https://www.tensorflow.org/api_docs/python/tf/case).
*   **[`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)**: Extension types can be used as arguments and return values for the `func` argument to [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function).
*   **Tensor ops**: Extension types can be extended to support most TensorFlow ops that accept Tensor inputs (such as [`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul), [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather), and [`tf.reduce_sum`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)). Go to the "_Dispatch_" section below for more information.
*   **Distribution strategy**: Extension types can be used as per-replica values.

For more details, see the section on "TensorFlow APIs that support ExtensionTypes" below.

Requirements
------------

### Field types

All fields—instance variables—must be declared, and a type annotation must be provided for each field. The following type annotations are supported:

| Type | Example |
| --- | --- |
| Python integers | `i: int` |
| Python floats | `f: float` |
| Python strings | `s: str` |
| Python booleans | `b: bool` |
| Python `None` | `n: None` |
| [Tensor shapes](https://www.tensorflow.org/api_docs/python/tf/TensorShape) | `shape: tf.TensorShape` |
| [Tensor `dtype`s](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType) | `dtype: tf.DType` |
| [Tensors](https://www.tensorflow.org/api_docs/python/tf/Tensor) | `t: tf.Tensor` |
| [Extension types](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType) | `mt: MyMaskedTensor` |
| [Ragged tensors](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor) | `rt: tf.RaggedTensor` |
| [Sparse tensors](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) | `st: tf.SparseTensor` |
| [Indexed slices](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices) | `s: tf.IndexedSlices` |
| [Optional tensors](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional) | `o: tf.experimental.Optional` |
| [Type unions](https://docs.python.org/3/library/typing.html#typing.Union) | `int_or_float: typing.Union[int, float]` |
| [Tuples](https://docs.python.org/3/library/typing.html#typing.Tuple) | `params: typing.Tuple[int, float, tf.Tensor, int]` |
| [Var-length tuples](https://docs.python.org/3/library/typing.html#typing.Tuple) | `lengths: typing.Tuple[int, ...]` |
| [Mappings](https://docs.python.org/3/library/typing.html#typing.Mapping) | `tags: typing.Mapping[str, tf.Tensor]` |
| [Optional values](https://docs.python.org/3/library/typing.html#typing.Optional) | `weight: typing.Optional[tf.Tensor]` |

### Mutability

Extension types are required to be immutable. This ensures that they can be properly tracked by TensorFlow's graph-tracing mechanisms. If you find yourself wanting to mutate an extension type value, consider instead defining methods that transform values. For example, rather than defining a `set_mask` method to mutate a `MaskedTensor`, you could define a `replace_mask` method that returns a new `MaskedTensor`:

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  def replace_mask(self, new_mask):
      self.values.shape.assert_is_compatible_with(new_mask.shape)
      return MaskedTensor(self.values, new_mask)
```

Functionality added by `ExtensionType`
--------------------------------------

The `ExtensionType` base class provides the following functionality:

*   A constructor (`__init__`).
*   A printable representation method (`__repr__`).
*   Equality and inequality operators (`__eq__`).
*   A validation method (`__validate__`).
*   Enforced immutability.
*   A nested `TypeSpec`.
*   Tensor API dispatch support.

Go to the "Customizing `ExtensionType`s" section below for more information on customizing this functionality.

### Constructor

The constructor added by `ExtensionType` takes each field as a named argument (in the order they were listed in the class definition). This constructor will type-check each parameter, and convert them where necessary. In particular, `Tensor` fields are converted using [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor); `Tuple` fields are converted to `tuple`s; and `Mapping` fields are converted to immutable dicts.

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

# Constructor takes one parameter for each field.
mt = MaskedTensor(values=[[1, 2, 3], [4, 5, 6]],
                  mask=[[True, True, False], [True, False, True]])

# Fields are type-checked and converted to the declared types.
# For example, `mt.values` is converted to a Tensor.
print(mt.values)
```

The constructor raises an `TypeError` if a field value can not be converted to its declared type:

```
try:
  MaskedTensor([1, 2, 3], None)
except TypeError as e:
  print(f"Got expected TypeError: {e}")
```

The default value for a field can be specified by setting its value at the class level:

```
class Pencil(tf.experimental.ExtensionType):
  color: str = "black"
  has_erasor: bool = True
  length: tf.Tensor = 1.0

Pencil()
```

```
Pencil(length=0.5, color="blue")
```

### Printable representation

`ExtensionType` adds a default printable representation method (`__repr__`) that includes the class name and the value for each field:

```
print(MaskedTensor(values=[1, 2, 3], mask=[True, True, False]))
```

### Equality operators

`ExtensionType` adds default equality operators (`__eq__` and `__ne__`) that consider two values equal if they have the same type and all their fields are equal. Tensor fields are considered equal if they have the same shape and are elementwise equal for all elements.

```
a = MaskedTensor([1, 2], [True, False])
b = MaskedTensor([[3, 4], [5, 6]], [[False, True], [True, True]])
print(f"a == a: {a==a}")
print(f"a == b: {a==b}")
print(f"a == a.values: {a==a.values}")
```

### Validation method

`ExtensionType` adds a `__validate__` method, which can be overridden to perform validation checks on fields. It is run after the constructor is called, and after fields have been type-checked and converted to their declared types, so it can assume that all fields have their declared types.

The following example updates `MaskedTensor` to validate the `shape`s and `dtype`s of its fields:

```
class MaskedTensor(tf.experimental.ExtensionType):
  """A tensor paired with a boolean mask, indicating which values are valid."""
  values: tf.Tensor
  mask: tf.Tensor
  def __validate__(self):
    self.values.shape.assert_is_compatible_with(self.mask.shape)
    assert self.mask.dtype.is_bool, 'mask.dtype must be bool'
```

```
try:
  MaskedTensor([1, 2, 3], [0, 1, 0])  # Wrong `dtype` for mask.
except AssertionError as e:
  print(f"Got expected AssertionError: {e}")
```

```
try:
  MaskedTensor([1, 2, 3], [True, False])  # shapes don't match.
except ValueError as e:
  print(f"Got expected ValueError: {e}")
```

### Enforced immutability

`ExtensionType` overrides the `__setattr__` and `__delattr__` methods to prevent mutation, ensuring that extension type values are immutable.

```
mt = MaskedTensor([1, 2, 3], [True, False, True])
```

```
try:
  mt.mask = [True, True, True]
except AttributeError as e:
  print(f"Got expected AttributeError: {e}")
```

```
try:
  mt.mask[0] = False
except TypeError as e:
  print(f"Got expected TypeError: {e}")
```

```
try:
  del mt.mask
except AttributeError as e:
  print(f"Got expected AttributeError: {e}")
```

### Nested TypeSpec

Each `ExtensionType` class has a corresponding `TypeSpec` class, which is created automatically and stored as `<extension_type_name>.Spec`.

This class captures all the information from a value _except_ for the values of any nested tensors. In particular, the `TypeSpec` for a value is created by replacing any nested Tensor, ExtensionType, or CompositeTensor with its `TypeSpec`.

```
class Player(tf.experimental.ExtensionType):
  name: tf.Tensor
  attributes: Mapping[str, tf.Tensor]

anne = Player("Anne", {"height": 8.3, "speed": 28.1})
anne_spec = tf.type_spec_from_value(anne)
print(anne_spec.name)  # Records `dtype` and `shape`, but not the string value.
print(anne_spec.attributes)  # Records keys and TensorSpecs for values.
```

`TypeSpec` values can be constructed explicitly, or they can be built from an `ExtensionType` value using [`tf.type_spec_from_value`](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value):

```
spec1 = Player.Spec(name=tf.TensorSpec([], tf.float32), attributes={})
spec2 = tf.type_spec_from_value(anne)
```

`TypeSpec`s are used by TensorFlow to divide values into a **static component** and a **dynamic component**:

*   The **static component** (which is fixed at graph-construction time) is encoded with a [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec).
*   The **dynamic component** (which can vary each time the graph is run) is encoded as a list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)s.

For example, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) retraces its wrapped function whenever an argument has a previously unseen `TypeSpec`:

```
@tf.function
def anonymize_player(player):
  print("<<TRACING>>")
  return Player("<anonymous>", player.attributes)
```

```
# Function gets traced (first time the function has been called):
anonymize_player(Player("Anne", {"height": 8.3, "speed": 28.1}))
```

```
# Function does NOT get traced (same TypeSpec: just tensor values changed)
anonymize_player(Player("Bart", {"height": 8.1, "speed": 25.3}))
```

```
# Function gets traced (new TypeSpec: keys for attributes changed):
anonymize_player(Player("Chuck", {"height": 11.0, "jump": 5.3}))
```

For more information, see the [tf.function Guide](https://www.tensorflow.org/guide/function#rules_of_tracing).

Customizing `ExtensionType`s
----------------------------

In addition to simply declaring fields and their types, extension types may:

*   Override the default printable representation (`__repr__`).
*   Define methods.
*   Define `classmethod`s and `staticmethod`s.
*   Define properties.
*   Override the default constructor (`__init__`).
*   Override the default equality operator (`__eq__`).
*   Define operators (such as `__add__` and `__lt__`).
*   Declare default values for fields.
*   Define subclasses.

### Overriding the default printable representation

You can override this default string conversion operator for extension types. The following example updates the `MaskedTensor` class to generate a more readable string representation when values are printed in Eager mode.

```
class MaskedTensor(tf.experimental.ExtensionType):
  """A tensor paired with a boolean mask, indicating which values are valid."""
  values: tf.Tensor
  mask: tf.Tensor       # shape=values.shape; false for invalid values.

  def __repr__(self):
    return masked_tensor_str(self.values, self.mask)

def masked_tensor_str(values, mask):
  if isinstance(values, tf.Tensor):
    if hasattr(values, 'numpy') and hasattr(mask, 'numpy'):
      return f'<MaskedTensor {masked_tensor_str(values.numpy(), mask.numpy())}>'
    else:
      return f'MaskedTensor(values={values}, mask={mask})'
  if len(values.shape) == 1:
    items = [repr(v) if m else '_' for (v, m) in zip(values, mask)]
  else:
    items = [masked_tensor_str(v, m) for (v, m) in zip(values, mask)]
  return '[%s]' % ', '.join(items)

mt = MaskedTensor(values=[[1, 2, 3], [4, 5, 6]],
                  mask=[[True, True, False], [True, False, True]])
print(mt)
```

### Defining methods

Extension types may define methods, just like any normal Python class. For example, the `MaskedTensor` type could define a `with_default` method that returns a copy of `self` with masked values replaced by a given `default` value. Methods may optionally be annotated with the [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) decorator.

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  def with_default(self, default):
    return tf.where(self.mask, self.values, default)

MaskedTensor([1, 2, 3], [True, False, True]).with_default(0)
```

### Defining `classmethod`s and `staticmethod`s

Extension types may define methods using the `@classmethod` and `@staticmethod` decorators. For example, the `MaskedTensor` type could define a factory method that masks any element with a given value:

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  def __repr__(self):
    return masked_tensor_str(self.values, self.mask)

  @staticmethod
  def from_tensor_and_value_to_mask(values, value_to_mask):
    return MaskedTensor(values, values != value_to_mask)

x = tf.constant([[1, 0, 2], [3, 0, 0]])
MaskedTensor.from_tensor_and_value_to_mask(x, 0)
```

### Defining properties

Extension types may define properties using the `@property` decorator, just like any normal Python class. For example, the `MaskedTensor` type could define a `dtype` property that's a shorthand for the `dtype` of the values:

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  @property
  def dtype(self):
    return self.values.dtype

MaskedTensor([1, 2, 3], [True, False, True]).dtype
```

### Overriding the default constructor

You can override the default constructor for extension types. Custom constructors must set a value for every declared field; and after the custom constructor returns, all fields will be type-checked, and values will be converted as described above.

```
class Toy(tf.experimental.ExtensionType):
  name: str
  price: tf.Tensor
  def __init__(self, name, price, discount=0):
    self.name = name
    self.price = price * (1 - discount)

print(Toy("ball", 5.0, discount=0.2))  # On sale -- 20% off!
```

Alternatively, you might consider leaving the default constructor as-is, but adding one or more factory methods. For example:

```
class Toy(tf.experimental.ExtensionType):
  name: str
  price: tf.Tensor

  @staticmethod
  def new_toy_with_discount(name, price, discount):
    return Toy(name, price * (1 - discount))

print(Toy.new_toy_with_discount("ball", 5.0, discount=0.2))
```

### Overriding the default equality operator (`__eq__`)

You can override the default `__eq__` operator for extension types. The following example updates `MaskedTensor` to ignore masked elements when comparing for equality.

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  def __repr__(self):
    return masked_tensor_str(self.values, self.mask)

  def __eq__(self, other):
    result = tf.math.equal(self.values, other.values)
    result = result | ~(self.mask & other.mask)
    return tf.reduce_all(result)

x = MaskedTensor([1, 2, 3, 4], [True, True, False, True])
y = MaskedTensor([5, 2, 0, 4], [False, True, False, True])
print(x == y)
```

### Using forward references

If the type for a field has not been defined yet, you may use a string containing the name of the type instead. In the following example, the string `"Node"` is used to annotate the `children` field because the `Node` type hasn't been (fully) defined yet.

```
class Node(tf.experimental.ExtensionType):
  value: tf.Tensor
  children: Tuple["Node", ...] = ()

Node(3, [Node(5), Node(2)])
```

### Defining subclasses

Extension types may be subclassed using the standard Python syntax. Extension type subclasses may add new fields, methods, and properties; and may override the constructor, the printable representation, and the equality operator. The following example defines a basic `TensorGraph` class that uses three `Tensor` fields to encode a set of edges between nodes. It then defines a subclass that adds a `Tensor` field to record a "feature value" for each node. The subclass also defines a method to propagate the feature values along the edges.

```
class TensorGraph(tf.experimental.ExtensionType):
  num_nodes: tf.Tensor
  edge_src: tf.Tensor   # edge_src[e] = index of src node for edge e.
  edge_dst: tf.Tensor   # edge_dst[e] = index of dst node for edge e.

class TensorGraphWithNodeFeature(TensorGraph):
  node_features: tf.Tensor  # node_features[n] = feature value for node n.

  def propagate_features(self, weight=1.0) -> 'TensorGraphWithNodeFeature':
    updates = tf.gather(self.node_features, self.edge_src) * weight
    new_node_features = tf.tensor_scatter_nd_add(
        self.node_features, tf.expand_dims(self.edge_dst, 1), updates)
    return TensorGraphWithNodeFeature(
        self.num_nodes, self.edge_src, self.edge_dst, new_node_features)

g = TensorGraphWithNodeFeature(  # Edges: 0->1, 4->3, 2->2, 2->1
    num_nodes=5, edge_src=[0, 4, 2, 2], edge_dst=[1, 3, 2, 1],
    node_features=[10.0, 0.0, 2.0, 5.0, -1.0, 0.0])

print("Original features:", g.node_features)
print("After propagating:", g.propagate_features().node_features)
```

### Defining private fields

An extension type's fields may be marked private by prefixing them with an underscore (following standard Python conventions). This does not impact the way that TensorFlow treats the fields in any way; but simply serves as a signal to any users of the extension type that those fields are private.

### Customizing the `ExtensionType`'s `TypeSpec`

Each `ExtensionType` class has a corresponding `TypeSpec` class, which is created automatically and stored as `<extension_type_name>.Spec`. For more information, see the section "Nested TypeSpec" above.

To customize the `TypeSpec`, simply define your own nested class named `Spec`, and `ExtensionType` will use that as the basis for the automatically constructed `TypeSpec`. You can customize the `Spec` class by:

*   Overriding the default printable representation.
*   Overriding the default constructor.
*   Defining methods, `classmethod`s, `staticmethod`s, and properties.

The following example customizes the `MaskedTensor.Spec` class to make it easier to use:

```
class MaskedTensor(tf.experimental.ExtensionType):
  values: tf.Tensor
  mask: tf.Tensor

  shape = property(lambda self: self.values.shape)
  dtype = property(lambda self: self.values.dtype)

  def __repr__(self):
    return masked_tensor_str(self.values, self.mask)

  def with_values(self, new_values):
    return MaskedTensor(new_values, self.mask)

  class Spec:
    def __init__(self, shape, dtype=tf.float32):
      self.values = tf.TensorSpec(shape, dtype)
      self.mask = tf.TensorSpec(shape, tf.bool)

    def __repr__(self):
      return f"MaskedTensor.Spec(shape={self.shape}, dtype={self.dtype})"

    shape = property(lambda self: self.values.shape)
    dtype = property(lambda self: self.values.dtype)
```

Tensor API dispatch
-------------------

Extension types can be "tensor-like", in the sense that they specialize or extend the interface defined by the [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) type. Examples of tensor-like extension types include `RaggedTensor`, `SparseTensor`, and `MaskedTensor`. **_Dispatch decorators_** can be used to override the default behavior of TensorFlow operations when applied to tensor-like extension types. TensorFlow currently defines three dispatch decorators:

*   [`@tf.experimental.dispatch_for_api(tf_api)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api)
*   [`@tf.experimental.dispatch_for_unary_elementwise_apis(x_type)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis)
*   [`@tf.experimental.dispatch_for_binary_elementwise_apis(x_type, y_type)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis)

### Dispatch for a single API

The [`tf.experimental.dispatch_for_api`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api) decorator overrides the default behavior of a specified TensorFlow operation when it is called with the specified signature. For example, you can use this decorator to specify how [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack) should process `MaskedTensor` values:

```
@tf.experimental.dispatch_for_api(tf.stack)
def masked_stack(values: List[MaskedTensor], axis = 0):
  return MaskedTensor(tf.stack([v.values for v in values], axis),
                      tf.stack([v.mask for v in values], axis))
```

This overrides the default implementation for [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack) whenever it is called with a list of `MaskedTensor` values (since the `values` argument is annotated with `typing.List[MaskedTensor]`):

```
x = MaskedTensor([1, 2, 3], [True, True, False])
y = MaskedTensor([4, 5, 6], [False, True, True])
tf.stack([x, y])
```

To allow [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack) to handle lists of mixed `MaskedTensor` and `Tensor` values, you can refine the type annotation for the `values` parameter and update the body of the function appropriately:

```
tf.experimental.unregister_dispatch_for(masked_stack)

def convert_to_masked_tensor(x):
  if isinstance(x, MaskedTensor):
    return x
  else:
    return MaskedTensor(x, tf.ones_like(x, tf.bool))

@tf.experimental.dispatch_for_api(tf.stack)
def masked_stack_v2(values: List[Union[MaskedTensor, tf.Tensor]], axis = 0):
  values = [convert_to_masked_tensor(v) for v in values]
  return MaskedTensor(tf.stack([v.values for v in values], axis),
                      tf.stack([v.mask for v in values], axis))
x = MaskedTensor([1, 2, 3], [True, True, False])
y = tf.constant([4, 5, 6])
tf.stack([x, y, x])
```

For a list of APIs that can be overridden, see the API documentation for [`tf.experimental.dispatch_for_api`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api).

### Dispatch for all unary elementwise APIs

The [`tf.experimental.dispatch_for_unary_elementwise_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis) decorator overrides the default behavior of **_all_** unary elementwise ops (such as [`tf.math.cos`](https://www.tensorflow.org/api_docs/python/tf/math/cos)) whenever the value for the first argument (typically named `x`) matches the type annotation `x_type`. The decorated function should take two arguments:

*   `api_func`: A function that takes a single parameter and performs the elementwise operation (for example, [`tf.abs`](https://www.tensorflow.org/api_docs/python/tf/math/abs)).
*   `x`: The first argument to the elementwise operation.

The following example updates all unary elementwise operations to handle the `MaskedTensor` type:

```
@tf.experimental.dispatch_for_unary_elementwise_apis(MaskedTensor)
 def masked_tensor_unary_elementwise_api_handler(api_func, x):
   return MaskedTensor(api_func(x.values), x.mask)
```

This function will now be used whenever a unary elementwise operation is called on a `MaskedTensor`.

```
x = MaskedTensor([1, -2, -3], [True, False, True])
 print(tf.abs(x))
```

```
print(tf.ones_like(x, dtype=tf.float32))
```

### Dispatch for binary all elementwise APIs

Similarly, [`tf.experimental.dispatch_for_binary_elementwise_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis) can be used to update all binary elementwise operations to handle the `MaskedTensor` type:

```
@tf.experimental.dispatch_for_binary_elementwise_apis(MaskedTensor, MaskedTensor)
def masked_tensor_binary_elementwise_api_handler(api_func, x, y):
  return MaskedTensor(api_func(x.values, y.values), x.mask & y.mask)
```

```
x = MaskedTensor([1, -2, -3], [True, False, True])
y = MaskedTensor([[4], [5]], [[True], [False]])
tf.math.add(x, y)
```

For a list of the elementwise APIs that are overridden, go to the API documentation for [`tf.experimental.dispatch_for_unary_elementwise_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis) and [`tf.experimental.dispatch_for_binary_elementwise_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis).

Batchable `ExtensionType`s
--------------------------

An `ExtensionType` is _batchable_ if a single instance can be used to represent a batch of values. Typically, this is accomplished by adding batch dimensions to all nested `Tensor`s. The following TensorFlow APIs require that any extension type inputs be batchable:

*   [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) (`batch`, `unbatch`, `from_tensor_slices`)
*   [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) (`fit`, `evaluate`, `predict`)
*   [`tf.map_fn`](https://www.tensorflow.org/api_docs/python/tf/map_fn)

By default, `BatchableExtensionType` creates batched values by batching any nested `Tensor`s, `CompositeTensor`s, and `ExtensionType`s. If this is not appropriate for your class, then you will need to use [`tf.experimental.ExtensionTypeBatchEncoder`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder) to override this default behavior. For example, it would not be appropriate to create a batch of [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) values by simply stacking individual sparse tensors' `values`, `indices`, and `dense_shape` fields -- in most cases, you can't stack these tensors, since they have incompatible shapes; and even if you could, the result would not be a valid `SparseTensor`.

### `BatchableExtensionType` example: `Network`

As an example, consider a simple `Network` class used for load balancing, which tracks how much work is left to do at each node, and how much bandwidth is available to move work between nodes:

```
class Network(tf.experimental.ExtensionType):  # This version is not batchable.
  work: tf.Tensor       # work[n] = work left to do at node n
  bandwidth: tf.Tensor  # bandwidth[n1, n2] = bandwidth from n1->n2

net1 = Network([5., 3, 8], [[0., 2, 0], [2, 0, 3], [0, 3, 0]])
net2 = Network([3., 4, 2], [[0., 2, 2], [2, 0, 2], [2, 2, 0]])
```

To make this type batchable, change the base type to `BatchableExtensionType`, and adjust the shape of each field to include optional batch dimensions. The following example also adds a `shape` field to keep track of the batch shape. This `shape` field is not required by [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) or [`tf.map_fn`](https://www.tensorflow.org/api_docs/python/tf/map_fn), but it _is_ required by [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras).

```
class Network(tf.experimental.BatchableExtensionType):
  shape: tf.TensorShape  # batch shape. A single network has shape=[].
  work: tf.Tensor        # work[*shape, n] = work left to do at node n
  bandwidth: tf.Tensor   # bandwidth[*shape, n1, n2] = bandwidth from n1->n2

  def __init__(self, work, bandwidth):
    self.work = tf.convert_to_tensor(work)
    self.bandwidth = tf.convert_to_tensor(bandwidth)
    work_batch_shape = self.work.shape[:-1]
    bandwidth_batch_shape = self.bandwidth.shape[:-2]
    self.shape = work_batch_shape.merge_with(bandwidth_batch_shape)

  def __repr__(self):
    return network_repr(self)

def network_repr(network):
  work = network.work
  bandwidth = network.bandwidth
  if hasattr(work, 'numpy'):
    work = ' '.join(str(work.numpy()).split())
  if hasattr(bandwidth, 'numpy'):
    bandwidth = ' '.join(str(bandwidth.numpy()).split())
  return (f"<Network shape={network.shape} work={work} bandwidth={bandwidth}>")
```

```
net1 = Network([5., 3, 8], [[0., 2, 0], [2, 0, 3], [0, 3, 0]])
net2 = Network([3., 4, 2], [[0., 2, 2], [2, 0, 2], [2, 2, 0]])
batch_of_networks = Network(
    work=tf.stack([net1.work, net2.work]),
    bandwidth=tf.stack([net1.bandwidth, net2.bandwidth]))
print(f"net1={net1}")
print(f"net2={net2}")
print(f"batch={batch_of_networks}")
```

You can then use [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) to iterate through a batch of networks:

```
dataset = tf.data.Dataset.from_tensor_slices(batch_of_networks)
for i, network in enumerate(dataset):
  print(f"Batch element {i}: {network}")
```

And you can also use `map_fn` to apply a function to each batch element:

```
def balance_work_greedy(network):
  delta = (tf.expand_dims(network.work, -1) - tf.expand_dims(network.work, -2))
  delta /= 4
  delta = tf.maximum(tf.minimum(delta, network.bandwidth), -network.bandwidth)
  new_work = network.work + tf.reduce_sum(delta, -1)
  return Network(new_work, network.bandwidth)

tf.map_fn(balance_work_greedy, batch_of_networks)
```

TensorFlow APIs that support `ExtensionType`s
---------------------------------------------

### @tf.function

[`tf.function`](https://www.tensorflow.org/guide/function) is a decorator that precomputes TensorFlow graphs for Python functions, which can substantially improve the performance of your TensorFlow code. Extension type values can be used transparently with [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)-decorated functions.

```
class Pastry(tf.experimental.ExtensionType):
  sweetness: tf.Tensor  # 2d embedding that encodes sweetness
  chewiness: tf.Tensor  # 2d embedding that encodes chewiness

@tf.function
def combine_pastry_features(x: Pastry):
  return (x.sweetness + x.chewiness) / 2

cookie = Pastry(sweetness=[1.2, 0.4], chewiness=[0.8, 0.2])
combine_pastry_features(cookie)
```

If you wish to explicitly specify the `input_signature` for [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function), then you can do so using the extension type's `TypeSpec`.

```
pastry_spec = Pastry.Spec(tf.TensorSpec([2]), tf.TensorSpec(2))

@tf.function(input_signature=[pastry_spec])
def increase_sweetness(x: Pastry, delta=1.0):
  return Pastry(x.sweetness + delta, x.chewiness)

increase_sweetness(cookie)
```

#### Concrete functions

Concrete functions encapsulate individual traced graphs that are built by [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). Extension types can be used transparently with concrete functions.

```
cf = combine_pastry_features.get_concrete_function(pastry_spec)
cf(cookie)
```

### Control flow operations

Extension types are supported by TensorFlow's control-flow operations:

*   [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
*   [`tf.case`](https://www.tensorflow.org/api_docs/python/tf/case)
*   [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
*   [`tf.identity`](https://www.tensorflow.org/api_docs/python/tf/identity)

```
# Example: using tf.cond to select between two MaskedTensors. Note that the
# two MaskedTensors don't need to have the same shape.
a = MaskedTensor([1., 2, 3], [True, False, True])
b = MaskedTensor([22., 33, 108, 55], [True, True, True, False])
condition = tf.constant(True)
print(tf.cond(condition, lambda: a, lambda: b))
```

```
# Example: using tf.while_loop with MaskedTensor.
cond = lambda i, _: i < 10
def body(i, mt):
  return i + 1, mt.with_values(mt.values + 3 / 7)
print(tf.while_loop(cond, body, [0, b])[1])
```

### Autograph control flow

Extension types are also supported by control flow statements in [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) (using autograph). In the following example, the `if` statement and `for` statements are automatically converted to [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond) and [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop) operations, which support extension types.

```
@tf.function
def fn(x, b):
  if b:
    x = MaskedTensor(x, tf.less(x, 0))
  else:
    x = MaskedTensor(x, tf.greater(x, 0))
  for i in tf.range(5 if b else 7):
    x = x.with_values(x.values + 1 / 2)
  return x

print(fn(tf.constant([1., -2, 3]), tf.constant(True)))
print(fn(tf.constant([1., -2, 3]), tf.constant(False)))
```

### Keras

[tf.keras](https://www.tensorflow.org/guide/keras) is TensorFlow's high-level API for building and training deep learning models. Extension types may be passed as inputs to a Keras model, passed between Keras layers, and returned by Keras models. Keras currently puts two requirements on extension types:

*   They must be batchable (go to "Batchable `ExtensionType`s" above).
*   They must have a field or property named `shape`. `shape[0]` is assumed to be the batch dimension.

The following two subsections give examples showing how extension types can be used with Keras.

#### Keras example: `Network`

For the first example, consider the `Network` class defined in the "Batchable `ExtensionType`s" section above, which can be used for load balancing work between nodes. Its definition is repeated here:

```
class Network(tf.experimental.BatchableExtensionType):
  shape: tf.TensorShape  # batch shape. A single network has shape=[].
  work: tf.Tensor        # work[*shape, n] = work left to do at node n
  bandwidth: tf.Tensor   # bandwidth[*shape, n1, n2] = bandwidth from n1->n2

  def __init__(self, work, bandwidth):
    self.work = tf.convert_to_tensor(work)
    self.bandwidth = tf.convert_to_tensor(bandwidth)
    work_batch_shape = self.work.shape[:-1]
    bandwidth_batch_shape = self.bandwidth.shape[:-2]
    self.shape = work_batch_shape.merge_with(bandwidth_batch_shape)

  def __repr__(self):
    return network_repr(self)
```

```
single_network = Network(  # A single network with 4 nodes.
    work=[8.0, 5, 12, 2],
    bandwidth=[[0.0, 1, 2, 2], [1, 0, 0, 2], [2, 0, 0, 1], [2, 2, 1, 0]])

batch_of_networks = Network(  # Batch of 2 networks, each w/ 2 nodes.
    work=[[8.0, 5], [3, 2]],
    bandwidth=[[[0.0, 1], [1, 0]], [[0, 2], [2, 0]]])
```

You can define a new Keras layer that processes `Network`s.

```
class BalanceNetworkLayer(tf.keras.layers.Layer):
  """Layer that balances work between nodes in a network.

  Shifts work from more busy nodes to less busy nodes, constrained by bandwidth.
  """
  def call(self, inputs):
    # This function is defined above in the "Batchable `ExtensionType`s" section.
    return balance_work_greedy(inputs)
```

You can then use these layers to create a simple model. To feed an `ExtensionType` into a model, you can use a `tf.keras.layer.Input` layer with `type_spec` set to the extension type's `TypeSpec`. If the Keras model will be used to process batches, then the `type_spec` must include the batch dimension.

```
input_spec = Network.Spec(shape=None,
                          work=tf.TensorSpec(None, tf.float32),
                          bandwidth=tf.TensorSpec(None, tf.float32))
model = tf.keras.Sequential([
    tf.keras.layers.Input(type_spec=input_spec),
    BalanceNetworkLayer(),
    ])
```

Finally, you can apply the model to a single network and to a batch of networks.

```
model(single_network)
```

```
model(batch_of_networks)
```

#### Keras example: MaskedTensor

In this example, `MaskedTensor` is extended to support `Keras`. `shape` is defined as a property that is calculated from the `values` field. Keras requires that you add this property to both the extension type and its `TypeSpec`. `MaskedTensor` also defines a `__name__` variable, which will be required for `SavedModel` serialization (below).

```
class MaskedTensor(tf.experimental.BatchableExtensionType):
  # __name__ is required for serialization in SavedModel; see below for details.
  __name__ = 'extension_type_colab.MaskedTensor'

  values: tf.Tensor
  mask: tf.Tensor

  shape = property(lambda self: self.values.shape)
  dtype = property(lambda self: self.values.dtype)

  def with_default(self, default):
    return tf.where(self.mask, self.values, default)

  def __repr__(self):
    return masked_tensor_str(self.values, self.mask)

  class Spec:
    def __init__(self, shape, dtype=tf.float32):
      self.values = tf.TensorSpec(shape, dtype)
      self.mask = tf.TensorSpec(shape, tf.bool)

    shape = property(lambda self: self.values.shape)
    dtype = property(lambda self: self.values.dtype)

    def with_shape(self):
      return MaskedTensor.Spec(tf.TensorSpec(shape, self.values.dtype),
                               tf.TensorSpec(shape, self.mask.dtype))
```

Next, the dispatch decorators are used to override the default behavior of several TensorFlow APIs. Since these APIs are used by standard Keras layers (such as the `Dense` layer), overriding these will allow us to use those layers with `MaskedTensor`. For the purposes of this example, `matmul` for masked tensors is defined to treat the masked values as zeros (that is, to not include them in the product).

```
@tf.experimental.dispatch_for_unary_elementwise_apis(MaskedTensor)
def unary_elementwise_op_handler(op, x):
 return MaskedTensor(op(x.values), x.mask)

@tf.experimental.dispatch_for_binary_elementwise_apis(
    Union[MaskedTensor, tf.Tensor],
    Union[MaskedTensor, tf.Tensor])
def binary_elementwise_op_handler(op, x, y):
  x = convert_to_masked_tensor(x)
  y = convert_to_masked_tensor(y)
  return MaskedTensor(op(x.values, y.values), x.mask & y.mask)

@tf.experimental.dispatch_for_api(tf.matmul)
def masked_matmul(a: MaskedTensor, b,
                  transpose_a=False, transpose_b=False,
                  adjoint_a=False, adjoint_b=False,
                  a_is_sparse=False, b_is_sparse=False,
                  output_type=None):
  if isinstance(a, MaskedTensor):
    a = a.with_default(0)
  if isinstance(b, MaskedTensor):
    b = b.with_default(0)
  return tf.matmul(a, b, transpose_a, transpose_b, adjoint_a,
                   adjoint_b, a_is_sparse, b_is_sparse, output_type)
```

You can then construct a Keras model that accepts `MaskedTensor` inputs, using standard Keras layers:

```
input_spec = MaskedTensor.Spec([None, 2], tf.float32)

masked_tensor_model = tf.keras.Sequential([
    tf.keras.layers.Input(type_spec=input_spec),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1)])
masked_tensor_model.compile(loss='binary_crossentropy', optimizer='rmsprop')
```

```
a = MaskedTensor([[1., 2], [3, 4], [5, 6]],
                  [[True, False], [False, True], [True, True]])
masked_tensor_model.fit(a, tf.constant([[1], [0], [1]]), epochs=3)
print(masked_tensor_model(a))
```

### SavedModel

A [SavedModel](https://www.tensorflow.org/guide/saved_model) is a serialized TensorFlow program, including both weights and computation. It can be built from a Keras model or from a custom model. In either case, extension types can be used transparently with the functions and methods defined by a SavedModel.

SavedModel can save models, layers, and functions that process extension types, as long as the extension types have a `__name__` field. This name is used to register the extension type, so it can be located when the model is loaded.

#### Example: saving a Keras model

Keras models that use extension types may be saved using `SavedModel`.

```
masked_tensor_model_path = tempfile.mkdtemp()
tf.saved_model.save(masked_tensor_model, masked_tensor_model_path)
imported_model = tf.saved_model.load(masked_tensor_model_path)
imported_model(a)
```

#### Example: saving a custom model

SavedModel can also be used to save custom [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module) subclasses with functions that process extension types.

```
class CustomModule(tf.Module):
  def __init__(self, variable_value):
    super().__init__()
    self.v = tf.Variable(variable_value)

  @tf.function
  def grow(self, x: MaskedTensor):
    """Increase values in `x` by multiplying them by `self.v`."""
    return MaskedTensor(x.values * self.v, x.mask)

module = CustomModule(100.0)

module.grow.get_concrete_function(MaskedTensor.Spec(shape=None,
                                                    dtype=tf.float32))
custom_module_path = tempfile.mkdtemp()
tf.saved_model.save(module, custom_module_path)
imported_model = tf.saved_model.load(custom_module_path)
imported_model.grow(MaskedTensor([1., 2, 3], [False, True, False]))
```

#### Loading a SavedModel when the `ExtensionType` is unavailable

If you load a `SavedModel` that uses an `ExtensionType`, but that `ExtensionType` is not available (that is, it has not been imported), then you will get a warning and TensorFlow will fall back to using an "anonymous extension type" object. This object will have the same fields as the original type, but will lack any further customization you have added for the type, such as custom methods or properties.

#### Using `ExtensionType`s with TensorFlow Serving

Currently, [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving) (and other consumers of the SavedModel "signatures" dictionary) require that all inputs and outputs be raw tensors. If you wish to use TensorFlow Serving with a model that uses extension types, then you can add wrapper methods that compose or decompose extension type values from tensors. For example:

```
class CustomModuleWrapper(tf.Module):
  def __init__(self, variable_value):
    super().__init__()
    self.v = tf.Variable(variable_value)

  @tf.function
  def var_weighted_mean(self, x: MaskedTensor):
    """Mean value of unmasked values in x, weighted by self.v."""
    x = MaskedTensor(x.values * self.v, x.mask)
    return (tf.reduce_sum(x.with_default(0)) /
            tf.reduce_sum(tf.cast(x.mask, x.dtype)))

  @tf.function()
  def var_weighted_mean_wrapper(self, x_values, x_mask):
    """Raw tensor wrapper for var_weighted_mean."""
    return self.var_weighted_mean(MaskedTensor(x_values, x_mask))

module = CustomModuleWrapper([3., 2., 8., 5.])

module.var_weighted_mean_wrapper.get_concrete_function(
    tf.TensorSpec(None, tf.float32), tf.TensorSpec(None, tf.bool))
custom_module_path = tempfile.mkdtemp()
tf.saved_model.save(module, custom_module_path)
imported_model = tf.saved_model.load(custom_module_path)
x = MaskedTensor([1., 2., 3., 4.], [False, True, False, True])
imported_model.var_weighted_mean_wrapper(x.values, x.mask)
```

### `Dataset`s

[`tf.data`](https://www.tensorflow.org/guide/data) is an API that enables you to build complex input pipelines from simple, reusable pieces. Its core data structure is [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset), which represents a sequence of elements, in which each element consists of one or more components.

#### Building `Dataset`s with extension types

Datasets can be built from extension type values using [`Dataset.from_tensors`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensors), [`Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices), or [`Dataset.from_generator`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_generator):

```
ds = tf.data.Dataset.from_tensors(Pastry(5, 5))
iter(ds).next()
```

```
mt = MaskedTensor(tf.reshape(range(20), [5, 4]), tf.ones([5, 4]))
ds = tf.data.Dataset.from_tensor_slices(mt)
for value in ds:
  print(value)
```

```
def value_gen():
  for i in range(2, 7):
    yield MaskedTensor(range(10), [j%i != 0 for j in range(10)])

ds = tf.data.Dataset.from_generator(
    value_gen, output_signature=MaskedTensor.Spec(shape=[10], dtype=tf.int32))
for value in ds:
  print(value)
```

#### Batching and unbatching `Dataset`s with extension types

Datasets with extension types can be batchand and unbatched using [`Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch) and [`Dataset.unbatch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#unbatch).

```
batched_ds = ds.batch(2)
for value in batched_ds:
  print(value)
```

```
unbatched_ds = batched_ds.unbatch()
for value in unbatched_ds:
  print(value)
```

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-03-23 UTC.
