# Source: https://onnxruntime.ai/docs/reference/operators/reduced-operator-config-file.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#reduced-operator-config-file) Reduced operator config file 

The reduced operator config file is an input to the ONNX Runtime build-from-source script. It specifies which operators are included in the runtime. A reduced set of operators in ONNX Runtime permits a smaller build binary size. A smaller runtime is used in constrained environments, such as mobile and web deployments.

This article shows you how to generate the reduced operator config file using the `create_reduced_build_config.py` script. You can also generate the reduced operator config file by [converting ONNX models to ORT format](/docs/performance/model-optimizations/ort-format-models.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [The create_reduced_build_config.py script](#the-create_reduced_build_configpy-script)
- [Configuration file format](#configuration-file-format)
- [Type reduction format](#type-reduction-format)
  - [Per-operator type information](#per-operator-type-information)
  - [Globally allowed types](#globally-allowed-types)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#the-create_reduced_build_configpy-script) The create_reduced_build_config.py script 

To create a reduced operator configuration file, run the script [create_reduced_build_config.py](https://github.com/microsoft/onnxruntime/blob/main/tools/python/create_reduced_build_config.py) on your model/s.

The kernel configuration file can be manually edited as needed. The configuration can be created from either ONNX or ORT format models.

``` highlight
create_reduced_build_config.py --help
usage: Script to create a reduced build config file from ONNX or ORT format model/s. [-h] [-f ] [-t] model_path_or_dir config_path

positional arguments:
  model_path_or_dir     Path to a single model, or a directory that will be recursively searched for models to process.
  config_path           Path to write configuration file to.

optional arguments:
  -h, --help            show this help message and exit
  -f , --format 
                        Format of model/s to process. (default: ONNX)
  -t, --enable_type_reduction
                        Enable tracking of the specific types that individual operators require. Operator implementations MAY support limiting the type support included
                        in the build to these types. Only possible with ORT format models. (default: False)
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configuration-file-format) Configuration file format

The basic format of the operator reduction configuration file is `<operator domain>;<opset for domain>;<op1>[,op2]...`

e.g.

``` highlight
#domain;opset;op1,op2...
ai.onnx;12;Add,Cast,Concat,Squeeze
```

The opset can match either the opset import for each model, or the initial ONNX opset that the operator version was first available in. If manually editing the configuration file, using the opset import value from the model is simplest.

e.g. if a model imports opset 12 of ONNX, all ONNX operators in that model can be listed under opset 12 for the 'ai.onnx' domain.

[Netron](https://netron.app/) can be used to view an ONNX model properties to discover the opset imports. Additionally, the ONNX operator specs for [DNN](https://github.com/onnx/onnx/blob/master/docs/Operators.md) and [traditional ML](https://github.com/onnx/onnx/blob/master/docs/Operators-ml.md) operators list the individual operator versions.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#type-reduction-format) Type reduction format

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#per-operator-type-information) Per-operator type information

If the types an operator implementation supports can be limited to a specific set of types, this is specified in a JSON string immediately after the operator name in the configuration file.

**It is highly recommended that you first generate the configuration file using ORT format models with type reduction enabled in order to see which operators support type reduction, and how the entry is defined for the individual operators.**

The required types are generally listed per input and/or output of the operator. The type information is in a map, with 'inputs' and 'outputs' keys. The value for 'inputs' or 'outputs' is a map between the index number of the input/output and the required list of types.

For example, both the input and output types are relevant to ai.onnx:Cast. Type information for input 0 and output 0 could look like this:

``` highlight
, "outputs": }
```

which is added directly after the operator name in the configuration file. E.g.:

``` highlight
ai.onnx;12;Add,Cast, "outputs": },Concat,Squeeze
```

If, for example, the types of inputs 0 and 1 were important, the entry may look like this (e.g. ai.onnx:Gather):

``` highlight
}
```

Finally some operators do non-standard things and store their type information under a 'custom' key. ai.onnx.OneHot is an example of this, where the three input types are combined into a triple.

``` highlight

```

For these reasons, it is best to generate the configuration file first, and manually edit any entries if needed.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#globally-allowed-types) Globally allowed types

It is also possible to limit the types supported by all operators to a specific set of types. These are referred to as *globally allowed types*. They may be specified in the configuration file on a separate line.

The format for specifying globally allowed types for all operators is:

``` highlight
!globally_allowed_types;T0,T1,...
```

`Ti` should be a C++ scalar type supported by ONNX and ORT. At most one globally allowed types specification is allowed.

Specifying per-operator type information and specifying globally allowed types are mutually exclusive - it is an error to specify both.