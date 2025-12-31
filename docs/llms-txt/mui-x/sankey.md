# Source: https://mui.com/x/react-charts/sankey.md

---
title: React Sankey chart
productId: x-charts
components: SankeyChart, SankeyPlot, SankeyTooltip, SankeyTooltipContent
---

# Charts - Sankey [<span class="plan-pro"></span>](/x/introduction/licensing/#pro-plan 'Pro plan')🧪

Sankey charts are great for visualizing flows between different elements.

:::info
This feature is in preview. It is ready for production use, but its API, visuals and behavior may change in future minor or patch releases.
:::

## Basics

The Sankey chart requires a specific data structure with two main parts: `nodes` and `links`.

- The `nodes` array is optional but allows the customization of individual nodes.
- The `links` array defines the connections between nodes and must specify `source`, `target`, and `value`.

### Automatic nodes

If a node is referenced in `links` but not defined in the `nodes` array, it is automatically created with the ID as the label.

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

export default function SankeyBasicDataStructure() {
  return (
    <SankeyChart
      height={250}
      series={{
        data: {
          links: [
            { source: 'A', target: 'B', value: 10 },
            { source: 'A', target: 'C', value: 5 },
            { source: 'B', target: 'D', value: 8 },
            { source: 'C', target: 'D', value: 3 },
          ],
        },
      }}
    />
  );
}

```

### Explicit nodes

When an explicit node definition is provided, it allows customizing labels and colors for each node.

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

export default function SankeyDetailedDataStructure() {
  return (
    <SankeyChart
      height={250}
      series={{
        data: {
          nodes: [
            { id: 'source', label: 'Energy Source', color: '#e57373' },
            { id: 'oil', label: 'Oil Production', color: '#f06292' },
            { id: 'gas', label: 'Natural Gas', color: '#ba68c8' },
            { id: 'usage', label: 'Energy Usage', color: '#64b5f6' },
          ],
          links: [
            { source: 'source', target: 'oil', value: 30, color: '#e57373' },
            { source: 'source', target: 'gas', value: 20, color: '#e57373' },
            { source: 'oil', target: 'usage', value: 25, color: '#f06292' },
            { source: 'gas', target: 'usage', value: 15, color: '#ba68c8' },
          ],
        },
      }}
    />
  );
}

```

## Styling

### Default node styles

Default styles can be applied to all nodes using the `nodeOptions` prop:

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import ChartsUsageDemo from 'docsx/src/modules/components/ChartsUsageDemo';

const data = {
  nodes: [
    { id: 'A', label: 'Source A' },
    { id: 'B', label: 'Process B' },
    { id: 'C', label: 'Process C' },
    { id: 'D', label: 'Output D' },
  ],
  links: [
    { source: 'A', target: 'B', value: 15 },
    { source: 'A', target: 'C', value: 10 },
    { source: 'B', target: 'D', value: 12 },
    { source: 'C', target: 'D', value: 8 },
  ],
};

export default function SankeyNodeStyling() {
  return (
    <ChartsUsageDemo
      componentName="SankeyChart"
      data={{
        color: {
          knob: 'input',
          defaultValue: '#1976d2',
        },
        width: {
          knob: 'number',
          defaultValue: 15,
          min: 5,
          max: 50,
        },
        padding: {
          knob: 'number',
          defaultValue: 10,
          min: 0,
          max: 50,
        },
        showLabels: {
          knob: 'switch',
          defaultValue: true,
        },
      }}
      renderDemo={(props) => (
        <SankeyChart
          height={300}
          series={{
            data,
            nodeOptions: {
              color: props.color,
              width: props.width,
              padding: props.padding,
              showLabels: props.showLabels,
            },
          }}
        />
      )}
      getCode={({ props }) => {
        return `import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

<SankeyChart
  height={300}
  series={{
    data: {
      // ... your data
    },
    nodeOptions: {
      color: '${props.color}',
      width: ${props.width},
      padding: ${props.padding},
      showLabels: ${props.showLabels},
    },
  }}
/>`;
      }}
    />
  );
}

