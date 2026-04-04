# Source: https://docs.prefect.io/integrations/prefect-aws/api-ref/prefect_aws-utilities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# utilities

# `prefect_aws.utilities`

Utilities for working with AWS services.

## Functions

### `hash_collection` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/utilities.py#L8" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
hash_collection(collection) -> int
```

Use visit\_collection to transform and hash a collection.

**Args:**

* `collection`: The collection to hash.

**Returns:**

* The hash of the transformed collection.

### `ensure_path_exists` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/utilities.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ensure_path_exists(doc: Union[Dict, List], path: List[str])
```

Ensures the path exists in the document, creating empty dictionaries or lists as
needed.

**Args:**

* `doc`: The current level of the document or sub-document.
* `path`: The remaining path parts to ensure exist.

### `assemble_document_for_patches` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/utilities.py#L73" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
assemble_document_for_patches(patches)
```

Assembles an initial document that can successfully accept the given JSON Patch
operations.

**Args:**

* `patches`: A list of JSON Patch operations.

**Returns:**

* An initial document structured to accept the patches.

Example:

```python  theme={null}
patches = [
    {"op": "replace", "path": "/name", "value": "Jane"},
    {"op": "add", "path": "/contact/address", "value": "123 Main St"},
    {"op": "remove", "path": "/age"}
]

initial_document = assemble_document_for_patches(patches)

#output
{
    "name": {},
    "contact": {},
    "age": {}
}
```


Built with [Mintlify](https://mintlify.com).