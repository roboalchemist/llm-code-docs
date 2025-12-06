# Source: https://docs.vespa.ai/en/reference/ranking/model-files.html.md

# Stateless model reference

 

_.model_ files are used in[stateless model evaluation](../../ranking/stateless-model-evaluation.html). These are files with [ranking expressions](../../basics/ranking.html), located in [models](../applications/application-packages.html) / a subdirectory of _models_, with _.model_ suffix:

```
├── models
│   └── my_model.model
└── services.xml
```

## .model file format specification

```
model [name] {

    inputs {
        ([input-name] [[input-type](tensor.html#tensor-type-spec)])*
    }

    constants {[constant](#constant)*
    }

    (function [name]([argument-name]*) {
        expression: [[ranking expression](ranking-expressions.html)]
    })*

}
```

The elements can appear in any order (and number).

### Constant element

```
[constant-name] [type]?: [scalar,[tensor on literal form](tensor.html#tensor-literal-form), orfile:followed by a file reference]
```

| Name | Description |
| --- | --- |
| name | The name of the constant, written either the full feature name `constant(myName)`, or just as `name`. |
| type | The type of the constant, either `double` or a [tensor type](tensor.html#tensor-type-spec). If omitted, the type is double. |
| value | A number, a [tensor on literal form](tensor.html#tensor-literal-form), or `file:` followed by a path relative to the model file to a file containing the constant. The file must be stored on the [tensor JSON Format](../schemas/document-json-format.html#tensor) and end with `.json`. The file may be lz4 compressed, in which case the ending must be `.json.lz4`. |

Constant examples:

```
constants {
    myDouble: 0.5
    constant(myOtherDouble) double: 0.6
    constant(myArray) tensor(x[3]):[1, 2, 3]
    constant(myMap) tensor(key{}):{key1: 1.0, key2: 2.0}
    constant(myLargeTensor) tensor(x[10000]): file:constants/myTensor.json.lz4
}
```

## Model example

This file must be saved as `example.model` somewhere in the[models](../applications/application-packages.html) directory tree, and the same directory must also contain `myLargeConstant.json.lz4` with a tensor as compressed json.

```
model example {

    # All inputs that are not scalar (aka 0-dimensional tensor) must be declared
    inputs {
        input1 tensor(name{},x[3])
        input2 tensor(x[3])
    }

    constants {
        constant(constant1) tensor(x[3]):{{x:0}:0.5, {x:1}:1.5, {x:2}:2.5}
        constant(constant2): 3.0
        constant(myLargeConstant) tensor(x[10000]): file:myLargeConstant.json.lz4
    }

    function foo1() {
        expression: reduce(sum(input1 * input2, name) * constant1, max, x) * constant2
    }

    function foo2() {
        expression: reduce(sum(input1 * input2, name) * constant(constant1asLarge), max, x) * constant2
    }

}
```

This makes the model _example_ available with the functions _foo1_ and _foo2_.

 Copyright © 2025 - [Cookie Preferences](#)

