# Source: https://recharts.github.io/en-US/api/Legend/

### Legend 

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

#### Parent Components 

Legend consumes context provided by these components:

- [`<AreaChart />`](/en-US/api/AreaChart/)
- [`<BarChart />`](/en-US/api/BarChart/)
- [`<ComposedChart />`](/en-US/api/ComposedChart/)
- [`<FunnelChart />`](/en-US/api/FunnelChart/)
- [`<LineChart />`](/en-US/api/LineChart/)
- [`<PieChart />`](/en-US/api/PieChart/)
- [`<ScatterChart />`](/en-US/api/ScatterChart/)

#### Properties 

- :::: 
  [[align](#align)][\"left\" \| \"right\" \| \"center\"]*optional*

  ::: section
  Horizontal alignment of the whole Legend container:

  - `left`: shows the Legend to the left of the chart, and chart width reduces automatically to make space for it.
  - `right` shows the Legend to the right of the chart, and chart width reduces automatically.
  - `center` shows the Legend in the middle of chart, and chart width remains unchanged.

  The exact behavior changes depending on \'verticalAlign\' prop.
  :::

  [DEFAULT: ]`"center"`
  ::::

- ::: 
  [[children](#children)][ReactNode]*optional*
  :::

- ::::: 
  [[content](#content)][ReactNode \| Function]*optional*

  ::: section
  If set to a React element, the option will be used to render the legend. If set to a function, the function is called once for each item
  :::

  ::: format
  FORMAT:

  ``` format-code
  <Legend content= />} />
  <Legend content= />
  ```
  :::
  :::::

- ::: 
  [[dangerouslySetInnerHTML](#dangerouslySetInnerHTML)][Object]*optional*
  :::

- ::::: 
  [[formatter](#formatter)][Formatter]*optional*

  ::: section
  Function to customize how content is serialized before rendering.
  :::

  ::: format
  FORMAT:

  ``` format-code
  (value, entry, index) => <span style=}></span>
  https://codesandbox.io/s/legend-formatter-rmzp9
  ```
  :::
  :::::

- :::: 
  [[height](#height)][string \| number]*optional*

  ::: section
  The height of legend.
  :::
  ::::

- :::: 
  [[iconSize](#iconSize)][number]*optional*

  ::: section
  The size of icon in each legend item.
  :::

  [DEFAULT: ]`14`
  ::::

- :::: 
  [[iconType](#iconType)][\"none\" \| \"circle\" \| \"cross\" \| \"diamond\" \| \"line\" \| \"plainline\" \| \"rect\" \| \"square\" \| \"star\" \| \"triangle\" \| \"wye\"]*optional*

  ::: section
  The type of icon in each legend item.
  :::
  ::::

- :::: 
  [[inactiveColor](#inactiveColor)][string]*optional*

  ::: section
  The color of the icon when the item is inactive.
  :::

  [DEFAULT: ]`"#ccc"`
  ::::

- :::: 
  [[itemSorter](#itemSorter)][null \| \"dataKey\" \| \"value\" \| Function]*optional*

  ::: section
  Sorts Legend items. Defaults to `value` which means it will sort alphabetically by the label.

  If `null` is provided then the payload is not sorted. Be aware that without sort, the order of items may change between renders!
  :::

  [DEFAULT: ]`"value"`
  ::::

- :::: 
  [[layout](#layout)][\"horizontal\" \| \"vertical\"]*optional*

  ::: section
  The layout of legend items inside the legend container.
  :::

  [DEFAULT: ]`"horizontal"`
  ::::

- ::: 
  [[payloadUniqBy](#payloadUniqBy)][false \| true \| UniqueFunc\<LegendPayload\>]*optional*
  :::

- :::: 
  [[portal](#portal)][null \| HTMLElement]*optional*

  ::: section
  If portal is defined, then Legend will use this element as a target for rendering using React Portal: <https://react.dev/reference/react-dom/createPortal>

  If this is undefined then Legend renders inside the recharts-wrapper element.
  :::
  ::::

- :::: 
  [[verticalAlign](#verticalAlign)][\"top\" \| \"bottom\" \| \"middle\"]*optional*

  ::: section
  The alignment of the whole Legend container:

  - `bottom`: shows the Legend below chart, and chart height reduces automatically to make space for it.
  - `top`: shows the Legend above chart, and chart height reduces automatically.
  - `middle`: shows the Legend in the middle of chart, covering other content, and chart height remains unchanged. The exact behavior changes depending on `align` prop.
  :::

  [DEFAULT: ]`"bottom"`
  ::::

- :::: 
  [[width](#width)][string \| number]*optional*

  ::: section
  The width of legend.
  :::
  ::::

- ::::: 
  [[wrapperStyle](#wrapperStyle)][React.CSSProperties]*optional*

  ::: section
  The style of legend container which is a \"position: absolute;\" div element. Because the position of legend is quite flexible, so you can change the position by the value of top, left, right, bottom in this option. And the format of wrapperStyle is the same as React inline style.
  :::

  ::: format
  FORMAT:

  ``` format-code
  
  https://reactjs.org/docs/dom-elements.html#style
  ```
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
  [[onBBoxUpdate](#onBBoxUpdate)][Function]*optional*
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
  [[onClick](#onClick)][Function]*optional*

  ::: section
  The customized event handler of click on the items in this group
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

- ::: 
  [[onMouseDown](#onMouseDown)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::: 
  [[onMouseDownCapture](#onMouseDownCapture)][AdaptChildMouseEventHandler\<P, T\>]*optional*
  :::

- ::::: 
  [[onMouseEnter](#onMouseEnter)][Function]*optional*

  ::: section
  The customized event handler of mouseenter on the items in this group
  :::

  ::: format
  FORMAT:

  ``` format-code
  https://recharts.github.io/examples/LegendEffectOpacity
  ```
  :::
  :::::

- ::::: 
  [[onMouseLeave](#onMouseLeave)][Function]*optional*

  ::: section
  The customized event handler of mouseleave on the items in this group
  :::

  ::: format
  FORMAT:

  ``` format-code
  https://recharts.github.io/examples/LegendEffectOpacity
  ```
  :::
  :::::

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