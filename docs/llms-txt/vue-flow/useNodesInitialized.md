# Source: https://vueflow.dev/typedocs/functions/useNodesInitialized.md

---
url: /typedocs/functions/useNodesInitialized.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useNodesInitialized()

> **useNodesInitialized**(`options`): `ComputedRef`<`boolean`>

Composable for getting the initialized state of all nodes.

When a new node is added to the graph, it is not immediately initialized.
That's because the node's bounds are not yet known.
This composable will return false and then true when all nodes are initialized, i.e. when their bounds are known.

## Parameters

• **options**: `UseNodesInitializedOptions` = `...`

Options

## Returns

`ComputedRef`<`boolean`>

boolean indicating whether all nodes are initialized
