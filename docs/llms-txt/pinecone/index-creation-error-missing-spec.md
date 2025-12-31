# Source: https://docs.pinecone.io/troubleshooting/index-creation-error-missing-spec.md

# Index creation error - missing spec parameter

## Problem

Using the [new API](/reference/api), creating an index requires passing appropriate values into the `spec` parameter. Without this `spec` parameter, the `create_index` method raises the following error:

```console console theme={null}
TypeError: Pinecone.create_index() missing 1 required positional argument: 'spec'
```

## Solution

Set the `spec` parameter. For guidance on how to set this parameter, see [Create an index](/guides/index-data/create-an-index#create-a-serverless-index).
