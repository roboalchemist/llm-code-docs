# Source: https://recharts.github.io/en-US/api/Funnel/

### Funnel 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

Funnel consumes context provided by these components:

- [`<FunnelChart />`](/en-US/api/FunnelChart/)

#### Child Components 

Funnel provides context for these components:

- [`<LabelList />`](/en-US/api/LabelList/)
- [`<Cell />`](/en-US/api/Cell/)

#### Properties 

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
  [[dataKey](#dataKey)][String \| Number \| Function]

  The key or getter of a group of data which should be unique in a LineChart.
  :::

- ::: 
  [[nameKey](#nameKey)][String]

  The key of each sector\'s name.

  [DEFAULT: ]`"name"`
  :::

- ::: 
  [[legendType](#legendType)][\'line\' \| \'plainline\' \| \'square\' \| \'rect\'\| \'circle\' \| \'cross\' \| \'diamond\' \| \'square\' \| \'star\' \| \'triangle\' \| \'wye\' \| \'none\']*optional*

  The type of icon in legend. If set to \'none\', no legend item will be rendered.

  [DEFAULT: ]`"rect"`
  :::

- ::: 
  [[activeShape](#activeShape)][Object \| ReactElement \| Function \| boolean]*optional*

  The customized shape to be rendered if shape is active via Tooltip, or active index prop is set.
  :::

- ::: 
  [[shape](#shape)][Object \| ReactElement \| Function \| boolean]*optional*

  The customized shape to be rendered.
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][Boolean \| \"auto\"]

  If set false, animation of line will be disabled.

  [DEFAULT: ]`"auto"`
  :::

- ::: 
  [[animationBegin](#animationBegin)][Number]

  Specifies when the animation should begin, the unit of this option is ms.

  [DEFAULT: ]`400`
  :::

- ::: 
  [[animationDuration](#animationDuration)][Number]

  Specifies the duration of animation, the unit of this option is ms.

  [DEFAULT: ]`1500`
  :::

- ::: 
  [[animationEasing](#animationEasing)][\'ease\' \| \'ease-in\' \| \'ease-out\' \| \'ease-in-out\' \| \'linear\']

  The type of easing function.

  [DEFAULT: ]`"ease"`
  :::

- ::: 
  [[id](#id)][String]*optional*

  The unique id of this component, which will be used to generate unique clip path id internally. This props is suggested to be set in SSR.
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

  The customized event handler of click on the area in this group

  ::: examples
  Examples:

  - [A BarChart with customized click event handler](/en-US/examples/BarChartWithCustomizedEvent)
  :::
  ::::

- ::: 
  [[onMouseDown](#onMouseDown)][Function]*optional*

  The customized event handler of mousedown on the area in this group
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][Function]*optional*

  The customized event handler of mouseup on the area in this group
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][Function]*optional*

  The customized event handler of mousemove on the area in this group
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][Function]*optional*

  The customized event handler of mouseover on the area in this group
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][Function]*optional*

  The customized event handler of mouseout on the area in this group
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter on the area in this group
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave on the area in this group
  :::