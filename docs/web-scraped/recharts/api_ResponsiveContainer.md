# Source: https://recharts.github.io/en-US/api/ResponsiveContainer/

### ResponsiveContainer 

A container component to make charts adapt to the size of parent container. One of the props width and height should be a percentage string.

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Child Components 

ResponsiveContainer provides context for these components:

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
  [[aspect](#aspect)][ Number]*optional*

  width / height. If specified, the height will be calculated by width / aspect.
  :::

- ::: 
  [[width](#width)][Percentage \| Number]

  The percentage value of the chart\'s width or a fixed width.

  [DEFAULT: ]`"100%"`
  :::

- ::: 
  [[height](#height)][Percentage \| Number]

  The percentage value of the chart\'s width or a fixed height.

  [DEFAULT: ]`"100%"`
  :::

- ::: 
  [[minWidth](#minWidth)][Number]*optional*

  The minimum width of the container.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[minHeight](#minHeight)][Number]*optional*

  The minimum height of the container.
  :::

- ::: 
  [[debounce](#debounce)][Number]

  If specified a positive number, debounced function will be used to handle the resize event.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[onResize](#onResize)][Function]*optional*

  If specified provides a callback providing the updated chart width and height values.
  :::