# Source: https://recharts.github.io/en-US/api/PolarAngleAxis/

### PolarAngleAxis 

#### Parent Components 

PolarAngleAxis consumes context provided by these components:

- [`<PieChart />`](/en-US/api/PieChart/)
- [`<RadarChart />`](/en-US/api/RadarChart/)
- [`<RadialBarChart />`](/en-US/api/RadialBarChart/)

#### Child Components 

PolarAngleAxis provides context for these components:

- [`<Label />`](/en-US/api/Label/)

#### Properties 

- ::: 
  [[allowDecimals](#allowDecimals)][boolean]*optional*

  [DEFAULT: ]`false`
  :::

- :::: 
  [[allowDuplicatedCategory](#allowDuplicatedCategory)][boolean]*optional*

  ::: section
  Allow the axis has duplicated categories or not when the type of axis is \"category\".
  :::

  [DEFAULT: ]`true`
  ::::

- ::: 
  [[angleAxisId](#angleAxisId)][string \| number]*optional*

  [DEFAULT: ]`0`
  :::

- :::: 
  [[axisLine](#axisLine)][false \| true \| React.SVGProps\<SVGLineElement\>]*optional*

  ::: section
  If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props merged by the internal calculated props and the option.
  :::

  [DEFAULT: ]`true`
  ::::

- :::: 
  [[axisLineType](#axisLineType)][\"circle\" \| \"polygon\"]*optional*

  ::: section
  The type of axis line.
  :::

  [DEFAULT: ]`"polygon"`
  ::::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- :::: 
  [[cx](#cx)][string \| number]*optional*

  ::: section
  The x-coordinate of center. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[cy](#cy)][string \| number]*optional*

  ::: section
  The y-coordinate of center. When used inside a chart context, this prop is calculated based on the chart\'s dimensions, and this prop is ignored.

  This is only used when rendered outside a chart context.
  :::

  [DEFAULT: ]`0`
  ::::

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]*optional*

  ::: section
  Decides how to extract the value from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value.

  If undefined, it will reuse the dataKey of graphical items.
  :::
  ::::

- ::: 
  [[domain](#domain)][Array\<readonly string\> \| Array\<readonly number\> \| readonly \[AxisDomainItem, AxisDomainItem\] \| Function]*optional*
  :::

- :::: 
  [[orientation](#orientation)][string \| number]*optional*

  ::: section
  The orientation of axis text.
  :::

  [DEFAULT: ]`"outer"`
  ::::

- :::: 
  [[radius](#radius)][string \| number]*optional*

  ::: section
  The outer radius of circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.
  :::
  ::::

- ::: 
  [[reversed](#reversed)][boolean]*optional*

  [DEFAULT: ]`false`
  :::

- ::: 
  [[scale](#scale)][(union of 17 variants)]*optional*

  [DEFAULT: ]`"auto"`
  :::

- :::: 
  [[tick](#tick)][(union of 5 variants)]*optional*

  ::: section
  If false set, ticks will not be drawn. If true set, ticks will be drawn which have the props calculated internally. If object set, ticks will be drawn which have the props merged by the internal calculated props and the option. If ReactElement set, the option can be the custom tick element. If set a function, the function will be called to render customized ticks.
  :::

  [DEFAULT: ]`true`
  ::::

- ::: 
  [[tickCount](#tickCount)][number]*optional*
  :::

- :::: 
  [[tickFormatter](#tickFormatter)][Function]*optional*

  ::: section
  The formatter function of ticks.
  :::
  ::::

- :::: 
  [[tickLine](#tickLine)][false \| true \| React.SVGProps\<SVGLineElement\>]*optional*

  ::: section
  If false set, tick lines will not be drawn. If true set, tick lines will be drawn which have the props calculated internally. If object set, tick lines will be drawn which have the props merged by the internal calculated props and the option.
  :::

  [DEFAULT: ]`true`
  ::::

- :::: 
  [[ticks](#ticks)][Array\<readonly TickItem\>]*optional*

  ::: section
  The array of every tick\'s value and angle.
  :::
  ::::

- ::: 
  [[tickSize](#tickSize)][number]*optional*

  [DEFAULT: ]`8`
  :::

- :::: 
  [[type](#type)][\"number\" \| \"category\"]*optional*

  ::: section
  The type of axis.
  :::

  [DEFAULT: ]`"category"`
  ::::

- ::: 
  [[zIndex](#zIndex)][number]*optional*

  [DEFAULT: ]`500`
  :::

- ::: 
  [[onAbort](#onAbort)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAbortCapture](#onAbortCapture)][AdaptChildReactEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationEnd](#onAnimationEnd)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationEndCapture](#onAnimationEndCapture)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIteration](#onAnimationIteration)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationIterationCapture](#onAnimationIterationCapture)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onAnimationStart](#onAnimationStart)][AdaptChildAnimationEventHandler\<P, T\>]*optional*
  :::

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
  The customized event handler of click on the ticks of this axis
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
  The customized event handler of mousedown on the the ticks of this axis
  :::
  ::::

- ::: 
  [[onMouseDownCapture](#onMouseDownCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseEnter](#onMouseEnter)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseenter on the ticks of this axis
  :::
  ::::

- :::: 
  [[onMouseLeave](#onMouseLeave)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseleave on the ticks of this axis
  :::
  ::::

- :::: 
  [[onMouseMove](#onMouseMove)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mousemove on the ticks of this axis
  :::
  ::::

- ::: 
  [[onMouseMoveCapture](#onMouseMoveCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOut](#onMouseOut)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseout on the ticks of this axis
  :::
  ::::

- ::: 
  [[onMouseOutCapture](#onMouseOutCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseOver](#onMouseOver)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseover on the ticks of this axis
  :::
  ::::

- ::: 
  [[onMouseOverCapture](#onMouseOverCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- :::: 
  [[onMouseUp](#onMouseUp)][AdaptChildMouseEventHandler\<P, T\>]*optional*

  ::: section
  The customized event handler of mouseup on the ticks of this axis
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