```

### Default link styles

Default styles can be applied to all links using the `linkOptions` prop:

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import ChartsUsageDemo from 'docsx/src/modules/components/ChartsUsageDemo';

const data = {
  nodes: [
    { id: 'A', label: 'Source A' },
    { id: 'B', label: 'Process B' },
    { id: 'C', label: 'Process C' },
    { id: 'D', label: 'Output D' },
  ],
  links: [
    { source: 'A', target: 'B', value: 15 },
    { source: 'A', target: 'C', value: 10 },
    { source: 'B', target: 'D', value: 12 },
    { source: 'C', target: 'D', value: 8 },
  ],
};

export default function SankeyLinkStyling() {
  return (
    <ChartsUsageDemo
      componentName="SankeyChart"
      data={{
        color: {
          knob: 'input',
          defaultValue: '#90a4ae',
        },
        opacity: {
          knob: 'number',
          defaultValue: 0.8,
          min: 0.1,
          max: 1,
          step: 0.1,
        },
        showValues: {
          knob: 'switch',
          defaultValue: true,
        },
      }}
      renderDemo={(props) => (
        <SankeyChart
          height={300}
          series={{
            data,
            linkOptions: {
              color: props.color,
              opacity: props.opacity,
              showValues: props.showValues,
            },
            nodeOptions: {
              showLabels: false,
            },
          }}
        />
      )}
      getCode={({ props }) => {
        return `import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

<SankeyChart
  height={300}
  series={{
    data: {
      // ... your data
    },
    linkOptions: {
      color: '${props.color}',
      opacity: ${props.opacity},
      showValues: ${props.showValues},
    },
  }}
/>`;
      }}
    />
  );
}

```

### Link color keywords

Link colors can use special keyword values to automatically inherit colors from their connected nodes:

- `'source'` - The link inherits the color of its source node
- `'target'` - The link inherits the color of its target node

This feature works for both individual link colors and the default link color in `linkOptions`:

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import ChartsUsageDemo from 'docsx/src/modules/components/ChartsUsageDemo';

const data = {
  nodes: [
    { id: 'Input', label: 'Input' },
    { id: 'ProcessA', label: 'Process A' },
    { id: 'ProcessB', label: 'Process B' },
    { id: 'Output', label: 'Output' },
  ],
  links: [
    { source: 'Input', target: 'ProcessA', value: 30 },
    { source: 'Input', target: 'ProcessB', value: 20 },
    { source: 'ProcessA', target: 'Output', value: 25 },
    { source: 'ProcessB', target: 'Output', value: 15 },
  ],
};

export default function SankeyLinkKeywordColors() {
  return (
    <ChartsUsageDemo
      componentName="SankeyChart"
      data={{
        linkColorMode: {
          knob: 'radio',
          options: ['default', 'source', 'target'],
          defaultValue: 'source',
        },
      }}
      renderDemo={(props) => {
        const linkColor =
          props.linkColorMode === 'default' ? undefined : props.linkColorMode;

        return (
          <SankeyChart
            height={300}
            series={{
              data,
              nodeOptions: {
                showLabels: true,
              },
              linkOptions: {
                color: linkColor,
                opacity: 0.6,
              },
            }}
          />
        );
      }}
      getCode={({ props }) => {
        const linkColor =
          props.linkColorMode === 'default' ? undefined : props.linkColorMode;

        return `import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

<SankeyChart
  height={300}
  series={{
    data,
    linkOptions: {
      color: ${linkColor ? `'${linkColor}'` : 'undefined'},
      opacity: 0.6,
    },
  }}
/>`;
      }}
    />
  );
}

