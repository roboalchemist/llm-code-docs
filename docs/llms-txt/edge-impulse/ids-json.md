# Source: https://docs.edgeimpulse.com/tools/specifications/files/ids-json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ids.json

The `ids.json` file is passed to [custom AI labeling blocks](/studio/organizations/custom-blocks/custom-ai-labeling-blocks). It lists the data sample IDs to operate on as integers.

## File structure

```json  theme={"system"}
{
    "ids": [ <id>, <id>, ..., <id> ]
}
```

## File example

```json  theme={"system"}
{
    "ids": [ 1440653288, 1440653283, ..., 1440653252 ]
}
```


Built with [Mintlify](https://mintlify.com).