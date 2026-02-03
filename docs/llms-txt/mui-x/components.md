# Source: https://mui.com/x/react-charts/components.md

---
title: Charts - Custom components
productId: x-charts
components: ChartsClipPath, ChartsSurface
---

# Charts - Custom components

Create custom chart components using the provided hooks.

The MUI X Charts package provides a set of hooks to aid in the creation of custom Chart components.

## Interact with dimensions

The following sections detail how to handle the various dimensions when building custom Charts, including height, width, margins, scale, and series data.

### Drawing area

Drawing area refers to the space available to plot data (such as scatter points, lines, or pie arcs).
Charts dimensions are defined by the following props:

- `height` and `width` for the SVG size; if not provided, these values are derived from the container
- `margin` for the space between the SVG border and the axes or the drawing area
- The axes dimension properties (`xAxis[].height` and `yAxis[].width`) that add extra space to draw axes

The `margin` is used to leave space for extra elements, or to let data items overflow the drawing area.

You can use the `useDrawingArea()` hook in the Chart subcomponents to get the coordinates of the drawing area:

```jsx
import { useDrawingArea } from '@mui/x-charts';

const { left, top, width, height } = useDrawingArea();
```

```tsx
import * as React from 'react';
import { styled } from '@mui/material/styles';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { LinePlot } from '@mui/x-charts/LineChart';
import { useDrawingArea } from '@mui/x-charts/hooks';

const StyledPath = styled('path')(({ theme }) => ({
  fill: 'none',
  stroke: theme.palette.text.primary,
  shapeRendering: 'crispEdges',
  strokeWidth: 1,
  pointerEvents: 'none',
}));

const StyledText = styled('text')(({ theme }) => ({
  stroke: 'none',
  fill: theme.palette.text.primary,
  shapeRendering: 'crispEdges',
}));

function DrawingAreaBox() {
  const { left, top, width, height } = useDrawingArea();
  return (
    <React.Fragment>
      <StyledPath
        d={`M ${left} ${top} l ${width} 0 l 0 ${height} l -${width} 0 Z`}
      />
      <circle cx={left} cy={top} r={3} style={{ fill: 'red' }} />
      <circle cx={left + width} cy={top + height} r={3} style={{ fill: 'red' }} />
      <StyledText
        x={left}
        y={top}
        textAnchor="start"
        dominantBaseline="text-after-edge"
      >
        ({left},{top})
      </StyledText>
      <StyledText
        x={left + width}
        y={top + height}
        textAnchor="end"
        dominantBaseline="text-before-edge"
      >
        ({left + width},{top + height})
      </StyledText>
    </React.Fragment>
  );
}
export default function BasicScaleDemo() {
  return (
    <ChartContainer
      height={300}
      series={[
        {
          type: 'line',
          data: [13, 13, 54, 651, 657, 987, 64, 654, 954, 654, 897, 84],
        },
      ]}
      xAxis={[{ data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], position: 'none' }]}
      yAxis={[{ position: 'none' }]}
    >
      <LinePlot />
      <DrawingAreaBox />
    </ChartContainer>
  );
}

```

### Scales

Some Charts, such as Line, Bar, and Scatter, do a mapping between their series' data and the SVG coordinates.

For example, a line chart series with a value of $36,725 on the 6th of December 2022 could be mapped to coordinates (628, 514).
This operation can also be reversed:
The coordinate `x=628` would be associated with the 6th of December 2022 and `y=514` would be associated with the value $36,725.

