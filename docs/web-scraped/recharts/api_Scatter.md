# Source: https://recharts.github.io/en-US/api/Scatter/

### Scatter 

#### Parent Components 

Scatter consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<FunnelChart />`](/en-US/api/FunnelChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Child Components 

Scatter provides context for these components:

- [`<Cell />`](/en-US/api/Cell/)
- [`<ErrorBar />`](/en-US/api/ErrorBar/)
- [`<LabelList />`](/en-US/api/LabelList/)

#### Properties 

- :::::: 
  [[activeShape](#activeShape)][(union of 12 variants)]*optional*

  ::: section
  This component is rendered when this graphical item is activated (could be by mouse hover, touch, keyboard, programmatically).
  :::

  ::: format
  FORMAT:

  ``` format-code
  <Scatter activeShape=} />
  ```
  :::

  ::: examples
  Examples:

  - [Scatter chart with custom active shape](http://recharts.github.io/en-US/examples/SimpleScatterChart/)
  :::
  ::::::

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

  [DEFAULT: ]`400`
  ::::

- :::: 
  [[animationEasing](#animationEasing)][\"linear\" \| \"ease\" \| \"ease-in\" \| \"ease-out\" \| \"ease-in-out\"]*optional*

  ::: section
  The type of easing function.
  :::

  [DEFAULT: ]`"linear"`
  ::::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- ::: 
  [[className](#className)][string]*optional*
  :::

- ::: 
  [[data](#data)][Array\<any\>]*optional*
  :::

- :::: 
  [[dataKey](#dataKey)][string \| number \| Function]*optional*

  ::: section
  Decides how to extract the numerical value of this Scatter from the data:

  - `string`: the name of the field in the data object;
  - `number`: the index of the field in the data;
  - `function`: a function that receives the data object and returns the value of this Scatter.

  If undefined, it will reuse the dataKey of YAxis.
  :::
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
  If set false, animation of Scatter points will be disabled. If set \"auto\", the animation will be disabled in SSR and enabled in browser.
  :::

  [DEFAULT: ]`"auto"`
  ::::

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

- ::::: 
  [[legendType](#legendType)][\"none\" \| \"circle\" \| \"cross\" \| \"diamond\" \| \"line\" \| \"plainline\" \| \"rect\" \| \"square\" \| \"star\" \| \"triangle\" \| \"wye\"]*optional*

  ::: section
  The type of icon in legend. If set to \'none\', no legend item will be rendered.
  :::

  [DEFAULT: ]`"circle"`

  ::: format
  FORMAT:

  ``` format-code
  <Scatter legendType="diamond" />
  ```
  :::
  :::::

- :::::: 
  [[line](#line)][(union of 5 variants)]*optional*

  ::: section
  Renders line connecting individual points. Options:

  - `false`: no line is drawn.
  - `true`: a default line is drawn.
  - `ReactElement`: the option is the custom line element.
  - `function`: the function will be called to render customized line.
  - `object`: the option is the props of Curve element.

  Also see the `lineType` prop which controls how is this line calculated.
  :::

  [DEFAULT: ]`false`

  ::: format
  FORMAT:

  ``` format-code
  <Scatter line />
  <Scatter line= />
  <Scatter line=} />
  ```
  :::

  ::: examples
  Examples:

  - [Scatter chart with joint line](/en-US/examples/JointLineScatterChart/)
  :::
  ::::::

- ::::: 
  [[lineJointType](#lineJointType)][\"step\" \| \"basis\" \| \"basisClosed\" \| \"basisOpen\" \| \"bumpX\" \| \"bumpY\" \| \"bump\" \| \"linear\" \| \"linearClosed\" \| \"natural\" \| \"monotoneX\" \| \"monotoneY\" \| \"monotone\" \| \"stepBefore\" \| \"stepAfter\" \| CurveFactory]*optional*

  ::: section
  Determines the shape of joint line. Same as `type` prop on Curve, Line and Area components.

  Has no effect if `line` prop is not set or is false or if `lineType` is \'fitting\'.
  :::

  [DEFAULT: ]`"linear"`

  ::: examples
  Examples:

  - [Scatter chart with joint line](http://recharts.github.io/en-US/examples/JointLineScatterChart/)
  :::
  :::::

- :::::: 
  [[lineType](#lineType)][\"fitting\" \| \"joint\"]*optional*

  ::: section
  Determines calculation method of the line if the `line` prop is set. Options:

  - `'joint'`: line will be generated by connecting all the points.
  - `'fitting'`: line will be generated by fitting algorithm (linear regression).

  Has no effect if `line` prop is not set or is false.
  :::

  [DEFAULT: ]`"joint"`

  ::: format
  FORMAT:

  ``` format-code
  <Scatter line lineType="fitting" />
  ```
  :::

  ::: examples
  Examples:

  - [Scatter chart with joint line](http://recharts.github.io/en-US/examples/JointLineScatterChart/)
  :::
  ::::::

- :::: 
  [[name](#name)][string]*optional*

  ::: section
  The name of data. This option will be used in tooltip and legend to represent this graphical item. If no value was set to this option, the value of dataKey will be used alternatively.
  :::
  ::::

- :::::: 
  [[shape](#shape)][(union of 12 variants)]*optional*

  ::: section
  Determines the shape of individual data points. Can be one of the predefined shapes as a string. If set a ReactElement, the shape of line can be customized. If set a function, the function will be called to render customized shape.
  :::

  [DEFAULT: ]`"circle"`

  ::: format
  FORMAT:

  ``` format-code
  <Scatter shape= />
  <Scatter shape="diamond" />
  ```
  :::

  ::: examples
  Examples:

  - [Scatter chart with custom shapes](/en-US/examples/JointLineScatterChart/)
  :::
  ::::::

- ::: 
  [[tooltipType](#tooltipType)][\"none\"]*optional*
  :::

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
  [[zAxisId](#zAxisId)][string \| number]*optional*

  ::: section
  The id of ZAxis which is corresponding to the data. Required when there are multiple ZAxes.

  ZAxis does not render directly, has no ticks and no tick line. It is used to control the size of each scatter point.
  :::

  [DEFAULT: ]`0`

  ::: examples
  Examples:

  - [Scatter chart with Z axis](/en-US/examples/ThreeDimScatterChart/)
  :::
  :::::

- ::::: 
  [[zIndex](#zIndex)][number]*optional*

  ::: section
  Z-Index of this component and its children. The higher the value, the more on top it will be rendered. Components with higher zIndex will appear in front of components with lower zIndex. If undefined or 0, the content is rendered in the default layer without portals.
  :::

  [DEFAULT: ]`600`

  ::: examples
  Examples:

  - [Z-Index and layers guide](/en-US/guide/zIndex/)
  :::
  :::::

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

- ::: 
  [[onClick](#onClick)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

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

- ::: 
  [[onMouseDown](#onMouseDown)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseDownCapture](#onMouseDownCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseEnter](#onMouseEnter)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseLeave](#onMouseLeave)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseMove](#onMouseMove)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseMoveCapture](#onMouseMoveCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseOut](#onMouseOut)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseOutCapture](#onMouseOutCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseOver](#onMouseOver)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseOverCapture](#onMouseOverCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseUp](#onMouseUp)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

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