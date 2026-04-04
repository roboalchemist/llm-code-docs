# Source: https://gojs.net/intro/tools.html

Title: Tools

URL Source: https://gojs.net/intro/tools.html

Markdown Content:
[Tool](https://gojs.net/latest/api/symbols/Tool.html)s handle all of the input events. There are many kinds of predefined Tool classes that implement all of the common operations that users do.

For flexibility and simplicity, all input events are canonicalized as [InputEvent](https://gojs.net/latest/api/symbols/InputEvent.html)s and redirected by the diagram to go to the [Diagram.currentTool](https://gojs.net/latest/api/symbols/Diagram.html#currentTool). By default the Diagram.currentTool is an instance of [ToolManager](https://gojs.net/latest/api/symbols/ToolManager.html) held as the [Diagram.toolManager](https://gojs.net/latest/api/symbols/Diagram.html#toolManager). The ToolManager implements support for all mode-less tools. The ToolManager is responsible for finding another tool that is ready to run and then making it the new current tool. This causes the new tool to process all of the input events (mouse, keyboard, and touch) until the tool decides that it is finished, at which time the diagram's current tool reverts back to the [Diagram.defaultTool](https://gojs.net/latest/api/symbols/Diagram.html#defaultTool), which is normally the ToolManager, again.

Although the terminology includes the word "mouse", often that refers to both mouse events and touch events.

See samples that make use of [Tool](https://gojs.net/latest/api/symbols/Tool.html)s in the [samples index](https://gojs.net/latest/samples/index.html#tools).

Predefined Tools
----------------

Each [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) has an instance of most of the tool classes, all managed by the diagram's [ToolManager](https://gojs.net/latest/api/symbols/ToolManager.html). If you want to change the interactive behavior, in many common cases you may be able to do so by setting properties on the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html), on your [Part](https://gojs.net/latest/api/symbols/Part.html)s, or on individual [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s. But more generally you may need to modify one or more of the tools, which are accessible as properties of the [Diagram.toolManager](https://gojs.net/latest/api/symbols/Diagram.html#toolManager).

Some tools want to run when a mouse-down occurs. These tools include:

*   [ToolManager.actionTool](https://gojs.net/latest/api/symbols/ToolManager.html#actionTool), an [ActionTool](https://gojs.net/latest/api/symbols/ActionTool.html), for allowing "buttons" and other [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s to grab events from the regular tools
*   [ToolManager.relinkingTool](https://gojs.net/latest/api/symbols/ToolManager.html#relinkingTool), a [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html), for reconnecting an existing [Link](https://gojs.net/latest/api/symbols/Link.html)
*   [ToolManager.linkReshapingTool](https://gojs.net/latest/api/symbols/ToolManager.html#linkReshapingTool), a [LinkReshapingTool](https://gojs.net/latest/api/symbols/LinkReshapingTool.html), for changing the route of a [Link](https://gojs.net/latest/api/symbols/Link.html)
*   [ToolManager.resizingTool](https://gojs.net/latest/api/symbols/ToolManager.html#resizingTool), a [ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html), for changing the [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize) of a [Part](https://gojs.net/latest/api/symbols/Part.html) or an object within a [Part](https://gojs.net/latest/api/symbols/Part.html)
*   [ToolManager.rotatingTool](https://gojs.net/latest/api/symbols/ToolManager.html#rotatingTool), a [RotatingTool](https://gojs.net/latest/api/symbols/RotatingTool.html), for changing the [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle) of a [Part](https://gojs.net/latest/api/symbols/Part.html) or an object within a [Part](https://gojs.net/latest/api/symbols/Part.html)

Some tools want to run when a mouse-move occurs after a mouse-down. These tools include:

*   [ToolManager.linkingTool](https://gojs.net/latest/api/symbols/ToolManager.html#linkingTool), a [LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html), for drawing a new [Link](https://gojs.net/latest/api/symbols/Link.html)
*   [ToolManager.draggingTool](https://gojs.net/latest/api/symbols/ToolManager.html#draggingTool), a [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html), for moving or copying selected [Part](https://gojs.net/latest/api/symbols/Part.html)s
*   [ToolManager.dragSelectingTool](https://gojs.net/latest/api/symbols/ToolManager.html#dragSelectingTool), a [DragSelectingTool](https://gojs.net/latest/api/symbols/DragSelectingTool.html), for rubber-band selection of some [Part](https://gojs.net/latest/api/symbols/Part.html)s within a rectangular area
*   [ToolManager.panningTool](https://gojs.net/latest/api/symbols/ToolManager.html#panningTool), a [PanningTool](https://gojs.net/latest/api/symbols/PanningTool.html), for panning/scrolling the diagram

Some tools only want to run upon a mouse-up event after a mouse-down. These tools include:

*   [ToolManager.contextMenuTool](https://gojs.net/latest/api/symbols/ToolManager.html#contextMenuTool), a [ContextMenuTool](https://gojs.net/latest/api/symbols/ContextMenuTool.html), for showing a context menu for a [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)
*   [ToolManager.textEditingTool](https://gojs.net/latest/api/symbols/ToolManager.html#textEditingTool), a [TextEditingTool](https://gojs.net/latest/api/symbols/TextEditingTool.html), for in-place editing of [TextBlock](https://gojs.net/latest/api/symbols/TextBlock.html)s in selected [Part](https://gojs.net/latest/api/symbols/Part.html)s
*   [ToolManager.clickCreatingTool](https://gojs.net/latest/api/symbols/ToolManager.html#clickCreatingTool), a [ClickCreatingTool](https://gojs.net/latest/api/symbols/ClickCreatingTool.html), for inserting a new [Part](https://gojs.net/latest/api/symbols/Part.html) when the user clicked
*   [ToolManager.clickSelectingTool](https://gojs.net/latest/api/symbols/ToolManager.html#clickSelectingTool), a [ClickSelectingTool](https://gojs.net/latest/api/symbols/ClickSelectingTool.html), for selecting or de-selecting a [Part](https://gojs.net/latest/api/symbols/Part.html)

To change the behavior of a tool, you may be able to set properties on the tool, on the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html), on a particular [Part](https://gojs.net/latest/api/symbols/Part.html), or on a particular [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html).

*    For example, to disable the rubber-band selection tool ([DragSelectingTool](https://gojs.net/latest/api/symbols/DragSelectingTool.html)), set `diagram.toolManager.dragSelectingTool.isEnabled = false;`. 
*    You can change the appearance of a selected Part (actually its selection Adornment) by setting [Part.selectionAdornmentTemplate](https://gojs.net/latest/api/symbols/Part.html#selectionAdornmentTemplate). (See [Selection](https://gojs.net/latest/intro/selection.html) for more discussion.) 
*    You can enable users to draw new links interactively ([LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html)) by setting [GraphObject.fromLinkable](https://gojs.net/latest/api/symbols/GraphObject.html#fromLinkable) and [GraphObject.toLinkable](https://gojs.net/latest/api/symbols/GraphObject.html#toLinkable) on the port objects of your nodes. 
*    You can disable the movement of a Part ([DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html)), including Nodes and Groups, by setting [Part.movable](https://gojs.net/latest/api/symbols/Part.html#movable) to false. 
*    You can limit the movement of a Part by setting [Part.minLocation](https://gojs.net/latest/api/symbols/Part.html#minLocation) and/or [Part.maxLocation](https://gojs.net/latest/api/symbols/Part.html#maxLocation). For more general limitations, set [Part.dragComputation](https://gojs.net/latest/api/symbols/Part.html#dragComputation) to a function that computes the desired new location. 
*    You can disable resizing any part ([ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html)) by setting [Diagram.allowResize](https://gojs.net/latest/api/symbols/Diagram.html#allowResize) to false. 
*    Tooltips, implemented by the [ToolManager](https://gojs.net/latest/api/symbols/ToolManager.html), are discussed in [ToolTips](https://gojs.net/latest/intro/tooltips.html). 
*    Context menus, implemented by the [ContextMenuTool](https://gojs.net/latest/api/symbols/ContextMenuTool.html), are discussed in [Context Menus](https://gojs.net/latest/intro/contextMenus.html). 

More detail is available in the section about [Permissions](https://gojs.net/latest/intro/permissions.html).

Some commonly set properties include:

*    Enable inserting parts via double-clicking by the [ClickCreatingTool](https://gojs.net/latest/api/symbols/ClickCreatingTool.html) by setting [ClickCreatingTool.archetypeNodeData](https://gojs.net/latest/api/symbols/ClickCreatingTool.html#archetypeNodeData) to a node data object. 
*    Control what parts become selected by [DragSelectingTool](https://gojs.net/latest/api/symbols/DragSelectingTool.html) by setting [DragSelectingTool.isPartialInclusion](https://gojs.net/latest/api/symbols/DragSelectingTool.html#isPartialInclusion). 
*    Customize the link data that is copied when a new link is drawn by [LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html) by setting [LinkingTool.archetypeLinkData](https://gojs.net/latest/api/symbols/LinkingTool.html#archetypeLinkData). 
*    Limit how parts are resized by the [ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html) by setting [ResizingTool.cellSize](https://gojs.net/latest/api/symbols/ResizingTool.html#cellSize), [ResizingTool.maxSize](https://gojs.net/latest/api/symbols/ResizingTool.html#maxSize), or [ResizingTool.minSize](https://gojs.net/latest/api/symbols/ResizingTool.html#minSize). 
*    Limit how parts are rotated by the [RotatingTool](https://gojs.net/latest/api/symbols/RotatingTool.html) by setting [RotatingTool.snapAngleEpsilon](https://gojs.net/latest/api/symbols/RotatingTool.html#snapAngleEpsilon) or [RotatingTool.snapAngleMultiple](https://gojs.net/latest/api/symbols/RotatingTool.html#snapAngleMultiple). 

Remember that all of the individual tools are available via the [Diagram.toolManager](https://gojs.net/latest/api/symbols/Diagram.html#toolManager). For example, to enable the [ClickCreatingTool](https://gojs.net/latest/api/symbols/ClickCreatingTool.html):

```
myDiagram.toolManager.clickCreatingTool.archetypeNodeData =
  { key: "Node", text: "some description", color: "green" };
```

You can also set tool properties when using the constructor to define your [Diagram](https://gojs.net/latest/api/symbols/Diagram.html):

```
const diagram =
  new go.Diagram("myDiagramDiv",
    {
      allowCopy: false,
      "grid.visible": true,
      "grid.gridCellSize": new go.Size(30, 20),
      "clickCreatingTool.archetypeNodeData":  // a node data JavaScript object
        { key: "Node", text: "some description", color: "green" },
      "dragSelectingTool.box":  // an unbound Part
        new go.Part({ layerName: "Tool" })
          .add(
            new go.Shape({ name: "SHAPE", fill: null, stroke: "blue", strokeWidth: 3 })
          ),
      "draggingTool.isGridSnapEnabled": true,
      "linkReshapingTool.handleArchetype":  // a GraphObject that is copied for each handle
        new go.Shape({ width: 10, height: 10, fill: "yellow" }),
      "resizingTool.isGridSnapEnabled": true,
      "rotatingTool.snapAngleMultiple": 90,
      "rotatingTool.snapAngleEpsilon": 45
    }
  );
```

At this time the syntax for setting properties on predefined subobjects only works for the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) constructor.

The Tool Lifecycle
------------------

While each prebuilt tool in GoJS is used for a different purpose, all Tools are guaranteed to share some functions and properties. All tools share a general "lifecycle" -- that is, the order in which these common functions are called. One can think of this cycle as "starting" when the ToolManager is alerted of some input event and begins searching through the pertinent list of tools (i.e., if the mouse-down event is registered, ToolManager starts searching its [ToolManager.mouseDownTools](https://gojs.net/latest/api/symbols/ToolManager.html#mouseDownTools) list). Below is a diagram representing the general lifecycle of a tool.

For more information on how these specific functions work, see the [Tool](https://gojs.net/latest/api/symbols/Tool.html) documentation.

Tools and Adornments
--------------------

[Adornment](https://gojs.net/latest/api/symbols/Adornment.html)s are used for more than indicating that a [Part](https://gojs.net/latest/api/symbols/Part.html) is selected. Each [Tool](https://gojs.net/latest/api/symbols/Tool.html) that is in the [ToolManager.mouseDownTools](https://gojs.net/latest/api/symbols/ToolManager.html#mouseDownTools) list (in other words, any mode-less tool that is started with a mouse-down or finger-down event) gets the opportunity to add its own Adornments for its own purposes when a Part is selected.

### ResizingTool

When a [Part](https://gojs.net/latest/api/symbols/Part.html) is resizable, the [ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html) adds an [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) containing eight resize handles, four at the corners and four at the middles of the sides.

If you want to let the user resize the whole node, just set [Part.resizable](https://gojs.net/latest/api/symbols/Part.html#resizable) to true. In this case resizing will set the Node's [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize).

```
diagram.add(
  new go.Node("Auto", { resizable: true })
    .add(
      new go.Shape("RoundedRectangle", { fill: "orange" }),
      new go.TextBlock("Hello!", { margin: 5 })
    ));
diagram.commandHandler.selectAll();
```

If you want the user to resize a particular object within the node, you need to name that object and assign [Part.resizeObjectName](https://gojs.net/latest/api/symbols/Part.html#resizeObjectName). Resizing will set the [Part.resizeObject](https://gojs.net/latest/api/symbols/Part.html#resizeObject)'s [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize), in this case the Shape's desiredSize.

```
diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",  // resize the Shape, not the Node
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "orange",
          width: 50, height: 30
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

You can limit the minimum and maximum size for the resized object by setting [GraphObject.maxSize](https://gojs.net/latest/api/symbols/GraphObject.html#maxSize) and [GraphObject.minSize](https://gojs.net/latest/api/symbols/GraphObject.html#minSize). Note that these GraphObject properties are set on the [Part.resizeObject](https://gojs.net/latest/api/symbols/Part.html#resizeObject), not on the [Part](https://gojs.net/latest/api/symbols/Part.html) itself.

```
diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "orange",
          width: 50, height: 30,
          // limit size by setting or binding maxSize and/or minSize
          maxSize: new go.Size(100, 40), minSize: new go.Size(20, 20)
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

You can also cause resizing to be multiples of a given size by setting [Part.resizeCellSize](https://gojs.net/latest/api/symbols/Part.html#resizeCellSize).

```
diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",
      resizeCellSize: new go.Size(10, 10),  // new size will be multiples of resizeCellSize
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "orange",
          width: 50, height: 30,
          maxSize: new go.Size(100, 40), minSize: new go.Size(20, 20)
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

When an object is resizable, it is commonplace to try to remember the new size by updating the model data, so that it can be saved and loaded later. This can be accomplished with a TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html) on the [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize) property. But note that the binding needs to be on the actual GraphObject that is resized, not on the whole Node. In this case, because the [Part.resizeObjectName](https://gojs.net/latest/api/symbols/Part.html#resizeObjectName) is referring to a Shape, that means the binding needs to be on the Shape.

```
diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "orange",
          width: 50, height: 30
        })
        // TwoWay Binding of the desiredSize
        .bindTwoWay("desiredSize", "size", go.Size.parse, go.Size.stringify),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

You can customize all eight standard resize handles by setting [ResizingTool.archetypeHandle](https://gojs.net/latest/api/symbols/ResizingTool.html#archetypeHandle). For example, to change all of the handles to be slightly larger yellow circles:

```
diagram.toolManager.resizingTool.handleArchetype =
  new go.Shape("Circle", {
    width: 10, height: 10, fill: "yellow", cursor: "pointer"
  });

diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",
      selectionAdorned: false  // don't show selection Adornment, a rectangle
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "gray",
          width: 50, height: 30,
          maxSize: new go.Size(100, 40), minSize: new go.Size(20, 20)
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

Note that the ResizingTool will automatically set each resize handle's [GraphObject.cursor](https://gojs.net/latest/api/symbols/GraphObject.html#cursor) appropriately. Note also that because [Part.selectionAdorned](https://gojs.net/latest/api/symbols/Part.html#selectionAdorned) is false, there is no blue rectangle default selection adornment.

You can customize the resize handles by setting [Part.resizeAdornmentTemplate](https://gojs.net/latest/api/symbols/Part.html#resizeAdornmentTemplate). For example, to allow the user to only change the width of a Shape in a Node, the [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) should have only two resize handles: one at the left and one at the right. The Adornment is implemented as a Spot Panel that surrounds a [Placeholder](https://gojs.net/latest/api/symbols/Placeholder.html), representing the adorned Shape, with two rectangular blue Shapes, each representing a handle. There is also a TextBlock placed above the adorned shape showing the shape's current width.

```
diagram.add(
  new go.Node("Vertical", {
      resizable: true, resizeObjectName: "SHAPE",
      resizeAdornmentTemplate:  // specify what resize handles there are and how they look
        new go.Adornment("Spot")
          .add(
            new go.Placeholder(),  // takes size and position of adorned object
            new go.Shape("Circle", { // left resize handle
                alignment: go.Spot.Left, cursor: "col-resize",
                desiredSize: new go.Size(9, 9),
                fill: "lightblue", stroke: "dodgerblue"
              }),
            new go.Shape("Circle", {  // right resize handle
                alignment: go.Spot.Right, cursor: "col-resize",
                desiredSize: new go.Size(9, 9),
                fill: "lightblue", stroke: "dodgerblue"
              }),
            new go.TextBlock({ // show the width as text
                alignment: go.Spot.Top, alignmentFocus: new go.Spot(0.5, 1, 0, -2),
                stroke: "dodgerblue"
              })
              .bindObject("text", "adornedObject",
                          shp => shp.naturalBounds.width.toFixed(0))
          ),
      selectionAdorned: false  // don't show selection Adornment, a rectangle
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE",
          fill: "orange",
          width: 50, height: 30,
          maxSize: new go.Size(200, 40), minSize: new go.Size(20, 20)
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

There are examples custom resizing tools defined in the samples and extensions directories: [Resize Multiple Tool](https://gojs.net/latest/samples/ResizeMultiple.html), [Lane Resizing Tool (in Swim Lanes)](https://gojs.net/latest/samples/swimLanes.html), and [Lane Resizing Tool (in Swim Lanes Vertical)](https://gojs.net/latest/samples/swimLanesVertical.html).

### RotatingTool

When a [Part](https://gojs.net/latest/api/symbols/Part.html) is rotatable, the [RotatingTool](https://gojs.net/latest/api/symbols/RotatingTool.html) adds an [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) containing one rotate handle a short distance from the object at the object's angle. Since the default [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle) is zero, the rotate handle typically starts to the right of the object.

If you want to let the user rotate the whole node, just set [Part.rotatable](https://gojs.net/latest/api/symbols/Part.html#rotatable) to true. Rotating will set the Node's [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle).

```
diagram.add(
  new go.Node("Auto", { rotatable: true, locationSpot: go.Spot.Center })
    .add(
      new go.Shape("RoundedRectangle", { fill: "orange" }),
      new go.TextBlock("Hello!", { margin: 5 })
    ));
diagram.commandHandler.selectAll();
```

If you want the user to rotate a particular object within the node, you need to name that object and assign [Part.rotateObjectName](https://gojs.net/latest/api/symbols/Part.html#rotateObjectName). Rotating will set the [Part.rotateObject](https://gojs.net/latest/api/symbols/Part.html#rotateObject)'s [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle), in this case the Shape's angle.

```
diagram.add(
  new go.Node("Vertical", {
      rotatable: true, rotateObjectName: "SHAPE",  // rotate the Shape, not the Node
      locationSpot: go.Spot.Center, locationObjectName: "SHAPE",
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE", fill: "orange",
          width: 50, height: 30
        }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

When an object is rotatable, it is commonplace to try to remember the new angle by updating the model data, so that it can be saved and loaded later. This can be accomplished with a TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html) on the [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle) property. But note that the binding needs to be on the actual GraphObject that is rotated, not on the whole Node. In this case, because the [Part.rotateObjectName](https://gojs.net/latest/api/symbols/Part.html#rotateObjectName) is referring to a Shape, that means the binding needs to be on the Shape.

```
diagram.add(
  new go.Node("Vertical", {
      rotatable: true, rotateObjectName: "SHAPE",
      locationSpot: go.Spot.Center, locationObjectName: "SHAPE",
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
          name: "SHAPE", fill: "orange",
          width: 50, height: 30
        })
        .bindTwoWay("angle"),  // TwoWay Binding of angle
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

Another common customization is to position the rotate handle above the object when it is not rotated, i.e. when its [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle) is zero. This is accomplished by setting [RotatingTool.handleAngle](https://gojs.net/latest/api/symbols/RotatingTool.html#handleAngle) to 270.

```
diagram.add(
  new go.Node("Auto", { rotatable: true, locationSpot: go.Spot.Center })
    .bindTwoWay("angle")  // TwoWay Binding of Node.angle
    .add(
      new go.Shape("RoundedRectangle", { fill: "orange" }),
      new go.TextBlock("Hello!", { margin: 5 })
    ));
diagram.toolManager.rotatingTool.handleAngle = 270;
diagram.commandHandler.selectAll();
```

You can customize the rotate handle by setting [Part.rotateAdornmentTemplate](https://gojs.net/latest/api/symbols/Part.html#rotateAdornmentTemplate).

```
diagram.add(
  new go.Node("Vertical", {
      rotatable: true, rotateObjectName: "SHAPE",
      locationSpot: go.Spot.Center, locationObjectName: "SHAPE",
      rotateAdornmentTemplate:  // specify appearance of rotation handle
        new go.Adornment({ locationSpot: go.Spot.Center })
          .add(
            new go.Shape("BpmnActivityLoop", {
                width: 12, height: 12, cursor: "pointer",
                background: "transparent", stroke: "dodgerblue", strokeWidth: 2
              })
          ),
      selectionObjectName: "SHAPE"
    })
    .add(
      new go.Shape("RoundedRectangle", {
        name: "SHAPE", fill: "orange",
        width: 50, height: 30
      }),
      new go.TextBlock("Hello!", { margin: 3 })
    ));
diagram.commandHandler.selectAll();
```

There are example custom rotating tools defined in the samples and extensions directories: [Rotate Multiple Tool](https://gojs.net/latest/samples/RotateMultiple.html) and [Horizontal Text Rotating Tool (in Seating Chart)](https://gojs.net/latest/samples/seatingChart.html).

### RelinkingTool

When a [Link](https://gojs.net/latest/api/symbols/Link.html) is [Link.relinkableFrom](https://gojs.net/latest/api/symbols/Link.html#relinkableFrom) and/or [Link.relinkableTo](https://gojs.net/latest/api/symbols/Link.html#relinkableTo), the [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html) adds one or two [Adornment](https://gojs.net/latest/api/symbols/Adornment.html)s, a diamond at each relinkable end of a selected link. The user can drag a relinking handle to reconnect that end of the link to another port.

The [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html) will automatically update the relationships between the nodes/ports, both in the diagram and in the model. No [Binding](https://gojs.net/latest/api/symbols/Binding.html)s are needed for such model updates.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("Rectangle", {
          fill: "lightgray",
          portId: "", fromLinkable: true, toLinkable: true
        }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.linkTemplate =
  new go.Link({ relinkableFrom: true, relinkableTo: true })
    .add(
      new go.Shape(),
      new go.Shape({ toArrow: "Standard" })
    );

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta" },
  { key: 3, text: "Gamma" },
  { key: 4, text: "Delta" }
];
const linkDataArray = [
  { from: 1, to: 4 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);

diagram.select(diagram.findLinkForData(linkDataArray[0]));
```

The relinking handles can be customized by setting [RelinkingTool.fromHandleArchetype](https://gojs.net/latest/api/symbols/RelinkingTool.html#fromHandleArchetype) and [RelinkingTool.toHandleArchetype](https://gojs.net/latest/api/symbols/RelinkingTool.html#toHandleArchetype). At the current time they cannot be customized by setting a property on the Link.

You can limit which pairs of ports between which the user may draw new links or reconnect existing links. This topic is covered by [Link Validation](https://gojs.net/latest/intro/validation.html).

### LinkReshapingTool

When a [Link](https://gojs.net/latest/api/symbols/Link.html) is [Part.reshapable](https://gojs.net/latest/api/symbols/Part.html#reshapable), the [LinkReshapingTool](https://gojs.net/latest/api/symbols/LinkReshapingTool.html) adds an [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) with several reshape handles at the interior points of a selected link's route. When the user drags a reshape handle, the route of the Link, held by [Link.points](https://gojs.net/latest/api/symbols/Link.html#points), is modified.

When a link is reshapable, it is commonplace to try to remember the new route by updating the link data in the [GraphLinksModel](https://gojs.net/latest/api/symbols/GraphLinksModel.html), so that it can be saved and loaded later. This can be accomplished with a TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html) on the [Link.points](https://gojs.net/latest/api/symbols/Link.html#points) property. If one also uses the property name "points" on the link data, [Model.toJson](https://gojs.net/latest/api/symbols/Model.html#toJson) will automatically convert the [List](https://gojs.net/latest/api/symbols/List.html) of [Point](https://gojs.net/latest/api/symbols/Point.html)s into an Array of numbers and vice-versa.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc", go.Point.parse)
    .add(
      new go.Shape("Rectangle", { fill: "lightgray" }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.linkTemplate =
  new go.Link({ reshapable: true, routing: go.Routing.Orthogonal })
    .bindTwoWay("points")  // TwoWay Binding of Link.points
    .add(
      new go.Shape(),
      new go.Shape({ toArrow: "Standard" })
    );

diagram.model = new go.GraphLinksModel([
  { key: 1, text: "Alpha", loc: "0 0" },
  { key: 2, text: "Beta", loc: "200 50" }
], [
  { from: 1, to: 2 }
]);

diagram.select(diagram.findLinkForData(diagram.model.linkDataArray[0]));
```

The reshape handles are small blue squares. The reshape handles can be customized by setting [LinkReshapingTool.handleArchetype](https://gojs.net/latest/api/symbols/LinkReshapingTool.html#handleArchetype). At the current time they cannot be customized by setting a property on the Link.

By setting [Link.resegmentable](https://gojs.net/latest/api/symbols/Link.html#resegmentable) to true, users can add or remove segments from links. The resegmenting handles are even smaller blue diamonds at the middle of each segment. When the user drags a resegmenting handle, a new segment is inserted into the link's route. For orthogonal links, two new segments are introduced in order to maintain orthogonality. When the user reshapes the link so that adjacent segments are co-linear (or nearly so), the segment(s) are removed from the route.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc", go.Point.parse)
    .add(
      new go.Shape("Rectangle", { fill: "lightgray" }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.linkTemplate =
  new go.Link({
      reshapable: true, resegmentable: true,
      routing: go.Routing.Orthogonal
    })
    .bindTwoWay("points")  // TwoWay Binding of Link.points
    .add(
      new go.Shape(),
      new go.Shape({ toArrow: "Standard" })
    );

diagram.model = new go.GraphLinksModel([
  { key: 1, text: "Alpha", loc: "0 0" },
  { key: 2, text: "Beta", loc: "200 50" }
], [
  { from: 1, to: 2 }
]);

diagram.select(diagram.findLinkForData(diagram.model.linkDataArray[0]));
```

The resegmenting handles can be customized by setting [LinkReshapingTool.midHandleArchetype](https://gojs.net/latest/api/symbols/LinkReshapingTool.html#midHandleArchetype). At the current time they cannot be customized by setting a property on the Link. Also at the current time resegmenting is not supported on Bezier-curved links.

If you want your users to be able to reshape Shape geometries that are not Link paths, there is the [Geometry Reshaping Tool](https://gojs.net/latest/extensions/GeometryReshapingTool.js) used by the [Polygon Drawing](https://gojs.net/latest/samples/PolygonDrawing.html) and [Freehand Drawing](https://gojs.net/latest/samples/FreehandDrawing.html) samples in the extensions directory. It is defined in a separate JS file that you can load into your app.

Tools and Tool Parts
--------------------

Some tools make use of special [Part](https://gojs.net/latest/api/symbols/Part.html)s that they add to the "Tool" [Layer](https://gojs.net/latest/api/symbols/Layer.html) as feedback during the tool's operation.

### DragSelectingTool

The [DragSelectingTool](https://gojs.net/latest/api/symbols/DragSelectingTool.html) uses the [DragSelectingTool.box](https://gojs.net/latest/api/symbols/DragSelectingTool.html#box) to show the area in which it will select Parts. Normally this is a simple magenta rectangular shape, which you can customize. For example here is a drag-selecting box that is in the shape of a blue-outlined cloud.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc", go.Point.parse)
    .add(
      new go.Shape("Rectangle", { fill: "lightgray" }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.toolManager.dragSelectingTool.isPartialInclusion = true;
diagram.toolManager.dragSelectingTool.box =
  new go.Part({ layerName: "Tool" })
    .add(
      new go.Shape("Cloud", {
          name: "SHAPE",
          fill: null, stroke: "dodgerblue", strokeWidth: 2
        })
    );

diagram.model = new go.GraphLinksModel([
  { key: 1, text: "Alpha", loc: "0 0" },
  { key: 2, text: "Beta", loc: "200 50" }
], [
  { from: 1, to: 2 }
]);
```

Note that the [DragSelectingTool](https://gojs.net/latest/api/symbols/DragSelectingTool.html) expects that the object in the "box" to be resized is named "SHAPE". The object should be rectangular too, or else the user might be misled by the area in which parts will be selected. Finally note also that the box is not an Adornment because it does not "adorn" any Part. It is just an unbound Part that is used temporarily by the DragSelectingTool.

There are examples of in-the-background-dragging tools defined in the extensions directory: [Realtime Drag Selecting Tool](https://gojs.net/latest/samples/RealtimeDragSelecting.html), [Drag Creating Tool](https://gojs.net/latest/samples/DragCreating.html), and [Drag Zooming Tool](https://gojs.net/latest/samples/DragZooming.html). Each is defined in a separate JS file that you can load into your app.

### LinkingTool and RelinkingTool

The linking tools, [LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html) and [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html), inherit from a base class, [LinkingBaseTool](https://gojs.net/latest/api/symbols/LinkingBaseTool.html), that uses several Parts: a temporary Link and temporary "to" and "from" Nodes.

To customize the appearance and behavior of the temporary Link that is shown during a linking operation, you need to modify or replace the [LinkingBaseTool.temporaryLink](https://gojs.net/latest/api/symbols/LinkingBaseTool.html#temporaryLink). The default temporary link is a blue line with a standard arrowhead. The originating port and the potential target port are shown by the [LinkingBaseTool.temporaryFromNode](https://gojs.net/latest/api/symbols/LinkingBaseTool.html#temporaryFromNode) and [LinkingBaseTool.temporaryToNode](https://gojs.net/latest/api/symbols/LinkingBaseTool.html#temporaryToNode). The default temporary ports are magenta rectangles.

```
diagram.nodeTemplate =
  new go.Node("Spot")
    .bind("location", "loc", go.Point.parse)
    .add(
      new go.Shape("RoundedRectangle", {
          width: 100, height: 40, fill: "lightyellow",
          portId: "", fromLinkable: true, toLinkable: true, cursor: "pointer"
        }),
      new go.TextBlock()
        .bind("text")
    );

diagram.toolManager.linkingTool.temporaryLink =
  new go.Link({ layerName: "Tool" })
    .add(
      new go.Shape({ stroke: "red", strokeWidth: 2, strokeDashArray: [4, 2] })
    );

const tempfromnode =
  new go.Node({ layerName: "Tool" })
    .add(
      new go.Shape("RoundedRectangle", {
          stroke: "chartreuse", strokeWidth: 3, fill: null,
          portId: "", width: 1, height: 1
        })
    );
diagram.toolManager.linkingTool.temporaryFromNode = tempfromnode;
diagram.toolManager.linkingTool.temporaryFromPort = tempfromnode.port;

const temptonode =
  new go.Node({ layerName: "Tool" })
    .add(
      new go.Shape("RoundedRectangle", {
          stroke: "cyan", strokeWidth: 3, fill: null,
          portId: "", width: 1, height: 1
        })
    );
diagram.toolManager.linkingTool.temporaryToNode = temptonode;
diagram.toolManager.linkingTool.temporaryToPort = temptonode.port;

diagram.model = new go.GraphLinksModel([
  { text: "Alpha", loc: "0 0" },
  { text: "Beta", loc: "200 50" },
  { text: "Gamma", loc: "400 0" }
]);  // start off with no links
```

Try drawing a link from one node to the other. You will notice that the nodes (actually the ports) are highlighted by the temporary nodes in chartreuse and cyan. The temporary link is a dashed red line without an arrowhead.

If your app also supports relinking you will probably want to do the same customizations on the [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html).

There are examples of linking tools defined in the samples and extensions directories: [Polyline Linking Tool](https://gojs.net/latest/samples/PolylineLinking.html), [Messaging Tool (in Sequence Diagram)](https://gojs.net/latest/samples/sequenceDiagram.html), and [Custom Linking Tool (in Grafcet Diagram)](https://gojs.net/latest/samples/sequenceDiagram.html)

Custom Tools
------------

The GoJS samples and extensions demonstrate a number of custom tools, including:

*   [Column Resizing Tool and Row Resizing Tool](https://gojs.net/latest/samples/ColumnResizing.html)
*   [Curved Link Reshaping Tool](https://gojs.net/latest/samples/CurvedLinkReshaping.html)
*   [Drag Creating Tool](https://gojs.net/latest/samples/DragCreating.html)
*   [Drag Zooming Tool](https://gojs.net/latest/samples/DragZooming.html)
*   [Freehand Drawing Tool](https://gojs.net/latest/samples/FreehandDrawing.html)
*   [Geometry Reshaping Tool](https://gojs.net/latest/samples/GeometryReshaping.html) also used by the [Polygon Drawing](https://gojs.net/latest/samples/PolygonDrawing.html), and the [Freehand Drawing](https://gojs.net/latest/samples/FreehandDrawing.html) samples 
*   [Guided Dragging Tool](https://gojs.net/latest/samples/GuidedDragging.html)
*   [Lasso Selecting Tool](https://gojs.net/latest/samples/LassoSelecting.html)
*   [Link Label Dragging Tool](https://gojs.net/latest/samples/LinkLabelDragging.html)
*   [Link Label On Path Dragging Tool](https://gojs.net/latest/samples/LinkLabelOnPathDragging.html)
*   [Link Shifting Tool](https://gojs.net/latest/samples/LinkShifting.html)
*   [Node Label Dragging Tool](https://gojs.net/latest/samples/NodeLabelDragging.html)
*   [Non-Realtime Dragging Tool](https://gojs.net/latest/samples/NonRealtimeDragging.html)
*   [Orthogonal Link Reshaping Tool](https://gojs.net/latest/samples/OrthogonalLinkReshaping.html)
*   [Overview Resizing Tool](https://gojs.net/latest/samples/OverviewResizing.html)
*   [Polygon Drawing Tool](https://gojs.net/latest/samples/PolygonDrawing.html)
*   [Polyline Linking Tool](https://gojs.net/latest/samples/PolylineLinking.html)
*   [Port Shifting Tool](https://gojs.net/latest/samples/PortShifting.html)
*   [Realtime Drag Selecting Tool](https://gojs.net/latest/samples/RealtimeDragSelecting.html)
*   [Rescaling Tool](https://gojs.net/latest/samples/Rescaling.html)
*   [Resize Multiple Tool](https://gojs.net/latest/samples/ResizeMultiple.html)
*   [Rotate Multiple Tool](https://gojs.net/latest/samples/RotateMultiple.html)
*   [Sector Reshaping Tool](https://gojs.net/latest/samples/SectorReshaping.html)
*   [Snap Link Reshaping Tool](https://gojs.net/latest/samples/SnapLinkReshaping.html)
*   [Spot Rotating Tool](https://gojs.net/latest/samples/SpotRotating.html)
*   [Field Dragging Tool](https://gojs.net/latest/samples/dragDropFields.html)
*   [Lane Resizing Tool (in Swim Lanes)](https://gojs.net/latest/samples/swimLanes.html)
*   [Lane Resizing Tool (in Swim Lanes Vertical)](https://gojs.net/latest/samples/swimLanesVertical.html)
