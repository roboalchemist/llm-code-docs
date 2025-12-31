# Source: https://recharts.github.io/en-US/api/Tooltip/

### Tooltip 

Tooltip is rendered by html nodes.

#### Parent Components 

Tooltip consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<PieChart />`](/en-US/api/PieChart/)
- [`<RadarChart />`](/en-US/api/RadarChart/)
- [`<RadialBarChart />`](/en-US/api/RadialBarChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)
- [`<Treemap />`](/en-US/api/Treemap/)

#### Properties 

- ::: 
  [[separator](#separator)][String]

  The separator between name and value.

  [DEFAULT: ]`"' : '"`
  :::

- ::: 
  [[offset](#offset)][Number]

  The offset size between the position of tooltip and the active position.

  [DEFAULT: ]`10`
  :::

- ::: 
  [[filterNull](#filterNull)][Boolean]

  When an item of the payload has value null or undefined, this item won\'t be displayed.

  [DEFAULT: ]`true`
  :::

- :::: 
  [[itemStyle](#itemStyle)][Object]

  The style of default tooltip content item which is a li element.

  [DEFAULT: ]``

  ::: examples
  Examples:

  - [React Inline style](https://reactjs.org/docs/dom-elements.html#style)
  :::
  ::::

- :::: 
  [[wrapperStyle](#wrapperStyle)][Object]

  The style of tooltip wrapper which is a dom element.

  [DEFAULT: ]``

  ::: examples
  Examples:

  - [React Inline style](https://reactjs.org/docs/dom-elements.html#style)
  :::
  ::::

- :::: 
  [[contentStyle](#contentStyle)][Object]

  The style of tooltip content which is a dom element.

  [DEFAULT: ]``

  ::: examples
  Examples:

  - [React Inline style](https://reactjs.org/docs/dom-elements.html#style)
  :::
  ::::

- :::: 
  [[labelStyle](#labelStyle)][Object]

  The style of default tooltip label which is a p element.

  [DEFAULT: ]``

  ::: examples
  Examples:

  - [React Inline style](https://reactjs.org/docs/dom-elements.html#style)
  :::
  ::::

- :::: 
  [[cursor](#cursor)][Boolean \| Object \| ReactElement]

  If set false, no cursor will be drawn when tooltip is active. If set a object, the option is the configuration of cursor. If set a React element, the option is the custom react element of drawing cursor.

  [DEFAULT: ]`true`

  ::: format
  FORMAT:

  ``` format-code
  <Tooltip cursor= />
  <Tooltip cursor=} />
  <Tooltip cursor= />
  ```
  :::
  ::::

- :::: 
  [[allowEscapeViewBox](#allowEscapeViewBox)][Object]*optional*

  This option allows the tooltip to extend beyond the viewBox of the chart itself.

  [DEFAULT: ]``

  ::: format
  FORMAT:

  ``` format-code
  
  
  
  ```
  :::
  ::::

- ::: 
  [[active](#active)][Boolean]

  If set true, the tooltip is displayed even after onMouseLeave. If set false, the tooltip is always hidden.
  :::

- :::: 
  [[position](#position)][Object]*optional*

  If this field is set, the tooltip position will be fixed and will not move anymore.

  ::: format
  FORMAT:

  ``` format-code
  
  ```
  :::
  ::::

- ::::: 
  [[content](#content)][ReactElement \| Function]*optional*

  If set a React element, the option is the custom react element of rendering tooltip. If set a function, the function will be called to render tooltip content.

  ::: format
  FORMAT:

  ``` format-code
  <Tooltip content= />} />
  <Tooltip content= />
  ```
  :::

  ::: examples
  Examples:

  - [Customize tooltip content](/en-US/examples/CustomContentOfTooltip)
  :::
  :::::

- :::: 
  [[formatter](#formatter)][Function]*optional*

  The formatter function of value in tooltip. If you return an array, the first entry will be the formatted \"value\", and the second entry will be the formatted \"name\"

  ::: format
  FORMAT:

  ``` format-code
  (value, name, props) => "formatted value"
  (value, name, props) => ["formatted value", "formatted name"]
  ```
  :::
  ::::

- ::: 
  [[labelFormatter](#labelFormatter)][Function]*optional*

  The formatter function of label in tooltip.
  :::

- ::: 
  [[itemSorter](#itemSorter)][Function]

  Sort function of payload

  [DEFAULT: ]`"name"`
  :::

- ::: 
  [[shared](#shared)][Boolean]*optional*

  If true, tooltip will appear on top of all bars on an axis tick. If false, tooltip will appear on individual bars. Currently only supported in BarChart and RadialBarChart.
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][Boolean \| \"auto\"]

  If set false, animation of tooltip will be disabled.

  [DEFAULT: ]`"auto"`
  :::

- ::: 
  [[animationDuration](#animationDuration)][Number]

  Specifies the duration of animation, the unit of this option is ms.

  [DEFAULT: ]`400`
  :::

- ::: 
  [[animationEasing](#animationEasing)][\'ease\' \| \'ease-in\' \| \'ease-out\' \| \'ease-in-out\' \| \'linear\']

  The type of easing function.

  [DEFAULT: ]`"ease"`
  :::