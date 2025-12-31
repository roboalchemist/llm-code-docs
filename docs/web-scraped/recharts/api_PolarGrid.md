# Source: https://recharts.github.io/en-US/api/PolarGrid/

### PolarGrid 

#### Parent Components 

PolarGrid consumes context provided by these components:

- [`<PieChart />`](/en-US/api/PieChart/)
- [`<RadarChart />`](/en-US/api/RadarChart/)
- [`<RadialBarChart />`](/en-US/api/RadialBarChart/)

#### Properties 

- ::: 
  [[angleAxisId](#angleAxisId)][string \| number]*optional*

  [DEFAULT: ]`0`
  :::

- :::: 
  [[cx](#cx)][string \| number]*optional*

  ::: section
  The x-coordinate of center. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::
  ::::

- :::: 
  [[cy](#cy)][string \| number]*optional*

  ::: section
  The y-coordinate of center. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::
  ::::

- :::: 
  [[gridType](#gridType)][\"circle\" \| \"polygon\"]*optional*

  ::: section
  The type of polar grids.
  :::

  [DEFAULT: ]`"polygon"`
  ::::

- :::: 
  [[innerRadius](#innerRadius)][number]*optional*

  ::: section
  The radius of the inner polar grid. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::
  ::::

- :::: 
  [[outerRadius](#outerRadius)][number]*optional*

  ::: section
  The radius of the outer polar grid. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::
  ::::

- :::: 
  [[polarAngles](#polarAngles)][Array\<readonly number\>]*optional*

  ::: section
  The array of every line grid\'s angle.
  :::
  ::::

- :::: 
  [[polarRadius](#polarRadius)][Array\<readonly number\>]*optional*

  ::: section
  The array of every circle grid\'s radius.
  :::
  ::::

- ::: 
  [[radialLines](#radialLines)][boolean]*optional*

  [DEFAULT: ]`true`
  :::

- ::: 
  [[radiusAxisId](#radiusAxisId)][string \| number]*optional*

  [DEFAULT: ]`0`
  :::

- ::::: 
  [[zIndex](#zIndex)][number]*optional*

  ::: section
  Z-Index of this component and its children. The higher the value, the more on top it will be rendered. Components with higher zIndex will appear in front of components with lower zIndex. If undefined or 0, the content is rendered in the default layer without portals.
  :::

  [DEFAULT: ]`-100`

  ::: examples
  Examples:

  - [Z-Index and layers guide](/en-US/guide/zIndex/)
  :::
  :::::