```

### Node alignment

The node alignment determines how nodes are positioned within the Sankey chart. The layout follows these principles:

- Nodes are grouped into columns based on the graph structure
- Source nodes always appear to the left of their target nodes
- Some nodes have fixed positions (determined by the graph topology), while others can be positioned more flexibly (affected by alignment)

For example, in the demonstration below:

- Nodes A, B, D, G, I, and K have fixed positions because moving them would require creating a new column
- Node E can be placed in either the first or second column
- Node F is flexible and can be positioned in columns 4, 5, or 6

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import { Stack } from '@mui/system';
import Typography from '@mui/material/Typography';

export default function SankeyNodeAlignment() {
  return (
    <Stack spacing={2} width={'100%'}>
      <Stack flex={1} direction={['column', 'column', 'row']} spacing={2}>
        <Stack width={'100%'}>
          <Typography>Left</Typography>
          <SankeyChart
            height={200}
            series={{
              data,
              nodeOptions: {
                align: 'left',
                sort: nodeSortFunction,
              },
            }}
          />
        </Stack>
        <Stack width={'100%'}>
          <Typography>Right</Typography>
          <SankeyChart
            height={200}
            series={{
              data,
              nodeOptions: {
                align: 'right',
                sort: nodeSortFunction,
              },
            }}
          />
        </Stack>
      </Stack>
      <Stack flex={1} direction={['column', 'column', 'row']} spacing={2}>
        <Stack width={'100%'}>
          <Typography>Justify</Typography>
          <SankeyChart
            height={200}
            series={{
              data,
              nodeOptions: {
                align: 'justify',
                sort: nodeSortFunction,
              },
            }}
          />
        </Stack>
        <Stack width={'100%'}>
          <Typography>Center</Typography>
          <SankeyChart
            height={200}
            series={{
              data,
              nodeOptions: {
                align: 'center',
                sort: nodeSortFunction,
              },
            }}
          />
        </Stack>
      </Stack>
    </Stack>
  );
}

const data = {
  nodes: [],
  links: [
    { source: 'A', target: 'B', value: 2 },
    { source: 'B', target: 'D', value: 4 },
    { source: 'E', target: 'D', value: 4 },
    { source: 'D', target: 'F', value: 1 },
    { source: 'D', target: 'G', value: 7 },
    { source: 'G', target: 'H', value: 2 },
    { source: 'G', target: 'I', value: 5 },
    { source: 'I', target: 'J', value: 3 },
    { source: 'I', target: 'K', value: 2 },
  ],
};

// Sort nodes alphabetically by label
const nodeSortFunction = (a: any, b: any) => {
  const labelA = a.label || a.id;
  const labelB = b.label || b.id;
  return labelA.localeCompare(labelB);
};

```

### Curve correction

The `curveCorrection` prop adjusts the look of the links between nodes by modifying the x-coordinate of the control points in the curve function.
In some instances, this creates better-looking connections but is dependent on the graph layout, and is especially impacted by the chart height.

Higher values create plumper links, while lower values create thinner connections. The default value is `10`.

```tsx
import * as React from 'react';
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';

const data = {
  links: [
    { source: 'C', target: 'Y', value: 10 },
    { source: 'A', target: 'X', value: 25 },
    { source: 'B', target: 'X', value: 10 },
    { source: 'X', target: 'Z', value: 25 },
    { source: 'Y', target: 'Z', value: 8 },
    { source: 'B', target: 'Y', value: 5 },
  ],
};

export default function SankeyCurveCorrection() {
  const [curveCorrection, setCurveCorrection] = React.useState(10);

  return (
    <Box sx={{ width: '100%' }}>
      <SliderHandle
        curveCorrection={curveCorrection}
        setCurveCorrection={setCurveCorrection}
      />
      <SankeyChart
        height={400}
        series={{
          data,
          linkOptions: {
            curveCorrection,
          },
        }}
      />
    </Box>
  );
}

function SliderHandle(props: {
  curveCorrection: number;
  setCurveCorrection: (value: number) => void;
}) {
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
        Curve Correction: {props.curveCorrection}
      </Typography>
      <Slider
        value={props.curveCorrection}
        onChange={(_, value) => props.setCurveCorrection(value as number)}
        min={-20}
        max={20}
        step={1}
        sx={{ mb: 3 }}
        marks={[
          { value: -20, label: '-20' },
          { value: -10, label: '-10' },
          { value: 0, label: '0' },
          { value: 5, label: '5' },
          { value: 10, label: '10 (default)' },
          { value: 20, label: '20' },
        ]}
      />
    </React.Fragment>
  );
}

```

## Value formatting

You can customize how values are displayed in tooltips and labels using the `valueFormatter` prop.
This function receives the numeric value and a context object that provides information about what type of element is being formatted.

The context object contains:

- `location`: either `'tooltip'` or `'label'` to indicate where the formatted value is used
- `type`: either `'node'` or `'link'` to indicate what is being formatted
- `nodeId`: for nodes, the ID of the node being formatted
- `sourceId` and `targetId`: for links, the IDs of the source and target nodes

In the following demo, the value formatter adds relevant units to the values.
And when pointer is on top of a node, it display "total" to the tooltip.

