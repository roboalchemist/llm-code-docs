# Source: https://docs.mage.ai/development/blocks/transformers/templates.md

# Source: https://docs.mage.ai/development/blocks/sensors/templates.md

# Source: https://docs.mage.ai/development/blocks/data_loaders/templates.md

# Source: https://docs.mage.ai/development/blocks/data_exporters/templates.md

# Source: https://docs.mage.ai/development/blocks/conditionals/templates.md

# Source: https://docs.mage.ai/development/blocks/callbacks/templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Callback templates

## Base

```python  theme={"system"}
if 'callback' not in globals():
    from mage_ai.data_preparation.decorators import callback


@callback('success')
def success_callback(**kwargs):
    pass


@callback('failure')
def failure_callback(**kwargs):
    pass
```


Built with [Mintlify](https://mintlify.com).