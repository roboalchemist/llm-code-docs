# Source: https://recharts.github.io/en-US/api/Area/

### Area 

#### Parent Components 

Area consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<FunnelChart />`](/en-US/api/FunnelChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Child Components 

Area provides context for these components:

- [`<LabelList />`](/en-US/api/LabelList/)

#### Properties 

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]

  ::: section
  Decides how to extract the value of this Area from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value of this Area.

  If undefined, it will reuse the dataKey of YAxis.
  :::
  ::::

- :::: 
  [[activeDot](#activeDot)][false \| true \| Function \| Partial\<ActiveDotProps\> \| ReactNode]*optional*

  ::: section
  The dot is shown when user enter an area chart and this chart has tooltip. If false set, no active dot will not be drawn. If true set, active dot will be drawn which have the props calculated internally. If object set, active dot will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom active dot element. If set a function, the function will be called to render customized active dot.
  :::

  [DEFAULT: ]`true`
  ::::

- :::: 
  [[animationBegin](#animationBegin)][number]*optional*

  ::: section
  Specifies when the animation should begin, the unit of this option is ms.
  :::

  [DEFAULT: ]`0`
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

- :::: 
  [[baseLine](#baseLine)][number \| Array\<readonly NullableCoordinate\>]*optional*

  ::: section
  Baseline of the area:

  - number: uses the corresponding axis value as a flat baseline;
  - an array of coordinates: describes a custom baseline path.
  :::
  ::::

- ::: 
  [[baseValue](#baseValue)][number \| \"dataMin\" \| \"dataMax\"]*optional*
  :::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- ::: 
  [[className](#className)][string]*optional*
  :::

- :::: 
  [[connectNulls](#connectNulls)][boolean]*optional*

  ::: section
  Whether to connect the curve across null points.
  :::

  [DEFAULT: ]`false`
  ::::

- ::: 
  [[data](#data)][Array\<unknown\>]*optional*
  :::

- :::: 
  [[dot](#dot)][false \| true \| Function \| Partial\<Props\> \| ReactNode]*optional*

  ::: section
  If false set, dots will not be drawn. If true set, dots will be drawn which have the props calculated internally. If object set, dots will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom dot element. If set a function, the function will be called to render customized dot.
  :::

  [DEFAULT: ]`false`
  ::::

- :::: 
  [[hide](#hide)][boolean]*optional*

  ::: section
  Hides the whole graphical element when true.

  Hiding an element is different from removing it from the chart: Hidden graphical elements are still visible in Legend, and can be included in axis domain calculations, depending on `includeHidden` props of your XAxis/YAxis.
  :::

  [DEFAULT: ]`false`
  ::::

- :::: 
  [[id](#id)][string]*optional*

  ::: section
  Unique identifier of this component. Used as a HTML attribute `id`, and also to identify this element internally.

  If undefined, Recharts will generate a unique ID automatically.
  :::
  ::::

- :::: 
  [[isAnimationActive](#isAnimationActive)][false \| true \| \"auto\"]*optional*

  ::: section
  If set false, animation of area will be disabled. If set \"auto\", the animation will be disabled in SSR and enabled in browser.
  :::

  [DEFAULT: ]`"auto"`
  ::::

- ::: 
  [[isRange](#isRange)][boolean]*optional*
  :::

- :::: 
  [[label](#label)][false \| true \| ReactNode \| Function \| Props]*optional*

  ::: section
  Renders one label for each data point. Options:

  - `true`: renders default labels;
  - `false`: no labels are rendered;
  - `object`: the props of LabelList component;
  - `ReactElement`: a custom label element;
  - `function`: a render function of custom label.
  :::

  [DEFAULT: ]`false`
  ::::

- :::: 
  [[legendType](#legendType)][\"none\" \| \"circle\" \| \"cross\" \| \"diamond\" \| \"line\" \| \"plainline\" \| \"rect\" \| \"square\" \| \"star\" \| \"triangle\" \| \"wye\"]*optional*

  ::: section
  The type of icon in legend. If set to \'none\', no legend item will be rendered.
  :::

  [DEFAULT: ]`"line"`
  ::::

- :::: 
  [[name](#name)][string]*optional*

  ::: section
  The name of data. This option will be used in tooltip and legend to represent this graphical item. If no value was set to this option, the value of dataKey will be used alternatively.
  :::
  ::::

- :::: 
  [[stackId](#stackId)][string \| number]*optional*

  ::: section
  When two Areas have the same axisId and same stackId, then the two Areas are stacked in the chart.
  :::
  ::::

- :::: 
  [[stroke](#stroke)][string]*optional*

  ::: section
  The stroke color. If \"none\", no line will be drawn.
  :::

  [DEFAULT: ]`"#3182bd"`
  ::::

- :::: 
  [[strokeWidth](#strokeWidth)][string \| number]*optional*

  ::: section
  The width of the stroke
  :::

  [DEFAULT: ]`1`
  ::::

- ::: 
  [[tooltipType](#tooltipType)][\"none\"]*optional*
  :::

- ::::: 
  [[type](#type)][\"step\" \| \"basis\" \| \"basisClosed\" \| \"basisOpen\" \| \"bumpX\" \| \"bumpY\" \| \"bump\" \| \"linear\" \| \"linearClosed\" \| \"natural\" \| \"monotoneX\" \| \"monotoneY\" \| \"monotone\" \| \"stepBefore\" \| \"stepAfter\" \| CurveFactory]*optional*

  ::: section
  The interpolation type of curve. Allows custom interpolation function.
  :::

  [DEFAULT: ]`"linear"`

  ::: examples
  Examples:

  - [An AreaChart which has two area with different interpolation.](/en-US/examples/CardinalAreaChart/)
  - [https://github.com/d3/d3-shape#curves](https://github.com/d3/d3-shape#curves)
  :::
  :::::

- :::: 
  [[unit](#unit)][string \| number]*optional*

  ::: section
  The unit of data. This option will be used in tooltip.
  :::
  ::::

- :::: 
  [[xAxisId](#xAxisId)][string \| number]*optional*

  ::: section
  The id of XAxis which is corresponding to the data. Required when there are multiple XAxes.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[yAxisId](#yAxisId)][string \| number]*optional*

  ::: section
  The id of YAxis which is corresponding to the data. Required when there are multiple YAxes.
  :::

  [DEFAULT: ]`0`
  ::::

- ::::: 
  [[zIndex](#zIndex)][number]*optional*

  ::: section
  Z-Index of this component and its children. The higher the value, the more on top it will be rendered. Components with higher zIndex will appear in front of components with lower zIndex. If undefined or 0, the content is rendered in the default layer without portals.
  :::

  [DEFAULT: ]`100`

  ::: examples
  Examples:

  - [Z-Index and layers guide](/en-US/guide/zIndex/)
  :::
  :::::

- ::: 
  [[onAbort](#onAbort)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAbortCapture](#onAbortCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onAnimationEnd](#onAnimationEnd)][AnimationEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of animation end
  :::
  ::::

- ::: 
  [[onAnimationEndCapture](#onAnimationEndCapture)][AnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIteration](#onAnimationIteration)][AnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIterationCapture](#onAnimationIterationCapture)][AnimationEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onAnimationStart](#onAnimationStart)][AnimationEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of animation start
  :::
  ::::

- ::: 
  [[onAnimationStartCapture](#onAnimationStartCapture)][AnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAuxClick](#onAuxClick)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAuxClickCapture](#onAuxClickCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBeforeInput](#onBeforeInput)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBeforeInputCapture](#onBeforeInputCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBlur](#onBlur)][FocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onBlurCapture](#onBlurCapture)][FocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlay](#onCanPlay)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayCapture](#onCanPlayCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayThrough](#onCanPlayThrough)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCanPlayThroughCapture](#onCanPlayThroughCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onChange](#onChange)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onChangeCapture](#onChangeCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onClick](#onClick)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of click on the curve
  :::
  ::::

- ::: 
  [[onClickCapture](#onClickCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionEnd](#onCompositionEnd)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionEndCapture](#onCompositionEndCapture)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionStart](#onCompositionStart)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionStartCapture](#onCompositionStartCapture)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionUpdate](#onCompositionUpdate)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCompositionUpdateCapture](#onCompositionUpdateCapture)][CompositionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onContextMenu](#onContextMenu)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onContextMenuCapture](#onContextMenuCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCopy](#onCopy)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCopyCapture](#onCopyCapture)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCut](#onCut)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onCutCapture](#onCutCapture)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDoubleClick](#onDoubleClick)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDoubleClickCapture](#onDoubleClickCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDrag](#onDrag)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragCapture](#onDragCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnd](#onDragEnd)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEndCapture](#onDragEndCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnter](#onDragEnter)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragEnterCapture](#onDragEnterCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragExit](#onDragExit)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragExitCapture](#onDragExitCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragLeave](#onDragLeave)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragLeaveCapture](#onDragLeaveCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragOver](#onDragOver)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragOverCapture](#onDragOverCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragStart](#onDragStart)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDragStartCapture](#onDragStartCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDrop](#onDrop)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDropCapture](#onDropCapture)][DragEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDurationChange](#onDurationChange)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onDurationChangeCapture](#onDurationChangeCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEmptied](#onEmptied)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEmptiedCapture](#onEmptiedCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEncrypted](#onEncrypted)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEncryptedCapture](#onEncryptedCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEnded](#onEnded)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onEndedCapture](#onEndedCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onError](#onError)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onErrorCapture](#onErrorCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onFocus](#onFocus)][FocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onFocusCapture](#onFocusCapture)][FocusEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onGotPointerCapture](#onGotPointerCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onGotPointerCaptureCapture](#onGotPointerCaptureCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInput](#onInput)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInputCapture](#onInputCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInvalid](#onInvalid)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onInvalidCapture](#onInvalidCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyDown](#onKeyDown)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyDownCapture](#onKeyDownCapture)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyPress](#onKeyPress)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyPressCapture](#onKeyPressCapture)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyUp](#onKeyUp)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onKeyUpCapture](#onKeyUpCapture)][KeyboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoad](#onLoad)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadCapture](#onLoadCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedData](#onLoadedData)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedDataCapture](#onLoadedDataCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedMetadata](#onLoadedMetadata)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadedMetadataCapture](#onLoadedMetadataCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadStart](#onLoadStart)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLoadStartCapture](#onLoadStartCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLostPointerCapture](#onLostPointerCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onLostPointerCaptureCapture](#onLostPointerCaptureCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseDown](#onMouseDown)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mousedown on the curve
  :::
  ::::

- ::: 
  [[onMouseDownCapture](#onMouseDownCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseEnter](#onMouseEnter)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mouseenter on the curve
  :::
  ::::

- :::: 
  [[onMouseLeave](#onMouseLeave)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mouseleave on the curve
  :::
  ::::

- :::: 
  [[onMouseMove](#onMouseMove)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mousemove on the curve
  :::
  ::::

- ::: 
  [[onMouseMoveCapture](#onMouseMoveCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOut](#onMouseOut)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mouseout on the curve
  :::
  ::::

- ::: 
  [[onMouseOutCapture](#onMouseOutCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOver](#onMouseOver)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mouseover on the curve
  :::
  ::::

- ::: 
  [[onMouseOverCapture](#onMouseOverCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseUp](#onMouseUp)][CurveMouseEventHandler]*optional*

  ::: section
  The customized event handler of mouseup on the curve
  :::
  ::::

- ::: 
  [[onMouseUpCapture](#onMouseUpCapture)][RechartsMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPaste](#onPaste)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPasteCapture](#onPasteCapture)][ClipboardEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPause](#onPause)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPauseCapture](#onPauseCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlay](#onPlay)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlayCapture](#onPlayCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlaying](#onPlaying)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPlayingCapture](#onPlayingCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerCancel](#onPointerCancel)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerCancelCapture](#onPointerCancelCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerDown](#onPointerDown)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerDownCapture](#onPointerDownCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerEnter](#onPointerEnter)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerEnterCapture](#onPointerEnterCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerLeave](#onPointerLeave)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerLeaveCapture](#onPointerLeaveCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerMove](#onPointerMove)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerMoveCapture](#onPointerMoveCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOut](#onPointerOut)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOutCapture](#onPointerOutCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOver](#onPointerOver)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerOverCapture](#onPointerOverCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerUp](#onPointerUp)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onPointerUpCapture](#onPointerUpCapture)][PointerEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onProgress](#onProgress)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onProgressCapture](#onProgressCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onRateChange](#onRateChange)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onRateChangeCapture](#onRateChangeCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onReset](#onReset)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onResetCapture](#onResetCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onScroll](#onScroll)][UIEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onScrollCapture](#onScrollCapture)][UIEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeeked](#onSeeked)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeekedCapture](#onSeekedCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeeking](#onSeeking)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSeekingCapture](#onSeekingCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSelect](#onSelect)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSelectCapture](#onSelectCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onStalled](#onStalled)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onStalledCapture](#onStalledCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSubmit](#onSubmit)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSubmitCapture](#onSubmitCapture)][FormEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSuspend](#onSuspend)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onSuspendCapture](#onSuspendCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTimeUpdate](#onTimeUpdate)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTimeUpdateCapture](#onTimeUpdateCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchCancel](#onTouchCancel)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchCancelCapture](#onTouchCancelCapture)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchEnd](#onTouchEnd)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchEndCapture](#onTouchEndCapture)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchMove](#onTouchMove)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchMoveCapture](#onTouchMoveCapture)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchStart](#onTouchStart)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTouchStartCapture](#onTouchStartCapture)][TouchEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTransitionEnd](#onTransitionEnd)][TransitionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onTransitionEndCapture](#onTransitionEndCapture)][TransitionEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onVolumeChange](#onVolumeChange)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onVolumeChangeCapture](#onVolumeChangeCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWaiting](#onWaiting)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWaitingCapture](#onWaitingCapture)][ReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWheel](#onWheel)][WheelEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onWheelCapture](#onWheelCapture)][WheelEventHandler\<P, T\>]*optional*
  :::