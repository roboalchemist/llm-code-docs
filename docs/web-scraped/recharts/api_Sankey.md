# Source: https://recharts.github.io/en-US/api/Sankey/

### Sankey 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Child Components 

Sankey provides context for these components:

- [`<Tooltip />`](/en-US/api/Tooltip/)

#### Properties 

- ::: 
  [[nameKey](#nameKey)][String]*optional*

  The key of each sector\'s name.

  [DEFAULT: ]`"name"`
  :::

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]*optional*

  The key of a group of data which should be unique in a SankeyChart.

  [DEFAULT: ]`"value"`
  :::

- ::: 
  [[width](#width)][Percentage \| Number]

  The percentage value of the chart\'s width or a fixed width.
  :::

- ::: 
  [[height](#height)][Percentage \| Number]

  The percentage value of the chart\'s width or a fixed height.
  :::

- :::: 
  [[data](#data)][Object]

  The source data, including the array of nodes, and the relationships, represented by links.

  ::: format
  FORMAT:

  ``` format-code
  nodes: [
    ,
    ,
    ,
    ,
    ,
  ],
  links: [
    ,
    ,
    ,
    ,
  ],
  ```
  :::
  ::::

- ::: 
  [[sort](#sort)][Boolean]*optional*

  Whether to sort the nodes on th y axis, or to display them as user-defined.

  [DEFAULT: ]`true`
  :::

- ::: 
  [[nodePadding](#nodePadding)][Number]*optional*

  The padding between the nodes

  [DEFAULT: ]`10`
  :::

- ::: 
  [[nodeWidth](#nodeWidth)][Number]

  The width of node

  [DEFAULT: ]`10`
  :::

- ::: 
  [[linkCurvature](#linkCurvature)][Number]

  The curvature of width

  [DEFAULT: ]`0.5`
  :::

- ::: 
  [[iterations](#iterations)][Number]

  The number of the iterations between the links

  [DEFAULT: ]`32`
  :::

- :::: 
  [[node](#node)][Object \| ReactElement]*optional*

  If set a object, the option is the configuration of nodes. If set a React element, the option is the custom react element of drawing the nodes.

  ::: format
  FORMAT:

  ``` format-code
  <Sankey node= />
  <Sankey node=} />
  ```
  :::
  ::::

- :::: 
  [[link](#link)][Object \| ReactElement]*optional*

  If set a object, the option is the configuration of links. If set a React element, the option is the custom react element of drawing the links.

  ::: format
  FORMAT:

  ``` format-code
  <Sankey link= />
  <Sankey link=} />
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
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click on the area in this group
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter on the area in this group
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave on the area in this group
  :::

- ::: 
  [[align](#align)][\'left\' \| \'justify\']*optional*

  If set to \'justify\', the start nodes will be aligned to the left edge of the chart and the end nodes will be aligned to the right edge of the chart. If set to \'left\', the start nodes will be aligned to the left edge of the chart.

  [DEFAULT: ]`"justify"`
  :::

- ::: 
  [[verticalAlign](#verticalAlign)][\'justify\' \| \'top\']*optional*

  Controls the vertical spacing of nodes within a depth. \'justify\' distributes nodes evenly and balances link paths, while \'top\' positions the group starting from the top edge of the chart.

  [DEFAULT: ]`"justify"`
  :::