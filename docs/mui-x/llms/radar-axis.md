# Source: https://mui.com/x/api/charts/radar-axis.md

# RadarAxis API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Radar](/x/react-charts/radar/)

## Import

```jsx
import { RadarAxis } from '@mui/x-charts/RadarChart';
// or
import { RadarAxis } from '@mui/x-charts';
// or
import { RadarAxis } from '@mui/x-charts-pro';
// or
import { RadarAxis } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| angle | `number` | - | No |  |
| classes | `object` | - | No | Override or extend the styles applied to the component. |
| divisions | `number` | `1` | No |  |
| dominantBaseline | `'alphabetic' \| 'auto' \| 'central' \| 'hanging' \| 'ideographic' \| 'inherit' \| 'mathematical' \| 'middle' \| 'no-change' \| 'reset-size' \| 'text-after-edge' \| 'text-before-edge' \| 'use-script' \| func` | - | No |  |
| labelOrientation | `'horizontal' \| 'rotated'` | `'horizontal'` | No |  |
| metric | `string` | - | No |  |
| textAnchor | `'end' \| 'inherit' \| 'middle' \| 'start' \| func` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## CSS

### Rule name

| Global class | Rule name | Description |
|--------------|-----------|-------------|
| - | label | Styles applied to every label element. |
| - | line | Styles applied to the line element. |
| - | root | Styles applied to the root element. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/RadarChart/RadarAxis/RadarAxis.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/RadarChart/RadarAxis/RadarAxis.tsx)