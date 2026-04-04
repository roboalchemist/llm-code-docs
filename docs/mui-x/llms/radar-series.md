# Source: https://mui.com/x/api/charts/radar-series.md

# RadarSeries API

## Import

```jsx
import { RadarSeries } from '@mui/x-charts-premium'
// or
import { RadarSeries } from '@mui/x-charts-pro'
// or
import { RadarSeries } from '@mui/x-charts'
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| data | `number[]` | - | Yes |  |
| type | `'radar'` | - | Yes |  |
| color | `string` | - | No |  |
| colorGetter | `(data: ColorCallbackValue<TValue>) => string` | - | No |  |
| fillArea | `boolean` | - | No |  |
| hideMark | `boolean` | - | No |  |
| highlightScope | `HighlightScope` | - | No |  |
| id | `SeriesId` | - | No |  |
| label | `string \| ((location: 'tooltip' \| 'legend') => string)` | - | No |  |
| labelMarkType | `ChartsLabelMarkType` | - | No |  |
| valueFormatter | `SeriesValueFormatter<TValue>` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.