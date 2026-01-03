# Utilities Reference

**Source:** https://reactflow.dev/api-reference/utilities

## Node Utilities

### applyNodeChanges

Apply node changes to your node array.

```typescript
import { applyNodeChanges, NodeChange } from '@xyflow/react';

const updatedNodes = applyNodeChanges(changes, nodes);
```

### getConnectedEdges

Get all edges connected to a node.

```typescript
import { getConnectedEdges } from '@xyflow/react';

const edges = getConnectedEdges([node], allEdges);
```

### getOutgoers

Get all connected downstream nodes.

```typescript
import { getOutgoers } from '@xyflow/react';

const outgoers = getOutgoers(node, nodes, edges);
```

### getIncomers

Get all connected upstream nodes.

```typescript
import { getIncomers } from '@xyflow/react';

const incomers = getIncomers(node, nodes, edges);
```

### nodeToString

Convert node to string representation.

```typescript
import { nodeToString } from '@xyflow/react';

const str = nodeToString(node);
```

## Edge Utilities

### applyEdgeChanges

Apply edge changes to your edge array.

```typescript
import { applyEdgeChanges, EdgeChange } from '@xyflow/react';

const updatedEdges = applyEdgeChanges(changes, edges);
```

### addEdge

Add a new edge to the edge array.

```typescript
import { addEdge, Connection } from '@xyflow/react';

const newEdges = addEdge(connection, edges);
```

### deleteElements

Delete nodes and edges.

```typescript
import { deleteElements } from '@xyflow/react';

const { nodes: newNodes, edges: newEdges } = deleteElements(
  { nodes: nodesToDelete, edges: edgesToDelete },
  nodes,
  edges
);
```

## Path Utilities

### getBezierPath

Calculate bezier curve path.

```typescript
import { getBezierPath } from '@xyflow/react';

const [path, labelX, labelY] = getBezierPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

### getSmoothedPath

Calculate smoothed path.

```typescript
import { getSmoothedPath } from '@xyflow/react';

const [path, labelX, labelY] = getSmoothedPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

### getStraightPath

Calculate straight path.

```typescript
import { getStraightPath } from '@xyflow/react';

const [path, labelX, labelY] = getStraightPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

## Layout Utilities

### useLayouting

Hook for applying layout algorithms.

```typescript
import { useLayouting } from '@xyflow/react';

const { run } = useLayouting();

// Apply layout to current nodes
run({ nodes, edges });
```

---
