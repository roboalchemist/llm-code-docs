# Source: https://gojs.net/intro/

Title: Introduction

URL Source: https://gojs.net/intro/

Markdown Content:
Introduction to GoJS Diagramming Components
-------------------------------------------

**GoJS** is a JavaScript library that lets you easily create interactive diagrams in web browsers. **GoJS** supports graphical templates and data-binding of graphical object properties to model data. You only need to save and restore the model, consisting of simple JavaScript objects holding whatever properties your app needs. Many predefined tools and commands implement the standard behaviors that most diagrams need. Customization of appearance and behavior is mostly a matter of setting properties.

A Simple GoJS Diagram
---------------------

The following code defines a node template and model data, which produces a small diagram with a handful of nodes and links.

```
// the node template describes how each Node should be constructed
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(  // the Shape will be sized to go around the TextBlock
      new go.Shape("RoundedRectangle")
        // Shape.fill is bound to Node.data.color
        .bind("fill", "color"),
      new go.TextBlock({ margin: 8}) // Specify a margin to add some room around the text
        // TextBlock.text is bound to Node.data.text
        .bind("text")
    );

// the Model holds only the essential information describing the diagram
diagram.model = new go.GraphLinksModel(
[ // a JavaScript Array of JavaScript objects, one per node;
  // the "color" property is added specifically for this app
  { key: 1, text: "Alpha", color: "lightblue" },
  { key: 2, text: "Beta", color: "orange" },
  { key: 3, text: "Gamma", color: "lightgreen" },
  { key: 4, text: "Delta", color: "pink" }
],
[ // a JavaScript Array of JavaScript objects, one per link
  { from: 1, to: 2 },
  { from: 1, to: 3 },
  { from: 2, to: 2 },
  { from: 3, to: 4 },
  { from: 4, to: 1 }
]);

// enable Ctrl-Z to undo and Ctrl-Y to redo
diagram.undoManager.isEnabled = true;
```

You can interact with this diagram in many ways:

