# Source: https://mui.com/x/api/data-grid/grid-row-order-change-params.md

# GridRowOrderChangeParams API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Flat row reordering](/x/react-data-grid/row-ordering/#implementing-row-reordering)

## Import

```jsx
import { GridRowOrderChangeParams } from '@mui/x-data-grid-premium'
// or
import { GridRowOrderChangeParams } from '@mui/x-data-grid-pro'
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| newParent | `GridRowId \| null` | - | Yes |  |
| oldIndex | `number` | - | Yes |  |
| oldParent | `GridRowId \| null` | - | Yes |  |
| row | `GridRowModel` | - | Yes |  |
| targetIndex | `number` | - | Yes |  |

> **Note**: The `ref` is forwarded to the root element.