These mappings depend on the dimensions of the SVG and the drawing area.
They also depend on [axis properties](/x/react-charts/axis/) such as the scale (linear, log, square root) and min/max values.
All of this data is available in the [`d3-scale` objects](https://github.com/d3/d3-scale).

You can use `useXScale()` and `useYScale()` to access these scales.
Both accept a number or a string.
Use a number to select the index of the axis to be used, or a string to select an axis by its ID.

The scale object is generated so that it maps values to SVG coordinates.
The drawing area is automatically accounted for.

#### Value to coordinate

The default `d3-scale` method maps from values to coordinates.
For example, you can get the `x=0` coordinate as follows:

```jsx
// get the default x-axis scale
const xAxisScale = useXScale();
// get the position associated to the value 0
const xOrigin = xAxisScale(0);
```

```tsx
import * as React from 'react';
import { styled } from '@mui/material/styles';
import { ScaleLinear } from '@mui/x-charts-vendor/d3-scale';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { LinePlot } from '@mui/x-charts/LineChart';
import { useDrawingArea, useXScale, useYScale } from '@mui/x-charts/hooks';

const x = Array.from({ length: 21 }, (_, index) => -1 + 0.2 * index);
const linear = x.map((v) => -1 + v);
const poly = x.map((v) => -1 + v ** 2 - v);

const StyledPath = styled('path')<{ color: 'primary' | 'secondary' }>(
  ({ theme, color }) => ({
    fill: 'none',
    stroke: theme.palette.text[color],
    shapeRendering: 'crispEdges',
    strokeWidth: 1,
    pointerEvents: 'none',
  }),
);

function CartesianAxis() {
  // Get the drawing area bounding box
  const { left, top, width, height } = useDrawingArea();

  // Get the two scale
  const yAxisScale = useYScale() as ScaleLinear<any, any>;
  const xAxisScale = useXScale() as ScaleLinear<any, any>;

  const yOrigin = yAxisScale(0);
  const xOrigin = xAxisScale(0);

  const xTicks = [-2, -1, 1, 2, 3];
  const yTicks = [-2, -1, 1, 2, 3, 4, 5];

  return (
    <React.Fragment>
      {yTicks.map((value) => (
        <StyledPath
          key={value}
          d={`M ${left} ${yAxisScale(value)} l ${width} 0`}
          color="secondary"
        />
      ))}
      {xTicks.map((value) => (
        <StyledPath
          key={value}
          d={`M ${xAxisScale(value)} ${top} l 0 ${height}`}
          color="secondary"
        />
      ))}
      <StyledPath d={`M ${left} ${yOrigin} l ${width} 0`} color="primary" />
      <StyledPath d={`M ${xOrigin} ${top} l 0 ${height}`} color="primary" />
    </React.Fragment>
  );
}
export default function OriginDemo() {
  return (
    <ChartContainer
      margin={{ top: 5, left: 5, right: 5, bottom: 5 }}
      height={300}
      series={[
        {
          type: 'line',
          data: linear,
        },

        {
          type: 'line',
          data: poly,
        },
      ]}
      xAxis={[{ data: x, scaleType: 'linear', min: -1, max: 3, position: 'none' }]}
      yAxis={[{ min: -2, max: 5, position: 'none' }]}
    >
      <CartesianAxis />
      <LinePlot />
    </ChartContainer>
  );
}

```

#### Coordinate to value

The `d3-scale` object lets you convert a coordinate to a data value with the `invert()` method.

The next example contains two lines drawn using different y-axes.
By using `invert()`, the value associated with the current mouse coordinate `y` can be resolved as follows:

```jsx
<text>{leftAxisScale.invert(yCoordinate).toFixed(0)}</text>
```

```tsx
import * as React from 'react';
import { ScaleLinear } from '@mui/x-charts-vendor/d3-scale';
import { styled } from '@mui/material/styles';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { LinePlot } from '@mui/x-charts/LineChart';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { useDrawingArea, useYScale } from '@mui/x-charts/hooks';

const StyledPath = styled('path')(({ theme }) => ({
  fill: 'none',
  stroke: theme.palette.text.primary,
  shapeRendering: 'crispEdges',
  strokeWidth: 1,
  pointerEvents: 'none',
  strokeDasharray: '5 2',
}));

const StyledText = styled('text')(({ theme }) => ({
  stroke: 'none',
  fill: theme.palette.text.primary,
  shapeRendering: 'crispEdges',
}));

function ValueHighlight(props: { svgRef: React.RefObject<SVGSVGElement | null> }) {
  const { svgRef } = props;

  // Get the drawing area bounding box
  const { left, top, width, height } = useDrawingArea();

  // Get the two scale
  const leftAxisScale = useYScale('left_axis_id') as ScaleLinear<any, any>;
  const rightAxisScale = useYScale('right_axis_id') as ScaleLinear<any, any>;

  const [mouseY, setMouseY] = React.useState<null | number>(null);

  React.useEffect(() => {
    const element = svgRef.current;
    if (element === null) {
      return () => {};
    }

    const handleMouseOut = () => {
      setMouseY(null);
    };

    const handleMouseMove = (event: MouseEvent) => {
      const x = event.offsetX;
      const y = event.offsetY;
      if (x < left || x > left + width) {
        setMouseY(null);
        return;
      }
      if (y < top - 10 || y > top + height + 10) {
        // Allows some margin if slightly on top/bottom of the drawing area
        setMouseY(null);
        return;
      }
      setMouseY(Math.max(Math.min(top + height, y), top)); // clamp to the drawing area
    };

    element.addEventListener('mouseout', handleMouseOut);
    element.addEventListener('mousemove', handleMouseMove);
    return () => {
      element.removeEventListener('mouseout', handleMouseOut);
      element.removeEventListener('mousemove', handleMouseMove);
    };
  }, [height, left, top, width, svgRef]);

  if (mouseY === null) {
    return null;
  }
  return (
    <React.Fragment>
      <StyledPath d={`M ${left} ${mouseY} l ${width} 0`} />
      <StyledText
        x={left + 5}
        y={mouseY}
        textAnchor="start"
        dominantBaseline="text-after-edge"
      >
        {leftAxisScale.invert(mouseY).toFixed(0)}
      </StyledText>

      <StyledText
        x={left + width - 5}
        y={mouseY}
        textAnchor="end"
        dominantBaseline="text-after-edge"
      >
        {rightAxisScale.invert(mouseY).toFixed(0)}
      </StyledText>
    </React.Fragment>
  );
}
export default function ScaleDemo() {
  const svgRef = React.useRef<SVGSVGElement>(null);
  return (
    <ChartContainer
      ref={svgRef}
      height={300}
      series={[
        {
          type: 'line',
          data: [5, 15, 20, 24, 30, 38, 40, 51, 52, 61],
          yAxisId: 'left_axis_id',
        },
        {
          type: 'line',
          data: [
            50134, 48361, 46362, 44826, 42376, 40168, 38264, 36159, 34259, 32168,
          ],
          yAxisId: 'right_axis_id',
        },
      ]}
      xAxis={[
        {
          data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          scaleType: 'point',
          position: 'none',
        },
      ]}
      yAxis={[
        { id: 'left_axis_id', position: 'left' },
        { id: 'right_axis_id', position: 'right', width: 50 },
      ]}
    >
      <LinePlot />
      <ChartsYAxis axisId="left_axis_id" />
      <ChartsYAxis axisId="right_axis_id" />
      <ValueHighlight svgRef={svgRef} />
    </ChartContainer>
  );
}

```

### Series

Series information is accessible through the `useSeries()` hook for all series types, and the `use[Type]Series()` hook for a specific series type.
These hooks return the order of the series and their configuration, including data points, color, and more.

You can use that information to create custom charts.
For example, you can use `useLineSeries()` to obtain the series of a Line Chart and display an indicator of the minimum and maximum values of each series:

```tsx
import * as React from 'react';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { LinePlot } from '@mui/x-charts/LineChart';
import { useLineSeries, useXAxis, useXScale, useYScale } from '@mui/x-charts/hooks';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { DefaultizedLineSeriesType } from '@mui/x-charts/models';

function ExtremaLabels() {
  const lineSeries = useLineSeries();

  if (!lineSeries) {
    return null;
  }

  return (
    <React.Fragment>
      {lineSeries.map((series) => (
        <SingleSeriesExtremaLabels series={series} />
      ))}
    </React.Fragment>
  );
}

function SingleSeriesExtremaLabels({
  series,
}: {
  series: DefaultizedLineSeriesType;
}) {
  const xAxis = useXAxis('x');

  const min = series.data.reduce(
    (acc, value, index) =>
      value != null && value < acc.value ? { index, value } : acc,
    { index: -1, value: Infinity },
  );
  const max = series.data.reduce(
    (acc, value, index) =>
      value != null && value > acc.value ? { index, value } : acc,
    { index: -1, value: -Infinity },
  );

  return (
    <React.Fragment>
      <PointLabel
        x={xAxis.data?.[min.index]}
        y={min.value}
        placement="below"
        color={series.color}
      />
      <PointLabel
        x={xAxis.data?.[max.index]}
        y={max.value}
        placement="above"
        color={series.color}
      />
    </React.Fragment>
  );
}

function PointLabel({
  x,
  y,
  placement,
  color,
}: {
  x: number;
  y: number;
  placement: 'above' | 'below';
  color: string;
}) {
  const xAxisScale = useXScale();
  const yAxisScale = useYScale();

  const left = xAxisScale(x) ?? 0;
  const top = (yAxisScale(y) ?? 0) + (placement === 'below' ? 20 : -20);

  return (
    <Box
      sx={{
        position: 'absolute',
        left,
        top,
        translate: '-50% -50%',
        border: `2px solid ${color}`,
        borderRadius: 1,
        px: 1,
      }}
    >
      <Typography variant="caption">{y}</Typography>
    </Box>
  );
}

export default function SeriesDemo() {
  return (
    <Box sx={{ position: 'relative', width: '100%' }}>
      <ChartDataProvider
        xAxis={[{ id: 'x', data: [1, 2, 3, 5, 8, 10], height: 28 }]}
        series={[
          { id: 'a', type: 'line', data: [4, 6, 4, 9, 3, 5] },
          { id: 'b', type: 'line', data: [3, 7, 8, 2, 4, 9] },
        ]}
        yAxis={[{ min: 0, max: 10 }]}
        height={300}
      >
        <ChartsSurface>
          <LinePlot />
          <ChartsXAxis />
          <ChartsYAxis />
        </ChartsSurface>
        <ExtremaLabels />
      </ChartDataProvider>
    </Box>
  );
}

```

## HTML components

Use the `ChartDataProvider` to access chart data from any component.
This lets you create HTML components that interact with the data.

In the next example, notice that the `MyCustomLegend` component displays the series names and colors.
This creates an HTML `<table>` element, which can be customized in any way.

```tsx
import Box from '@mui/material/Box';
import { useLegend } from '@mui/x-charts/hooks';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { BarPlot } from '@mui/x-charts/BarChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';

function MyCustomLegend() {
  const { items } = useLegend();
  return (
    <table
      style={{
        marginLeft: 40,
        marginRight: 40,
      }}
    >
      <tbody>
        {items.map((v) => {
          return (
            <tr key={v.id}>
              <td aria-hidden>
                <div
                  style={{
                    background: v.color,
                    height: 10,
                    width: 10,
                    marginRight: 10,
                    flexShrink: 0,
                    borderRadius: 5,
                  }}
                />
              </td>
              <td>{`${v.label}`}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

const veryLongText =
  "Second Series. You should always try to avoid long sentences. But oftentimes, it's not possible. So, we need to handle them gracefully. This is a very long sentence that should be fully readable.";

export default function HtmlLegend() {
  return (
    <Box sx={{ height: 400, display: 'flex', flexDirection: 'column' }}>
      <ChartDataProvider
        series={[
          { label: 'First Series', type: 'bar', data: [100, 200] },
          { label: veryLongText, type: 'bar', data: [45, 333] },
        ]}
        xAxis={[{ data: ['A', 'B'], scaleType: 'band', id: 'x-axis', height: 28 }]}
      >
        <ChartsSurface>
          <BarPlot />
          <ChartsXAxis axisId="x-axis" />
          <ChartsYAxis />
        </ChartsSurface>
        <MyCustomLegend />
      </ChartDataProvider>
    </Box>
  );
}

```

:::warning
Note that the HTML components are not part of the SVG hierarchy.
This means they must be outside of the `ChartsSurface` component to avoid mixing HTML and SVG, and inside of the `ChartDataProvider` component to get access to the data.
:::


# ChartsClipPath API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Custom components](/x/react-charts/components/)

## Import

```jsx
import { ChartsClipPath } from '@mui/x-charts/ChartsClipPath';
// or
import { ChartsClipPath } from '@mui/x-charts';
// or
import { ChartsClipPath } from '@mui/x-charts-pro';
// or
import { ChartsClipPath } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `string` | - | Yes |  |
| offset | `{ bottom?: number, left?: number, right?: number, top?: number }` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/ChartsClipPath/ChartsClipPath.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/ChartsClipPath/ChartsClipPath.tsx)

# ChartsSurface API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Custom components](/x/react-charts/components/)
- [Charts - Composition](/x/react-charts/composition/)

## Import

```jsx
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
// or
import { ChartsSurface } from '@mui/x-charts';
// or
import { ChartsSurface } from '@mui/x-charts-pro';
// or
import { ChartsSurface } from '@mui/x-charts-premium';
```

> **Note**: The `ref` is forwarded to the root element.

> Any other props supplied will be provided to the root element (native element).

## CSS

### Rule name

| Global class | Rule name | Description |
|--------------|-----------|-------------|
| - | root | Styles applied to the root element. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/ChartsSurface/ChartsSurface.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/ChartsSurface/ChartsSurface.tsx)