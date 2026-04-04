# API Reference: Components

**Source:** https://reactflow.dev/api-reference/components

## ReactFlow

The main component that wraps your entire flow diagram.

### Props

```typescript
interface ReactFlowProps {
  nodes: Node[];
  edges: Edge[];
  onNodesChange?: (changes: NodeChange[]) => void;
  onEdgesChange?: (changes: EdgeChange[]) => void;
  onConnect?: (connection: Connection) => void;
  onConnectStart?: (event: ReactMouseEvent, handle: Handle) => void;
  onConnectEnd?: (event: React.MouseEvent) => void;
  nodeTypes?: Record<string, ComponentType<NodeProps>>;
  edgeTypes?: Record<string, ComponentType<EdgeProps>>;
  fitView?: boolean;
  fitViewOptions?: FitViewOptions;
  attributionPosition?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

### Example

```javascript
<ReactFlow
  nodes={nodes}
  edges={edges}
  onNodesChange={onNodesChange}
  onEdgesChange={onEdgesChange}
  onConnect={onConnect}
  fitView
>
  <Background />
  <Controls />
</ReactFlow>
```

## Background

Renders a background pattern behind the flow.

```typescript
interface BackgroundProps {
  color?: string;
  pattern?: 'dots' | 'lines' | 'cross';
  size?: number;
  gap?: number;
  variant?: 'dots' | 'cross' | 'lines';
}
```

## Controls

Renders UI controls for zooming and fitting the view.

```typescript
interface ControlsProps {
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  showZoom?: boolean;
  showFitView?: boolean;
  showInteractive?: boolean;
  fitViewOptions?: FitViewOptions;
  onZoomIn?: () => void;
  onZoomOut?: () => void;
  onFitView?: () => void;
}
```

## MiniMap

Renders a miniature version of the entire graph.

```typescript
interface MiniMapProps {
  nodeColor?: string | ((node: Node) => string);
  nodeStrokeColor?: string | ((node: Node) => string);
  maskColor?: string;
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
}
```

## NodeToolbar

Displays a toolbar when a node is selected.

```typescript
interface NodeToolbarProps {
  nodeId?: string | string[];
  isVisible?: boolean;
  position?: Position;
  offset?: number;
}
```

## NodeResizer

Allows resizing nodes.

```typescript
interface NodeResizerProps {
  minWidth?: number;
  minHeight?: number;
  maxWidth?: number;
  maxHeight?: number;
  isVisible?: boolean;
  handleClassName?: string;
}
```

---
