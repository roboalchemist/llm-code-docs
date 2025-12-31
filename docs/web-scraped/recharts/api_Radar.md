# Source: https://recharts.github.io/en-US/api/Radar/

### Radar 

#### Parent Components 

Radar consumes context provided by these components:

- [`<RadarChart />`](/en-US/api/RadarChart/)

#### Child Components 

Radar provides context for these components:

- [`<LabelList />`](/en-US/api/LabelList/)

#### Properties 

- ::: 
  [[dataKey](#dataKey)][String \| Number \| Function]

  The key of a group of data which should be unique in a radar chart.
  :::

- ::: 
  [[points](#points)][Array]

  The coordinates of all the vertexes of the radar shape, like \[\].
  :::

- ::: 
  [[shape](#shape)][Element \| Function]

  The custom shape element. If set a function, the function will be called to render customized shape.
  :::

- ::: 
  [[dot](#dot)][Bool \| Object \| Element \| Function]

  If false set, dots will not be drawn. If true set, dots will be drawn which have the props calculated internally. If object set, dots will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom dot element. If set a function, the function will be called to render customized dot.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[legendType](#legendType)][\'line\' \| \'plainline\' \| \'square\' \| \'rect\'\| \'circle\' \| \'cross\' \| \'diamond\' \| \'square\' \| \'star\' \| \'triangle\' \| \'wye\' \| \'none\']*optional*

  The type of icon in legend. If set to \'none\', no legend item will be rendered.

  [DEFAULT: ]`"rect"`
  :::

- ::: 
  [[label](#label)][Bool \| Object \| Element \| Function]

  If false set, labels will not be drawn. If true set, labels will be drawn which have the props calculated internally. If object set, labels will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom label element. If set a function, the function will be called to render customized label.

  [DEFAULT: ]`false`
  :::

- ::: 
  [[isAnimationActive](#isAnimationActive)][Boolean \| \"auto\"]

  If set false, animation of polygon will be disabled.

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