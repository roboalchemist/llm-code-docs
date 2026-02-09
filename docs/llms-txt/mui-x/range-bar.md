# Source: https://mui.com/x/react-charts/range-bar.md

---
title: React Range Bar chart
productId: x-charts
components: BarChartPremium, RangeBarPlot, ChartDataProviderPremium, ChartContainerPremium
---

# Charts - Range Bar [<span class="plan-premium"></span>](/x/introduction/licensing/#premium-plan 'Premium plan')

Range bar charts highlight the range between minimum and maximum values across categories.

## Overview

A range bar chart displays the span between two values for each category.

Each bar extends from a lower to an upper value, and is commonly used for visualizing data like temperature ranges, project timelines, or performance intervals.

## Basics

A range bar chart is created by rendering a `BarChartPremium` where at least one series has the type `'rangeBar'`.

Each data point in a range bar series consists of a `{ start: number, end: number }` object.

```tsx
import * as React from 'react';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import { AxisValueFormatterContext } from '@mui/x-charts/models';
import { BarChartPremium } from '@mui/x-charts-premium/BarChartPremium';
import { temperatureBerlinPorto } from '../dataset/temperatureBerlinPorto';

export default function BasicRangeBar() {
  return (
    <Stack width="100%" spacing={2}>
      <Typography textAlign="center">
        Average monthly temperature ranges in °C for Porto and Berlin in 1991-2020
      </Typography>
      <BarChartPremium
        xAxis={[
          {
            data: temperatureBerlinPorto.months,
            valueFormatter: (v: string, context: AxisValueFormatterContext) =>
              context.location === 'tick' ? v.slice(0, 3) : v,
          },
        ]}
        yAxis={[{ valueFormatter: (value: number) => `${value}°C` }]}
        series={[
          {
            id: 'porto',
            type: 'rangeBar',
            label: 'Porto, Portugal',
            valueFormatter: (value) =>
              value === null ? null : `${value[0]}°C - ${value[1]}°C`,
            data: temperatureBerlinPorto.porto,
          },
          {
            id: 'berlin',
            type: 'rangeBar',
            label: 'Berlin, Germany',
            valueFormatter: (value) =>
              value === null ? null : `${value[0]}°C - ${value[1]}°C`,
            data: temperatureBerlinPorto.berlin,
          },
        ]}
        height={300}
      />
      <Typography variant="caption">
        Source: IPMA (Porto), climate-data.org (Berlin)
      </Typography>
    </Stack>
  );
}

```

## Customization

### Grid

You can add a grid in the background of the chart with the `grid` prop.

