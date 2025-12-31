# Source: https://recharts.github.io/en-US/api/RadarChart/

### RadarChart 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

RadarChart consumes context provided by these components:

- [`<ResponsiveContainer />`](/en-US/api/ResponsiveContainer/)

#### Child Components 

RadarChart provides context for these components:

- [`<PolarAngleAxis />`](/en-US/api/PolarAngleAxis/)
- [`<PolarRadiusAxis />`](/en-US/api/PolarRadiusAxis/)
- [`<PolarGrid />`](/en-US/api/PolarGrid/)
- [`<Legend />`](/en-US/api/Legend/)
- [`<Tooltip />`](/en-US/api/Tooltip/)
- [`<Radar />`](/en-US/api/Radar/)
- [`<Customized />`](/en-US/api/Customized/)
- validate svg elements\...

#### Properties 

- ::: 
  [[width](#width)][Number]

  The width of chart container.
  :::

- ::: 
  [[height](#height)][Number]

  The height of chart container.
  :::

- :::: 
  [[data](#data)][Array]

  The source data, in which each element is an object.

  ::: format
  FORMAT:

  ``` format-code
  []
  []
  ```
  :::
  ::::

- ::: 
  [[cx](#cx)][Percentage \| Number]

  The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of width.

  [DEFAULT: ]`"50%"`
  :::

- ::: 
  [[cy](#cy)][Percentage \| Number]

  The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of height.

  [DEFAULT: ]`"50%"`
  :::

- ::: 
  [[startAngle](#startAngle)][Number]

  The angle of first radial direction line.

  [DEFAULT: ]`90`
  :::

- ::: 
  [[endAngle](#endAngle)][Number]

  The angle of last point in the circle which should be startAngle - 360 or startAngle + 360. We\'ll calculate the direction of chart by \'startAngle\' and \'endAngle\'.

  [DEFAULT: ]`-270`
  :::

- ::: 
  [[innerRadius](#innerRadius)][Percentage \| Number]

  The inner radius of first circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[outerRadius](#outerRadius)][Percentage \| Number]

  The outer radius of last circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.

  [DEFAULT: ]`"80%"`
  :::

- :::: 
  [[margin](#margin)][Object]

  The sizes of whitespace around the container.

  [DEFAULT: ]`""`

  ::: format
  FORMAT:

  ``` format-code
  
  ```
  :::
  ::::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The function will be called when mouse enter the \'Radar\'.
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The function will be called when mouse leave the \'Radar\'.
  :::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The function will be called when click the \'Radar\'.
  :::

- ::: 
  [[onDoubleClick](#onDoubleClick)][Function]*optional*

  The customized event handler of dblclick in this chart.
  :::

- ::: 
  [[onContextMenu](#onContextMenu)][Function]*optional*

  The customized event handler of contextmenu in this chart.
  :::