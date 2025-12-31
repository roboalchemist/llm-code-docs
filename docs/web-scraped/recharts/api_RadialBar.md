# Source: https://recharts.github.io/en-US/api/RadialBar/

### RadialBar 

#### Parent Components 

RadialBar consumes context provided by these components:

- [`<RadialBarChart />`](/en-US/api/RadialBarChart/)

#### Child Components 

RadialBar provides context for these components:

- [`<Cell />`](/en-US/api/Cell/)
- [`<LabelList />`](/en-US/api/LabelList/)

#### Properties 

- ::: 
  [[cx](#cx)][Number]*\@deprecated*

  The x-coordinate of center.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[cy](#cy)][Number]*\@deprecated*

  The y-coordinate of center.

  [DEFAULT: ]`0`
  :::

- ::: 
  [[legendType](#legendType)][\'line\' \| \'plainline\' \| \'square\' \| \'rect\'\| \'circle\' \| \'cross\' \| \'diamond\' \| \'square\' \| \'star\' \| \'triangle\' \| \'wye\' \| \'none\']*optional*

  The type of icon in legend. If set to \'none\', no legend item will be rendered.

  [DEFAULT: ]`"rect"`
  :::

- ::: 
  [[label](#label)][Boolean \| Object \| ReactElement \| Function]

  If false set, labels will not be drawn. If true set, labels will be drawn which have the props calculated internally. If object set, labels will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom label element. If set a function, the function will be called to render customized label.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[background](#background)][Boolean \| Object \| ReactElement \| Function]

  If false set, background of bars will not be drawn. If true set, background of bars will be drawn which have the props calculated internally. If object set, background of bars will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom background element. If set a function, the function will be called to render customized background.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[data](#data)][Array]

  The source data which each element is an object.

  [DEFAULT: ]`[]`
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][Boolean \| \"auto\"]

  If set false, animation of radial bars will be disabled.

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

  [DEFAULT: ]`"ease"`
  :::

- ::: 
  [[onAnimationStart](#onAnimationStart)][Function]*optional*

  The customized event handler of animation start
  :::

- ::: 
  [[onAnimationEnd](#onAnimationEnd)][Function]*optional*

  The customized event handler of animation end
  :::

- ::: 
  [[onClick](#onClick)][Function]*optional*

  The customized event handler of click on the sectors in this group
  :::

- ::: 
  [[onMouseDown](#onMouseDown)][Function]*optional*

  The customized event handler of mousedown on the sectors in this group
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][Function]*optional*

  The customized event handler of mouseup on the sectors in this group
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][Function]*optional*

  The customized event handler of mousemove on the sectors in this group
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][Function]*optional*

  The customized event handler of mouseover on the sectors in this group
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][Function]*optional*

  The customized event handler of mouseout on the sectors in this group
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  The customized event handler of mouseenter on the sectors in this group
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  The customized event handler of mouseleave on the sectors in this group
  :::