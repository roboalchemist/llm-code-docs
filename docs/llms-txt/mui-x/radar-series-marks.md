# Source: https://mui.com/x/api/charts/radar-series-marks.md

# RadarSeriesMarks API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Radar](/x/react-charts/radar/)

## Import

```jsx
import { RadarSeriesMarks } from '@mui/x-charts/RadarChart';
// or
import { RadarSeriesMarks } from '@mui/x-charts';
// or
import { RadarSeriesMarks } from '@mui/x-charts-pro';
// or
import { RadarSeriesMarks } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| classes | `object` | - | No | Override or extend the styles applied to the component. |
| onItemClick | `function(event: React.MouseEvent<SVGPathElement, MouseEvent>, radarItemIdentifier: RadarItemIdentifier) => void` | - | No |  |
| seriesId | `string` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/RadarChart/RadarSeriesPlot/RadarSeriesMarks.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/RadarChart/RadarSeriesPlot/RadarSeriesMarks.tsx)