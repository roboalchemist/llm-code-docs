# Source: https://gojs.net/intro/events.html

Title: Events

URL Source: https://gojs.net/intro/events.html

Markdown Content:
There are three basic kinds of events that **GoJS** deals with: [DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html)s, [InputEvent](https://gojs.net/latest/api/symbols/InputEvent.html)s, and [ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html)s. This page discusses the first two; see [Changed Events](https://gojs.net/latest/intro/changedEvents.html) for the last kind of event.

Diagram Events
--------------

[DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html)s represent general user-initiated changes to a diagram. You can register one or more diagram event handlers by calling [Diagram.addDiagramListener](https://gojs.net/latest/api/symbols/Diagram.html#addDiagramListener). You can also register a diagram event handler in [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) initialization options when calling the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) constructor. Each kind of diagram event is distinguished by its name.

Currently defined diagram event names include:

*    "**InitialAnimationStarting**", the initial default animation is about to start; do not modify the diagram or its model in the event listener. This can be useful for modifying the [AnimationManager.defaultAnimation](https://gojs.net/latest/api/symbols/AnimationManager.html#defaultAnimation) to make a custom initial animation. See [AnimationManager.initialAnimationStyle](https://gojs.net/latest/api/symbols/AnimationManager.html#initialAnimationStyle) for details. 
*    "**AnimationStarting**", a default animation ([AnimationManager.defaultAnimation](https://gojs.net/latest/api/symbols/AnimationManager.html#defaultAnimation)) is about to start; do not modify the diagram or its model in the event listener. 
*    "**AnimationFinished**", a default animation ([AnimationManager.defaultAnimation](https://gojs.net/latest/api/symbols/AnimationManager.html#defaultAnimation)) just completed; do not modify the diagram or its model in the event listener. 
*    "**BackgroundSingleClicked**", when a mouse left-button single-click happened in the background of the Diagram, not on a Part; if you make any changes, start and commit your own transaction. 
*    "**BackgroundDoubleClicked**", when a mouse left-button double-click happened in the background of the Diagram, not on a Part; if you make any changes, start and commit your own transaction. 
*    "**BackgroundContextClicked**", when a mouse right-button single-click happened in the background of the Diagram, not on a Part; if you make any changes, start and commit your own transaction. 
*    "**ChangingSelection**", an operation is about to change the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection) collection, which is also the value of the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject); do not make any changes to the selection or the diagram or the model in the event listener; note that just setting [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) will not raise this event, but tools and commands will. 
*    "**ChangedSelection**", an operation has just changed the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection) collection, which is also the value of the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject); do not make any changes to the selection or the diagram or the model in the event listener; note that just setting [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) will not raise this event, but tools and commands will. 
*    "**ClipboardChanged**", Parts have been copied to the clipboard by [CommandHandler.copySelection](https://gojs.net/latest/api/symbols/CommandHandler.html#copySelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Parts; if you make any changes, start and commit your own transaction. 
*    "**ClipboardPasted**", Parts have been copied from the clipboard into the Diagram by [CommandHandler.pasteSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#pasteSelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection), and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**DocumentBoundsChanged**", the area of the diagram's Parts, [Diagram.documentBounds](https://gojs.net/latest/api/symbols/Diagram.html#documentBounds), has changed; the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the old Rect. 
*    "**ExternalObjectsDropped**", Parts have been copied into the Diagram by drag-and-drop from outside of the Diagram; the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the set of Parts that were dropped (which is also the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection)), the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the source Diagram, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**GainedFocus**", the diagram has gained keyboard focus, such as after a call to [Diagram.focus](https://gojs.net/latest/api/symbols/Diagram.html#focus). 
*    "**InitialLayoutCompleted**", the whole diagram layout has updated for the first time since a major change to the Diagram, such as replacing the Model; if you make any changes, you do not need to start and commit your own transaction. 
*    "**LayoutCompleted**", the whole diagram layout has just been updated; if you make any changes, you do not need to start and commit your own transaction. 
*    "**LinkDrawn**", the user has just created a new Link using [LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the new Link, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**LinkRelinked**", the user has just reconnected an existing Link using [RelinkingTool](https://gojs.net/latest/api/symbols/RelinkingTool.html) or [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the modified Link, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the GraphObject port that the link was disconnected from, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**LinkReshaped**", the user has just rerouted an existing Link using [LinkReshapingTool](https://gojs.net/latest/api/symbols/LinkReshapingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the modified Link, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the List of Points of the link's original route, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**LostFocus**", the diagram has lost keyboard focus ("blur"). 
*    "**Modified**", the [Diagram.isModified](https://gojs.net/latest/api/symbols/Diagram.html#isModified) property has been set to a new value -- useful for marking a window as having been modified since the last save; do not modify the Diagram or its Model in the event listener. 
*    "**ObjectSingleClicked**", a click that occurred on a GraphObject; the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the GraphObject; if you make any changes, start and commit your own transaction. 
*    "**ObjectDoubleClicked**", a double-click that occurred on a GraphObject; the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the GraphObject; if you make any changes, start and commit your own transaction. 
*    "**ObjectContextClicked**", a context-click that occurred on a GraphObject; the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the GraphObject; if you make any changes, start and commit your own transaction. 
*    "**PartCreated**", the user inserted a new Part by [ClickCreatingTool](https://gojs.net/latest/api/symbols/ClickCreatingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the new Part, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**PartResized**", the user has changed the size of a GraphObject by [ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the GraphObject, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the original Size, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**PartRotated**", the user has changed the angle of a GraphObject by [RotatingTool](https://gojs.net/latest/api/symbols/RotatingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the GraphObject, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the original angle in degrees, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionMoved**", the user has moved selected Parts by [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is a Set of the moved Parts, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionCopied**", the user has copied selected Parts by [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is Set of the newly copied Parts, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionDeleting**", the user is about to delete selected Parts by [CommandHandler.deleteSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#deleteSelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection) collection of Parts to be deleted, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionDeleted**", the user has deleted selected Parts by [CommandHandler.deleteSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#deleteSelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Parts that were deleted, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionGrouped**", the user has made a new Group out of the selected Parts by [CommandHandler.groupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#groupSelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the new Group, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SelectionUngrouped**", the user has removed a selected Group but kept its members by [CommandHandler.ungroupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#ungroupSelection); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Groups that were ungrouped, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the collection of former member Parts that were ungrouped, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SubGraphCollapsed**", the user has collapsed selected Groups by [CommandHandler.collapseSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseSubGraph); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Groups that were collapsed, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**SubGraphExpanded**", the user has expanded selected Groups by [CommandHandler.expandSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#expandSubGraph); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Groups that were expanded, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**TextEdited**", the user has changed the string value of a TextBlock by [TextEditingTool](https://gojs.net/latest/api/symbols/TextEditingTool.html); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the edited TextBlock, the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is the original string, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**ThemeChanged**", the diagram's theme has changed, maybe as a result of setting [ThemeManager.currentTheme](https://gojs.net/latest/api/symbols/ThemeManager.html#currentTheme) or calling [ThemeManager.set](https://gojs.net/latest/api/symbols/ThemeManager.html#set). 
*    "**TreeCollapsed**", the user has collapsed selected Nodes with subtrees by [CommandHandler.collapseTree](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseTree); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Nodes that were collapsed, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**TreeExpanded**", the user has expanded selected Nodes with subtrees by [CommandHandler.expandTree](https://gojs.net/latest/api/symbols/CommandHandler.html#expandTree); the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is the collection of Nodes that were expanded, and this is called within a transaction, so that you do not have to start and commit your own transaction. 
*    "**ViewportBoundsChanged**", the visible area of the Diagram, [Diagram.viewportBounds](https://gojs.net/latest/api/symbols/Diagram.html#viewportBounds), has changed; the [DiagramEvent.subject](https://gojs.net/latest/api/symbols/DiagramEvent.html#subject) is an object whose "scale" property is the old [Diagram.scale](https://gojs.net/latest/api/symbols/Diagram.html#scale) value, whose "position" property is the old [Diagram.position](https://gojs.net/latest/api/symbols/Diagram.html#position) value, whose "bounds" property is the old [Diagram.viewportBounds](https://gojs.net/latest/api/symbols/Diagram.html#viewportBounds) value, whose "canvasSize" property is the old size of the [Diagram.div](https://gojs.net/latest/api/symbols/Diagram.html#div), and whose "newCanvasSize" property is the new size of the [Diagram.div](https://gojs.net/latest/api/symbols/Diagram.html#div); the [DiagramEvent.parameter](https://gojs.net/latest/api/symbols/DiagramEvent.html#parameter) is also the old viewportBounds Rect. Do not modify the Diagram position or scale (i.e. the viewport bounds) in the listener. 

DiagramEvents do not necessarily correspond to mouse events or keyboard events or touch events. Nor do they necessarily correspond to changes to the diagram's model -- for tracking such changes, use [Model.addChangedListener](https://gojs.net/latest/api/symbols/Model.html#addChangedListener) or [Diagram.addModelChangedListener](https://gojs.net/latest/api/symbols/Diagram.html#addModelChangedListener). DiagramEvents only occur because the user did something, perhaps indirectly.

In addition to the DiagramEvent listeners there are also circumstances where detecting such changes is common enough to warrant having properties that are event handlers. Because these events do not necessarily correspond to any particular input or diagram event, these event handlers have custom arguments that are specific to the situation.

One very common such event property is [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click), which if non-null is a function that is called whenever the user clicks on that object. This is most commonly used to specify behavior for "Button"s, but it and the other "click" event properties, "doubleClick" and "contextClick", can be useful on any GraphObject.

Another common event property is [Part.selectionChanged](https://gojs.net/latest/api/symbols/Part.html#selectionChanged), which (if non-null) is called whenever [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) changes. In this case the event handler function is passed a single argument, the Part. There is no need for additional arguments because the function can check the current value of [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) to decide what to do.

Model [ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html)s are more complete and reliable than depending on [DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html)s. For example, the "LinkDrawn" DiagramEvent is not raised when code adds a link to a diagram. That DiagramEvent is only raised when the user draws a new link using the [LinkingTool](https://gojs.net/latest/api/symbols/LinkingTool.html). Furthermore the link has not yet been routed, so [Link.points](https://gojs.net/latest/api/symbols/Link.html#points) will not have been computed. In fact, creating a new link may invalidate a [Layout](https://gojs.net/latest/api/symbols/Layout.html), so all of the nodes may be moved in the near future.

Sometimes you want to update a database as the user makes changes to a diagram. Usually you will want to implement a [Model](https://gojs.net/latest/api/symbols/Model.html)[ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html) listener, by calling [Model.addChangedListener](https://gojs.net/latest/api/symbols/Model.html#addChangedListener) or [Diagram.addModelChangedListener](https://gojs.net/latest/api/symbols/Diagram.html#addModelChangedListener), that notices the changes to the model and decides what to record in the database. See the discussion of [Changed Events](https://gojs.net/latest/intro/changedEvents.html) and the [Update Demo](https://gojs.net/latest/samples/updateDemo.html).

This example demonstrates handling several diagram events: **"ObjectSingleClicked"**, **"BackgroundDoubleClicked"**, and **"ClipboardPasted"**.

```
function showMessage(s) {
  document.getElementById("diagramEventsMsg").textContent = s;
}

diagram.addDiagramListener("ObjectSingleClicked",
    e => {
      const part = e.subject.part;
      if (!(part instanceof go.Link)) showMessage("Clicked on " + part.data.text);
    });

diagram.addDiagramListener("BackgroundDoubleClicked",
    e => showMessage("Double-clicked at " + e.diagram.lastInput.documentPoint));

diagram.addDiagramListener("ClipboardPasted",
    e => showMessage("Pasted " + e.diagram.selection.count + " parts"));

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta", group: 4 },
  { key: 3, text: "Gamma", group: 4 },
  { key: 4, text: "Omega", isGroup: true },
  { key: 5, text: "Delta" }
];
const linkDataArray = [
  { from: 1, to: 2 },  // from outside the Group to inside it
  { from: 2, to: 3 },  // this link is a member of the Group
  { from: 4, to: 5 }  // from the Group to a Node
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

(message)

Input Events
------------

When a low-level HTML DOM event occurs, **GoJS** canonicalizes the keyboard/mouse/touch event information into a new [InputEvent](https://gojs.net/latest/api/symbols/InputEvent.html) that can be passed to various event-handling methods and saved for later examination.

An InputEvent keeps the [InputEvent.key](https://gojs.net/latest/api/symbols/InputEvent.html#key) and [InputEvent.code](https://gojs.net/latest/api/symbols/InputEvent.html#code) for keyboard events, the [InputEvent.button](https://gojs.net/latest/api/symbols/InputEvent.html#button) for mouse events, the [InputEvent.viewPoint](https://gojs.net/latest/api/symbols/InputEvent.html#viewPoint) for mouse and touch events, and [InputEvent.modifiers](https://gojs.net/latest/api/symbols/InputEvent.html#modifiers) for keyboard and mouse events.

The diagram's event handlers also record the [InputEvent.documentPoint](https://gojs.net/latest/api/symbols/InputEvent.html#documentPoint), which is the [InputEvent.viewPoint](https://gojs.net/latest/api/symbols/InputEvent.html#viewPoint) in document coordinates at the time of the mouse event, and the [InputEvent.timestamp](https://gojs.net/latest/api/symbols/InputEvent.html#timestamp), which records the time that the event occurred in milliseconds.

The InputEvent class also provides many handy properties for particular kinds of events. [InputEvent.commandKey](https://gojs.net/latest/api/symbols/InputEvent.html#commandKey) is a read-only property that is convenient for use in overrides of [CommandHandler.doKeyDown](https://gojs.net/latest/api/symbols/CommandHandler.html#doKeyDown) or [Tool.doKeyDown](https://gojs.net/latest/api/symbols/Tool.html#doKeyDown), instead of looking at both [InputEvent.key](https://gojs.net/latest/api/symbols/InputEvent.html#key) and [InputEvent.code](https://gojs.net/latest/api/symbols/InputEvent.html#code) in order to decide how to handle the keyboard event. Examples include [InputEvent.control](https://gojs.net/latest/api/symbols/InputEvent.html#control) (if the control key had been pressed) and [InputEvent.left](https://gojs.net/latest/api/symbols/InputEvent.html#left) (if the left/primary mouse button was pressed).

Some tools find the "current" [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) at the mouse point. This is remembered as the [InputEvent.targetObject](https://gojs.net/latest/api/symbols/InputEvent.html#targetObject).

Higher-level input events
-------------------------

Some tools detect a sequence of input events to compose somewhat more abstract user events. Examples include "click" (mouse-down-and-up very close to each other) and "hover" (motionless mouse for some time). The tools will call an event handler (if there is any) for the current [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) at the mouse point. The event handler is held as the value of a property on the object. It then also "bubbles" the event up the chain of [GraphObject.panel](https://gojs.net/latest/api/symbols/GraphObject.html#panel)s until it ends with a [Part](https://gojs.net/latest/api/symbols/Part.html). This allows a "click" event handler to be declared on a [Panel](https://gojs.net/latest/api/symbols/Panel.html) and have it apply even if the click actually happens on an element deep inside the panel. If there is no object at the mouse point, the event occurs on the diagram.

Click-like event properties include [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click), [GraphObject.doubleClick](https://gojs.net/latest/api/symbols/GraphObject.html#doubleClick), and [GraphObject.contextClick](https://gojs.net/latest/api/symbols/GraphObject.html#contextClick). They also occur when there is no GraphObject -- the event happened in the diagram's background: [Diagram.click](https://gojs.net/latest/api/symbols/Diagram.html#click), [Diagram.doubleClick](https://gojs.net/latest/api/symbols/Diagram.html#doubleClick), and [Diagram.contextClick](https://gojs.net/latest/api/symbols/Diagram.html#contextClick). These are all properties that you can set to a function that is the event handler. These events are caused by both mouse events and touch events.

Mouse-over-like event properties include [GraphObject.mouseEnter](https://gojs.net/latest/api/symbols/GraphObject.html#mouseEnter), [GraphObject.mouseOver](https://gojs.net/latest/api/symbols/GraphObject.html#mouseOver), and [GraphObject.mouseLeave](https://gojs.net/latest/api/symbols/GraphObject.html#mouseLeave). But only [Diagram.mouseOver](https://gojs.net/latest/api/symbols/Diagram.html#mouseOver) applies to the diagram.

Hover-like event properties include [GraphObject.mouseHover](https://gojs.net/latest/api/symbols/GraphObject.html#mouseHover) and [GraphObject.mouseHold](https://gojs.net/latest/api/symbols/GraphObject.html#mouseHold). The equivalent diagram properties are [Diagram.mouseHover](https://gojs.net/latest/api/symbols/Diagram.html#mouseHover) and [Diagram.mouseHold](https://gojs.net/latest/api/symbols/Diagram.html#mouseHold).

There are also event properties for dragging operations: [GraphObject.mouseDragEnter](https://gojs.net/latest/api/symbols/GraphObject.html#mouseDragEnter), [GraphObject.mouseDragLeave](https://gojs.net/latest/api/symbols/GraphObject.html#mouseDragLeave), and [GraphObject.mouseDrop](https://gojs.net/latest/api/symbols/GraphObject.html#mouseDrop). These apply to stationary objects, not the objects being dragged. And they also occur when dragging by touch events, not just mouse events.

This example demonstrates handling three higher-level input events: clicking on nodes and entering/leaving groups.

```
function showMessage(s) {
  document.getElementById("inputEventsMsg").textContent = s;
}

diagram.nodeTemplate =
  new go.Node("Auto", {
      click: (e, obj) => showMessage("Clicked on " + obj.part.data.text)
    })
    .add(
      new go.Shape("Ellipse", { fill: "white" }),
      new go.TextBlock()
        .bind("text")
    );

diagram.groupTemplate =
  new go.Group("Vertical", {
      click: (e, obj) => showMessage("Clicked on " + obj.part.data.text),
      mouseEnter: (e, obj, prev) => {  // change group's background brush
        const shape = obj.part.findObject("SHAPE");
        if (shape) shape.fill = "red";
      },
      mouseLeave: (e, obj, next) => {  // restore to original brush
        const shape = obj.part.findObject("SHAPE");
        if (shape) shape.fill = "rgba(128,128,128,0.33)";
      }
    })
    .add(
      new go.TextBlock({ alignment: go.Spot.Left, font: "Bold 12pt Sans-Serif" })
        .bind("text"),
      new go.Panel("Auto")
        .add(
          new go.Shape("RoundedRectangle", {
              name: "SHAPE",
              parameter1: 14,
              fill: "rgba(128,128,128,0.33)"
            }),
          new go.Placeholder({ padding: 5 })
        )
    );

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta", group: 4 },
  { key: 3, text: "Gamma", group: 4 },
  { key: 4, text: "Omega", isGroup: true },
  { key: 5, text: "Delta" }
];
const linkDataArray = [
  { from: 1, to: 2 },  // from outside the Group to inside it
  { from: 2, to: 3 },  // this link is a member of the Group
  { from: 4, to: 5 }  // from the Group to a Node
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

(message)

Clicking and Selecting
----------------------

This example demonstrates both the "click" and the "selectionChanged" events:

```
function showMessage(s) {
  document.getElementById("changeMethodsMsg").textContent = s;
}

diagram.nodeTemplate =
  new go.Node("Auto", {
      click: (e, obj) => showMessage("Clicked on " + obj.part.data.text),
      selectionAdorned: false,
      selectionChanged: part => {
        const shape = part.elt(0);
        shape.fill = part.isSelected ? "red" : "white";
      }
    })
   .add(
      new go.Shape("Ellipse", { fill: "white" }),
      new go.TextBlock()
        .bind("text")
    );

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta" },
  { key: 3, text: "Gamma" }
];
const linkDataArray = [
  { from: 1, to: 2 },
  { from: 2, to: 3 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

(message)

Try Ctrl-A to select everything. Note the distinction between the [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click) event property and the [Part.selectionChanged](https://gojs.net/latest/api/symbols/Part.html#selectionChanged) event property. Both are methods that get called when something has happened to the node. The [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click) occurs when the user clicks on the node, which happens to select the node. But the [Part.selectionChanged](https://gojs.net/latest/api/symbols/Part.html#selectionChanged) occurs even when there is no click event or even any mouse event -- it was due to a property change to the node.
