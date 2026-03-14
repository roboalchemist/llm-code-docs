# Source: https://docs.mage.ai/design/blocks/scratchpad.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scratchpad

> Use these blocks to experiment and write throw away code.

Scratchpad blocks aren't used when executing a pipeline.

![Blocks](https://mage-ai.github.io/assets/blocks/scratchpad.gif)

## Getting data from other blocks

If you want to read the output data from another block, use the following sample code:

```python  theme={"system"}
from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('pipelined_uuid', 'block_uuid', 'output_0')
```

* Change the value of `pipelined_uuid` to match your current pipeline UUID.
* Change the value of `block_uuid` to match the UUID of the block you want to read data from.


Built with [Mintlify](https://mintlify.com).