See [Axis—Grid](/x/react-charts/axis/#grid) documentation for more information.

### Border radius

A range bar chart supports rounded corners. To achieve it, set the value of the `borderRadius` prop on the `BarChartPremium` to any positive value.

When using composition, you can set the `borderRadius` prop on the `RangeBarPlot` component.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import {
  BarChartPremium,
  BarChartPremiumProps,
} from '@mui/x-charts-premium/BarChartPremium';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

export default function RangeBarBorderRadius() {
  const [layout, setLayout] = React.useState<'horizontal' | 'vertical'>('vertical');
  const [radius, setRadius] = React.useState(10);
  const [reverse, setReverse] = React.useState(false);

  return (
    <Stack direction="column" spacing={1} sx={{ width: '100%', maxWidth: 600 }}>
      <Stack direction="row" spacing={4} flexWrap="wrap" justifyContent="center">
        <Stack direction="column" spacing={1} flex={1}>
          <Typography gutterBottom>Border Radius</Typography>
          <Slider
            value={radius}
            onChange={(event, value) => setRadius(value as number)}
            valueLabelDisplay="auto"
            min={0}
            max={50}
            sx={{ mt: 2 }}
          />
        </Stack>
        <TextField
          select
          sx={{ minWidth: 150 }}
          label="layout"
          value={layout}
          onChange={(event) =>
            setLayout(event.target.value as 'horizontal' | 'vertical')
          }
        >
          <MenuItem value="horizontal">Horizontal</MenuItem>
          <MenuItem value="vertical">Vertical</MenuItem>
        </TextField>

        <FormControlLabel
          checked={reverse}
          control={
            <Checkbox onChange={(event) => setReverse(event.target.checked)} />
          }
          label="Reverse"
          labelPlacement="end"
        />
      </Stack>
      <BarChartPremium
        series={[
          {
            type: 'rangeBar',
            datasetKeys: { start: 'low', end: 'high' },
            layout,
          },
        ]}
        margin={{ left: 0 }}
        {...getChartSettings(layout, reverse)}
        borderRadius={radius}
      />
      <HighlightedCode
        code={`<BarChartPremium
  // ...
  borderRadius={${radius}}
/>`}
        language="jsx"
        copyButtonHidden
      />
    </Stack>
  );
}

const dataset = [
  [3, -7, '1st'],
  [0, -5, '2nd'],
  [10, 0, '3rd'],
  [9, 6, '4th'],
].map(([high, low, order]) => ({
  high,
  low,
  order,
}));

function getChartSettings(
  layout: 'vertical' | 'horizontal',
  reverse: boolean,
): Partial<BarChartPremiumProps> {
  return {
    dataset,
    height: 300,
    xAxis: layout === 'horizontal' ? [{ reverse }] : [{ dataKey: 'order' }],
    yAxis:
      layout === 'horizontal'
        ? [{ scaleType: 'band', dataKey: 'order' }]
        : [{ reverse }],
    slotProps: {
      legend: {
        direction: 'horizontal',
        position: { vertical: 'bottom', horizontal: 'center' },
      },
    },
  };
}

```

### Color

As with other charts, you can modify the series color either directly, or with the color palette.

An alternative is to use a `colorMap`, which maps values to colors. The color set by `colorMap` has priority over other color settings.

:::warning
Unlike other chart types, the `colorMap` property does not work for the numerical axis of range bar charts (that is, the y-axis for vertical range bar charts and the x-axis for horizontal range bar charts).
:::

You can learn more about the `colorMap` in the [Styling docs](/x/react-charts/styling/#values-color).

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import {
  BarChartPremium,
  RangeBarSeries,
} from '@mui/x-charts-premium/BarChartPremium';

const series = [
  {
    type: 'rangeBar',
    data: [
      [-2, 4],
      [4, 10],
      [-1, 3],
      [2, 13],
      [6, 7],
      [8, 12],
    ],
  } satisfies RangeBarSeries,
];

export default function RangeBarColorScale() {
  const [colorX, setColorX] = React.useState<
    'None' | 'piecewise' | 'continuous' | 'ordinal'
  >('piecewise');

  return (
    <Stack direction="column" spacing={1} sx={{ width: '100%', maxWidth: 600 }}>
      <Stack direction="row" spacing={1}>
        <TextField
          select
          sx={{ minWidth: 150 }}
          label="x-axis colorMap"
          value={colorX}
          onChange={(event) =>
            setColorX(
              event.target.value as 'None' | 'piecewise' | 'continuous' | 'ordinal',
            )
          }
        >
          <MenuItem value="None">None</MenuItem>
          <MenuItem value="piecewise">piecewise</MenuItem>
          <MenuItem value="continuous">continuous</MenuItem>
          <MenuItem value="ordinal">ordinal</MenuItem>
        </TextField>
      </Stack>

      <BarChartPremium
        height={300}
        grid={{ horizontal: true }}
        series={series}
        xAxis={[
          {
            data: [
              new Date(2019, 1, 1),
              new Date(2020, 1, 1),
              new Date(2021, 1, 1),
              new Date(2022, 1, 1),
              new Date(2023, 1, 1),
              new Date(2024, 1, 1),
            ],
            valueFormatter: (value: Date) => value.getFullYear().toString(),
            colorMap:
              (colorX === 'ordinal' && {
                type: 'ordinal',
                colors: [
                  '#ccebc5',
                  '#a8ddb5',
                  '#7bccc4',
                  '#4eb3d3',
                  '#2b8cbe',
                  '#08589e',
                ],
              }) ||
              (colorX === 'continuous' && {
                type: 'continuous',
                min: new Date(2019, 1, 1),
                max: new Date(2024, 1, 1),
                color: ['green', 'orange'],
              }) ||
              (colorX === 'piecewise' && {
                type: 'piecewise',
                thresholds: [new Date(2021, 1, 1), new Date(2023, 1, 1)],
                colors: ['blue', 'red', 'blue'],
              }) ||
              undefined,
          },
        ]}
        margin={{ left: 0 }}
      />
      <HighlightedCode
        code={[
          `<BarChart`,
          '  /* ... */',
          // ColorX
          ...(colorX === 'None' ? ['  xAxis={[{}]}'] : []),
          ...(colorX === 'ordinal'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'ordinal',`,
                `      colors: ['#ccebc5', '#a8ddb5', '#7bccc4', '#4eb3d3', '#2b8cbe', '#08589e']`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorX === 'continuous'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'continuous',`,
                `      min: new Date(2019, 1, 1),`,
                `      max: new Date(2024, 1, 1),`,
                `      color: ['green', 'orange']`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorX === 'piecewise'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'piecewise',`,
                `      thresholds: [new Date(2021, 1, 1), new Date(2023, 1, 1)],`,
                `      colors: ['blue', 'red', 'blue'],`,
                `    }`,
                '  }]}',
              ]
            : []),

          `/>`,
        ].join('\n')}
        language="jsx"
        copyButtonHidden
      />
    </Stack>
  );
}

