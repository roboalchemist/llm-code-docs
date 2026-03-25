# Source: https://docs.startree.ai/thirdeye/operators.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Each node in a detection pipeline uses an operator. Operators have a determined goal, inputs and outputs, and a set of parameters to customize their behavior.

The operator type is given in the JSON configuration.

```json  theme={null}
{
  "name": "my-detection-rule",
  ...
  "template": {
    "nodes": [
      {
        "name": "root",
        "type": "AnomalyDetector",    # THE OPERATOR TYPE
        "params": {
          ...
        }, 
        ...
      }
      ...  
      ]
  }
```

This section describes all the operators.

Built with [Mintlify](https://mintlify.com).
