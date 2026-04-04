# Types Reference

**Source:** https://reactflow.dev/api-reference/types

## Core Types

### Node

```typescript
interface Node<T = any> {
  id: string;
  position: XYPosition;
  data: T;
  type?: string;
  selected?: boolean;
  dragging?: boolean;
  isConnectable?: boolean | IsConnectableFunc;
  dragHandle?: string;
  parentNode?: string;
  extent?: 'parent' | Extent;
  expandParent?: boolean;
  width?: number;
  height?: number;
  style?: CSSProperties;
  className?: string;
}
```

### Edge

```typescript
interface Edge<T = any> {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string | null;
  targetHandle?: string | null;
  type?: string;
  data?: T;
  animated?: boolean;
  hidden?: boolean;
  style?: CSSProperties;
  className?: string;
  zIndex?: number;
  ariaLabel?: string;
  interactionWidth?: number;
}
```

### Connection

```typescript
interface Connection {
  source: string;
  sourceHandle: string | null;
  target: string;
  targetHandle: string | null;
}
```

### XYPosition

```typescript
interface XYPosition {
  x: number;
  y: number;
}
```

### Viewport

```typescript
interface Viewport {
  x: number;
  y: number;
  zoom: number;
}
```

## Change Types

### NodeChange

```typescript
type NodeChange =
  | NodePositionChange
  | NodeDimensionsChange
  | NodeSelectionChange
  | NodeRemoveChange
  | NodeResetChange;
```

### EdgeChange

```typescript
type EdgeChange =
  | EdgeSelectionChange
  | EdgeRemoveChange
  | EdgeResetChange;
```

---