```

### CSS

You can customize the range bar chart elements using CSS selectors.

Like a bar chart, each series renders a `g` element that contains a `data-series` attribute.
You can use this attribute to target elements based on their series.

```tsx
import * as React from 'react';
import { barElementClasses } from '@mui/x-charts/BarChart';
import {
  BarChartPremium,
  rangeBarClasses,
  RangeBarSeries,
} from '@mui/x-charts-premium/BarChartPremium';

const settings = {
  xAxis: [{ data: ['group A', 'group B', 'group C'] }],
  series: [
    {
      type: 'rangeBar',
      id: '1',
      data: [
        [4, 3],
        [5, 8],
        [2, 4],
      ],
    },
    {
      type: 'rangeBar',
      id: '2',
      data: [
        [1, 6],
        [5, 6],
        [3, 9],
      ],
    },
    {
      type: 'rangeBar',
      id: '3',
      data: [
        [1, 5],
        [2, 4],
        [3, 8],
      ],
    },
  ] satisfies RangeBarSeries[],
  height: 300,
  margin: { left: 0 },
} as const;

export default function RangeBarGradient() {
  return (
    <BarChartPremium
      {...settings}
      sx={{
        [`& .${rangeBarClasses.series}[data-series="2"] .${barElementClasses.root}`]:
          {
            fill: 'url(#bar-gradient)',
          },
      }}
    >
      <defs>
        <Gradient id="bar-gradient" />
      </defs>
    </BarChartPremium>
  );
}

function Gradient(props: React.SVGProps<SVGLinearGradientElement>) {
  return (
    <linearGradient gradientTransform="rotate(90)" {...props}>
      <stop offset="5%" stopColor="gold" />
      <stop offset="95%" stopColor="red" />
    </linearGradient>
  );
}

