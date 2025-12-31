# Source: https://recharts.github.io/en-US/api/Bar/

### Bar 

#### Parent Components 

Bar consumes context provided by these components:

- [`<BarChart />`](/en-US/api/BarChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)

#### Child Components 

Bar provides context for these components:

- [`<Cell />`](/en-US/api/Cell/)
- [`<LabelList />`](/en-US/api/LabelList/)
- [`<ErrorBar />`](/en-US/api/ErrorBar/)

#### Properties 

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]

  Decides how to extract the value of this Bar from the data: - \`string\`: the name of the field in the data object; - \`number\`: the index of the field in the data; - \`function\`: a function that receives the data object and returns the value of this Bar.
  :::

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

- ::: 
  [[legendType](#legendType)][\'line\' \| \'plainline\' \| \'square\' \| \'rect\'\| \'circle\' \| \'cross\' \| \'diamond\' \| \'square\' \| \'star\' \| \'triangle\' \| \'wye\' \| \'none\']*optional*

  The type of icon in legend. If set to \'none\', no legend item will be rendered.

  [DEFAULT: ]`"rect"`
  :::

- :::: 
  [[label](#label)][Boolean \| Object \| ReactElement \| Function]

  Renders one label for each bar. Options: - \`true\`: renders default labels; - \`false\`: no labels are rendered; - \`object\`: the props of LabelList component; - \`ReactElement\`: a custom label element; - \`function\`: a render function of custom label.

  [DEFAULT: ]`false`

  ::: format
  FORMAT:

  ``` format-code
  <Bar dataKey="value" label />
  <Bar dataKey="value" label=} />
  <Bar dataKey="value" label= />
  ```
  :::
  ::::

- ::: 
  [[barSize](#barSize)][Number \| Percentage]*optional*

  The width or height of each bar. If the barSize is not specified, the size of bar will be calculated by the barCategoryGap, barGap and the quantity of bar groups.
  :::

- ::: 
  [[maxBarSize](#maxBarSize)][Number]

  The maximum width of bar in a horizontal chart, or maximum height in a vertical chart.
  :::

- :::: 
  [[minPointSize](#minPointSize)][Number \| Function]

  The minimal height of a bar in a horizontal chart, or the minimal width of a bar in a vertical chart. By default, 0 values are not shown. To visualize a 0 (or close to zero) point, set the minimal point size to a pixel value like 3. In stacked bar charts, minPointSize might not be respected for tightly packed values. So we strongly recommend not using this props in stacked BarChart. You may provide a function to conditionally change this prop based on Bar value.

  [DEFAULT: ]`0`

  ::: examples
  Examples:

  - [A BarChart with non-zero minPointSize](/en-US/examples/BarChartWithMinHeight)
  :::
  ::::

- :::: 
  [[background](#background)][Boolean \| Object \| ReactElement \| Function]

  Renders a background for each bar. Options: - \`false\`: no background; - \`true\`: renders default background; - \`object\`: the props of background rectangle; - \`ReactElement\`: a custom background element; - \`function\`: a render function of custom background.

  [DEFAULT: ]`false`

  ::: examples
  Examples:

  - [BarChart has background](/en-US/examples/BarChartHasBackground)
  :::
  ::::

- ::::: 
  [[shape](#shape)][ReactElement \| Function]*optional*

  If set a ReactElement, the shape of bar can be customized. If set a function, the function will be called to render customized shape. By default, renders a rectangle.

  ::: format
  FORMAT:

  ``` format-code
  <Bar dataKey="value" shape=/>
  <Bar dataKey="value" shape=/>
  ```
  :::

  ::: examples
  Examples:

  - [A bar chart with customized shape](/en-US/examples/CustomShapeBarChart)
  :::
  :::::

- ::::: 
  [[activeBar](#activeBar)][Boolean \| Object \| ReactElement \| Function]*optional*

  The active bar is shown when a user enters a bar chart and this chart has tooltip. Options: - \`false\`: all bars are passive, nothing happens on mouse events; - \`true\`: active bar is rendered separately but the default props are the same as others: so mouse events do not change its appearance. className and zIndex are different though; - \`object\`: the props of active bar; - \`function\`: the render function of active bar; - \`ReactElement\`: the active bar element.

  [DEFAULT: ]`false`

  ::: format
  FORMAT:

  ``` format-code
  <Bar dataKey="value" activeBar= />
  <Bar dataKey="value" activeBar=} />
  <Bar dataKey="value" activeBar= />
  <Bar dataKey="value" activeBar= />
  ```
  :::

  ::: examples
  Examples:

  - [A bar chart with active bar](/en-US/examples/SimpleBarChart)
  :::
  :::::

- ::::: 
  [[stackId](#stackId)][String \| Number]*optional*

  When two Bars have the same axisId and same stackId, then the two Bars are stacked in the chart.

  ::: format
  FORMAT:

  ``` format-code
  <BarChart data= width= height=>
    <Bar stackId="pv" dataKey="pv01" />
    <Bar stackId="pv" dataKey="pv02" />
    <Bar stackId="uv" dataKey="uv01" />
    <Bar stackId="uv" dataKey="uv02" />
  </BarChart>
  ```
  :::

  ::: examples
  Examples:

  - [A stacked bar chart](/en-US/examples/StackedBarChart)
  - [A bar chart with stacked bars and unstacked bars](/en-US/examples/MixBarChart)
  :::
  :::::

- ::: 
  [[unit](#unit)][String \| Number]*optional*

  The unit of data. This option will be used in tooltip.
  :::

- ::: 
  [[name](#name)][String \| Number]*optional*

  The name of data. This option will be used in tooltip and legend to represent a bar. If no value was set to this option, the value of dataKey will be used alternatively.
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][Boolean \| \"auto\"]*optional*

  If set false, animation of bar will be disabled. If set \"auto\", the animation will be disabled in SSR and enabled in browser.

  [DEFAULT: ]`"auto"`
  :::

- ::: 
  [[animationBegin](#animationBegin)][Number]

  Specifies when the animation should begin, the unit of this option is ms.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[animationDuration](#animationDuration)][Number]

  Specifies the duration of animation, the unit of this option is ms.

  [DEFAULT: ]`400`
  :::

- ::: 
  [[animationEasing](#animationEasing)][\'ease\' \| \'ease-in\' \| \'ease-out\' \| \'ease-in-out\' \| \'linear\']

  The type of easing function.

  [DEFAULT: ]`"'ease'"`
  :::

- ::: 
  [[id](#id)][String]*optional*

  The unique identifier of this component. Used as a HTML attribute \`id\`, and also to identify this element internally. If undefined, Recharts will generate a unique ID automatically.
  :::

- ::: 
  [[onAnimationStart](#onAnimationStart)][Function]*optional*

  The customized event handler of animation start
  :::

- ::: 
  [[onAnimationEnd](#onAnimationEnd)][Function]*optional*

  The customized event handler of animation end
  :::

- :::: 
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click on the bars in this group

  ::: examples
  Examples:

  - [A BarChart with customized click event handler](/en-US/examples/BarChartWithCustomizedEvent)
  :::
  ::::

- ::: 
  [[onMouseDown](#onMouseDown)][Function]*optional*

  The customized event handler of mousedown on the bars in this group
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][Function]*optional*

  The customized event handler of mouseup on the bars in this group
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][Function]*optional*

  The customized event handler of mousemove on the bars in this group
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][Function]*optional*

  The customized event handler of mouseover on the bars in this group
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][Function]*optional*

  The customized event handler of mouseout on the bars in this group
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter on the bars in this group
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave on the bars in this group
  :::