*   You can select a part (a [Node](https://gojs.net/latest/api/symbols/Node.html) or a [Link](https://gojs.net/latest/api/symbols/Link.html)) by clicking on it. Selected nodes are highlighted with an [Adornment](https://gojs.net/latest/api/symbols/Adornment.html) that is a blue rectangle surrounding the node. Selected links are highlighted with a blue line following the path of the link.
*   Multiple parts may be selected at once. Hold the Shift key down when clicking to add to the selection. Hold the Control key down when clicking to toggle whether that part is selected.
*   Another way to multi-select is to mouse-down at a point in the background (not on a part), wait a moment, and then drag a box. Parts that are fully in the box when the mouse-up occurs are selected. The Shift and Control modifiers work then as well.
*   Ctrl-A selects all parts in the diagram.
*   Move one or more nodes by selecting them and dragging.
*   Copying selected parts works with either copy/paste (Ctrl-C/Ctrl-V) or with Ctrl-mouse-drag.
*   Delete selected parts with the Delete key.
*   Ctrl-Z to undo the previous modification and Ctrl-Y to redo it.
*   If scrollbars are visible or if the whole collection of parts is smaller than the viewable area of the diagram (the "viewport"), you can pan the diagram with a mouse-down in the background (not on a part) if you drag without waiting.
*   Use the mouse wheel to scroll up and down and Shift-mouse-wheel to scroll left and right. Ctrl-mouse-wheel zooms in and out.

You can also pan, pinch zoom, select, copy, move, delete, undo, and redo with your fingers on a touch device. Most commands that can be invoked from a keyboard can be invoked from the default context menu that you get by pressing your finger and holding it motionless for a moment.

What is unique about all of the examples in the documentation is that they are all "live" -- there are no screenshots! They are actual [Diagram](https://gojs.net/latest/api/symbols/Diagram.html)s implemented by the source code shown. You can interact with them -- some even display animation.

If you'd like to see more examples of what **GoJS** can do, see the [GoJS Samples directory](https://gojs.net/latest/samples/index.html). To make it easier to search the JavaScript code and documentation or to experiment by modifying the samples, you can install the **GoJS** kit in various manners:

*   Download a ZIP file from our [Download](https://gojs.net/latest/download.html) page.
*   Clone or download from [GoJS on GitHub](https://github.com/NorthwoodsSoftware/GoJS).
*   Install GoJS using `npm install gojs` and `npm create gojs-kit@latest`.

GoJS Concepts
-------------

[Diagram](https://gojs.net/latest/api/symbols/Diagram.html)s consist of [Part](https://gojs.net/latest/api/symbols/Part.html)s: [Node](https://gojs.net/latest/api/symbols/Node.html)s that may be connected by [Link](https://gojs.net/latest/api/symbols/Link.html)s and that may be grouped together into [Group](https://gojs.net/latest/api/symbols/Group.html)s. All of these parts are gathered together in [Layer](https://gojs.net/latest/api/symbols/Layer.html)s and are arranged by [Layout](https://gojs.net/latest/api/symbols/Layout.html)s and [Router](https://gojs.net/latest/api/symbols/Router.html)s.

Each diagram has a [Model](https://gojs.net/latest/api/symbols/Model.html) that holds and interprets your application data to determine node-to-node link relationships and group-member relationships. Most parts are data-bound to your application data. The diagram automatically creates a [Node](https://gojs.net/latest/api/symbols/Node.html) or a [Group](https://gojs.net/latest/api/symbols/Group.html) for each data item in the model's [Model.nodeDataArray](https://gojs.net/latest/api/symbols/Model.html#nodeDataArray) and a [Link](https://gojs.net/latest/api/symbols/Link.html) for each data item in the model's [GraphLinksModel.linkDataArray](https://gojs.net/latest/api/symbols/GraphLinksModel.html#linkDataArray). You can add whatever properties you need to each data object, but there are just a few properties that each kind of model expects. They are shown in bold in the gray data objects.

Each [Node](https://gojs.net/latest/api/symbols/Node.html) or [Link](https://gojs.net/latest/api/symbols/Link.html) is normally defined by a template that declares its appearance and behavior. Each template consists of [Panel](https://gojs.net/latest/api/symbols/Panel.html)s of [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s such as [TextBlock](https://gojs.net/latest/api/symbols/TextBlock.html)s or [Shape](https://gojs.net/latest/api/symbols/Shape.html)s. There are default templates for all parts, but almost all applications will specify custom templates in order to achieve the desired appearance and behavior. Data bindings of [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) properties to model data properties make each Node or Link unique for the data.

The nodes may be positioned manually (interactively or programmatically) or may be arranged automatically by the [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) and by each [Group.layout](https://gojs.net/latest/api/symbols/Group.html#layout). Nodes are positioned either by their top-left corner point ([GraphObject.position](https://gojs.net/latest/api/symbols/GraphObject.html#position)) or by a programmer-defined spot in the node ([Part.location](https://gojs.net/latest/api/symbols/Part.html#location) and [Part.locationSpot](https://gojs.net/latest/api/symbols/Part.html#locationSpot)).

[Tool](https://gojs.net/latest/api/symbols/Tool.html)s handle mouse and keyboard and touch or stylus events. Each diagram has a number of tools that perform interactive tasks such as selecting parts or dragging them or drawing a new link between two nodes. The [ToolManager](https://gojs.net/latest/api/symbols/ToolManager.html) determines which tool should be running, depending on the mouse events and current circumstances.

Each diagram also has a [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) that implements various commands, such as Delete or Copy. The CommandHandler interprets keyboard events, such as Ctrl-Z, when the ToolManager is running.

The diagram provides the ability to scroll the parts of the diagram and to zoom in or out. The diagram also contains all of the layers, which in turn contain all of the parts (nodes and links). The parts in turn are composed of possibly nested panels of text, shapes, and images. This hierarchy of JavaScript objects in memory forms the "visual tree" of everything that may be drawn by the diagram.

Animations are implemented and controlled by the [AnimationManager](https://gojs.net/latest/api/symbols/AnimationManager.html). Automatic animations happen after automatic layouts and upon the execution of various commands. You can define your own custom [Animation](https://gojs.net/latest/api/symbols/Animation.html)s.

The [Overview](https://gojs.net/latest/api/symbols/Overview.html) class allows the user to see the whole model and to control what part of it that the diagram displays. The [Palette](https://gojs.net/latest/api/symbols/Palette.html) class holds parts that the user may drag-and-drop into a diagram.

You can select one or more parts in the diagram. The template implementation may change the appearance of the node or link when it is selected. The diagram may also add [Adornment](https://gojs.net/latest/api/symbols/Adornment.html)s to indicate selection and to support tools such as resizing a node or reconnecting a link. Adornments are also how tooltips and context menus are implemented.

All programmatic changes to [Diagram](https://gojs.net/latest/api/symbols/Diagram.html), [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html), [Model](https://gojs.net/latest/api/symbols/Model.html) or model data state should be performed within a single transaction per user action, to make sure updating happens correctly and to support undo/redo. All of the predefined tools and commands perform transactions, so each user action is automatically undoable if the [UndoManager](https://gojs.net/latest/api/symbols/UndoManager.html) is enabled. [DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html)s on Diagrams, and event handlers on Diagrams and GraphObjects, are all documented whether they are raised within a transaction or whether you need to conduct a transaction in order to change the model or the diagram.

Creating a Diagram
------------------

**GoJS** does not depend on any JavaScript library or framework, so you should be able to use it in any environment. However it does require that the environment support modern HTML and JavaScript.

### Loading GoJS

Before you can execute any JavaScript code to build a Diagram, you will need to load the **GoJS** library. When you include the library, the "`go`" JavaScript object will hold all of the **GoJS** types. During development we recommend that you load "go-debug.js" instead of "go.js", for additional run-time error checking and debugging ability.

We recommend that you declare that your web page supports modern HTML:

```
<!DOCTYPE html>  <!-- Declare standards mode. -->
<html>
  <head>
  . . .
  <!-- Include the GoJS library. -->
  <script src="go-debug.js"></script>
```

If depending on your npm environment:

`import * as go from "gojs";`
If you want to use ECMAScript modules, use `go-module.js` or `go.mjs` in the `release/` directory. However your build environment may automatically make this choice for you.

The extension classes are implemented in TypeScript and compiled as ECMAScript modules in the `extensionsJSM/` directory. That directory is present in the kit downloaded from our [website](https://gojs.net/latest/download.html) or [GitHub](https://github.com/NorthwoodsSoftware/GoJS), or in the `create-gojs-kit` npm package that you can install using `npm create gojs-kit@latest`. The extension classes are compiled into regular script-loadable JavaScript in the `extensions/` directory.

`import { DoubleTreeLayout } from "./path/to/gojs-kit/dist/extensionsJSM/DoubleTreeLayout.js";`
If you are using [RequireJS](https://requirejs.org/), the **GoJS** library supports UMD module definitions. Copy each extension file into your project, and update its `require` statement so that all of your code loads the same GoJS library and only does so once.

### Hosting GoJS in a Div Element

Every [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) must be hosted by an HTML Div element. **GoJS** will manage the contents of that Div element, but you may position and size and style the Div as you would any HTML element. The diagram will add a Canvas element to that Div element that the diagram will draw in -- this is what users actually see. The Canvas element is automatically sized to have the same size as the Div element.

```
<body>
  . . .
  <!-- The DIV for a Diagram needs an explicit size or else we won't see anything.
       In this case we also add a border to help see the edges. -->
  <div id="myDiagramDiv" style="border: solid 1px blue; width:400px; height:150px"></div>
```

Then you can create the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) in JavaScript with a reference to that Div element. Build the diagram by constructing plain JavaScript objects and adding them to the diagram's model. Note that all references in JavaScript code to **GoJS** types such as [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) are prefixed with "`go.`".

```
<!-- Create the Diagram in the DIV element using JavaScript. -->
<!-- The "go" object is the "namespace" that holds all of the GoJS types. -->
<script>
  const diagram = new go.Diagram("myDiagramDiv");
  diagram.model = new go.GraphLinksModel(
    [{ key: 1, text: "Hello" },   // two node data, in an Array
     { key: 2, text: "World!" }],
    [{ from: 1, to: 2 }]  // one link data, in an Array
  );
</script>
```

That one HTML DIV element and little bit of JavaScript code are the complete implementation of the "Hello World!" live diagram that you see above.

### Developing your Diagram

**GoJS** outputs error or warning messages when something goes wrong. When developing with **GoJS**, be sure to check your browser's developer console for information. The "go-debug.js" version of the library contains extra type-checking and error-checking code, and should be used during development. The "go.js" version has less error checking, but is faster as a result, and should be used in production.

Your JavaScript code should only use properties and methods that are documented in the [API](https://gojs.net/latest/api/index.html). The **GoJS** libraries are "minified", so if you look at an instance of a **GoJS** class in the debugger, you will see many one or two letter property names. All of those are internal names that you should not use. At the current time the only one letter property names are "x" and "y" on [Point](https://gojs.net/latest/api/symbols/Point.html), [Rect](https://gojs.net/latest/api/symbols/Rect.html), [Spot](https://gojs.net/latest/api/symbols/Spot.html) and [LayoutVertex](https://gojs.net/latest/api/symbols/LayoutVertex.html). The only two letter property name is [InputEvent.up](https://gojs.net/latest/api/symbols/InputEvent.html#up). Otherwise you should not try to use any one or two letter property names on any **GoJS**-defined objects.

Do not modify the prototypes of the **GoJS** classes.

 Only use the properties and methods documented in the [API](https://gojs.net/latest/api/index.html).

You can also use [TypeScript](https://www.typescriptlang.org/) in order to get better "edit-time" and "compile-time" type checking and "edit-time" documentation. The TypeScript definition files for **GoJS** are named "go.d.ts" and "go-module.d.ts" and are located in the same directory as the libraries. The extension classes are implemented in TypeScript, available at `../extensionsJSM/` and compiled to JavaScript in `../extensionsJSM/` as modules and `../extensions/` as scripts. Copy the extension definitions into your project and make sure they import the same **GoJS** library as all of your code does.

To learn about new features and bug fixes, read the [Change Log](https://gojs.net/latest/changelog.html). Read about getting the latest releases at [Downloads](https://gojs.net/latest/download.html).

You can see the variety of kinds of diagrams that you can build at [GoJS Samples](https://gojs.net/latest/samples/index.html).

In the next introduction page we discuss [building **GoJS** Parts and adding them into Diagrams.](https://gojs.net/latest/intro/buildingObjects.html)
