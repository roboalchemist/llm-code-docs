# Source: https://gojs.net/intro/contextMenus.html

Title: Context Menus

URL Source: https://gojs.net/intro/contextMenus.html

Markdown Content:
**GoJS** provides a mechanism for you to define context menus for any object or for the diagram background.

Note: GoJS context menus cannot render outside of Diagrams, because they are objects inside the Diagram and therefore drawn only on the Diagram. If you need a context menu that may be drawn partially or fully outside the Diagram, use an [HTML context menu](https://gojs.net/intro/contextMenus.html#HTMLContextMenus).

A GoJS context menu is an [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) that is shown when the user context-clicks (right mouse click or long touch hold) an object that has its [GraphObject.contextMenu](https://gojs.net/latest/api/symbols/GraphObject.html#contextMenu) set. The context menu is bound to the same data as the part itself.

See samples that make use of context menus in the [samples index](https://gojs.net/latest/samples/index.html#contextmenus).

It is typical to implement a context menu as a "ContextMenu" Panel containing "ContextMenuButton"s, as you can see in the code below in the assignment of the Node's [GraphObject.contextMenu](https://gojs.net/latest/api/symbols/GraphObject.html#contextMenu) and [Diagram.contextMenu](https://gojs.net/latest/api/symbols/Diagram.html#contextMenu) properties. Each "ContextMenu" is just a "Vertical" Panel [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) that is shadowed. Each "ContextMenuButton" is a Panel on which you can set the [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click) event handler. In the event handler `obj.part` will be the whole context menu Adornment. `obj.part.adornedPart` will be the adorned Node or Link. The bound data is `obj.part.data`, which will be the same as `obj.part.adornedPart.data`.

You can see how the "ContextMenu" and "ContextMenuButton" builders are defined at [Buttons.js](https://gojs.net/latest/extensions/Buttons.js). There are examples of customizing buttons at [Introduction to Buttons](https://gojs.net/latest/intro/buttons.html). You may also wish to theme your own context menus, described on the [theming intro page](https://gojs.net/latest/intro/theming.html#BuilderObjects).

In this example each [Node](https://gojs.net/latest/api/symbols/Node.html) has its [GraphObject.contextMenu](https://gojs.net/latest/api/symbols/GraphObject.html#contextMenu) property set to an Adornment that shows a single button that when clicked changes the color property of the bound model data. The diagram gets its own context menu by setting [Diagram.contextMenu](https://gojs.net/latest/api/symbols/Diagram.html#contextMenu).

```
// This method is called as a context menu button's click handler.
// Rotate the selected node's color through a predefined sequence of colors.
function changeColor(e, obj) {
  diagram.commit(d => {
    // get the context menu that holds the button that was clicked
    const contextmenu = obj.part;
    // get the node data to which the Node is data bound
    const nodedata = contextmenu.data;
    // compute the next color for the node
    let newcolor = "lightblue";
    switch (nodedata.color) {
      case "lightblue": newcolor = "lightgreen"; break;
      case "lightgreen": newcolor = "lightyellow"; break;
      case "lightyellow": newcolor = "orange"; break;
      case "orange": newcolor = "lightblue"; break;
    }
    // modify the node data
    // this evaluates data Bindings and records changes in the UndoManager
    d.model.set(nodedata, "color", newcolor);
  }, "changed color");
}

// this is a normal Node template that also has a contextMenu defined for it
diagram.nodeTemplate =
  new go.Node("Auto", {
      contextMenu:     // define a context menu for each node
        go.GraphObject.build("ContextMenu")  // that has one button
          .add(
            go.GraphObject.build("ContextMenuButton", {
                click: changeColor,
                "ButtonBorder.fill": "white",
                "_buttonFillOver": "skyblue",
              })
              .add(new go.TextBlock("Change Color"))
            // more ContextMenuButtons would go here
          )
        // end Adornment

    })
    .add(
      new go.Shape("RoundedRectangle", { fill: "white" })
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

// also define a context menu for the diagram's background
diagram.contextMenu =
  go.GraphObject.build("ContextMenu")
    .add(
      go.GraphObject.build("ContextMenuButton", {
          click: (e, obj) => e.diagram.commandHandler.undo()
        })
        .add(new go.TextBlock("Undo"))
        .bindObject("visible", "", o => o.diagram.commandHandler.canUndo()),
      go.GraphObject.build("ContextMenuButton", {
          click: (e, obj) => e.diagram.commandHandler.redo()
        })
        .add(new go.TextBlock("Redo"))
        .bindObject("visible", "", o => o.diagram.commandHandler.canRedo()),
      // no binding, always visible button:
      go.GraphObject.build("ContextMenuButton", {
          click: (e, obj) => {
            e.diagram.commit(d => {
              const data = {};
              d.model.addNodeData(data);
              part = d.findPartForData(data);  // must be same data reference, not a new {}
              // set location to saved mouseDownPoint in ContextMenuTool
              part.location = d.toolManager.contextMenuTool.mouseDownPoint;
            }, 'new node');
          }
        })
        .add(new go.TextBlock("New Node"))
    );

const nodeDataArray = [
  { key: 1, text: "Alpha", color: "lightyellow" },
  { key: 2, text: "Beta", color: "orange" }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
diagram.undoManager.isEnabled = true;
```

Try context clicking a node and invoking the "Change Color" command a few times. With the diagram context menu you will be able to "Undo" and/or "Redo", or you can use Control-Z and/or Control-Y.

Positioning
-----------

There are two ways to customize the positioning of the context menu relative to the adorned GraphObject. One way is to override [ContextMenuTool.positionContextMenu](https://gojs.net/latest/api/symbols/ContextMenuTool.html#positionContextMenu). Another way is to have the context menu [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) include a [Placeholder](https://gojs.net/latest/api/symbols/Placeholder.html). The Placeholder is positioned to have the same size and position as the adorned object. The context menu will not to have a background, and thus will not display a shadow by default when using a Placeholder.

```
// this is a shared context menu button click event handler, just for demonstration
function cmCommand(e, obj) {
  const node = obj.part.adornedPart;  // the Node with the context menu
  const buttontext = obj.elt(1);  // the TextBlock
  alert(buttontext.text + " command on " + node.data.text);
}

// this is a normal Node template that also has a contextMenu defined for it
diagram.nodeTemplate =
  new go.Node("Auto", {
      contextMenu:                           // define a context menu for each node
        go.GraphObject.build("ContextMenu",  // that has several buttons around
            { type: go.Panel.Spot })
          .add(                              // a Placeholder object
            new go.Placeholder({ padding: 5 }),
            go.GraphObject.build("ContextMenuButton",
                { alignment: go.Spot.Top, alignmentFocus: go.Spot.Bottom, click: cmCommand })
              .add(new go.TextBlock("Top")),
            go.GraphObject.build("ContextMenuButton",
                { alignment: go.Spot.Right, alignmentFocus: go.Spot.Left, click: cmCommand })
              .add(new go.TextBlock("Right")),
            go.GraphObject.build("ContextMenuButton",
                { alignment: go.Spot.Bottom, alignmentFocus: go.Spot.Top, click: cmCommand })
              .add(new go.TextBlock("Bottom")),
            go.GraphObject.build("ContextMenuButton",
                { alignment: go.Spot.Left, alignmentFocus: go.Spot.Right, click: cmCommand })
              .add(new go.TextBlock("Left"))
          )  // end Adornment
    })
    .add(
      new go.Shape("RoundedRectangle", { fill: "white" })
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  { key: 1, text: "Alpha", color: "lightyellow" },
  { key: 2, text: "Beta", color: "orange" }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

HTML Context Menus
------------------

It is possible to define custom context menus using HTML instead of Adornments by using the [HTMLInfo](https://gojs.net/latest/api/symbols/HTMLInfo.html) class. The [Custom Context Menu sample](https://gojs.net/latest/samples/customContextMenu.html) and [Lightbox Context Menu sample](https://gojs.net/latest/samples/htmlLightBoxContextMenu.html) show two such custom context menus.

HTML context menus require more effort to implement than using the default **GoJS** "ContextMenu" and "ContextMenuButton". However you would have the full power of HTML/CSS/JavaScript to show whatever you want. This includes creating context menus that can exist or float outside of the Diagram.

There are two primary considerations when authoring HTML and CSS for context menus. The context menu should usually be a sibling Element of the Diagram and should never be nested inside a Diagram DIV:

```
<div style="position: relative;">
  <div id="myDiagramDiv" style="border: solid 1px black; width:400px; height:400px;"></div>
  <div id="contextMenu">
    <!-- ... context menu HTML -->
  </div>
</div>
```

And the ContextMenu may need a z-index set to ensure it is always on top. GoJS Diagrams have z-index of 2, and some tools a z-index of 100.

```
#contextMenu {
  z-index: 1000;
  ...
}
```

See the [Custom Context Menu sample](https://gojs.net/latest/samples/customContextMenu.html) and [Lightbox Context Menu sample](https://gojs.net/latest/samples/htmlLightBoxContextMenu.html) for HTML examples. See the [HTMLInteraction](https://gojs.net/latest/intro/HTMLInteraction.html) page for more discussion on HTML in GoJS.

Default Context Menu for Touch-enabled devices
----------------------------------------------

Touch devices are presumed to have no keyboard ability, which makes actions like copying and pasting more difficult. Because of this, **GoJS** provides a built-in default context menu on touch devices, implemented in HTML. The buttons on this menu are populated dynamically, depending on the target GraphObject (if any) and Diagram and their properties.

The default context menu can be disabled by setting [ContextMenuTool.defaultTouchContextMenu](https://gojs.net/latest/api/symbols/ContextMenuTool.html#defaultTouchContextMenu) to null. The [Lightbox Context Menu sample](https://gojs.net/latest/samples/htmlLightBoxContextMenu.html) contains a re-implementation of this menu if you wish to modify it.

If you define your own custom context menus, they will prevent the default context menu from appearing on touch devices. We recommend that your custom context menus include all common commands appropriate for your app.