```tsx
import {
  Unstable_SankeyChart as SankeyChart,
  type SankeyValueFormatterContext,
} from '@mui/x-charts-pro/SankeyChart';

const data = {
  nodes: [
    { id: 'Coal', label: 'Coal' },
    { id: 'Natural Gas', label: 'Natural Gas' },
    { id: 'Nuclear', label: 'Nuclear' },
    { id: 'Hydro', label: 'Hydro' },
    { id: 'Wind', label: 'Wind' },
    { id: 'Solar', label: 'Solar' },
    { id: 'Electricity', label: 'Electricity' },
    { id: 'Residential', label: 'Residential' },
    { id: 'Commercial', label: 'Commercial' },
    { id: 'Industrial', label: 'Industrial' },
  ],
  links: [
    { source: 'Coal', target: 'Electricity', value: 300 },
    { source: 'Natural Gas', target: 'Electricity', value: 400 },
    { source: 'Nuclear', target: 'Electricity', value: 200 },
    { source: 'Hydro', target: 'Electricity', value: 100 },
    { source: 'Wind', target: 'Electricity', value: 150 },
    { source: 'Solar', target: 'Electricity', value: 80 },
    { source: 'Electricity', target: 'Residential', value: 450 },
    { source: 'Electricity', target: 'Commercial', value: 350 },
    { source: 'Electricity', target: 'Industrial', value: 430 },
  ],
};

export default function SankeyValueFormatter() {
  return (
    <SankeyChart
      height={300}
      series={{
        data,
        valueFormatter: (value: number, context: SankeyValueFormatterContext) => {
          // Format the value as energy units
          const formatted =
            value >= 1000 ? `${(value / 1000).toFixed(1)} GWh` : `${value} MWh`;

          // You can customize formatting based on context type
          if (context.type === 'link') {
            return `${formatted}`;
          }

          return `${formatted} total`;
        },
        linkOptions: {
          showValues: true,
        },
      }}
    />
  );
}

```

## Sorting

Nodes are displayed in the same order as they are defined in the `nodes` array.
If a `nodes` array isn't provided, nodes are rendered according to the order in which they are referenced in the `links` array.

To dynamically customize the order, use the sorting functions for the element that needs sorting.

### Node sorting

The `nodeOptions.sort` property controls the vertical order of nodes within each column.

It accepts the following values:

- A **function** that receives two `SankeyLayoutNode` objects and returns a number (similar to [`Array.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#comparefn))
- `'auto'` (default): Uses the automatic sorting behavior, which aims to minimize links crossing each other
- `'fixed'`: Preserves the order from the `nodes` array, disabling automatic sorting

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import Typography from '@mui/material/Typography';

const data = {
  nodes: [
    { id: 'C' },
    { id: 'B' },
    { id: 'A' },
    { id: 'X' },
    { id: 'Y' },
    { id: 'Z' },
  ],
  links: [
    { source: 'C', target: 'Y', value: 10 },
    { source: 'A', target: 'X', value: 25 },
    { source: 'B', target: 'X', value: 10 },
    { source: 'X', target: 'Z', value: 25 },
    { source: 'Y', target: 'Z', value: 8 },
    { source: 'B', target: 'Y', value: 5 },
  ],
};

// Sort nodes alphabetically by label
const nodeSortFunction = (a: any, b: any) => {
  const labelA = a.label || a.id;
  const labelB = b.label || b.id;
  return labelB.localeCompare(labelA);
};

export default function SankeyNodeSorting() {
  return (
    <div
      style={{
        gap: '24px',
        display: 'flex',
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'center',
      }}
    >
      <div>
        <Typography variant="h6" gutterBottom>
          auto (default)
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            nodeOptions: {
              sort: 'auto',
            },
          }}
        />
      </div>

      <div>
        <Typography variant="h6" gutterBottom>
          fixed
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            nodeOptions: {
              sort: 'fixed',
            },
          }}
        />
      </div>

      <div>
        <Typography variant="h6" gutterBottom>
          Custom Function
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            nodeOptions: {
              sort: nodeSortFunction,
            },
          }}
        />
      </div>
    </div>
  );
}

```

### Link sorting

The `linkOptions.sort` property controls the order of links emanating from each node.

It accepts the following values:

- A **function** that receives two `SankeyLayoutLink` objects and returns a number
- `'auto'` (default): Uses the automatic sorting behavior, which aims to minimize links crossing each other
- `'fixed'`: Preserves the order from the `links` array, disabling automatic sorting

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import Typography from '@mui/material/Typography';

const data = {
  links: [
    { source: 'C', target: 'Y', value: 10 },
    { source: 'B', target: 'X', value: 10 },
    { source: 'B', target: 'Y', value: 5 },
    { source: 'X', target: 'Z', value: 25 },
    { source: 'Y', target: 'Z', value: 8 },
    { source: 'A', target: 'X', value: 25 },
  ],
};

// Sort links by value (descending)
const linkSortFunction = (a: any, b: any) => b.value - a.value;

export default function SankeyLinkSorting() {
  return (
    <div
      style={{
        gap: '24px',
        display: 'flex',
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'center',
      }}
    >
      <div>
        <Typography variant="h6" gutterBottom>
          auto (default)
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            linkOptions: {
              sort: 'auto',
            },
          }}
        />
      </div>

      <div>
        <Typography variant="h6" gutterBottom>
          fixed
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            linkOptions: {
              sort: 'fixed',
            },
          }}
        />
      </div>

      <div>
        <Typography variant="h6" gutterBottom>
          Custom Function
        </Typography>
        <SankeyChart
          height={300}
          series={{
            data,
            linkOptions: {
              sort: linkSortFunction,
            },
          }}
        />
      </div>
    </div>
  );
}

