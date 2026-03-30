# Source: https://docs.edgeimpulse.com/tools/specifications/files/ei-metadata-json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ei-metadata.json

The `ei-metadata.json` file can be used to update metadata for a clinical dataset data item after being processed by a [custom transformation block](/studio/organizations/custom-blocks/custom-transformation-blocks).

## File structure

```typescript  theme={"system"}
interface TransformBlockMetadataFile {
    version: 1;
    action: 'replace' | 'add' | 'replace-checks';
    metadata: { [ k: string ]: string };
}
```

## File example

```json  theme={"system"}
{
    'version': 1,
    'action': 'add',
    'metadata': {
        'now': '1734721115539'
    }
}
```

## Action definitions

`add`: the new metadata key-value pairs will be added to the existing metadata.

`replace`: the existing metadata will be deleted and the new metadata key-value pairs will be added.

`replace-checks`: the existing metadata keys that begin with `ei_check` will be deleted and the new metadata key-value pairs will be added.


Built with [Mintlify](https://mintlify.com).