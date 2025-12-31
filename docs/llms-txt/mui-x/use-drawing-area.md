# Source: https://mui.com/x/react-charts/hooks/use-drawing-area.md

---
title: Charts - useDrawingArea
productId: x-charts
---

# useDrawingArea

Access the chart's drawing area dimensions and coordinates.

The `useDrawingArea` hook provides access to the chart's drawing area dimensions and positioning, which is useful for positioning custom elements within the chart area.

## Usage

```js
import { useDrawingArea } from '@mui/x-charts/hooks';

function CustomOverlay() {
  const { left, right, top, bottom, width, height } = useDrawingArea();
  // Position custom elements within the chart area
}
```

This demo displays:

- A red dashed border showing the exact drawing area boundaries
- Corner markers at each corner of the drawing area
- A center cross marking the middle of the drawing area
- Real-time dimension and center point information

```tsx
import { useDrawingArea } from '@mui/x-charts/hooks';
import { LineChart } from '@mui/x-charts/LineChart';

function CustomOverlay() {
  const { left, top, width, height } = useDrawingArea();

  return (
    <g>
      {/* Drawing area border */}
      <rect
        x={left}
        y={top}
        width={width}
        height={height}
        fill="transparent"
        stroke="red"
        strokeWidth={2}
        strokeDasharray="5,5"
      />

      {/* Corner markers */}
      <circle cx={left} cy={top} r={4} fill="red" />
      <circle cx={width + left} cy={top} r={4} fill="red" />
      <circle cx={width + left} cy={top + height} r={4} fill="red" />
      <circle cx={left} cy={top + height} r={4} fill="red" />

      {/* Center cross */}
      <g stroke="red" strokeWidth={1}>
        <line
          x1={left + width / 2 - 10}
          y1={top + height / 2}
          x2={left + width / 2 + 10}
          y2={top + height / 2}
        />
        <line
          x1={left + width / 2}
          y1={top + height / 2 - 10}
          x2={left + width / 2}
          y2={top + height / 2 + 10}
        />
      </g>

      {/* Info text */}
      <text
        x={left + 10}
        y={top + 20}
        fontSize="12"
        fill="red"
        fontFamily="monospace"
      >
        Drawing Area: {width}×{height}
      </text>
      <text
        x={left + 10}
        y={top + 35}
        fontSize="12"
        fill="red"
        fontFamily="monospace"
      >
        Center: ({left + width / 2}, {top + height / 2})
      </text>
    </g>
  );
}

export default function UseDrawingArea() {
  return (
    <LineChart
      dataset={[
        { x: 1, y: 2 },
        { x: 2, y: 5 },
        { x: 3, y: 3 },
        { x: 4, y: 8 },
        { x: 5, y: 1 },
        { x: 6, y: 7 },
      ]}
      xAxis={[{ dataKey: 'x', label: 'X Axis' }]}
      yAxis={[{ label: 'Y Axis' }]}
      series={[{ dataKey: 'y', label: 'Sample Data', color: '#8884d8' }]}
      height={400}
      hideLegend
    >
      <CustomOverlay />
    </LineChart>
  );
}

```

## Return value

The hook returns an object with the following properties:

| Property | Type     | Description                                                        |
| :------- | :------- | :----------------------------------------------------------------- |
| `left`   | `number` | The gap between the left border of the SVG and the drawing area.   |
| `right`  | `number` | The gap between the right border of the SVG and the drawing area.  |
| `top`    | `number` | The gap between the top border of the SVG and the drawing area.    |
| `bottom` | `number` | The gap between the bottom border of the SVG and the drawing area. |
| `width`  | `number` | The width of the drawing area.                                     |
| `height` | `number` | The height of the drawing area.                                    |

## Caveats

This hook must be used within a chart context. See the [hooks overview](/x/react-charts/hooks/) for more information about proper usage.
