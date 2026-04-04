# Source: https://mui.com/x/api/data-grid/grid-charts-panel.md

# GridChartsPanel API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [DataGrid](/x/react-data-grid/#community-version-free-forever)
- [DataGridPro](/x/react-data-grid/#pro-version)
- [DataGridPremium](/x/react-data-grid/#premium-version)

## Import

```jsx
import { GridChartsPanel } from '@mui/x-data-grid-premium/components';
// or
import { GridChartsPanel } from '@mui/x-data-grid-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| getColumnName | `function(field: string) => string \| undefined` | - | No |  |
| schema | `object` | `{}` | No |  |

> **Note**: The `ref` is forwarded to the root element (GridRoot).

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-data-grid-premium/src/components/chartsPanel/GridChartsPanel.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-data-grid-premium/src/components/chartsPanel/GridChartsPanel.tsx)