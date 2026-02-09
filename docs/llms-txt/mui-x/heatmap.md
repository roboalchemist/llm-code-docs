# Source: https://mui.com/x/api/charts/heatmap.md

# Source: https://mui.com/x/react-charts/heatmap.md

---
title: React Heatmap chart
productId: x-charts
components: Heatmap, HeatmapPlot, HeatmapTooltip, HeatmapTooltipContent, FocusedHeatmapCell
---

# Charts - Heatmap [<span class="plan-pro"></span>](/x/introduction/licensing/#pro-plan 'Pro plan')

Heatmap charts visually represents data with color variations to highlight patterns and trends across two dimensions.

## Overview

Heatmaps are ideal for visualizing intensity variations across two categorical or continuous dimensions. They highlight areas of high and low concentration in a dataset, making it easy to detect trends, clusters, or anomalies at a glance. Each cell in a heatmap represents the intersection of two variables, with color encoding used to convey the magnitude of a numerical value.
```tsx
import { interpolateBlues } from 'd3-scale-chromatic';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { HeatmapValueType } from '@mui/x-charts-pro/models';
import bikeData from '../dataset/ParisBicycle.json';

const days = [
  new Date(2025, 1, 24),
  new Date(2025, 1, 25),
  new Date(2025, 1, 26),
  new Date(2025, 1, 27),
  new Date(2025, 1, 28),
  new Date(2025, 2, 1),
  new Date(2025, 2, 2),
];

const hours = [
  '00',
  '01',
  '02',
  '03',
  '04',
  '05',
  '06',
  '07',
  '08',
  '09',
  '10',
  '11',
  '12',
  '13',
  '14',
  '15',
  '16',
  '17',
  '18',
  '19',
  '20',
  '21',
  '22',
  '23',
];

const shortDayFormatter = new Intl.DateTimeFormat('en-US', { weekday: 'short' })
  .format;
const dateFormatter = new Intl.DateTimeFormat('en-US', {
  weekday: 'short',
  day: 'numeric',
  month: 'short',
  year: 'numeric',
}).format;

export default function HeatmapDemo() {
  return (
    <Stack width="100%">
      <Typography align="center" sx={{ width: '100%', mb: 1 }}>
        Bicycle count: Paris - Rivoli street (West-East)
      </Typography>
      <div style={{ flexGrow: 1, minHeight: 0 }}>
        <Heatmap
          height={400}
          margin={{ left: 2 }}
          xAxis={[
            {
              data: days,
              label: 'Day',
              valueFormatter: (value: Date, context) => {
                return context.location === 'tick'
                  ? shortDayFormatter(value)
                  : dateFormatter(value);
              },
              tickLabelStyle: { angle: 45 },
              height: 70,
            },
          ]}
          yAxis={[
            {
              data: hours,
              label: 'Hour of the day',
              tickLabelInterval: (_, index) => index % 2 === 0,
              valueFormatter: (value) => `${value}h`,
              width: 60,
            },
          ]}
          series={[
            {
              data: bikeData as unknown as HeatmapValueType[],
              label: 'Bicycle count',
              highlightScope: { highlight: 'item', fade: 'global' },
            },
          ]}
          zAxis={[
            {
              colorMap: {
                max: 700,
                type: 'continuous',

                color: (t: number) => interpolateBlues(Math.sqrt(t)),
              },
            },
          ]}
          hideLegend={false}
          slotProps={{
            legend: {
              direction: 'vertical',
              position: { vertical: 'top' },
              sx: { height: 200 },
            },
          }}
        />
      </div>
      <Typography variant="caption" textAlign="end">
        Data from{' '}
        <a href="https://parisdata.opendatasoft.com/explore/dataset/comptage-velo-donnees-compteurs/">
          Paris Data
        </a>
      </Typography>
    </Stack>
  );
}

```

## Basics

Heatmap charts series must contain a `data` property containing an array of 3-tuples.
The first two numbers in each tuple correspond to the x and y indexes of the cell, respectively.
The third number is the value for the given cell.

```jsx
<Heatmap
  series={[
    {
      data: [
        [0, 2, 2.7], // Cell (0, 2) receives the value 2.7
        [1, 2, 4.5], // Cell (1, 2) receives the value 4.5
      ],
    },
  ]}
/>
```

You can specify x and y ticks with the `xAxis` and `yAxis` props.

```tsx
import Box from '@mui/material/Box';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { data } from './dumbData';

export default function BasicHeatmap() {
  return (
    <Box sx={{ width: '100%', maxWidth: 400 }}>
      <Heatmap
        xAxis={[{ data: [1, 2, 3, 4] }]}
        yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
        series={[{ data }]}
        height={300}
      />
    </Box>
  );
}

```

