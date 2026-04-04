# Source: https://mui.com/x/api/charts/charts-wrapper.md

# ChartsWrapper API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Pie](/x/react-charts/pie/)
- [Charts - Radar](/x/react-charts/radar/)
- [Charts - Scatter](/x/react-charts/scatter/)

## Import

```jsx
import { ChartsWrapper } from '@mui/x-charts/ChartsWrapper';
// or
import { ChartsWrapper } from '@mui/x-charts';
// or
import { ChartsWrapper } from '@mui/x-charts-pro';
// or
import { ChartsWrapper } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extendVertically | `bool` | ``false` if the `height` prop is set. And `true` otherwise.` | No |  |
| hideLegend | `bool` | `false` | No |  |
| legendDirection | `'horizontal' \| 'vertical'` | `'horizontal'` | No |  |
| legendPosition | `{ horizontal?: 'center' \| 'end' \| 'start', vertical?: 'bottom' \| 'middle' \| 'top' }` | `{ horizontal: 'center', vertical: 'bottom' }` | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/ChartsWrapper/ChartsWrapper.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/ChartsWrapper/ChartsWrapper.tsx)