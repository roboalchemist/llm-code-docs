# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcountull.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcountull.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcountull.md

# DISTINCTCOUNTULL

The [UltraLogLog Sketch](https://arxiv.org/abs/2308.16862) from Dynatrace is a variant of *HyperLogLog* and is used for approximate distinct counts. The UltraLogLog sketch shares many of the same properties of a typical HyperLogLog sketch but requires less space and also provides a simpler and faster estimator.

Pinot uses an production-ready Java implementation available in [Hash4j](https://github.com/dynatrace-oss/hash4j/tree/main) available under the Apache license.

For exact distinct counting, see [DISTINCTCOUNT](https://github.com/pinot-contrib/pinot-docs/blob/latest/configuration-reference/functions/distinctcount.md).

## Signature

> distinctCountULL(**\<ullSketchColumn>, \<ullSketchPrecision>**) -> Long

* `ullSketchColumn` (required): Name of the column to aggregate on.
* `ullSketchPrecision` (optional): p which is the precision parameter, which controls both the size and accuracy of the sketch. If not supplied, the Helix default is used.

## Usage examples

These examples are based on the [Batch Quick Start](https://github.com/pinot-contrib/pinot-docs/blob/latest/basics/getting-started/quick-start.md#batch).

```
select distinctCountULL(teamID) AS value
from baseballStats 
```

| value |
| ----- |
| 150   |

```
select distinctCountULL(teamID, 14) AS value
from baseballStats 
```

| value |
| ----- |
| 149   |
