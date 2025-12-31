# Source: https://mui.com/x/api/charts/pie-arc.md

# PieArc API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Pie](/x/react-charts/pie/)
- [Charts - Pie demos](/x/react-charts/pie-demo/)

## Import

```jsx
import { PieArc } from '@mui/x-charts/PieChart';
// or
import { PieArc } from '@mui/x-charts';
// or
import { PieArc } from '@mui/x-charts-pro';
// or
import { PieArc } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| skipAnimation | `bool` | - | No |  |
| skipInteraction | `bool` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## CSS

### Rule name

| Global class | Rule name | Description |
|--------------|-----------|-------------|
| - | faded | Styles applied to the root element when faded. |
| - | focusIndicator | Styles applied to the focus indicator element. |
| - | highlighted | Styles applied to the root element when highlighted. |
| - | root | Styles applied to the root element. |
| - | series | Styles applied to the root element for a specified series.
Needs to be suffixed with the series ID: `.${pieArcClasses.series}-${seriesId}`. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/PieChart/PieArc.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/PieChart/PieArc.tsx)