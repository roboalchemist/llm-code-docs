# Source: https://recharts.github.io/en-US/api/ZAxis/

### ZAxis 

#### Parent Components 

ZAxis consumes context provided by these components:

- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Properties 

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]

  The key of data displayed in the axis.
  :::

- ::: 
  [[zAxisId](#zAxisId)][String \| Number]

  The unique id of z-axis.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[range](#range)][Array]

  The range of axis.

  [DEFAULT: ]`[64,64]`
  :::

- ::: 
  [[unit](#unit)][String \| Number]*optional*

  The unit of data displayed in the axis. This option will be used to represent an index unit in a scatter chart.
  :::

- ::: 
  [[name](#name)][String \| Number]*optional*

  The name of data displayed in the axis. This option will be used to represent an index in a scatter chart.
  :::

- :::: 
  [[scale](#scale)][\'auto\' \| \'linear\' \| \'pow\' \| \'sqrt\' \| \'log\' \| \'identity\' \| \'time\' \| \'band\' \| \'point\' \| \'ordinal\' \| \'quantile\' \| \'quantize\' \| \'utc\' \| \'sequential\' \| \'threshold\' \| Function]

  If \'auto\' set, the scale function is decided by the type of chart, and the props type.

  [DEFAULT: ]`"auto"`

  ::: format
  FORMAT:

  ``` format-code
  <ZAxis scale="log" />

  import  from 'd3-scale';
  const scale = scaleLog().base(Math.E);

  ...
    <ZAxis scale= />
  ...
  ```
  :::
  ::::