# Source: https://recharts.github.io/en-US/api/Brush/

### Brush 

#### Parent Components 

Brush consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Child Components 

Brush provides context for these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Properties 

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]

  Decides how to extract the value of this Brush from the data: - \`string\`: the name of the field in the data object; - \`number\`: the index of the field in the data; - \`function\`: a function that receives the data object and returns the value of this Brush.
  :::

- ::: 
  [[x](#x)][Number]

  The x-coordinate of brush. If left undefined, it will be computed from the chart\'s offset and margins.
  :::

- ::: 
  [[y](#y)][Number]

  The y-coordinate of brush. If left undefined, it will be computed from the chart\'s offset and margins.
  :::

- ::: 
  [[width](#width)][Number]

  The width of brush. If undefined, defaults to the chart width.
  :::

- ::: 
  [[height](#height)][Number]

  The height of brush in pixels.

  [DEFAULT: ]`40`
  :::

- ::: 
  [[travellerWidth](#travellerWidth)][Number]

  The width of each traveller.

  [DEFAULT: ]`5`
  :::

- ::: 
  [[gap](#gap)][Number]*optional*

  Number of data points to skip between chart refreshes.

  [DEFAULT: ]`1`
  :::

- ::: 
  [[startIndex](#startIndex)][Number]*optional*

  The default start index of brush. If the option is not set, the start index will be 0.
  :::

- ::: 
  [[endIndex](#endIndex)][Number]*optional*

  The default end index of brush. If the option is not set, the end index will be calculated by the length of data.
  :::

- ::: 
  [[tickFormatter](#tickFormatter)][Function]*optional*

  The formatter function of ticks.
  :::

- ::: 
  [[onChange](#onChange)][Function]*optional*

  The handler of changing the active scope of brush.
  :::