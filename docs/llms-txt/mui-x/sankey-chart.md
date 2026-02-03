# Source: https://mui.com/x/api/charts/sankey-chart.md

# SankeyChart API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- Charts - Export
- Charts - Sankey 🧪

## Import

```jsx
import { SankeyChart } from '@mui/x-charts-pro/SankeyChart';
// or
import { SankeyChart } from '@mui/x-charts-pro';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| series | `object` | - | Yes |  |
| classes | `object` | - | No | Override or extend the styles applied to the component. |
| colors | `Array<string> \| func` | `rainbowSurgePalette` | No |  |
| experimentalFeatures | `{ preferStrictDomainInLineCharts?: bool }` | - | No |  |
| height | `number` | - | No |  |
| highlightedItem | `{ nodeId: number \| string, seriesId: number \| string, subType: 'node', type: 'sankey' } \| { seriesId: number \| string, sourceId: number \| string, subType: 'link', targetId: number \| string, type: 'sankey' }` | - | No |  |
| id | `string` | - | No |  |
| loading | `bool` | `false` | No |  |
| localeText | `object` | - | No |  |
| margin | `number \| { bottom?: number, left?: number, right?: number, top?: number }` | - | No |  |
| onHighlightChange | `function(highlightedItem: SankeyHighlightItemData \| null) => void` | - | No |  |
| onLinkClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, link: SankeyLinkIdentifierWithData) => void` | - | No |  |
| onNodeClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, node: SankeyNodeIdentifierWithData) => void` | - | No |  |
| onTooltipItemChange | `function(tooltipItem: SeriesItemIdentifier<TSeries> \| null) => void` | - | No |  |
| slotProps | `object` | `{}` | No |  |
| slots | `object` | `{}` | No |  |
| tooltipItem | `{ nodeId: number \| string, seriesId: number \| string, subType: 'node', type: 'sankey' } \| { seriesId: number \| string, sourceId: number \| string, subType: 'link', targetId: number \| string, type: 'sankey' }` | - | No |  |
| width | `number` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Slots

| Name | Default | Class | Description |
|------|---------|-------|-------------|
| baseButton | `undefined` | - |  |
| baseIconButton | `undefined` | - |  |
| loadingOverlay | `ChartsLoadingOverlay` | - | Overlay component rendered when the chart is in a loading state. |
| noDataOverlay | `ChartsNoDataOverlay` | - | Overlay component rendered when the chart has no data to display. |
| toolbar | `ChartsToolbar` | - | Custom component for the toolbar. |
| tooltip | `ChartsTooltipRoot` | - | Custom component for the tooltip popper. |

## CSS

### Rule name

| Global class | Rule name | Description |
|--------------|-----------|-------------|
| - | linkLabels | Styles applied to the link label container. |
| - | links | Styles applied to the links container. |
| - | nodeLabels | Styles applied to the node label container. |
| - | nodes | Styles applied to the nodes container. |
| - | root | Styles applied to the root element. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts-pro/src/SankeyChart/SankeyChart.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts-pro/src/SankeyChart/SankeyChart.tsx)