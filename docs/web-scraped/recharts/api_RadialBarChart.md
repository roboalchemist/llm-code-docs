# Source: https://recharts.github.io/en-US/api/RadialBarChart/

### RadialBarChart 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

RadialBarChart consumes context provided by these components:

- [`<ResponsiveContainer />`](/en-US/api/ResponsiveContainer/)

#### Child Components 

RadialBarChart provides context for these components:

- [`<PolarAngleAxis />`](/en-US/api/PolarAngleAxis/)
- [`<PolarRadiusAxis />`](/en-US/api/PolarRadiusAxis/)
- [`<PolarGrid />`](/en-US/api/PolarGrid/)
- [`<Legend />`](/en-US/api/Legend/)
- [`<Tooltip />`](/en-US/api/Tooltip/)
- [`<RadialBar />`](/en-US/api/RadialBar/)
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

  The source data which each element is an object.

  ::: format
  FORMAT:

  ``` format-code
  []
  ```
  :::
  ::::

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
  [[barCategoryGap](#barCategoryGap)][Percentage\| Number]

  The gap between two bar categories, which can be a percent value or a fixed value.

  [DEFAULT: ]`"10%"`
  :::

- ::: 
  [[barGap](#barGap)][Number]

  The gap between two bars in the same category.

  [DEFAULT: ]`4`
  :::

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

  The start angle of all the bars.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[endAngle](#endAngle)][Number]

  The end angle of all the bars.

  [DEFAULT: ]`360`
  :::

- ::: 
  [[innerRadius](#innerRadius)][Percentage \| Number]

  The innerRadius of the radial bar which is most close to the center. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[outerRadius](#outerRadius)][Percentage \| Number]

  The outerRadius of the radial bar which is most far away from the center. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.

  [DEFAULT: ]`"80%"`
  :::

- ::: 
  [[barSize](#barSize)][Number]*optional*

  The size of each bar. If the barSize is not specified, the size of bar will be calculated by the barCategoryGap, barGap and the quantity of bar groups.
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The function will be called when mouse enter bars.
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The function will be called when mouse leave bars.
  :::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The function will be called when click bars.
  :::

- ::: 
  [[onDoubleClick](#onDoubleClick)][Function]*optional*

  The customized event handler of dblclick in this chart.
  :::

- ::: 
  [[onContextMenu](#onContextMenu)][Function]*optional*

  The customized event handler of contextmenu in this chart.
  :::