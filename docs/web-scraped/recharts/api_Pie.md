# Source: https://recharts.github.io/en-US/api/Pie/

### Pie 

#### Parent Components 

Pie consumes context provided by these components:

- [`<PieChart />`](/en-US/api/PieChart/)

#### Child Components 

Pie provides context for these components:

- [`<LabelList />`](/en-US/api/LabelList/)

#### Properties 

- ::::: 
  [[activeShape](#activeShape)][(union of 5 variants)]*optional\@deprecated*

  **Deprecated:** Use the \`shape\` prop to create each sector. \`isActive\` designates the \"active\" shape.

  ::: section
  This component is rendered when this graphical item is activated (could be by mouse hover, touch, keyboard, programmatically).
  :::

  ::: format
  FORMAT:

  ``` format-code
  <Pie activeShape= />
  https://recharts.github.io/examples/CustomActiveShapePieChart
  ```
  :::
  :::::

- :::: 
  [[animationBegin](#animationBegin)][number]*optional*

  ::: section
  Specifies when the animation should begin, the unit of this option is ms.
  :::

  [DEFAULT: ]`400`
  ::::

- :::: 
  [[animationDuration](#animationDuration)][number]*optional*

  ::: section
  Specifies the duration of animation, the unit of this option is ms.
  :::

  [DEFAULT: ]`1500`
  ::::

- :::: 
  [[animationEasing](#animationEasing)][\"linear\" \| \"ease\" \| \"ease-in\" \| \"ease-out\" \| \"ease-in-out\"]*optional*

  ::: section
  The type of easing function.
  :::

  [DEFAULT: ]`"ease"`
  ::::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- ::: 
  [[className](#className)][string]*optional*
  :::

- ::: 
  [[cornerRadius](#cornerRadius)][string \| number]*optional*
  :::

- :::: 
  [[cx](#cx)][string \| number]*optional*

  ::: section
  The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
  :::

  [DEFAULT: ]`"50%"`
  ::::

- :::: 
  [[cy](#cy)][string \| number]*optional*

  ::: section
  The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
  :::

  [DEFAULT: ]`"50%"`
  ::::

- ::: 
  [[dangerouslySetInnerHTML](#dangerouslySetInnerHTML)][Object]*optional*
  :::

- :::: 
  [[data](#data)][Array\<ChartDataInput\>]*optional*

  ::: section
  The source data which each element is an object.
  :::
  ::::

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]*optional*

  ::: section
  Decides how to extract the value of this Pie from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value of this Pie.
  :::

  [DEFAULT: ]`"value"`
  ::::

- :::: 
  [[endAngle](#endAngle)][number]*optional*

  ::: section
  Angle, in degrees, at which the chart should end. Can be used to generate partial pies.
  :::

  [DEFAULT: ]`360`
  ::::

- :::: 
  [[hide](#hide)][boolean]*optional*

  ::: section
  Hides the whole graphical element when true.

  Hiding an element is different from removing it from the chart: Hidden graphical elements are still visible in Legend, and can be included in axis domain calculations, depending on `includeHidden` props of your XAxis/YAxis.
  :::

  [DEFAULT: ]`false`
  ::::

- ::: 
  [[id](#id)][string]*optional*
  :::

- :::: 
  [[inactiveShape](#inactiveShape)][(union of 5 variants)]*optional\@deprecated*

  **Deprecated:** Use the \`shape\` prop to modify each sector.

  ::: section
  The shape of inactive sector.
  :::
  ::::

- :::: 
  [[innerRadius](#innerRadius)][string \| number]*optional*

  ::: section
  The inner radius of all the sectors. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[isAnimationActive](#isAnimationActive)][false \| true \| \"auto\"]*optional*

  ::: section
  If set false, animation will be disabled. If set \"auto\", the animation will be disabled in SSR and enabled in browser.
  :::

  [DEFAULT: ]`"auto"`
  ::::

- ::::: 
  [[label](#label)][(union of 6 variants)]*optional*

  ::: section
  Renders one label for each pie sector. Options:

  - `true`: renders default labels;
  - `false`: no labels are rendered;
  - `object` that has `position` prop: the props of LabelList component;
  - `object` that does not have `position` prop: the props of a custom Pie label (similar to Label with position \"outside\"); this variant supports `labelLine`
  - `ReactElement`: a custom label element;
  - `function`: a render function of custom label.

  Also see the `labelLine` prop that draws a line connecting each label to the corresponding sector.
  :::

  [DEFAULT: ]`false`

  ::: format
  FORMAT:

  ``` format-code
  <Pie label= />
  https://recharts.github.io/examples/PieChartWithCustomizedLabel
  ```
  :::
  :::::

- ::::: 
  [[labelLine](#labelLine)][(union of 5 variants)]*optional*

  ::: section
  If false set, label lines will not be drawn. If true set, label lines will be drawn which have the props calculated internally. If object set, label lines will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom label line element. If set a function, the function will be called to render customized label line.
  :::

  [DEFAULT: ]`true`

  ::: format
  FORMAT:

  ``` format-code
  <Pie labelLine= />
  https://recharts.github.io/examples/PieChartWithCustomizedLabel
  ```
  :::
  :::::

- :::: 
  [[legendType](#legendType)][\"none\" \| \"circle\" \| \"cross\" \| \"diamond\" \| \"line\" \| \"plainline\" \| \"rect\" \| \"square\" \| \"star\" \| \"triangle\" \| \"wye\"]*optional*

  ::: section
  The type of icon in legend. If set to \'none\', no legend item will be rendered.
  :::

  [DEFAULT: ]`"rect"`
  ::::

- :::: 
  [[maxRadius](#maxRadius)][number]*optional*

  ::: section
  the max radius of pie
  :::
  ::::

- :::: 
  [[minAngle](#minAngle)][number]*optional*

  ::: section
  The minimum angle of each unzero data.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[nameKey](#nameKey)][string \| number \| Function]*optional*

  ::: section
  The key of each sector\'s name.
  :::

  [DEFAULT: ]`"name"`
  ::::

- :::: 
  [[outerRadius](#outerRadius)][string \| number \| Function]*optional*

  ::: section
  The outer radius of all the sectors. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy. Function should return a string percentage or number.
  :::

  [DEFAULT: ]`"80%"`
  ::::

- ::::: 
  [[paddingAngle](#paddingAngle)][number]*optional*

  ::: section
  The angle between two sectors.
  :::

  [DEFAULT: ]`0`

  ::: format
  FORMAT:

  ``` format-code
  <Pie paddingAngle= />
  https://recharts.github.io/examples/PieChartWithPaddingAngle
  ```
  :::
  :::::

- :::: 
  [[rootTabIndex](#rootTabIndex)][number]*optional*

  ::: section
  The tabindex of wrapper surrounding the cells.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[shape](#shape)][(union of 8 variants)]*optional*

  ::: section
  The custom shape of a Pie Sector. Can also be used to render active sector by checking isActive.
  :::
  ::::

- :::: 
  [[startAngle](#startAngle)][number]*optional*

  ::: section
  Angle in degrees from which the chart should start.
  :::

  [DEFAULT: ]`0`
  ::::

- ::: 
  [[tooltipType](#tooltipType)][\"none\"]*optional*
  :::

- ::: 
  [[zIndex](#zIndex)][number]*optional*

  [DEFAULT: ]`100`
  :::

- ::: 
  [[onAbort](#onAbort)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAbortCapture](#onAbortCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onAnimationEnd](#onAnimationEnd)][AdaptChildAnimationEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of animation end.
  :::
  ::::

- ::: 
  [[onAnimationEndCapture](#onAnimationEndCapture)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIteration](#onAnimationIteration)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIterationCapture](#onAnimationIterationCapture)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onAnimationStart](#onAnimationStart)][AdaptChildAnimationEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of animation start.
  :::
  ::::

- ::: 
  [[onAnimationStartCapture](#onAnimationStartCapture)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAuxClick](#onAuxClick)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAuxClickCapture](#onAuxClickCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBeforeInput](#onBeforeInput)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBeforeInputCapture](#onBeforeInputCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBlur](#onBlur)][AdaptChildFocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBlurCapture](#onBlurCapture)][AdaptChildFocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlay](#onCanPlay)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayCapture](#onCanPlayCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayThrough](#onCanPlayThrough)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayThroughCapture](#onCanPlayThroughCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onChange](#onChange)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onChangeCapture](#onChangeCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onClick](#onClick)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of click on the sectors in this group.
  :::
  ::::

- ::: 
  [[onClickCapture](#onClickCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionEnd](#onCompositionEnd)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionEndCapture](#onCompositionEndCapture)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionStart](#onCompositionStart)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionStartCapture](#onCompositionStartCapture)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionUpdate](#onCompositionUpdate)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionUpdateCapture](#onCompositionUpdateCapture)][AdaptChildCompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onContextMenu](#onContextMenu)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onContextMenuCapture](#onContextMenuCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCopy](#onCopy)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCopyCapture](#onCopyCapture)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCut](#onCut)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCutCapture](#onCutCapture)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDoubleClick](#onDoubleClick)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDoubleClickCapture](#onDoubleClickCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDrag](#onDrag)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragCapture](#onDragCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnd](#onDragEnd)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEndCapture](#onDragEndCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnter](#onDragEnter)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnterCapture](#onDragEnterCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragExit](#onDragExit)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragExitCapture](#onDragExitCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragLeave](#onDragLeave)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragLeaveCapture](#onDragLeaveCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragOver](#onDragOver)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragOverCapture](#onDragOverCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragStart](#onDragStart)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragStartCapture](#onDragStartCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDrop](#onDrop)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDropCapture](#onDropCapture)][AdaptChildDragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDurationChange](#onDurationChange)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDurationChangeCapture](#onDurationChangeCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEmptied](#onEmptied)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEmptiedCapture](#onEmptiedCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEncrypted](#onEncrypted)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEncryptedCapture](#onEncryptedCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEnded](#onEnded)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEndedCapture](#onEndedCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onError](#onError)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onErrorCapture](#onErrorCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onFocus](#onFocus)][AdaptChildFocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onFocusCapture](#onFocusCapture)][AdaptChildFocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onGotPointerCapture](#onGotPointerCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onGotPointerCaptureCapture](#onGotPointerCaptureCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInput](#onInput)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInputCapture](#onInputCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInvalid](#onInvalid)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInvalidCapture](#onInvalidCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyDown](#onKeyDown)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyDownCapture](#onKeyDownCapture)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyPress](#onKeyPress)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyPressCapture](#onKeyPressCapture)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyUp](#onKeyUp)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyUpCapture](#onKeyUpCapture)][AdaptChildKeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoad](#onLoad)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadCapture](#onLoadCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedData](#onLoadedData)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedDataCapture](#onLoadedDataCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedMetadata](#onLoadedMetadata)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedMetadataCapture](#onLoadedMetadataCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadStart](#onLoadStart)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadStartCapture](#onLoadStartCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLostPointerCapture](#onLostPointerCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLostPointerCaptureCapture](#onLostPointerCaptureCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseDown](#onMouseDown)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mousedown on the sectors in this group.
  :::
  ::::

- ::: 
  [[onMouseDownCapture](#onMouseDownCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseEnter](#onMouseEnter)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseenter on the sectors in this group.
  :::
  ::::

- :::: 
  [[onMouseLeave](#onMouseLeave)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseleave on the sectors in this group.
  :::
  ::::

- :::: 
  [[onMouseMove](#onMouseMove)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mousemove on the sectors in this group.
  :::
  ::::

- ::: 
  [[onMouseMoveCapture](#onMouseMoveCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOut](#onMouseOut)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseout on the sectors in this group.
  :::
  ::::

- ::: 
  [[onMouseOutCapture](#onMouseOutCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOver](#onMouseOver)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseover on the sectors in this group.
  :::
  ::::

- ::: 
  [[onMouseOverCapture](#onMouseOverCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseUp](#onMouseUp)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseup on the sectors in this group.
  :::
  ::::

- ::: 
  [[onMouseUpCapture](#onMouseUpCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPaste](#onPaste)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPasteCapture](#onPasteCapture)][AdaptChildClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPause](#onPause)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPauseCapture](#onPauseCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlay](#onPlay)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlayCapture](#onPlayCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlaying](#onPlaying)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlayingCapture](#onPlayingCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerCancel](#onPointerCancel)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerCancelCapture](#onPointerCancelCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerDown](#onPointerDown)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerDownCapture](#onPointerDownCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerEnter](#onPointerEnter)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerEnterCapture](#onPointerEnterCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerLeave](#onPointerLeave)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerLeaveCapture](#onPointerLeaveCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerMove](#onPointerMove)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerMoveCapture](#onPointerMoveCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOut](#onPointerOut)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOutCapture](#onPointerOutCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOver](#onPointerOver)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOverCapture](#onPointerOverCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerUp](#onPointerUp)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerUpCapture](#onPointerUpCapture)][AdaptChildPointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onProgress](#onProgress)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onProgressCapture](#onProgressCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onRateChange](#onRateChange)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onRateChangeCapture](#onRateChangeCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onReset](#onReset)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onResetCapture](#onResetCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onScroll](#onScroll)][AdaptChildUIEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onScrollCapture](#onScrollCapture)][AdaptChildUIEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeeked](#onSeeked)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeekedCapture](#onSeekedCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeeking](#onSeeking)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeekingCapture](#onSeekingCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSelect](#onSelect)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSelectCapture](#onSelectCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onStalled](#onStalled)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onStalledCapture](#onStalledCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSubmit](#onSubmit)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSubmitCapture](#onSubmitCapture)][AdaptChildFormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSuspend](#onSuspend)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSuspendCapture](#onSuspendCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTimeUpdate](#onTimeUpdate)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTimeUpdateCapture](#onTimeUpdateCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchCancel](#onTouchCancel)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchCancelCapture](#onTouchCancelCapture)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchEnd](#onTouchEnd)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchEndCapture](#onTouchEndCapture)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchMove](#onTouchMove)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchMoveCapture](#onTouchMoveCapture)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchStart](#onTouchStart)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchStartCapture](#onTouchStartCapture)][AdaptChildTouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTransitionEnd](#onTransitionEnd)][AdaptChildTransitionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTransitionEndCapture](#onTransitionEndCapture)][AdaptChildTransitionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onVolumeChange](#onVolumeChange)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onVolumeChangeCapture](#onVolumeChangeCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWaiting](#onWaiting)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWaitingCapture](#onWaitingCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWheel](#onWheel)][AdaptChildWheelEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWheelCapture](#onWheelCapture)][AdaptChildWheelEventHandler\<P, T\>]*optional*
  :::