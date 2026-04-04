# Source: https://mui.com/x/api/data-grid/grid-charts-renderer-proxy.md

# GridChartsRendererProxy API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [DataGrid](/x/react-data-grid/#community-version-free-forever)
- [DataGridPro](/x/react-data-grid/#pro-version)
- [DataGridPremium](/x/react-data-grid/#premium-version)

## Import

```jsx
import { GridChartsRendererProxy } from '@mui/x-data-grid-premium/context';
// or
import { GridChartsRendererProxy } from '@mui/x-data-grid-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `string` | - | Yes |  |
| renderer | `func` | - | Yes |  |
| label | `string` | - | No |  |
| onRender | `func` | - | No |  |

> **Note**: The `ref` is forwarded to the root element (GridRoot).

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-data-grid-premium/src/context/GridChartsRendererProxy.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-data-grid-premium/src/context/GridChartsRendererProxy.tsx)