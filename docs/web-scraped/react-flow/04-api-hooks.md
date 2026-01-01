# API Reference: Hooks

**Source:** https://reactflow.dev/api-reference/hooks

## useNodes

Get the current nodes array.

```typescript
const nodes = useNodes();
```

## useEdges

Get the current edges array.

```typescript
const edges = useEdges();
```

## useReactFlow

Access the React Flow instance for programmatic control.

```typescript
const instance = useReactFlow();

// Available methods
instance.getNodes();
instance.getEdges();
instance.setNodes(nodes);
instance.setEdges(edges);
instance.deleteElements({ nodes, edges });
instance.getNode(nodeId);
instance.getEdge(edgeId);
instance.setCenter(x, y, zoomOptions);
instance.fitView(fitViewOptions);
instance.project(position);
```

## useOnSelectionChange

Listen to selection changes.

```typescript
useOnSelectionChange({
  onChange: ({ nodes, edges }) => {
    console.log('Selected:', nodes, edges);
  },
});
```

## useNodesData

Get data for specific nodes.

```typescript
const data = useNodesData(nodeIds);
```

## useEdgesData

Get data for specific edges.

```typescript
const data = useEdgesData(edgeIds);
```

## useViewport

Get current viewport state.

```typescript
const { x, y, zoom } = useViewport();
```

## useStore

Access the internal Zustand store directly.

```typescript
const store = useStore();
const nodes = store.getState().nodes;
```

## useConnection

Get the current connection being made.

```typescript
const connection = useConnection();
```

---
