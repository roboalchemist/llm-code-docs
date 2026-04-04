# Source: https://nx.dev/docs/reference/devkit/reverse.md

▸ **reverse**(`graph`): [`ProjectGraph`](/docs/reference/devkit/ProjectGraph)

Returns a new project graph where all the edges are reversed.

For instance, if project A depends on B, in the reversed graph
B will depend on A.

#### Parameters

| Name | Type |
| :------ | :------ |
| `graph` | [`ProjectGraph`](/docs/reference/devkit/ProjectGraph) |

#### Returns

[`ProjectGraph`](/docs/reference/devkit/ProjectGraph)