## Color mapping

To customize the color mapping, use the `zAxis` configuration.
You can either use the piecewise or continuous [color mapping](https://mui.com/x/react-charts/styling/#values-color).

```tsx
import { interpolateBlues } from 'd3-scale-chromatic';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { HeatmapValueType } from '@mui/x-charts-pro/models';

const dataset = [
  {
    london: 59,
    paris: 57,
    newYork: 86,
    seoul: 21,
    month: 'January',
  },
  {
    london: 50,
    paris: 52,
    newYork: 78,
    seoul: 28,
    month: 'February',
  },
  {
    london: 47,
    paris: 53,
    newYork: 106,
    seoul: 41,
    month: 'March',
  },
  {
    london: 54,
    paris: 56,
    newYork: 92,
    seoul: 73,
    month: 'April',
  },
  {
    london: 57,
    paris: 69,
    newYork: 92,
    seoul: 99,
    month: 'May',
  },
  {
    london: 60,
    paris: 63,
    newYork: 103,
    seoul: 144,
    month: 'June',
  },
  {
    london: 59,
    paris: 60,
    newYork: 105,
    seoul: 319,
    month: 'July',
  },
  {
    london: 65,
    paris: 60,
    newYork: 106,
    seoul: 249,
    month: 'August',
  },
  {
    london: 51,
    paris: 51,
    newYork: 95,
    seoul: 131,
    month: 'September',
  },
  {
    london: 60,
    paris: 65,
    newYork: 97,
    seoul: 55,
    month: 'October',
  },
  {
    london: 67,
    paris: 64,
    newYork: 76,
    seoul: 48,
    month: 'November',
  },
  {
    london: 61,
    paris: 70,
    newYork: 103,
    seoul: 25,
    month: 'December',
  },
];

const data = dataset.flatMap(
  ({ london, paris, newYork, seoul }, monthIndex): HeatmapValueType[] => [
    [0, monthIndex, london],
    [1, monthIndex, paris],
    [2, monthIndex, newYork],
    [3, monthIndex, seoul],
  ],
);

const xData = ['London', 'Paris', 'NewYork', 'Seoul'];
const yData = dataset.flatMap(({ month }) => month);

export default function ColorConfig() {
  return (
    <Heatmap
      height={400}
      width={600}
      xAxis={[{ data: xData }]}
      yAxis={[{ data: yData, width: 80 }]}
      series={[{ data }]}
      zAxis={[
        {
          min: 20,
          max: 300,
          colorMap: {
            type: 'continuous',
            color: interpolateBlues,
          },
        },
      ]}
    />
  );
}

```

## Highlight

You can choose to highlight the hovered element by setting `highlightScope.highlight` to `'item'`.
To fade the other item, set `highlightScope.fade` to `'global'`.

```tsx
import Box from '@mui/material/Box';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { data } from './dumbData';

export default function HighlightHeatmap() {
  return (
    <Box sx={{ width: '100%', maxWidth: 400 }}>
      <Heatmap
        xAxis={[{ data: [1, 2, 3, 4] }]}
        yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
        series={[{ data, highlightScope: { highlight: 'item', fade: 'global' } }]}
        height={300}
      />
    </Box>
  );
}

```

By default highlighted/faded effect is obtained by applying the CSS property `filter: saturate(...)` to cells.
To modify this styling, use the `heatmapClasses.highlighted` and `heatmapClasses.faded` CSS classes to override the applied style.

In the following demo, we replace the highlight saturation by a border radius and reduce the saturation of the faded cells.

```tsx
import Box from '@mui/material/Box';
import { Heatmap, heatmapClasses } from '@mui/x-charts-pro/Heatmap';
import { data } from './dumbData';

export default function HighlightClasses() {
  return (
    <Box sx={{ width: '100%', maxWidth: 400 }}>
      <Heatmap
        sx={{
          [`.${heatmapClasses.cell}`]: {
            [`&.${heatmapClasses.highlighted}`]: {
              filter: 'none', // Remove the default filter effect.
              rx: '10px', // Round the corners
            },
            [`&.${heatmapClasses.faded}`]: {
              filter: 'saturated(95%)', // Reduce the faded default saturation
            },
          },
        }}
        xAxis={[{ data: [1, 2, 3, 4] }]}
        yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
        series={[
          {
            data,
            highlightScope: {
              highlight: 'item',
              fade: 'global',
            },
          },
        ]}
        height={300}
      />
    </Box>
  );
}

```

## Click event

Use `onItemClick` to know which cell is clicked by user.

The first argument is the click event.
The second one is the item identifier.
It contains the properties `xIndex` and `yIndex` that are the indexes of the clicked cell along the x- and y-axes respectively.

If this cell has associated data, the `dataIndex` property indicates the position of the cell's data within the series' `data` array.

```tsx
import * as React from 'react';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import UndoOutlinedIcon from '@mui/icons-material/UndoOutlined';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import type { HeatmapItemIdentifier } from '@mui/x-charts-pro/models';
import { data } from './dumbData';

export default function HeatmapCellClick() {
  const [cellData, setCellData] = React.useState<HeatmapItemIdentifier | null>(null);

  return (
    <Stack
      direction={{ xs: 'column', md: 'row' }}
      spacing={{ xs: 0, md: 4 }}
      sx={{ width: '100%' }}
    >
      <Box sx={{ flexGrow: 1 }}>
        <Heatmap
          xAxis={[{ data: [1, 2, 3, 4] }]}
          yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
          series={[
            {
              data: data.filter((_, index) => index !== 5 && index !== 13),
              highlightScope: { highlight: 'item' },
            },
          ]}
          height={300}
          onItemClick={(event, params) => setCellData(params)}
        />
      </Box>

      <Stack direction="column" sx={{ width: { xs: '100%', md: '40%' } }}>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <Typography>Click on the chart</Typography>
          <IconButton
            aria-label="reset"
            size="small"
            onClick={() => {
              setCellData(null);
            }}
          >
            <UndoOutlinedIcon fontSize="small" />
          </IconButton>
        </Box>
        <HighlightedCode
          code={`// Data from cell click
${cellData ? JSON.stringify(cellData, null, 2) : '// The data will appear here'}
`}
          language="json"
          copyButtonHidden
        />
      </Stack>
    </Stack>
  );
}

```

## Common features

The heatmap shares several features with other charts.
This section only explains the details that are specific to the heatmap.
If you'd like to learn more about the shared features, you can visit their dedicated pages.

### Axes

The Heatmap axes can be customized like any other chart axis.
The available options are available in the [axis customization page](/x/react-charts/axis/#axis-customization).

### Tooltip

The Heatmap has an item tooltip that can be customized as described in the [Tooltip documentation page](/x/react-charts/tooltip/).

The only difference of the Heatmap Tooltip is its default content.
You can import the default tooltip, or only its content as follows:

```js
import { HeatmapTooltip, HeatmapTooltipContent } from '@mui/x-charts/Heatmap',
```

### Legend

The Heatmap comes with a legend which is by default the [ContinuousColorLegend](/x/react-charts/legend/#color-legend).

To display it set `hideLegend` to `false`.
You can modify it with `slots.legend` and `slotProps.legend`.

```tsx
import Box from '@mui/material/Box';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { data } from './dumbData';

export default function HeatmapLegend() {
  return (
    <Box sx={{ width: '100%', maxWidth: 400 }}>
      <Heatmap
        xAxis={[{ data: [1, 2, 3, 4] }]}
        yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
        series={[{ data }]}
        height={300}
        hideLegend={false}
        slotProps={{
          legend: {
            direction: 'vertical',
            position: { vertical: 'middle' },
            sx: { height: 200 },
          },
        }}
      />
    </Box>
  );
}

```

## Custom item

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import { Heatmap } from '@mui/x-charts-pro/Heatmap';
import { data } from './dumbData';

function CustomCell(props: any) {
  const { x, y, width, height, ownerState, ...other } = props;

  return (
    <React.Fragment>
      <rect
        {...other}
        x={x + 4}
        y={y + 4}
        width={width - 2 * 4}
        height={height - 2 * 4}
        fill={ownerState.color}
        clipPath={ownerState.isHighlighted ? undefined : 'inset(0px round 10px)'}
      />
      <text
        x={x + width / 2}
        y={y + height / 2}
        textAnchor="middle"
        dominantBaseline="middle"
        pointerEvents="none"
      >
        {ownerState.value}
      </text>
    </React.Fragment>
  );
}
export default function CustomItem() {
  return (
    <Box sx={{ width: '100%', maxWidth: 400 }}>
      <Heatmap
        slots={{ cell: CustomCell }}
        xAxis={[{ data: [1, 2, 3, 4] }]}
        yAxis={[{ data: ['A', 'B', 'C', 'D', 'E'] }]}
        series={[{ data, highlightScope: { highlight: 'item' } }]}
        height={300}
      />
    </Box>
  );
}

```