```

## Layout iterations

The `iterations` prop controls how many times the layout algorithm runs to optimize node positioning. More iterations generally result in better layouts but take longer to compute.

```tsx
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';
import ChartsUsageDemo from 'docsx/src/modules/components/ChartsUsageDemo';

const data = {
  nodes: [
    { id: 'A', label: 'Energy' },
    { id: 'B', label: 'Coal' },
    { id: 'C', label: 'Gas' },
    { id: 'D', label: 'Oil' },
    { id: 'E', label: 'Electricity' },
    { id: 'F', label: 'Heat' },
    { id: 'G', label: 'Residential' },
    { id: 'H', label: 'Commercial' },
    { id: 'I', label: 'Industrial' },
  ],
  links: [
    { source: 'A', target: 'B', value: 30 },
    { source: 'A', target: 'C', value: 25 },
    { source: 'A', target: 'D', value: 20 },
    { source: 'B', target: 'E', value: 25 },
    { source: 'C', target: 'E', value: 20 },
    { source: 'C', target: 'F', value: 5 },
    { source: 'D', target: 'F', value: 18 },
    { source: 'E', target: 'G', value: 15 },
    { source: 'E', target: 'H', value: 20 },
    { source: 'E', target: 'I', value: 10 },
    { source: 'F', target: 'G', value: 8 },
    { source: 'F', target: 'H', value: 10 },
    { source: 'F', target: 'I', value: 5 },
  ],
};

export default function SankeyIterations() {
  return (
    <ChartsUsageDemo
      componentName="SankeyChart"
      data={{
        iterations: {
          knob: 'slider',
          defaultValue: 32,
          min: 1,
          max: 100,
        },
      }}
      renderDemo={(props) => (
        <SankeyChart
          height={400}
          series={{
            data,
            iterations: props.iterations,
          }}
        />
      )}
      getCode={({ props }) => {
        return `import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

<SankeyChart
  height={400}
  series={{
    data: {
      // ... your data
    },
    iterations: ${props.iterations},
  }}
/>`;
      }}
    />
  );
}

