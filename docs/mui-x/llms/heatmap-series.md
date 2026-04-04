# Source: https://mui.com/x/api/charts/heatmap-series.md

# HeatmapSeries API

## Import

```jsx
import { HeatmapSeries } from '@mui/x-charts-premium'
// or
import { HeatmapSeries } from '@mui/x-charts-pro'
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `'heatmap'` | - | Yes |  |
| data | `readonly HeatmapValueType[]` | - | No |  |
| dataKey | `string` | - | No |  |
| highlightScope | `HighlightScope` | - | No |  |
| id | `SeriesId` | - | No |  |
| label | `string \| ((location: 'tooltip' \| 'legend') => string)` | - | No |  |
| labelMarkType | `ChartsLabelMarkType` | - | No |  |
| valueFormatter | `SeriesValueFormatter<TValue>` | - | No |  |
| xAxisId | `AxisId` | - | No |  |
| yAxisId | `AxisId` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.