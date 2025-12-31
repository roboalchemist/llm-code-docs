# Source: https://recharts.github.io/en-US/api/ReferenceDot/

### ReferenceDot 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

ReferenceDot consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Child Components 

ReferenceDot provides context for these components:

- [`<Label />`](/en-US/api/Label/)

#### Properties 

- ::: 
  [[xAxisId](#xAxisId)][String \| Number]

  The id of x-axis which is corresponding to the data.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[yAxisId](#yAxisId)][String \| Number]

  The id of y-axis which is corresponding to the data.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[x](#x)][Number \| String]

  If the x-axis specified by xAxisId is a number axis, the type of x must be Number. If the x-axis specified by xAxisId is a category axis, the value of x must be one of the categories, otherwise no dot will be drawn.
  :::

- ::: 
  [[y](#y)][Number \| String]

  If the y-axis specified by yAxisId is a number axis, the type of y must be Number. If the y-axis specified by yAxisId is a category axis, the value of y must be one of the categories, otherwise no dot will be drawn.
  :::

- ::: 
  [[ifOverflow](#ifOverflow)][\'discard\' \| \'hidden\' \| \'visible\' \| \'extendDomain\']

  Defines how to draw the reference dot if it falls partly outside the canvas. If set to \'discard\', the reference dot will not be drawn at all. If set to \'hidden\', the reference dot will be clipped to the canvas. If set to \'visible\', the reference dot will be drawn completely. If set to \'extendDomain\', the domain of the overflown axis will be extended such that the reference dot fits into the canvas.

  [DEFAULT: ]`"discard"`
  :::

- :::: 
  [[label](#label)][String \| Number \| ReactElement \| Function]*optional*

  If set a string or a number, default label will be drawn, and the option is content. If set a React element, the option is the custom react element of drawing label. If set a function, the function will be called to render customized label.

  ::: format
  FORMAT:

  ``` format-code
  <ReferenceDot x="a" y= label="MAX"/>
  <ReferenceDot x="a" y= label=/>
  <ReferenceDot x="a" y= label= />
  ```
  :::
  ::::

- ::: 
  [[shape](#shape)][ReactElement \| Function]*optional*

  If set a ReactElement, the shape of dot can be customized. If set a function, the function will be called to render customized shape.
  :::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click in this chart.
  :::

- ::: 
  [[onMouseDown](#onMouseDown)][Function]*optional*

  The customized event handler of mousedown in this chart.
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][Function]*optional*

  The customized event handler of mouseup in this chart.
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][Function]*optional*

  The customized event handler of mouseover in this chart.
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][Function]*optional*

  The customized event handler of mouseout in this chart.
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