```

## Interaction

### Click event

You can use the `onNodeClick` and `onLinkClick` props to handle click events on both nodes and links in the Sankey chart. The callback receives the mouse event and a `SankeyNodeIdentifierWithData` or `SankeyLinkIdentifierWithData` respectively, both of which contain information about the clicked item.

The `SankeyItemIdentifierWithData` type is a union of `SankeyNodeIdentifierWithData` and `SankeyLinkIdentifierWithData`, allowing you to handle both types of items in a single callback if needed.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import UndoOutlinedIcon from '@mui/icons-material/UndoOutlined';
import {
  Unstable_SankeyChart as SankeyChart,
  SankeyItemIdentifier,
} from '@mui/x-charts-pro/SankeyChart';
import { HighlightedCode } from '@mui/docs/HighlightedCode';

const getCircularReplacer = () => {
  const seen = new WeakSet();
  return (key: string, value: any) => {
    if (key === 'source' || key === 'target') {
      return '(Circular Node)';
    }
    if (key === 'sourceLinks' || key === 'targetLinks') {
      return '[...(Circular Links)]';
    }

    if (typeof value === 'object' && value !== null) {
      if (seen.has(value)) {
        return undefined;
      }
      seen.add(value);
    }
    return value;
  };
};

const sankeyChartsParams = {
  series: {
    data: {
      nodes: [
        { id: 'Coal', label: 'Coal' },
        { id: 'Natural Gas', label: 'Natural Gas' },
        { id: 'Nuclear', label: 'Nuclear' },
        { id: 'Hydro', label: 'Hydro' },
        { id: 'Wind', label: 'Wind' },
        { id: 'Solar', label: 'Solar' },
        { id: 'Electricity', label: 'Electricity' },
        { id: 'Residential', label: 'Residential' },
        { id: 'Commercial', label: 'Commercial' },
        { id: 'Industrial', label: 'Industrial' },
      ],
      links: [
        { source: 'Coal', target: 'Electricity', value: 30 },
        { source: 'Natural Gas', target: 'Electricity', value: 40 },
        { source: 'Nuclear', target: 'Electricity', value: 20 },
        { source: 'Hydro', target: 'Electricity', value: 10 },
        { source: 'Wind', target: 'Electricity', value: 15 },
        { source: 'Solar', target: 'Electricity', value: 8 },
        { source: 'Electricity', target: 'Residential', value: 45 },
        { source: 'Electricity', target: 'Commercial', value: 35 },
        { source: 'Electricity', target: 'Industrial', value: 43 },
      ],
    },
    highlightScope: {
      highlight: 'item',
    },
  },
  height: 400,
  margin: { left: 20, right: 120 },
} as const;

export default function SankeyClick() {
  const [itemData, setItemData] = React.useState<SankeyItemIdentifier>();

  return (
    <Stack
      direction={{ xs: 'column', md: 'row' }}
      spacing={{ xs: 0, md: 4 }}
      sx={{ width: '100%' }}
    >
      <Box sx={{ flexGrow: 1 }}>
        <SankeyChart
          {...sankeyChartsParams}
          onNodeClick={(event, d) => setItemData(d)}
          onLinkClick={(event, d) => setItemData(d)}
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
            }}
          >
            <UndoOutlinedIcon fontSize="small" />
          </IconButton>
        </Box>
        <HighlightedCode
          code={`// Data from item click
${itemData ? JSON.stringify(itemData, getCircularReplacer(), 2) : '// The data will appear here'}
`}
          language="json"
          copyButtonHidden
        />
      </Stack>
    </Stack>
  );
}

```

### Highlighting

You can highlight nodes and links by hovering over them or by controlling the highlighting programmatically. When an item is highlighted, other items can be faded out to improve focus.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { Unstable_SankeyChart as SankeyChart } from '@mui/x-charts-pro/SankeyChart';

