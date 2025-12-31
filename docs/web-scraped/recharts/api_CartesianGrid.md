# Source: https://recharts.github.io/en-US/api/CartesianGrid/

### CartesianGrid 

#### Parent Components 

CartesianGrid consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Properties 

- ::: 
  [[x](#x)][Number]

  The x-coordinate of grid. If left undefined, it will be computed from the chart\'s offset and margins.
  :::

- ::: 
  [[y](#y)][Number]

  The y-coordinate of grid. If left undefined, it will be computed from the chart\'s offset and margins.
  :::

- ::: 
  [[width](#width)][Number]

  The width of grid. If undefined, covers the full width of the chart plot area.
  :::

- ::: 
  [[height](#height)][Number]

  The height of grid. If undefined, covers the full height of the chart plot area.
  :::

- ::: 
  [[horizontal](#horizontal)][Boolean]

  If set false, no horizontal grid lines will be drawn.

  [DEFAULT: ]`true`
  :::

- ::: 
  [[vertical](#vertical)][Boolean]

  If set false, no vertical grid lines will be drawn.

  [DEFAULT: ]`true`
  :::

- ::: 
  [[horizontalPoints](#horizontalPoints)][Array]

  Array of coordinates in pixels where to draw horizontal grid lines. Has priority over syncWithTicks and horizontalValues.

  [DEFAULT: ]`[]`
  :::

- ::::: 
  [[horizontalCoordinatesGenerator](#horizontalCoordinatesGenerator)][Function]*optional*

  A function that generates the y-coordinates of all horizontal lines. The generator gets passed an object of the shape .

  ::: format
  FORMAT:

  ``` format-code
  <CartesianGrid strokeDasharray="3 3" horizontalCoordinatesGenerator= />
  ```
  :::

  ::: examples
  Examples:

  - [Cartesian grid with coordinate generators](https://codesandbox.io/s/cartesian-grid-with-coordinate-generators-my38cg)
  :::
  :::::

- ::: 
  [[verticalPoints](#verticalPoints)][Array]

  Array of coordinates in pixels where to draw vertical grid lines. Has priority over syncWithTicks and verticalValues.

  [DEFAULT: ]`[]`
  :::

- ::::: 
  [[verticalCoordinatesGenerator](#verticalCoordinatesGenerator)][Function]*optional*

  A function that generates the x-coordinates of all vertical lines. The generator gets passed an object of the shape .

  ::: format
  FORMAT:

  ``` format-code
  <CartesianGrid strokeDasharray="3 3" verticalCoordinatesGenerator= />
  ```
  :::

  ::: examples
  Examples:

  - [Cartesian grid with coordinate generators](https://codesandbox.io/s/cartesian-grid-with-coordinate-generators-my38cg)
  :::
  :::::

- :::: 
  [[fill](#fill)][String]*optional*

  The background color used to fill the space between grid lines

  [DEFAULT: ]`"none"`

  ::: format
  FORMAT:

  ``` format-code
  <CartesianGrid strokeDasharray="3 3" fill="red" />
  <CartesianGrid strokeDasharray="3 3" fill="#ccc" />
  ```
  :::
  ::::

- :::: 
  [[fillOpacity](#fillOpacity)][Number]*optional*

  The opacity of the background used to fill the space between grid lines

  ::: format
  FORMAT:

  ``` format-code
  <CartesianGrid strokeDasharray="3 3" fill="red" fillOpacity= />
  ```
  :::
  ::::

- :::: 
  [[strokeDasharray](#strokeDasharray)][String]*optional*

  The pattern of dashes and gaps used to paint the lines of the grid

  ::: format
  FORMAT:

  ``` format-code
  <CartesianGrid strokeDasharray="4" />
  <CartesianGrid strokeDasharray="4 1" />
  <CartesianGrid strokeDasharray="4 1 2" />
  ```
  :::
  ::::

- ::: 
  [[xAxisId](#xAxisId)][String \| Number]

  The id of XAxis which is corresponding to the data. Required when there are multiple XAxes.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[yAxisId](#yAxisId)][String \| Number]

  The id of YAxis which is corresponding to the data. Required when there are multiple YAxes.

  [DEFAULT: ]`0`
  :::