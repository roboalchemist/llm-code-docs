# Source: https://recharts.github.io/en-US/api/ReferenceArea/

### ReferenceArea 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

ReferenceArea consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Child Components 

ReferenceArea provides context for these components:

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
  [[x1](#x1)][Number \| String]*optional*

  A boundary value of the area. If the specified x-axis is a number axis, the type of x must be Number. If the specified x-axis is a category axis, the value of x must be one of the categories. If one of x1 or x2 is invalidate, the area will cover along x-axis.
  :::

- ::: 
  [[x2](#x2)][Number \| String]*optional*

  A boundary value of the area. If the specified x-axis is a number axis, the type of x must be Number. If the specified x-axis is a category axis, the value of x must be one of the categories. If one of x1 or x2 is invalidate, the area will cover along x-axis.
  :::

- ::: 
  [[y1](#y1)][Number \| String]*optional*

  A boundary value of the area. If the specified y-axis is a number axis, the type of y must be Number. If the specified y-axis is a category axis, the value of y must be one of the categories. If one of y1 or y2 is invalidate, the area will cover along y-axis.
  :::

- ::: 
  [[y2](#y2)][Number \| String]*optional*

  A boundary value of the area. If the specified y-axis is a number axis, the type of y must be Number. If the specified y-axis is a category axis, the value of y must be one of the categories. If one of y1 or y2 is invalidate, the area will cover along y-axis.
  :::

- :::: 
  [[ifOverflow](#ifOverflow)][\'discard\' \| \'hidden\' \| \'visible\' \| \'extendDomain\']

  Defines how to draw the reference area if it falls partly outside the canvas. If set to \'discard\', the reference area will not be drawn at all. If set to \'hidden\', the reference area will be clipped to the canvas. If set to \'visible\', the reference area will be drawn completely. If set to \'extendDomain\', the domain of the overflown axis will be extended such that the reference area fits into the canvas.

  [DEFAULT: ]`"discard"`

  ::: examples
  Examples:

  - [A LineChart with domain extending ReferenceArea](https://codesandbox.io/s/reference-area-ifoverflow-extenddomain-hdo35m)
  :::
  ::::

- ::::: 
  [[label](#label)][String \| Number \| ReactElement \| Function]*optional*

  If set a string or a number, default label will be drawn, and the option is content. If set a React element, the option is the custom react element of drawing label. If set a function, the function will be called to render customized label.

  ::: format
  FORMAT:

  ``` format-code
  <ReferenceArea x1="01" x2="08" label="MAX"/>
  <ReferenceArea y1= y2= label=/>
  ```
  :::

  ::: examples
  Examples:

  - [ReferenceLines with label](/en-US/examples/LineChartWithReferenceLines)
  :::
  :::::

- ::::: 
  [[shape](#shape)][ReactElement \| Function]*optional*

  Renders a svg returned by the react element or function.

  ::: format
  FORMAT:

  ``` format-code
  <ReferenceArea shape=/>
  ```
  :::

  ::: examples
  Examples:

  - [ReferenceArea with shape](https://codesandbox.io/s/reference-area-shape-502rx)
  :::
  :::::