export default function SankeyHighlighting() {
  const [nodeHighlight, setNodeHighlight] = React.useState<
    'nodes' | 'links' | 'incoming' | 'outgoing' | 'none'
  >('links');
  const [nodeFade, setNodeFade] = React.useState<'global' | 'none'>('global');
  const [linkHighlight, setLinkHighlight] = React.useState<
    'links' | 'nodes' | 'source' | 'target' | 'none'
  >('links');
  const [linkFade, setLinkFade] = React.useState<'global' | 'none'>('global');

  return (
    <Stack spacing={2} sx={{ width: '100%' }}>
      <Box sx={{ width: '100%' }}>
        <SankeyChart
          series={{
            data: {
              nodes: [
                { id: 'A', label: 'A' },
                { id: 'B', label: 'B' },
                { id: 'C', label: 'C' },
                { id: 'D', label: 'D' },
                { id: 'E', label: 'E' },
                { id: 'F', label: 'F' },
              ],
              links: [
                { source: 'A', target: 'D', value: 3 },
                { source: 'A', target: 'E', value: 4 },
                { source: 'B', target: 'D', value: 2 },
                { source: 'B', target: 'E', value: 3 },
                { source: 'C', target: 'E', value: 2 },
                { source: 'D', target: 'F', value: 5 },
                { source: 'E', target: 'F', value: 9 },
              ],
            },
            nodeOptions: {
              highlight: nodeHighlight,
              fade: nodeFade,
            },
            linkOptions: {
              highlight: linkHighlight,
              fade: linkFade,
            },
          }}
          height={300}
          margin={{ left: 80, right: 80 }}
        />
      </Box>
      <Stack
        direction={{ xs: 'column', sm: 'row' }}
        spacing={2}
        sx={{ width: '100%' }}
      >
        <Stack spacing={2} sx={{ flex: 1 }}>
          <TextField
            select
            label="Node Highlight"
            value={nodeHighlight}
            onChange={(event) =>
              setNodeHighlight(
                event.target.value as
                  | 'nodes'
                  | 'links'
                  | 'incoming'
                  | 'outgoing'
                  | 'none',
              )
            }
            fullWidth
          >
            <MenuItem value="nodes">nodes</MenuItem>
            <MenuItem value="links">links</MenuItem>
            <MenuItem value="incoming">incoming</MenuItem>
            <MenuItem value="outgoing">outgoing</MenuItem>
            <MenuItem value="none">none</MenuItem>
          </TextField>
          <TextField
            select
            label="Node Fade"
            value={nodeFade}
            onChange={(event) =>
              setNodeFade(event.target.value as 'global' | 'none')
            }
            fullWidth
          >
            <MenuItem value="global">global</MenuItem>
            <MenuItem value="none">none</MenuItem>
          </TextField>
        </Stack>
        <Stack spacing={2} sx={{ flex: 1 }}>
          <TextField
            select
            label="Link Highlight"
            value={linkHighlight}
            onChange={(event) =>
              setLinkHighlight(
                event.target.value as
                  | 'links'
                  | 'nodes'
                  | 'source'
                  | 'target'
                  | 'none',
              )
            }
            fullWidth
          >
            <MenuItem value="links">links</MenuItem>
            <MenuItem value="nodes">nodes</MenuItem>
            <MenuItem value="source">source</MenuItem>
            <MenuItem value="target">target</MenuItem>
            <MenuItem value="none">none</MenuItem>
          </TextField>
          <TextField
            select
            label="Link Fade"
            value={linkFade}
            onChange={(event) =>
              setLinkFade(event.target.value as 'global' | 'none')
            }
            fullWidth
          >
            <MenuItem value="global">global</MenuItem>
            <MenuItem value="none">none</MenuItem>
          </TextField>
        </Stack>
      </Stack>
    </Stack>
  );
}

