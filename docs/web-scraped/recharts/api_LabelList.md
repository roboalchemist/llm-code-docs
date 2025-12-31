# Source: https://recharts.github.io/en-US/api/LabelList/

### LabelList 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

LabelList consumes context provided by these components:

- [`<Area />`](/en-US/api/Area/)
- [`<Bar />`](/en-US/api/Bar/)
- [`<Line />`](/en-US/api/Line/)
- [`<Pie />`](/en-US/api/Pie/)
- [`<Radar />`](/en-US/api/Radar/)
- [`<RadialBar />`](/en-US/api/RadialBar/)
- [`<Scatter />`](/en-US/api/Scatter/)

#### Properties 

- :::: 
  [[angle](#angle)][number]*optional*

  ::: section
  Text rotation angle in degrees. The text will be rotated around the (x, y) coordinates as the pivot point. Positive values rotate clockwise, negative values rotate counterclockwise.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[clockWise](#clockWise)][boolean]*optional*

  ::: section
  The parameter to calculate the view box of label in radial charts.
  :::
  ::::

- :::::: 
  [[content](#content)][ReactNode \| Function]*optional*

  ::: section
  If set a React element, the option is the customized React element of rendering each label. If set to a function, the function is called once for each item
  :::

  ::: format
  FORMAT:

  ``` format-code
  <LabelList content= />
  ```
  :::

  ::: examples
  Examples:

  - [Customized content of LabelList in a BarChart](/en-US/examples/BarChartWithMinHeight/)
  :::
  ::::::

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]*optional*

  ::: section
  Decides how to extract the value of each label from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value of each label.

  If set, then valueAccessor will be ignored.

  Scatter requires this prop to be set. Other graphical components will show the same value as the dataKey of the component by default.
  :::
  ::::

- :::: 
  [[formatter](#formatter)][Function]*optional*

  ::: section
  Function to customize how content is serialized before rendering.
  :::
  ::::

- :::: 
  [[id](#id)][string]*optional*

  ::: section
  The unique id of this component, which will be used to generate unique clip path id internally. This props is suggested to be set in SSR.
  :::
  ::::

- :::: 
  [[offset](#offset)][string \| number]*optional*

  ::: section
  The offset to the specified \"position\". Direction of the offset depends on the position.
  :::

  [DEFAULT: ]`5`
  ::::

- :::: 
  [[position](#position)][\"end\" \| \"top\" \| \"left\" \| \"right\" \| \"bottom\" \| \"inside\" \| \"outside\" \| \"insideLeft\" \| \"insideRight\" \| \"insideTop\" \| \"insideBottom\" \| \"insideTopLeft\" \| \"insideBottomLeft\" \| \"insideTopRight\" \| \"insideBottomRight\" \| \"insideStart\" \| \"insideEnd\" \| \"center\" \| \"centerTop\" \| \"centerBottom\" \| \"middle\" \| %\` \| undefined; y?: number \| \`\$%\` \| undefined; }]*optional*

  ::: section
  The position of label relative to the view box.
  :::

  [DEFAULT: ]`"middle"`
  ::::

- ::: 
  [[textBreakAll](#textBreakAll)][boolean]*optional*

  [DEFAULT: ]`false`
  :::

- :::: 
  [[valueAccessor](#valueAccessor)][Function]*optional*

  ::: section
  The accessor function to get the value of each label. Is ignored if dataKey is specified.
  :::
  ::::

- ::::: 
  [[zIndex](#zIndex)][number]*optional*

  ::: section
  Z-Index of this component and its children. The higher the value, the more on top it will be rendered. Components with higher zIndex will appear in front of components with lower zIndex. If undefined or 0, the content is rendered in the default layer without portals.
  :::

  [DEFAULT: ]`2000`

  ::: examples
  Examples:

  - [Z-Index and layers guide](/en-US/guide/zIndex/)
  :::
  :::::