```

## Click event

The click event handlers in range bar charts work similarly to bar charts.

You read more about it in bar chart's [Click event](/x/react-charts/bars/#click-event) page.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import UndoOutlinedIcon from '@mui/icons-material/UndoOutlined';
import {
  BarChartPremium,
  RangeBarSeries,
} from '@mui/x-charts-premium/BarChartPremium';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import { BarItemIdentifier, ChartsAxisData } from '@mui/x-charts/models';
import { RangeBarItemIdentifier } from '@mui/x-charts-premium/models';

import type {} from '@mui/x-charts-premium/moduleAugmentation/rangeBarOnClick';

const barChartsParams = {
  series: [
    {
      type: 'rangeBar',
      id: 'series-1',
      data: [
        [3, 5],
        [4, 6],
        [1, 4],
        [6, 8],
        [5, 6],
      ],
      label: 'A',
      highlightScope: {
        highlight: 'item',
      },
    },
    {
      type: 'rangeBar',
      id: 'series-2',
      data: [
        [4, 6],
        [1, 4],
        [6, 8],
        [5, 6],
        [3, 5],
      ],
      label: 'B',
      highlightScope: {
        highlight: 'item',
      },
    },
  ] satisfies RangeBarSeries[],
  xAxis: [{ data: ['0', '3', '6', '9', '12'], id: 'axis1' }],
  height: 400,
  margin: { left: 0 },
} as const;

export default function RangeBarClick() {
  const [itemData, setItemData] = React.useState<
    BarItemIdentifier | RangeBarItemIdentifier
  >();
  const [axisData, setAxisData] = React.useState<ChartsAxisData | null>();

  return (
    <Stack
      direction={{ xs: 'column', md: 'row' }}
      spacing={{ xs: 0, md: 4 }}
      sx={{ width: '100%' }}
    >
      <Box sx={{ flexGrow: 1 }}>
        <BarChartPremium
          {...barChartsParams}
          onItemClick={(event, d) => setItemData(d)}
          onAxisClick={(event, d) => setAxisData(d)}
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
              setItemData(undefined);
              setAxisData(null);
            }}
          >
            <UndoOutlinedIcon fontSize="small" />
          </IconButton>
        </Box>
        <HighlightedCode
          code={`// Data from item click
${itemData ? JSON.stringify(itemData, null, 2) : '// The data will appear here'}

// Data from axis click
${axisData ? JSON.stringify(axisData, null, 2) : '// The data will appear here'}
`}
          language="json"
          copyButtonHidden
        />
      </Stack>
    </Stack>
  );
}

```

:::info
If you use `onAxisClick`, the `seriesValues` type will be missing `RangeBarValueType`.

In case you use `onItemClick`, the `itemIdentifier` type will be missing `RangeBarItemIdentifier`.

To correct both these types, you need to import the following file:

```ts
import type {} from '@mui/x-charts-pro/moduleAugmentation/rangeBarOnClick';
```

:::

## Animation

Animation in range bar charts works similarly to bar charts.

You read more about it in bar chart's [Animation](/x/react-charts/bars/#animation) page.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { HighlightScope } from '@mui/x-charts/context';
import {
  BarChartPremium,
  RangeBarSeries,
} from '@mui/x-charts-premium/BarChartPremium';
import { RangeBarValueType } from '@mui/x-charts-premium/models';

export default function RangeBarAnimation() {
  const [seriesNb, setSeriesNb] = React.useState(2);
  const [itemNb, setItemNb] = React.useState(5);
  const [skipAnimation, setSkipAnimation] = React.useState(false);

  const handleItemNbChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setItemNb(newValue);
  };
  const handleSeriesNbChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setSeriesNb(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <BarChartPremium
        height={300}
        series={series
          .slice(0, seriesNb)
          .map((s) => ({ ...s, data: s.data.slice(0, itemNb) }))}
        skipAnimation={skipAnimation}
        margin={{ left: 0 }}
      />
      <FormControlLabel
        checked={skipAnimation}
        control={
          <Checkbox onChange={(event) => setSkipAnimation(event.target.checked)} />
        }
        label="skipAnimation"
        labelPlacement="end"
      />
      <Typography id="input-item-number" gutterBottom>
        Number of items
      </Typography>
      <Slider
        value={itemNb}
        onChange={handleItemNbChange}
        valueLabelDisplay="auto"
        min={1}
        max={20}
        aria-labelledby="input-item-number"
      />
      <Typography id="input-series-number" gutterBottom>
        Number of series
      </Typography>
      <Slider
        value={seriesNb}
        onChange={handleSeriesNbChange}
        valueLabelDisplay="auto"
        min={1}
        max={10}
        aria-labelledby="input-series-number"
      />
    </Box>
  );
}

const highlightScope: HighlightScope = {
  highlight: 'series',
  fade: 'global',
};

