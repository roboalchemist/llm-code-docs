# Source: https://recharts.github.io/en-US/api/PieChart/

### PieChart 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Child Components 

PieChart provides context for these components:

- [`<Label />`](/en-US/api/Label/)
- [`<Legend />`](/en-US/api/Legend/)
- [`<Pie />`](/en-US/api/Pie/)
- [`<PolarAngleAxis />`](/en-US/api/PolarAngleAxis/)
- [`<PolarGrid />`](/en-US/api/PolarGrid/)
- [`<PolarRadiusAxis />`](/en-US/api/PolarRadiusAxis/)
- [`<Radar />`](/en-US/api/Radar/)
- [`<RadialBar />`](/en-US/api/RadialBar/)
- [`<Tooltip />`](/en-US/api/Tooltip/)

#### Properties 

- ::: 
  [[accessibilityLayer](#accessibilityLayer)][boolean]*optional*

  [DEFAULT: ]`true`
  :::

- ::: 
  [[barCategoryGap](#barCategoryGap)][string \| number]*optional*

  [DEFAULT: ]`"10%"`
  :::

- ::: 
  [[barGap](#barGap)][string \| number]*optional*

  [DEFAULT: ]`4`
  :::

- ::: 
  [[barSize](#barSize)][string \| number]*optional*
  :::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- ::: 
  [[className](#className)][string]*optional*
  :::

- ::: 
  [[cx](#cx)][string \| number]*optional*

  [DEFAULT: ]`"50%"`
  :::

- ::: 
  [[cy](#cy)][string \| number]*optional*

  [DEFAULT: ]`"50%"`
  :::

- :::: 
  [[data](#data)][Array\<any\>]*optional*

  ::: section
  The source data. Each element should be an object.
  :::
  ::::

- ::: 
  [[dataKey](#dataKey)][string \| number \| Function]*optional*
  :::

- ::: 
  [[desc](#desc)][string]*optional*
  :::

- ::: 
  [[endAngle](#endAngle)][number]*optional*

  [DEFAULT: ]`360`
  :::

- :::: 
  [[height](#height)][number \| \`\$%\`]*optional*

  ::: section
  The height of chart container. Can be a number or a percent string like \"100%\".
  :::
  ::::

- ::: 
  [[id](#id)][string]*optional*
  :::

- ::: 
  [[innerRadius](#innerRadius)][string \| number]*optional*

  [DEFAULT: ]`0`
  :::

- ::: 
  [[layout](#layout)][\"centric\" \| \"radial\"]*optional*

  [DEFAULT: ]`"centric"`
  :::

- :::: 
  [[margin](#margin)][Partial\<Margin\>]*optional*

  ::: section
  Empty space around the container.
  :::

  [DEFAULT: ]``
  ::::

- ::: 
  [[maxBarSize](#maxBarSize)][number]*optional*
  :::

- ::: 
  [[outerRadius](#outerRadius)][string \| number]*optional*

  [DEFAULT: ]`"80%"`
  :::

- :::: 
  [[responsive](#responsive)][boolean]*optional*

  ::: section
  If true, then it will listen to container size changes and adapt the SVG chart accordingly. If false, then it renders the chart at the specified width and height and will stay that way even if the container size changes.

  This is similar to ResponsiveContainer but without the need for an extra wrapper component. The `responsive` prop also uses standard CSS sizing rules, instead of custom resolution logic (like ResponsiveContainer does).
  :::

  [DEFAULT: ]`false`
  ::::

- ::: 
  [[reverseStackOrder](#reverseStackOrder)][boolean]*optional*

  [DEFAULT: ]`false`
  :::

- ::: 
  [[role](#role)][string]*optional*
  :::

- ::: 
  [[stackOffset](#stackOffset)][(union of 6 variants)]*optional*

  [DEFAULT: ]`"none"`
  :::

- ::: 
  [[startAngle](#startAngle)][number]*optional*

  [DEFAULT: ]`0`
  :::

- ::: 
  [[style](#style)][React.CSSProperties]*optional*
  :::

- :::: 
  [[syncId](#syncId)][string \| number]*optional*

  ::: section
  Charts with the same syncId will synchronize Tooltip and Brush events.
  :::
  ::::

- :::: 
  [[syncMethod](#syncMethod)][\"index\" \| \"value\" \| Function]*optional*

  ::: section
  Customize how the charts will synchronize tooltips and brushes.`index`: synchronize using the data index in the data array. Index expects that all data has the same length.`value`: synchronize using the data value on categorical axis (categorical: XAxis in horizontal layout, YAxis in vertical layout). function: a custom sync method which receives tick and data as argument and returns an index.
  :::

  [DEFAULT: ]`"index"`
  ::::

- ::: 
  [[tabIndex](#tabIndex)][number]*optional*
  :::

- ::: 
  [[throttleDelay](#throttleDelay)][number]*optional*
  :::

- ::: 
  [[title](#title)][string]*optional*
  :::

- :::: 
  [[width](#width)][number \| \`\$%\`]*optional*

  ::: section
  The width of chart container. Can be a number or a percent string like \"100%\".
  :::
  ::::

- :::: 
  [[onClick](#onClick)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of click in this chart.
  :::
  ::::

- :::: 
  [[onContextMenu](#onContextMenu)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of contextmenu in this chart.
  :::
  ::::

- :::: 
  [[onDoubleClick](#onDoubleClick)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of dblclick in this chart.
  :::
  ::::

- :::: 
  [[onMouseDown](#onMouseDown)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of mousedown in this chart.
  :::
  ::::

- :::: 
  [[onMouseEnter](#onMouseEnter)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of mouseenter in this chart.
  :::
  ::::

- :::: 
  [[onMouseLeave](#onMouseLeave)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of mouseleave in this chart.
  :::
  ::::

- :::: 
  [[onMouseMove](#onMouseMove)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of mousemove in this chart.
  :::
  ::::

- :::: 
  [[onMouseUp](#onMouseUp)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of mouseup in this chart.
  :::
  ::::

- :::: 
  [[onTouchEnd](#onTouchEnd)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of touchend in this chart.
  :::
  ::::

- :::: 
  [[onTouchMove](#onTouchMove)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of touchmove in this chart.
  :::
  ::::

- :::: 
  [[onTouchStart](#onTouchStart)][CategoricalChartFunc]*optional*

  ::: section
  The customized event handler of touchstart in this chart.
  :::
  ::::