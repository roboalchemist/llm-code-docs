# Source: https://recharts.github.io/en-US/api/ErrorBar/

### ErrorBar 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

ErrorBar consumes context provided by these components:

- [`<Bar />`](/en-US/api/Bar/)
- [`<Line />`](/en-US/api/Line/)
- [`<Scatter />`](/en-US/api/Scatter/)

#### Properties 

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]

  ::: section
  Decides how to extract the value of this ErrorBar from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value of this ErrorBar.

  The error values can be a single value for symmetric error bars; or an array of a lower and upper error value for asymmetric error bars.
  :::
  ::::

- ::: 
  [[animationBegin](#animationBegin)][number]*optional*

  [DEFAULT: ]`0`
  :::

- ::: 
  [[animationDuration](#animationDuration)][number]*optional*

  [DEFAULT: ]`400`
  :::

- ::: 
  [[animationEasing](#animationEasing)][\"linear\" \| \"ease\" \| \"ease-in\" \| \"ease-out\" \| \"ease-in-out\"]*optional*

  [DEFAULT: ]`"ease-in-out"`
  :::

- :::: 
  [[direction](#direction)][string \| number]*optional*

  ::: section
  Direction of the error bar. Usually determined by chart layout, except in Scatter chart. In Scatter chart, \"x\" means horizontal error bars, \"y\" means vertical error bars.
  :::
  ::::

- ::: 
  [[isAnimationActive](#isAnimationActive)][boolean]*optional*

  [DEFAULT: ]`true`
  :::

- :::: 
  [[stroke](#stroke)][string]*optional*

  ::: section
  The stroke color. If \"none\", no line will be drawn.
  :::

  [DEFAULT: ]`"black"`
  ::::

- :::: 
  [[strokeWidth](#strokeWidth)][string \| number]*optional*

  ::: section
  The width of the stroke
  :::

  [DEFAULT: ]`1.5`
  ::::

- :::: 
  [[width](#width)][string \| number]*optional*

  ::: section
  Width of the error bar ends
  :::

  [DEFAULT: ]`5`
  ::::

- ::: 
  [[zIndex](#zIndex)][number]*optional*

  [DEFAULT: ]`400`
  :::