const series = [
  {
    label: 'series 1',
    data: [
      [500, 2423],
      [300, 2210],
      [100, 764],
      [400, 1879],
      [200, 1478],
      [300, 1373],
      [500, 1891],
      [600, 2171],
      [100, 620],
      [300, 1269],
      [200, 724],
      [400, 1707],
      [300, 1188],
      [500, 1879],
      [100, 626],
      [400, 1635],
      [600, 2177],
      [100, 516],
      [500, 1793],
      [400, 1598],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 2',
    data: [
      [600, 2362],
      [500, 2254],
      [400, 1962],
      [300, 1336],
      [100, 586],
      [200, 1069],
      [600, 2194],
      [400, 1629],
      [600, 2173],
      [500, 2031],
      [400, 1757],
      [200, 862],
      [700, 2446],
      [200, 910],
      [700, 2430],
      [600, 2300],
      [200, 805],
      [500, 1835],
      [400, 1684],
      [600, 2197],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 3',
    data: [
      [300, 1145],
      [300, 1214],
      [200, 975],
      [600, 2266],
      [400, 1768],
      [700, 2341],
      [200, 747],
      [300, 1282],
      [500, 1780],
      [400, 1766],
      [600, 2115],
      [400, 1720],
      [300, 1057],
      [500, 2000],
      [400, 1716],
      [600, 2253],
      [100, 619],
      [400, 1626],
      [300, 1209],
      [500, 1786],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 4',
    data: [
      [600, 2361],
      [200, 979],
      [700, 2430],
      [400, 1768],
      [500, 1913],
      [700, 2342],
      [500, 1868],
      [300, 1319],
      [200, 1038],
      [600, 2139],
      [400, 1691],
      [200, 935],
      [600, 2262],
      [400, 1580],
      [100, 692],
      [400, 1559],
      [300, 1344],
      [300, 1442],
      [400, 1593],
      [500, 1889],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 5',
    data: [
      [200, 968],
      [300, 1371],
      [300, 1381],
      [300, 1060],
      [300, 1327],
      [200, 934],
      [500, 1779],
      [300, 1361],
      [200, 878],
      [300, 1055],
      [500, 1737],
      [700, 2380],
      [200, 875],
      [700, 2408],
      [300, 1066],
      [500, 1802],
      [300, 1442],
      [400, 1567],
      [400, 1552],
      [500, 1742],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 6',
    data: [
      [600, 2316],
      [500, 1845],
      [600, 2057],
      [300, 1479],
      [500, 1859],
      [300, 1015],
      [400, 1569],
      [300, 1448],
      [300, 1354],
      [300, 1007],
      [200, 799],
      [500, 1748],
      [300, 1454],
      [500, 1968],
      [300, 1129],
      [300, 1196],
      [600, 2158],
      [100, 540],
      [300, 1482],
      [200, 880],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 7',
    data: [
      [600, 2140],
      [600, 2082],
      [200, 708],
      [600, 2032],
      [100, 554],
      [300, 1365],
      [600, 2121],
      [400, 1639],
      [700, 2430],
      [700, 2440],
      [200, 814],
      [300, 1328],
      [200, 883],
      [500, 1811],
      [600, 2322],
      [500, 1743],
      [200, 700],
      [600, 2131],
      [300, 1473],
      [200, 957],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 8',
    data: [
      [300, 1074],
      [200, 744],
      [700, 2487],
      [200, 823],
      [600, 2252],
      [600, 2317],
      [600, 2139],
      [500, 1818],
      [600, 2256],
      [500, 1769],
      [300, 1123],
      [300, 1461],
      [100, 672],
      [300, 1335],
      [200, 960],
      [500, 1871],
      [600, 2305],
      [300, 1231],
      [600, 2005],
      [200, 908],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 9',
    data: [
      [500, 1792],
      [200, 886],
      [700, 2472],
      [400, 1546],
      [600, 2164],
      [600, 2323],
      [700, 2435],
      [300, 1268],
      [600, 2368],
      [600, 2158],
      [600, 2200],
      [300, 1316],
      [100, 552],
      [500, 1874],
      [500, 1771],
      [300, 1038],
      [500, 1838],
      [600, 2029],
      [500, 1793],
      [300, 1117],
    ] satisfies RangeBarValueType[],
  },
  {
    label: 'series 10',
    data: [
      [300, 1433],
      [300, 1161],
      [300, 1107],
      [400, 1517],
      [300, 1410],
      [300, 1058],
      [100, 676],
      [300, 1280],
      [500, 1936],
      [500, 1774],
      [100, 698],
      [500, 1721],
      [300, 1421],
      [200, 785],
      [500, 1752],
      [200, 800],
      [200, 990],
      [500, 1809],
      [500, 1985],
      [100, 665],
    ] satisfies RangeBarValueType[],
  },
].map((s) => ({ type: 'rangeBar', ...s, highlightScope }) satisfies RangeBarSeries);

```

## Composition

You can use the `ChartDataProviderPremium` to provide `series`, `xAxis`, and `yAxis` props for composition.

Besides the common chart components available for [composition](/x/react-charts/composition/), to compose a range bar chart you need to render the `RangeBarPlot` component to display the range bars and their labels.

Here's roughly a `BarChartPremium` is composed, which you can use as a reference:

```jsx
<ChartDataProviderPremium>
  <ChartsWrapper>
    <ChartsLegend />
    <ChartsSurface>
      <ChartsGrid />
      <g clipPath={`url(#${clipPathId})`}>
        <BarPlot />
        <RangeBarPlot />
        <ChartsOverlay />
        <ChartsAxisHighlight />
      </g>
      <ChartsAxis />
      <ChartsClipPath id={clipPathId} />
    </ChartsSurface>
    <ChartsTooltip />
  </ChartsWrapper>
</ChartDataProviderPremium>
```

In the example below, we follow a similar pattern and create a project schedule chart using range bars to represent task durations.

```tsx
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { RangeBarPlot, RangeBarSeries } from '@mui/x-charts-premium/BarChartPremium';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsClipPath } from '@mui/x-charts/ChartsClipPath';
import * as React from 'react';
import { useDataset } from '@mui/x-charts/hooks';
import { useTheme, styled } from '@mui/system';
import {
  ChartsTooltipContainer,
  useAxesTooltip,
  useItemTooltip,
} from '@mui/x-charts/ChartsTooltip';
import { ChartsAxisHighlight } from '@mui/x-charts/ChartsAxisHighlight';
import { ScatterValueType, XAxis, YAxis } from '@mui/x-charts/models';
import { rainbowSurgePalette } from '@mui/x-charts/colorPalettes';
import { ChartsWrapper } from '@mui/x-charts-pro/ChartsWrapper';
import { ChartsSurface } from '@mui/x-charts-pro/ChartsSurface';
import { ScatterPlot, ScatterSeries } from '@mui/x-charts/ScatterChart';
import { ChartDataProviderPremium } from '@mui/x-charts-premium/ChartDataProviderPremium';

const importantHappeningsLabels = [
  'Exploratory archaeology digs begin.',
  'South Boston Haul Road opens.',
  'New Broadway Bridge opens.\nLeverett Circle Connector Bridge opens.',
  'Leonard P. Zakim Bunker Hill Bridge completed.',
  'I-90 Connector from South Boston to Rt. 1A in East Boston opens in January.\nI-93 Northbound opens in March.\nI-93 Southbound opens in December.',
  'Tunnel from Storrow Drive to Leverett Circle Connector opens.',
  [
    'Full opening of I-93 South.',
    'Opening of Dewey Square Tunnel, including new entrance and exit ramps.',
    'Opening of the two cantilevered lanes on Leonard P. Zakim Bunker Hill Bridge.',
    'Opening of permanent ramps and roadways at I-90/I-93 Interchange and in other areas.',
  ].join('\n'),
  'Spectacle Island Park opens to the public.',
  'Restoration of Boston city streets.',
];
const importantHappenings = [
  { x: 1988, y: 3 },
  { x: 1993, y: 4 },
  { x: 1999, y: 5 },
  { x: 2002, y: 5 },
  { x: 2003, y: 5 },
  { x: 2004, y: 6 },
  { x: 2005, y: 6 },
  { x: 2006, y: 7 },
  { x: 2007, y: 8 },
] satisfies ScatterValueType[];

// Source: https://www.mass.gov/info-details/the-big-dig-project-background
const bigDigDataset = [
  {
    phase: 1,
    name: 'Conception & Initial Planning',
    startYear: 1970,
    endYear: 1982,
    duration: '~10 years',
    keyMilestones: [
      'Concept development to address Central Artery congestion',
      'Federal Highway Administration involvement',
    ],
  },
  {
    phase: 2,
    name: 'Planning & Federal Approval',
    startYear: 1982,
    endYear: 1987,
    duration: '5 years',
    keyMilestones: [
      '1982: Official planning begins',
      'Environmental Impact Statement preparation',
      '1985: Final EIS approval by FHWA',
      'April 1987: Congress approves federal funding and project scope',
    ],
  },
  {
    phase: 3,
    name: 'Design Development',
    startYear: 1987,
    endYear: 1991,
    duration: '4 years',
    keyMilestones: [
      'Detailed engineering and design work',
      'Permits and approvals',
      'Contract procurement preparation',
      'Route and interchange finalization',
    ],
  },
  {
    phase: 4,
    name: 'Ted Williams Tunnel Construction',
    startYear: 1991,
    endYear: 1995,
    duration: '4 years',
    keyMilestones: [
      'December 19, 1991: Official groundbreaking',
      'Underwater tunnel sections (steel tubes lowered by barges)',
      'December 1995: Ted Williams Tunnel opens (I-90 to Logan Airport)',
    ],
  },
  {
    phase: 5,
    name: 'Major Underground Construction',
    startYear: 1995,
    endYear: 2003,
    duration: '8 years',
    keyMilestones: [
      'Central Artery tunnel excavation',
      'Tunnel-jacking operations (freezing soil beneath rail lines)',
      'Bridge construction (Zakim Bunker Hill Bridge)',
      'Four major highway interchanges',
    ],
  },
  {
    phase: 6,
    name: 'Systems Installation & Testing',
    startYear: 2003,
    endYear: 2005,
    duration: '2-3 years',
    keyMilestones: [
      'Tunnel systems (ventilation, lighting, fire safety)',
      'Traffic management systems (1,400+ loop detectors, 430 CCTV cameras)',
      'Operations Control Center setup',
    ],
  },
  {
    phase: 7,
    name: 'Final Construction & Opening',
    startYear: 2005,
    endYear: 2006,
    duration: '1-2 years',
    keyMilestones: [
      'January 13, 2006: Final ramp opens (Exit 20B)',
      'Elevated highway demolition begins',
      "O'Neill Tunnel dedication",
    ],
  },
  {
    phase: 8,
    name: 'Rose Kennedy Greenway Development',
    startYear: 2006,
    endYear: 2007,
    duration: '1-2 years',
    keyMilestones: [
      'Creation of 300+ acres of open space',
      'Park and public space development',
      'December 31, 2007: Official project completion',
    ],
  },
  {
    phase: 9,
    name: 'Claims Resolution & Final Closeout',
    startYear: 2007,
    endYear: 2008,
    duration: '1 year',
    keyMilestones: [
      'Legal settlements ($407M from Bechtel/Parsons Brinckerhoff)',
      'Documentation finalization',
      'Warranty period begins',
    ],
  },
];

const xAxis = [
  {
    id: 'x',
    scaleType: 'linear',
    valueFormatter: (value) => value.toString(),
    label: 'Year',
  },
] satisfies XAxis[];
const yAxis = [
  {
    id: 'y',
    scaleType: 'band',
    dataKey: 'phase',
    label: 'Project Phase',
    width: 40,
  },
] satisfies YAxis[];

export default function RangeBarProjectSchedule() {
  const clipPathId = React.useId();
  const theme = useTheme();
  const palette = rainbowSurgePalette(theme.palette.mode);
  const colors = [palette[4], palette[1], palette[0]];

  const series = [
    {
      type: 'rangeBar',
      datasetKeys: { start: 'startYear', end: 'endYear' },
      xAxisId: 'x',
      yAxisId: 'y',
      layout: 'horizontal',
      colorGetter: (data) => {
        if (data.dataIndex < 3) {
          return colors[0];
        }

        if (data.dataIndex < 8) {
          return colors[1];
        }

        return colors[2];
      },
    } satisfies RangeBarSeries,
    {
      type: 'scatter',
      data: importantHappenings,
      color: palette[2],
    } satisfies ScatterSeries,
  ];

  return (
    <ChartDataProviderPremium
      dataset={bigDigDataset}
      xAxis={xAxis}
      yAxis={yAxis}
      series={series}
      height={300}
    >
      <ChartsWrapper legendPosition={{ vertical: 'bottom' }}>
        <ChartsSurface>
          <ChartsXAxis />
          <ChartsYAxis />
          <ChartsClipPath id={clipPathId} />
          <g clipPath={`url(#${clipPathId})`}>
            <RangeBarPlot skipAnimation />
            <ScatterPlot />
            <ChartsAxisHighlight y="band" />
          </g>
          <ChartsTooltipContainer>
            <TooltipContent />
          </ChartsTooltipContainer>
        </ChartsSurface>
        <Legend
          series={[
            {
              label: 'Phases 1-3: Planning & Initial Construction',
              color: colors[0],
            },
            {
              label: 'Phases 4-8: Major Construction',
              color: colors[1],
            },
            {
              label: 'Phase 9: Finalization & Closeout',
              color: colors[2],
            },
          ]}
        />
      </ChartsWrapper>
    </ChartDataProviderPremium>
  );
}

const TooltipContainer = styled('div')(({ theme }) => ({
  background: theme.palette.background.paper,
  border: `1px solid ${theme.palette.divider}`,
  padding: theme.spacing(1),
  borderRadius: theme.shape.borderRadius,
}));

function TooltipContent() {
  const dataset = useDataset<typeof bigDigDataset>();
  const itemTooltipData = useItemTooltip();
  const axesTooltipData = useAxesTooltip();

  if (itemTooltipData) {
    return <HappeningTooltip />;
  }

  const dataIndex = axesTooltipData?.[0]?.dataIndex;

  if (dataIndex === undefined) {
    return null;
  }

  const phase = dataset![dataIndex];

  return (
    <TooltipContainer>
      <Typography>
        Phase {phase.phase}: <strong>{phase.name}</strong> ({phase.startYear} -{' '}
        {phase.endYear})
      </Typography>
      <Typography variant="body2">Key Milestones:</Typography>
      <ul>
        {phase.keyMilestones.map((milestone, index) => (
          <li key={index}>
            <Typography variant="body2">{milestone}</Typography>
          </li>
        ))}
      </ul>
    </TooltipContainer>
  );
}

function HappeningTooltip() {
  const tooltipData = useItemTooltip<'scatter'>();
  const dataIndex = tooltipData?.identifier.dataIndex;

  if (dataIndex === undefined) {
    return null;
  }

  const happening = importantHappenings[dataIndex];

  return (
    <TooltipContainer>
      <Typography fontWeight="bold">{happening.x}</Typography>
      <Typography>
        {importantHappeningsLabels[dataIndex].split('\n').map((line, index) => (
          <React.Fragment key={index}>
            <span>{line}</span>
            <br />
          </React.Fragment>
        ))}
      </Typography>
    </TooltipContainer>
  );
}

function Legend({ series }: { series: { label: string; color: string }[] }) {
  return (
    <Stack direction="row" flexWrap="wrap" columnGap={2} justifyContent="center">
      {series.map((aSeries, index) => (
        <Stack key={index} alignItems="center" direction="row" marginBottom={0.5}>
          <div
            style={{
              width: 16,
              height: 16,
              backgroundColor: aSeries.color,
              marginRight: 8,
              borderRadius: 4,
            }}
          />
          <Typography variant="caption">{aSeries.label}</Typography>
        </Stack>
      ))}
    </Stack>
  );
}

```
