# Source: https://mui.com/x/react-charts/hooks/use-scale.md

---
title: Charts - useScale
productId: x-charts
---

# useScale

Access D3 scale functions for coordinate transformations.

The scale hooks provide access to D3 scale functions that can be used to convert data values to pixel coordinates within the chart.
Scale hooks accept an axis id as a parameter.
If provided, the hook returns the scale of the associated axis.
Otherwise it returns the scale of the default axis.

## Cartesian charts

Access the x-axis and y-axis scale function.

```js
import { useXScale, useYScale } from '@mui/x-charts/hooks';

function CustomComponent() {
  const xScale = useXScale(); // Default x-axis
  const xScaleById = useXScale('customAxisId'); // Specific x-axis
  const yScale = useYScale(); // Default y-axis
  const yScaleById = useYScale('leftAxis'); // Specific y-axis

  // Convert data value to pixel coordinate
  const xCoord = xScale(dataValue);
  const yCoord = yScale(dataValue);
}
```

## Polar charts

Access the rotation and radius scale functions for polar charts.

```js
import { useRotationScale, useRadiusScale } from '@mui/x-charts/hooks';

function CustomComponent() {
  const rotationScale = useRotationScale();
  const rotationScaleById = useRotationScale('rotationAxisId');
  const radiusScale = useRadiusScale();
  const radiusScaleById = useRadiusScale('radiusAxisId');
}
```

## Utility function

### getValueToPositionMapper

A utility function that returns a mapper function for converting values to positions, with special handling for band scales.

```js
import { getValueToPositionMapper } from '@mui/x-charts/hooks';

function CustomComponent() {
  const xScale = useXScale();
  const xMapper = getValueToPositionMapper(xScale);

  // For band scales, this centers the position within the band
  const position = xMapper(value);
}
```

## Usage example

This example shows how to use scale functions to position custom elements:

```tsx
import {
  useXScale,
  useYScale,
  getValueToPositionMapper,
  useLineSeries,
  useXAxis,
} from '@mui/x-charts/hooks';
import { LineChart } from '@mui/x-charts/LineChart';

const data = [
  { x: 1, y: 2 },
  { x: 2, y: 5 },
  { x: 3, y: 3 },
  { x: 4, y: 8 },
  { x: 5, y: 1 },
];

function CustomDataPoints() {
  const xScale = useXScale();
  const yScale = useYScale();
  const series = useLineSeries();
  const xAxis = useXAxis();

  // Use the value-to-position mapper to handle different scale types
  const xMapper = getValueToPositionMapper(xScale);
  const yMapper = getValueToPositionMapper(yScale);

  return (
    <g>
      {series.map((s) =>
        s.data.map((point, index) => {
          const x = xMapper(xAxis.data?.[index]);
          const y = yMapper(point);

          return (
            <g key={index}>
              {/* Custom data point */}
              <circle
                cx={x}
                cy={y}
                r={6}
                fill="red"
                stroke="white"
                strokeWidth={2}
              />
              {/* Value label */}
              <text
                x={x}
                y={y - 10}
                textAnchor="middle"
                fontSize="10"
                fill="red"
                fontWeight="bold"
              >
                ({index + 1}, {point})
              </text>
            </g>
          );
        }),
      )}
    </g>
  );
}

export default function UseScale() {
  return (
    <LineChart
      dataset={data}
      xAxis={[
        {
          dataKey: 'x',
          label: 'X Values',
        },
      ]}
      yAxis={[
        {
          dataKey: 'y',
          label: 'Y Values',
        },
      ]}
      series={[
        {
          dataKey: 'y',
          label: 'Sample Data',
          color: '#8884d8',
        },
      ]}
    >
      <CustomDataPoints />
    </LineChart>
  );
}

```

## Caveats

These hooks must be used within a chart context. See the [hooks overview](/x/react-charts/hooks/) for more information about proper usage.
