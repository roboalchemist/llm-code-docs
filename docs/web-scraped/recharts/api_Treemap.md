# Source: https://recharts.github.io/en-US/api/Treemap/

### Treemap 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

Treemap consumes context provided by these components:

- [`<ResponsiveContainer />`](/en-US/api/ResponsiveContainer/)

#### Properties 

- ::: 
  [[width](#width)][Number]

  The width of chart container.
  :::

- ::: 
  [[height](#height)][Number]

  The height of chart container.
  :::

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]

  The key of a group of data which should be unique in a treemap.

  [DEFAULT: ]`"'value'"`
  :::

- ::: 
  [[nameKey](#nameKey)][String]

  The key of each sector\'s name.

  [DEFAULT: ]`"'name'"`
  :::

- ::: 
  [[aspectRatio](#aspectRatio)][Number]

  The treemap will try to keep every single rectangle\'s aspect ratio near the aspectRatio given.

  [DEFAULT: ]`1.618033988749895`
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][boolean \| \"auto\"]

  If set false, animation of area will be disabled.

  [DEFAULT: ]`"auto"`
  :::

- ::: 
  [[animationBegin](#animationBegin)][Number]

  Specifies when the animation should begin, the unit of this option is ms.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[animationDuration](#animationDuration)][Number]

  Specifies the duration of animation, the unit of this option is ms.

  [DEFAULT: ]`1500`
  :::

- ::: 
  [[animationEasing](#animationEasing)][\'ease\' \| \'ease-in\' \| \'ease-out\' \| \'ease-in-out\' \| \'linear\']

  The type of easing function.

  [DEFAULT: ]`"linear"`
  :::

- ::: 
  [[onAnimationStart](#onAnimationStart)][Function]*optional*

  The customized event handler of animation start
  :::

- ::: 
  [[onAnimationEnd](#onAnimationEnd)][Function]*optional*

  The customized event handler of animation end
  :::