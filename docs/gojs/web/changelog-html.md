# Source: https://gojs.net/changelog.html

Title: Change Log

URL Source: https://gojs.net/changelog.html

Markdown Content:
GoJS Change Log
---------------

We maintain a [GitHub Repository](https://github.com/NorthwoodsSoftware/GoJS) that you can star to follow version updates.

GoJS 3.1
--------

GoJS 3.1 brings a number of new features, including the ability to manipulate any diagram using [only the keyboard](https://gojs.net/latest/intro/accessibility.html), and support for screen readers.

The complete list of new features is [detailed below](https://gojs.net/changelog.html#3.1).

### Changes for 3.1.7

*    Fixed the rendering of [Diagram.grid](https://gojs.net/changelog.html) when dynamically updating grid properties. 
*    Fixed the copying of attached properties when changing the category of a [Part](https://gojs.net/changelog.html). 

### Changes for 3.1.6

*    Fixed [CommandHandler.copiesParentKey](https://gojs.net/changelog.html) when copying subchildren in a [TreeModel](https://gojs.net/changelog.html). 
*    Fixed modifying only the [Shape.interval](https://gojs.net/changelog.html) property of a Shape in a "Grid" Panel to redraw the grid. 

### Changes for 3.1.5

*   Fixed undo of setting [Link.curve](https://gojs.net/changelog.html) to or from Bezier curve.
*    Fixed object picking within the Diagram viewport when the viewport has been updated but not yet redrawn (for example in a "ViewportBoundsChanged" [DiagramEvent](https://gojs.net/changelog.html) listener). 
*    Fixed [LinkReshapingTool](https://gojs.net/changelog.html) not to allow resegmenting when the [Link.curve](https://gojs.net/changelog.html) is Bezier unless [Link.isOrthogonal](https://gojs.net/changelog.html) is true. 
*   Fixed [Picture.sourceRect](https://gojs.net/changelog.html) setter not updating the Picture measurements.

### Changes for 3.1.4

*    Fixed [Diagram.moveParts](https://gojs.net/changelog.html) not to allow [Link.invalidateRoute](https://gojs.net/changelog.html) to recompute routes of Links whose Nodes are shifted by different distances when [Link.adjusting](https://gojs.net/changelog.html) is not None. 
*    Fixed [LinkReshapingTool](https://gojs.net/changelog.html) when handling multiple points in an orthogonal line. Also changed the z-ordering of reshape handles so that the end/outer handles are behind middle/inner handles, so that the ultimate handle is not in front of the penultimate handle. 
*    Fixed [Panel.findObject](https://gojs.net/changelog.html) so that it is no longer affected by whether there is an [Panel.itemTemplate](https://gojs.net/changelog.html) or template map. 
*    Fixed an inconsistency when querying the bounds of invisible [GraphObject](https://gojs.net/changelog.html)s (eg [GraphObject.getDocumentBounds](https://gojs.net/changelog.html)). 

### Changes for 3.1.3

*   Improved performance of JumpOver or JumpGap links.
*    Fixed some cases of invalid AvoidsNodes routing after removing Nodes or changing their visibility. 
*   Improved [Picture.source](https://gojs.net/changelog.html) caching.

### Changes for 3.1.2

*    Improved [LayeredDigraphLayout](https://gojs.net/changelog.html) routing of Bezier curve Links near their Nodes. 
*    Fixed SVG rendering of RowColumnDefinition backgrounds in Panels that themselves have backgrounds. 

### Changes for 3.1.1

*    Fixed [LinkReshapingTool](https://gojs.net/changelog.html) not to insert points into orthogonal routes unnecessarily. However, the behavior of that tool has changed to no longer try to repair routes that are not orthogonal to begin with. 
*   Fixed some cases of undo of link routes with ...Side Spots.
*    Improvements for use in mock-DOM environments like `jsdom` with `canvas`

New Features and Changes for GoJS 3.1
-------------------------------------

### Keyboard Controlled Focus Navigation and Virtual Pointer

The [CommandHandler](https://gojs.net/changelog.html) now supports keyboard-controlled focus navigation and a virtual pointer, so that the user need not use a mouse. Enable it in any Diagram with the `Ctrl-Alt-Enter` command.

This new functionality includes built-in minimal support for screen readers. However, each application will need to customize what is read in each situation. The [AriaCommandHandler](https://gojs.net/changelog.html) extension is now deprecated.

Read a summary at [Focus and Keyboard Control](https://gojs.net/latest/learn/interactivity.html#FocusKeyboardControlTools). Read more details at [Accessibility](https://gojs.net/latest/intro/accessibility.html).

### Using CSS variables for theming

The [ThemeManager](https://gojs.net/changelog.html) can now read CSS variables such that your GoJS templates can reuse variables from other parts of your UI. This functionality is controlled by the new [ThemeManager.readsCssVariables](https://gojs.net/changelog.html) property, which defaults to true. Read more at [Using CSS variables for theming](https://gojs.net/latest/intro/theming.html#ThemeCSS).

### Link routing improvements

Link routing is improved for links connecting member Nodes with their containing Groups, and for `...Side` Spot links that do not cross adjacent links.

Link routing for AvoidsNodes has also been improved when links are fully within Groups.

### Licensing improvements

3.1 comes with a new licensing mechanism for unlimited domains. If you have trouble upgrading, please contact support.

### The **LassoSelectingTool** extension

The [LassoSelectingTool](https://gojs.net/changelog.html) is an optional replacement for the standard [DragSelectingTool](https://gojs.net/changelog.html) that allows the user to freehand draw a line around the Parts that they want to select. Try it in the [Lasso Selecting](https://gojs.net/latest/samples/LassoSelecting.html) sample.

### Other New Features

*    "Toggle" switches are a new kind of predefined button which is commonly requested for the more complex node templates. See the [Toggle switches](https://gojs.net/latest/samples/Toggles.html) sample. 
*    The "AutoRepeatButton" has been moved from the "ScrollingTable" extension to be a built-in builder, as another type of predefined button. This makes it easier for you to use auto-repeating buttons in your diagrams. 
*    The [GuidedDraggingTool](https://gojs.net/changelog.html) extension has been improved to support centering a Part to have equal space on both sides. Try the tool in the [Guided Dragging](https://gojs.net/latest/samples/GuidedDragging.html) sample. 
*    The [CommandHandler.zoomToFit](https://gojs.net/changelog.html) command now takes an optional argument so that you can easily perform an animated zoom to a particular Rect in document coordinates. 
*    The new [CommandHandler.storageLocation](https://gojs.net/changelog.html) property may be set to "localStorage" or "sessionStorage" in order to save the clipboard state in a **Storage** object. For compatibility the value defaults to "memory". This subsumes the implementation in the [LocalStorageCommandHandler](https://gojs.net/changelog.html) extension, which remains for compatibility in versions of GoJS older than 3.1, but is now deprecated. 
*    The new [CommandHandler.downloadSvg](https://gojs.net/changelog.html) command makes it easy for your app to download an image of your diagram as SVG. For example, see the [Genogram](https://gojs.net/latest/samples/genogram.html) sample. 
*    The [DrawCommandHandler](https://gojs.net/changelog.html) extension has been extended with the [DrawCommandHandler.saveLocalFile](https://gojs.net/changelog.html) and [DrawCommandHandler.loadLocalFile](https://gojs.net/changelog.html) methods. This supports downloading a JSON-formatted text file produced by [Model.toJson](https://gojs.net/changelog.html), and loading such a file via either a [DrawCommandHandler.localFileInput](https://gojs.net/changelog.html)<input> element or a [DrawCommandHandler.localFileDropElement](https://gojs.net/changelog.html) drop-handling element. Try it in the [Local Files](https://gojs.net/latest/samples/saveAndLoadLocalFiles.html) sample. 
*   [SvgRendererOptions](https://gojs.net/changelog.html) now has the "svgFinished" option to allow modifying the whole <svg> element after it has been rendered by [Diagram.makeSvg](https://gojs.net/changelog.html). This is useful if you need to modify the SVG each time it is produced. 
*   [TextBlock.letterSpacing](https://gojs.net/changelog.html) and [TextBlock.wordSpacing](https://gojs.net/changelog.html) are new properties that affect the measurement and rendering of text. Caution: these properties are not supported on all platforms. 
*    New Node methods [Node.findSuccessorParts](https://gojs.net/changelog.html) and [Node.findPredecessorParts](https://gojs.net/changelog.html) walk the graph starting at a Node, collecting all of the Links and Nodes it sees, but not including the original Node itself. Basically [Node.findSuccessorParts](https://gojs.net/changelog.html) returns a [Set](https://gojs.net/changelog.html) of all Nodes and Links that are "downstream" from this Node or are "descendants" of this Node. [Node.findPredecessorParts](https://gojs.net/changelog.html) does the same, but walking backwards "upstream" or to "ancestors" of the Node. 
*   [Link.corner](https://gojs.net/changelog.html) is now supported for non-orthogonal link segments, so link path turns can look softer without using Bezier [Link.curve](https://gojs.net/changelog.html). For example, see the [Double Tree](https://gojs.net/latest/samples/doubleTree.html) sample, to which we added the setting `corner: 10`. 
*    The [LayeredDigraphLayout.centered](https://gojs.net/changelog.html) and [LayeredDigraphVertex.centered](https://gojs.net/changelog.html) properties control whether the nodes in each layer are aligned to the center (the default) or to the closer side (typically top or left side) of the layer. 
*    The [Router.isRoutable](https://gojs.net/changelog.html) method is an overridable predicate to help decide if a particular [Link](https://gojs.net/changelog.html) needs to be routed. 
*    One can now pass arguments to be passed to [GraphObject.apply](https://gojs.net/changelog.html) functions, to parameterize a call to an initialization function applied to GraphObjects. For examples, search the samples for calls to [GraphObject.apply](https://gojs.net/changelog.html) that have two (or more) arguments. Note how those applied functions also take two (or more) arguments. 
*    The [Rect.nearestSideDirection](https://gojs.net/changelog.html) and [Rect.nearestSideDirectionPoint](https://gojs.net/changelog.html) decide which side of a Rect is closest to the given point. 
*    The [Geometry](https://gojs.net/changelog.html) constructor now takes an optional second argument that is used as an initialization object. 
*    The "ToolTip" Adornment now detects [GraphObject.mouseOver](https://gojs.net/changelog.html) events and automatically extends how long the tooltip will stay visible by [ToolManager.toolTipDuration](https://gojs.net/changelog.html) milliseconds. 
*    If the [ToolManager.currentToolTip](https://gojs.net/changelog.html) is visible, the Escape key will hide it. Hit Escape again to clear the [Diagram.selection](https://gojs.net/changelog.html) and stop any ongoing tool. 
*    The [ContextMenuTool](https://gojs.net/changelog.html) now handles mouse wheel events in the standard fashion when that tool is running, including zooming the diagram scale. 
*    The [ResizingTool](https://gojs.net/changelog.html) can now resize the labels of Links, and the [RotatingTool](https://gojs.net/changelog.html) can now rotate the labels of Links, although they continue not to be able to resize or rotate whole Links or their Link paths. 
*    Animation performance has improved when starting and stopping multiple animations. 
*    An example Playwright test file is now in the Introduction page about [Testing](https://gojs.net/latest/intro/testing.html). 
*    We have added a [Venn Diagram](https://gojs.net/latest/samples/venn.html) sample. 
*    Minor API incompatibility: [ThemeBinding.themeSource](https://gojs.net/changelog.html) no longer accepts null as a value -- use the empty string instead. 

### Bug fix changes in 3.1 since 3.0

*    Bindings with [Item Templates](https://gojs.net/latest/intro/itemArrays.html) that use a named data source will not update unless explicitly updated via [Model.set](https://gojs.net/changelog.html) or equivalent. Binding updates on the containing Part will no longer indiscriminately update Item Template bindings. 
*    Links between a Group and members of that Group are now routed more consistently to stay within the group if the group's port completely contains the member node's port. Routes tend to be shorter than they used to be. 
*    Elements of Table Panels that stretch and also span multiple rows or columns no longer consider empty rows/columns to have infinite available space, and will not expand into them. Instead, those empty rows/columns will be considered of minimum size for measuring spanning elements, normally zero. This may make some Table elements smaller than they have been in previous versions, which will fix some designs where they were measured bigger than one would expect, causing other rows/columns to be clipped unnecessarily. 
*    Replacing the [Diagram.model](https://gojs.net/changelog.html) will first clear the [Diagram.selection](https://gojs.net/changelog.html) and the [Diagram.highlighteds](https://gojs.net/changelog.html) collections, allowing for any side effects to be performed to clean up from the old diagram. 
*    Fixed SVG rendering of panels with a background where one or more elements are invisible within the panel. It was possible this would draw the background in front of the remaining elements. 
*   Fixed [Placeholder](https://gojs.net/changelog.html)s incorrectly computing size during some animations.
*    Fixed [LayeredDigraphLayout](https://gojs.net/changelog.html) routing of Bezier curve Links when the link spots are `Spot.Center` or offset from there. 

* * *

### Old Change Logs

#### [Change log for 3.0](https://gojs.net/3.0.28/changelog.html)

#### [Change log for 2.3](https://gojs.net/2.3.19/changelog.html)

#### [Change log for 2.2](https://gojs.net/2.2.23/changelog.html) (unsupported)

#### [Change log for 2.1](https://gojs.net/2.1.56/changelog.html) (unsupported)

#### [Change log for 2.0](https://gojs.net/2.0.21/changelog.html) (unsupported)

#### [Change log for 1.*](https://gojs.net/1.8.38/changelog.html) (unsupported)
