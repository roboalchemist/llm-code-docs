# Source: https://keras.io/api/data_loading/text

Title: Keras documentation: Text data loading

URL Source: https://keras.io/api/data_loading/text

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/utils/text_dataset_utils.py#L10)

### `text_dataset_from_directory` function

```
keras.utils.text_dataset_from_directory(
    directory,
    labels="inferred",
    label_mode="int",
    class_names=None,
    batch_size=32,
    max_length=None,
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    follow_links=False,
    format="tf",
    verbose=True,
)
```

Generates a dataset from text files in a directory.

If your directory structure is:

```
main_directory/
...class_a/
......a_text_1.txt
......a_text_2.txt
...class_b/
......b_text_1.txt
......b_text_2.txt
```

Then calling 
```
text_dataset_from_directory(main_directory,
labels='inferred')
```
 will return a dataset that yields batches of texts from the subdirectories `class_a` and `class_b`, together with labels 0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

Only `.txt` files are supported at this time.

By default, this function will return a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) object. You can set `format="grain"` to return a `grain.IterDataset` object instead, which removes the TensorFlow dependency.

**Arguments**

*   **directory**: Directory where the data is located. If `labels` is `"inferred"`, it should contain subdirectories, each containing text files for a class. Otherwise, the directory structure is ignored.
*   **labels**: Either `"inferred"` (labels are generated from the directory structure), `None` (no labels), or a list/tuple of integer labels of the same size as the number of text files found in the directory. Labels should be sorted according to the alphanumeric order of the text file paths (obtained via `os.walk(directory)` in Python).
*   **label_mode**: String describing the encoding of `labels`. Options are:
    *   `"int"`: means that the labels are encoded as integers (e.g. for `sparse_categorical_crossentropy` loss).
    *   `"categorical"` means that the labels are encoded as a categorical vector (e.g. for `categorical_crossentropy` loss).
    *   `"binary"` means that the labels (there can be only 2) are encoded as `float32` scalars with values 0 or 1 (e.g. for `binary_crossentropy`).
    *   `None` (no labels).

*   **class_names**: Only valid if `"labels"` is `"inferred"`. This is the explicit list of class names (must match names of subdirectories). Used to control the order of the classes (otherwise alphanumerical order is used).
*   **batch_size**: Size of the batches of data. If `None`, the data will not be batched (the dataset will yield individual samples). Defaults to `32`.
*   **max_length**: Maximum size of a text string. Texts longer than this will be truncated to `max_length`.
*   **shuffle**: Whether to shuffle the data. If set to `False`, sorts the data in alphanumeric order. Defaults to `True`.
*   **seed**: Optional random seed for shuffling and transformations.
*   **validation_split**: Optional float between 0 and 1, fraction of data to reserve for validation.
*   **subset**: Subset of the data to return. One of `"training"`, `"validation"` or `"both"`. Only used if `validation_split` is set. When `subset="both"`, the utility returns a tuple of two datasets (the training and validation datasets respectively).
*   **follow_links**: Whether to visits subdirectories pointed to by symlinks. Defaults to `False`.
*   **format**: The format of the return object. Defaults to `"tf"`. Available options are:
    *   `"tf"`: returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) object. Requires TensorFlow to be installed.
    *   `"grain"`: returns a `grain.IterDataset` object. Requires Grain to be installed.

*   **verbose**: Whether to display number information on classes and number of files found. Defaults to `True`.

**Returns**

A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) (`format="tf"`) or `grain.IterDataset` (`format="grain"`) object.

When `format="tf"`: - If `label_mode` is `None`, it yields `string` tensors of shape `(batch_size,)`, containing the contents of a batch of text files. - Otherwise, it yields a tuple `(texts, labels)`, where `texts` has shape `(batch_size,)` and `labels` follows the format described below.

When `format="grain"`: - If `label_mode` is `None`, it yields a list of Python strings containing the contents of a batch of text files. - Otherwise, it yields a tuple `(texts, labels)`, where `texts` is a list of Python strings and `labels` follows the format described below.

Rules regarding labels format:

*   if `label_mode` is `int`, the labels are an `int32` tensor of shape `(batch_size,)`.
*   if `label_mode` is `binary`, the labels are a `float32` tensor of 1s and 0s of shape `(batch_size, 1)`.
*   if `label_mode` is `categorical`, the labels are a `float32` tensor of shape `(batch_size, num_classes)`, representing a one-hot encoding of the class index.

**Guides and examples using `text_dataset_from_directory`**

*   [Text classification from scratch](https://keras.io/examples/nlp/text_classification_from_scratch/)
*   [Text Classification using FNet](https://keras.io/examples/nlp/fnet_classification_with_keras_hub/)
*   [Float8 training and inference with a simple Transformer model](https://keras.io/examples/keras_recipes/float8_training_and_inference_with_transformer/)

* * *
