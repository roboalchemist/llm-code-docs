# Source: https://recharts.github.io/en-US/api/CartesianAxis/

### CartesianAxis 

#### Properties 

- ::: 
  [[x](#x)][Number]

  The x-coordinate of axis.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[y](#y)][Number]

  The y-coordinate of axis.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[width](#width)][Number]

  The width of axis.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[height](#height)][Number]

  The height of axis.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[orientation](#orientation)][\'top\' \| \'bottom\' \| \'left\' \| \'right\']

  The orientation of axis.

  [DEFAULT: ]`"'bottom'"`
  :::

- ::: 
  [[viewBox](#viewBox)][Object]

  The box of viewing area.

  [DEFAULT: ]`""`
  :::

- ::: 
  [[axisLine](#axisLine)][Boolean \| Object]

  If set false, no axis line will be drawn. If set a object, the option is the configuration of axis line.

  [DEFAULT: ]`true`
  :::

- ::: 
  [[tickLine](#tickLine)][Boolean \| Object]

  If set false, no axis tick lines will be drawn. If set a object, the option is the configuration of tick lines.

  [DEFAULT: ]`true`
  :::

- ::: 
  [[minTickGap](#minTickGap)][Number]

  The minimum gap between two adjacent labels.

  [DEFAULT: ]`"5"`
  :::

- ::: 
  [[tickSize](#tickSize)][Number]

  The length of tick line.

  [DEFAULT: ]`"6"`
  :::

- ::: 
  [[interval](#interval)][\"preserveStart\" \| \"preserveEnd\" \| \"preserveStartEnd\" \| Number]

  If set 0, all the ticks will be shown. If set preserveStart\", \"preserveEnd\" or \"preserveStartEnd\", the ticks which is to be shown or hidden will be calculated automatically.

  [DEFAULT: ]`"'preserveEnd'"`
  :::

- :::: 
  [[tick](#tick)][Boolean \| Object \| ReactElement \| Function]*optional*

  If set false, no ticks will be drawn. If set a object, the option is the configuration of ticks. If set a React element, the option is the custom react element of drawing ticks. If set a function, the function will be called to render customized tick.

  ::: examples
  Examples:

  - [A line chart with customized x-axis tick](/en-US/examples/CustomizedLabelLineChart)
  :::
  ::::

- ::: 
  [[label](#label)][String \| Number \| ReactElement \| Function]*optional*

  If set a string or a number, default label will be drawn, and the option is content. If set a React element, the option is the custom react element of drawing label. If set a function, the function will be called to render customized label.
  :::

- ::: 
  [[mirror](#mirror)][Boolean]

  If set true, flips ticks around the axis line, displaying the labels inside the chart instead of outside.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[tickMargin](#tickMargin)][Number]*optional*

  The margin between tick line and tick.
  :::