```

The highlighting behavior is configured separately for nodes and links through their respective options:

#### Node highlighting

Configure node highlighting behavior using `nodeOptions.highlight` and `nodeOptions.fade`:

- `nodeOptions.highlight`: Controls what gets highlighted when selecting a node
  - `'nodes'`: Highlight only the selected node
  - `'links'`: Highlight all links connected to the selected node
  - `'incoming'`: Highlight only incoming links to the selected node
  - `'outgoing'`: Highlight only outgoing links from the selected node
  - `'none'`: Disable node highlighting
- `nodeOptions.fade`: Controls the fade effect
  - `'global'`: Fade all non-highlighted items when a node is highlighted
  - `'none'`: No fade effect

#### Link highlighting

Configure link highlighting behavior using `linkOptions.highlight` and `linkOptions.fade`:

- `linkOptions.highlight`: Controls what gets highlighted when selecting a link
  - `'links'`: Highlight only the selected link
  - `'nodes'`: Highlight both source and target nodes of the selected link
  - `'source'`: Highlight only the source node of the selected link
  - `'target'`: Highlight only the target node of the selected link
  - `'none'`: Disable link highlighting
- `linkOptions.fade`: Controls the fade effect
  - `'global'`: Fade all non-highlighted items when a link is highlighted
  - `'none'`: No fade effect

### Controlled highlighting

You can control the highlighting externally using the `highlightedItem` and `onHighlightChange` props. This is useful when you want to programmatically highlight specific nodes or links, or synchronize highlighting with other UI elements.

The `highlightedItem` prop accepts either a `SankeyNodeIdentifier` or a `SankeyLinkIdentifier`:

For nodes:

```ts
{
  type: 'sankey',
  seriesId: string,
  subType: 'node',
  nodeId: string | number,
}
```

For links:

```ts
{
  type: 'sankey',
  seriesId: string,
  subType: 'link',
  sourceId: string | number,
  targetId: string | number,
}
```

The `onHighlightChange` callback is called whenever the highlighted item changes (either through user interaction or programmatic control), allowing you to keep your state synchronized.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import {
  Unstable_SankeyChart as SankeyChart,
  type SankeyNodeIdentifier,
  type SankeyLinkIdentifier,
} from '@mui/x-charts-pro/SankeyChart';

export default function SankeyControlledHighlight() {
  type HighlightItem = SankeyNodeIdentifier | SankeyLinkIdentifier | null;
  const [highlightedItem, setHighlightedItem] = React.useState<HighlightItem>({
    type: 'sankey',
    seriesId: 'auto-generated-id',
    subType: 'node',
    nodeId: 'A',
  });

  const handleHighlightChange: (item: HighlightItem) => void = (item) => {
    setHighlightedItem(item);
  };

  const handleToggleChange = (
    _event: React.MouseEvent<HTMLElement>,
    newValue: string | null,
  ) => {
    if (newValue === null) {
      setHighlightedItem(null);
      return;
    }

    if (newValue.startsWith('node-')) {
      const nodeId = newValue.replace('node-', '');
      setHighlightedItem({
        type: 'sankey',
        seriesId: 'auto-generated-id',
        subType: 'node',
        nodeId,
      });
    } else if (newValue.startsWith('link-')) {
      const [source, target] = newValue.replace('link-', '').split('-');
      setHighlightedItem({
        type: 'sankey',
        seriesId: 'auto-generated-id',
        subType: 'link',
        sourceId: source,
        targetId: target,
      });
    }
  };

  const getCurrentValue = () => {
    if (!highlightedItem) {
      return null;
    }
    if (highlightedItem.subType === 'node') {
      return `node-${highlightedItem.nodeId}`;
    }
    return `link-${highlightedItem.sourceId}-${highlightedItem.targetId}`;
  };

  return (
    <Box sx={{ width: '100%' }}>
      <FormControl sx={{ mb: 2 }}>
        <FormLabel>Controlled Highlighting</FormLabel>
        <ToggleButtonGroup
          value={getCurrentValue()}
          exclusive
          onChange={handleToggleChange}
          aria-label="highlight control"
          size="small"
        >
          <ToggleButton value="node-A" aria-label="highlight node A">
            Node A
          </ToggleButton>
          <ToggleButton value="node-C" aria-label="highlight node C">
            Node C
          </ToggleButton>
          <ToggleButton value="node-E" aria-label="highlight node E">
            Node E
          </ToggleButton>
          <ToggleButton value="link-A-C" aria-label="highlight link A to C">
            Link A→C
          </ToggleButton>
          <ToggleButton value="link-B-D" aria-label="highlight link B to D">
            Link B→D
          </ToggleButton>
        </ToggleButtonGroup>
      </FormControl>

      <SankeyChart
        series={{
          data: {
            nodes: [
              { id: 'A', label: 'Node A', color: '#3b82f6' },
              { id: 'B', label: 'Node B', color: '#10b981' },
              { id: 'C', label: 'Node C', color: '#f59e0b' },
              { id: 'D', label: 'Node D', color: '#ef4444' },
              { id: 'E', label: 'Node E', color: '#8b5cf6' },
            ],
            links: [
              { source: 'A', target: 'C', value: 30 },
              { source: 'A', target: 'D', value: 20 },
              { source: 'B', target: 'C', value: 25 },
              { source: 'B', target: 'D', value: 15 },
              { source: 'C', target: 'E', value: 35 },
              { source: 'D', target: 'E', value: 20 },
            ],
          },
          nodeOptions: {
            highlight: 'links',
            fade: 'global',
          },
          linkOptions: {
            highlight: 'nodes',
            fade: 'global',
          },
        }}
        height={300}
        highlightedItem={highlightedItem}
        onHighlightChange={handleHighlightChange}
      />
    </Box>
  );
}

```

## Tooltip

The Sankey chart has an item tooltip that can be customized as described in the [Tooltip documentation page](/x/react-charts/tooltip/).

The only difference of the Sankey Tooltip is its default content.
You can import the default tooltip, or only its content as follows:

```js
import { SankeyTooltip, SankeyTooltipContent } from '@mui/x-charts/SankeyChart',
```
