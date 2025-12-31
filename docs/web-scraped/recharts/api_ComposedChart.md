# Source: https://recharts.github.io/en-US/api/ComposedChart/

### ComposedChart 

A chart composed of line, area, and bar charts. When you just want to draw a chart of a single type like line, then LineChart is recommended.

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

ComposedChart consumes context provided by these components:

- [`<ResponsiveContainer />`](/en-US/api/ResponsiveContainer/)

#### Child Components 

ComposedChart provides context for these components:

- [`<XAxis />`](/en-US/api/XAxis/)
- [`<YAxis />`](/en-US/api/YAxis/)
- [`<ReferenceArea />`](/en-US/api/ReferenceArea/)
- [`<ReferenceDot />`](/en-US/api/ReferenceDot/)
- [`<ReferenceLine />`](/en-US/api/ReferenceLine/)
- [`<Brush />`](/en-US/api/Brush/)
- [`<CartesianGrid />`](/en-US/api/CartesianGrid/)
- [`<Legend />`](/en-US/api/Legend/)
- [`<Tooltip />`](/en-US/api/Tooltip/)
- [`<Area />`](/en-US/api/Area/)
- [`<Line />`](/en-US/api/Line/)
- [`<Bar />`](/en-US/api/Bar/)
- [`<Customized />`](/en-US/api/Customized/)
- validate svg elements\...

#### Properties 

- ::: 
  [[layout](#layout)][\'horizontal\' \| \'vertical\']

  The layout of chart defines the orientation of axes, graphical items, and tooltip.

  [DEFAULT: ]`"horizontal"`
  :::

- :::: 
  [[syncId](#syncId)][String]*optional*

  Charts with the same syncId will synchronize Tooltip and Brush events.

  ::: examples
  Examples:

  - [Two synchronized AreaChart](/en-US/examples/SynchronizedAreaChart)
  :::
  ::::

- ::: 
  [[syncMethod](#syncMethod)][\'index\' \| \'value\' \| function]*optional*

  Customize how the charts will synchronize tooltips and brushes. \`index\`: synchronize using the data index in the data array. Index expects that all data has the same length. \`value\`: synchronize using the data value on categorical axis (categorical: XAxis in horizontal layout, YAxis in vertical layout). function: a custom sync method which receives tick and data as argument and returns an index.

  [DEFAULT: ]`"index"`
  :::

- ::: 
  [[width](#width)][Percent \| Number]

  The width of chart container. Can be a number or a percent string like \"100%\".
  :::

- ::: 
  [[height](#height)][Percent \| Number]

  The height of chart container. Can be a number or a percent string like \"100%\".
  :::

- :::: 
  [[data](#data)][Array]

  The source data. Each element should be an object.

  ::: format
  FORMAT:

  ``` format-code
  []
  []
  ```
  :::
  ::::

- :::: 
  [[margin](#margin)][Object]

  Empty space around the container.

  [DEFAULT: ]`""`

  ::: format
  FORMAT:

  ``` format-code
  
  ```
  :::
  ::::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click in this chart.
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter in this chart.
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][Function]*optional*

  The customized event handler of mousemove in this chart.
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave in this chart.
  :::

- ::: 
  [[onDoubleClick](#onDoubleClick)][Function]*optional*

  The customized event handler of dblclick in this chart.
  :::

- ::: 
  [[onContextMenu](#onContextMenu)][Function]*optional*

  The customized event handler of contextmenu in this chart.
  :::

- :::: 
  [[stackOffset](#stackOffset)][\'sign\' \| \'expand\' \| \'none\' \| \'wiggle\' \| \'silhouette\' \| \'positive\']

  The type of offset function used to generate the lower and upper values in the series array. The types are built-in offsets in d3-shape. Only applicable for stacked Area or Bar charts. Has no effect when the stackId prop is not set on Area or Bar components.

  [DEFAULT: ]`"none"`

  ::: examples
  Examples:

  - [A barChart stacked by sign of value](/en-US/examples/BarChartStackedBySign)
  - [D3 stackOffset](https://github.com/d3/d3-shape#stack_offset)
  :::
  ::::

- ::: 
  [[reverseStackOrder](#reverseStackOrder)][Boolean]*optional*

  If false set, stacked items will be rendered left to right. If true set, stacked items will be rendered right to left. Render direction affects SVG layering, not x position.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[barCategoryGap](#barCategoryGap)][Percentage \| Number]

  The gap between two bar categories, which can be a percent value or a fixed value.

  [DEFAULT: ]`"10%"`
  :::

- ::: 
  [[barGap](#barGap)][Number]

  The gap between two bars in the same category.

  [DEFAULT: ]`4`
  :::

- ::: 
  [[barSize](#barSize)][Number]*optional*

  The width or height of each bar. If the barSize is not specified, the size of the bar will be calculated by the barCategoryGap, barGap and the quantity of bar groups.
  :::

- ::: 
  [[baseValue](#baseValue)][Number \| \'dataMin\' \| \'dataMax\']*optional*

  The base value of area.
  :::