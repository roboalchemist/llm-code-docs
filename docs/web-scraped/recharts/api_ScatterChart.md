# Source: https://recharts.github.io/en-US/api/ScatterChart/

### ScatterChart 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

ScatterChart consumes context provided by these components:

- [`<ResponsiveContainer />`](/en-US/api/ResponsiveContainer/)

#### Child Components 

ScatterChart provides context for these components:

- [`<XAxis />`](/en-US/api/XAxis/)
- [`<YAxis />`](/en-US/api/YAxis/)
- [`<ZAxis />`](/en-US/api/ZAxis/)
- [`<ReferenceArea />`](/en-US/api/ReferenceArea/)
- [`<ReferenceDot />`](/en-US/api/ReferenceDot/)
- [`<ReferenceLine />`](/en-US/api/ReferenceLine/)
- [`<Brush />`](/en-US/api/Brush/)
- [`<CartesianGrid />`](/en-US/api/CartesianGrid/)
- [`<Legend />`](/en-US/api/Legend/)
- [`<Tooltip />`](/en-US/api/Tooltip/)
- [`<Scatter />`](/en-US/api/Scatter/)
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