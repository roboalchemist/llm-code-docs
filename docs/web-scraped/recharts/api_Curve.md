# Source: https://recharts.github.io/en-US/api/Curve/

### Curve 

#### Properties 

- :::: 
  [[type](#type)][\'basis\' \| \'basisClosed\' \| \'basisOpen\' \| \'bumpX\' \| \'bumpY\' \| \'bump\' \| \'linear\' \| \'linearClosed\' \| \'natural\' \| \'monotoneX\' \| \'monotoneY\' \| \'monotone\' \| \'step\' \| \'stepBefore\' \| \'stepAfter\' \| Function]

  The interpolation type of curve. Allows custom interpolation function.

  [DEFAULT: ]`"linear"`

  ::: examples
  Examples:

  - [d3-shape interpolation](https://github.com/d3/d3-shape#curves)
  - [An AreaChart which has two area with different interpolation.](/en-US/examples/CardinalAreaChart)
  :::
  ::::

- ::: 
  [[baseLine](#baseLine)][Number \| Array]*optional*

  Baseline of the area: - number: uses the corresponding axis value as a flat baseline; - an array of coordinates: describes a custom baseline path.
  :::

- :::: 
  [[connectNulls](#connectNulls)][Boolean]

  Whether to connect the curve across null points.

  [DEFAULT: ]`false`

  ::: examples
  Examples:

  - [A lineChart connect nulls and a lineChart disconnect nulls](/en-US/examples/LineChartConnectNulls)
  - [An areaChart connect nulls and an areaChart disconnect nulls](/en-US/examples/AreaChartConnectNulls)
  :::
  ::::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click on the curve
  :::

- ::: 
  [[onMouseDown](#onMouseDown)][Function]*optional*

  The customized event handler of mousedown on the curve
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][Function]*optional*

  The customized event handler of mouseup on the curve
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][Function]*optional*

  The customized event handler of mousemove on the curve
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][Function]*optional*

  The customized event handler of mouseover on the curve
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][Function]*optional*

  The customized event handler of mouseout on the curve
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter on the curve
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave on the curve
  :::

- ::: 
  [[layout](#layout)][\'horizontal\' \| \'vertical\']*optional*

  This option affects the interpolation algorithm when the \`type\` prop is set to \'monotone\'. It also specifies the type of baseline when the curve is closed.
  :::

- ::: 
  [[points](#points)][Array]

  The coordinates of all the points in the curve.
  :::