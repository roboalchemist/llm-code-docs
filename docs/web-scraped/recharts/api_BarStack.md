# Source: https://recharts.github.io/en-US/api/BarStack/

### BarStack 

Available since Recharts 3.6

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Child Components 

BarStack provides context for these components:

- [`<Bar />`](/en-US/api/Bar/)

#### Properties 

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- :::: 
  [[radius](#radius)][number \| \[number, number, number, number\]]*optional*

  ::: section
  Radius applies only once to all bars inside of this stack group, as if they were one huge bar. Meaning that if you have three bars stacked together, and you set radius to 10, only the outer corners of the entire stack will be rounded: the middle bars will have square corners.

  Unless! The edge bars are smaller than the radius value, in which case the bars at the edge get a lot of radius and the middle one gets a little bit of radius.

  You may want to combine this with setting individual Bar components\' radius to their own values for best effect.`Bar.radius` prop will round corners of individual bars, while `BarStack.radius` will round corners of the entire stack.

  If you provide a single number, it applies to all four corners. If you provide an array of four numbers, they apply to top-left, top-right, bottom-right, bottom-left corners respectively.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[stackId](#stackId)][string \| number]*optional*

  ::: section
  When two Bars have the same axisId and same stackId, then the two Bars are stacked in the chart. This prop sets the stack ID for all Bar components inside this BarStack component. If undefined, a unique id will be generated automatically.

  When both BarStack and individual Bar components have stackId defined, the BarStack\'s stackId wins, and the individual Bar\'s stackId is ignored.
  :::
  ::::