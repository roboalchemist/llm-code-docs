# Source: https://gojs.net/intro/nodes.html

Title: Nodes

URL Source: https://gojs.net/intro/nodes.html

Markdown Content:
You can customize your nodes to have exactly the appearance and behavior that you want. So far you have only seen very simple nodes. But if you have seen the [Sample Applications](https://gojs.net/latest/samples/index.html), you have seen many other kinds of nodes.

In this page we demonstrate some of the choices you can make when designing your nodes.

Surrounding Content
-------------------

It is common to surround interesting information with a border or other background.

### Simple borders

Many of the simplest nodes just consist of a [Panel](https://gojs.net/latest/api/symbols/Panel.html) of type [Panel.Auto](https://gojs.net/latest/api/symbols/Panel.html#Auto) with a [Shape](https://gojs.net/latest/api/symbols/Shape.html) surrounding a [TextBlock](https://gojs.net/latest/api/symbols/TextBlock.html).

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("Rectangle")
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", color: "lightblue" }
];
```

### Shaped nodes

The Shape surrounding the content need not be rectangular. This example demonstrates a number of shapes.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape()
        .bind("figure", "fig")
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", color: "lightblue", fig: "RoundedRectangle" },
  { text: "Beta", color: "lightblue", fig: "Ellipse" },
  { text: "Gamma", color: "lightblue", fig: "Hexagon" },
  { text: "Delta", color: "lightblue", fig: "FramedRectangle" },
  { text: "Epsilon", color: "lightblue", fig: "Cloud" },
  { text: "Zeta", color: "lightblue", fig: "Procedure" }
];
```

The surrounding/background object need not be a [Shape](https://gojs.net/latest/api/symbols/Shape.html). You could use a [Picture](https://gojs.net/latest/api/symbols/Picture.html) or even a more complex object such as a [Panel](https://gojs.net/latest/api/symbols/Panel.html).

### Complex contents

The content of an Auto [Panel](https://gojs.net/latest/api/symbols/Panel.html) need not be limited to a single [TextBlock](https://gojs.net/latest/api/symbols/TextBlock.html) -- you can have arbitrarily complex panels of objects. In this example the content is a Table Panel with three rows of TextBlocks.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape({
          fill: new go.Brush("Linear", { 0: "white", 1: "lightblue" }),
          stroke: "darkblue", strokeWidth: 2
        }),
      new go.Panel("Table", { defaultAlignment: go.Spot.Left, margin: 4 })
        .addColumnDefinition(1, { width: 4 })
        .add(
          new go.TextBlock({
              row: 0, column: 0, columnSpan: 3, alignment: go.Spot.Center,
              font: "bold 12pt sans-serif"
            })
            .bind("text"),
          new go.TextBlock("First: ", { row: 1, column: 0 }),
          new go.TextBlock({ row: 1, column: 2 })
            .bind("text", "prop1"),
          new go.TextBlock("Second: ", { row: 2, column: 0 }),
          new go.TextBlock({ row: 2, column: 2 })
            .bind("text", "prop2")
        )
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", prop1: "value of 'prop1'", prop2: "the other property" }
];
```

### Fixed-size nodes

The above examples have the "Auto" Panel surround some content, where the content might be of different sizes. That results in the Nodes having different sizes.

If you want a [Panel](https://gojs.net/latest/api/symbols/Panel.html) (and thus a Node, because [Node](https://gojs.net/latest/api/symbols/Node.html) inherits from [Part](https://gojs.net/latest/api/symbols/Part.html) which inherits from [Panel](https://gojs.net/latest/api/symbols/Panel.html)) to be of fixed size, set [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize) on that panel. (Equivalently, you can set [GraphObject.width](https://gojs.net/latest/api/symbols/GraphObject.html#width) and [GraphObject.height](https://gojs.net/latest/api/symbols/GraphObject.html#height).) That may result in the clipping of content that is too large, or it may result in extra space if the content is smaller than the available area provided by the "Auto" Panel.

```
diagram.nodeTemplate =
  new go.Node("Auto", { desiredSize: new go.Size(100, 50) })  // on Panel
    .add(
      new go.Shape()
        .bind("figure", "fig")
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", color: "lightblue", fig: "RoundedRectangle" },
  { text: "Beta", color: "lightblue", fig: "Ellipse" },
  { text: "Gamma", color: "lightblue", fig: "Hexagon" },
  { text: "Delta", color: "lightblue", fig: "FramedRectangle" },
  { text: "Epsilon,Epsilon,Epsilon", color: "lightblue", fig: "Cloud" },
  { text: "Z", color: "lightblue", fig: "Procedure" }
];
```

Note how the "Epsilon..." TextBlock is measured with the constraint of having a limited width, as imposed by the Panel's width. That results in the text being wrapped before (maybe) being clipped.

You probably do not want to set the desiredSize of the main element, the Shape in this case above. If you did, that would not constrain how the content elements are sized within the Panel.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape({ desiredSize: new go.Size(100, 50) })  // not here!
        .bind("figure", "fig")
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", color: "lightblue", fig: "RoundedRectangle" },
  { text: "Beta", color: "lightblue", fig: "Ellipse" },
  { text: "Gamma", color: "lightblue", fig: "Hexagon" },
  { text: "Delta", color: "lightblue", fig: "FramedRectangle" },
  { text: "Epsilon,Epsilon,Epsilon", color: "lightblue", fig: "Cloud" },
  { text: "Z", color: "lightblue", fig: "Procedure" }
];
```

Note how the TextBlock is measured without the constraint of having a limited width from the Panel. That results in the text being treated as a single long line, which is then clipped by the Panel.

Stacked Content
---------------

Many simple nodes consist of a few objects positioned above each other or next to each other.

### Icons

Perhaps the most commonly seen kind of node can be implemented using a Vertical [Panel](https://gojs.net/latest/api/symbols/Panel.html).

```
diagram.nodeTemplate =
  new go.Node("Vertical")
    .add(
      new go.Picture({ maxSize: new go.Size(50, 50) })
        .bind("source", "img"),
      new go.TextBlock({
          margin: new go.Margin(3, 0, 0, 0),
          maxSize: new go.Size(100, 30),
          isMultiline: false
        })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Jellylorum", img: "images/50x40.png" }
];
```

Of course you are not limited to just two objects in a panel. In fact you can have as many GraphObjects in a "Vertical" or a "Horizontal" Panel as you like.

```
diagram.nodeTemplate =
  new go.Node("Vertical")
    .add(
      new go.TextBlock({
          margin: new go.Margin(3, 0, 0, 0),
          maxSize: new go.Size(100, 30),
          isMultiline: false,
          font: "bold 10pt sans-serif"
        })
        .bind("text", "head"),
      new go.Picture({ maxSize: new go.Size(50, 50) })
        .bind("source", "img"),
      new go.TextBlock({
          margin: new go.Margin(3, 0, 0, 0),
          maxSize: new go.Size(100, 30),
          isMultiline: false
        })
        .bind("text", "foot")
    );

diagram.model.nodeDataArray = [
  { head: "Kitten", foot: "Tantomile", img: "images/50x40.png" }
];
```

### Small icons

Another commonly seen kind of node can be implemented using a Horizontal [Panel](https://gojs.net/latest/api/symbols/Panel.html).

```
diagram.nodeTemplate =
  new go.Node("Horizontal")
    .add(
      new go.Picture({ maxSize: new go.Size(16, 16) })
        .bind("source", "img"),
      new go.TextBlock({ margin: new go.Margin(0, 0, 0, 2) })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alonzo", img: "images/50x40.png" }
];
```

Nested Panels
-------------

Panels can be nested. For example, here is a node consisting of a "Vertical" Panel consisting of an "Auto" Panel surrounding a "Vertical" Panel including a "Horizontal" Panel. The outer "Vertical" Panel arranges the main stuff on top and a TextBlock on the bottom. The "Auto" Panel supplies a border around everything but the bottom text. The inner "Vertical" Panel places three objects vertically in a stack. The "Horizontal" Panel which is the first element of the "Vertical" Panel places three objects horizontally in a row.

```
// common styling for each indicator
function makeIndicator(propName) {  // the data property name
  return new go.Shape("Circle", {
        width: 8, height: 8, fill: "white", strokeWidth: 0, margin: 5
      })
      .bind("fill", propName);
}

function makeImagePath(icon) { return "../samples/images/" + icon; }

diagram.nodeTemplate =
  new go.Node("Vertical")
    .add(
      new go.Panel("Auto", {
          background: "white",
          portId: ""  // this whole panel acts as the only port for the node
        })
        .add(
          new go.Shape(  // the border
            { fill: "transparent", stroke: "lightgray" }),
          new go.Panel("Vertical")  // everything within the border
            .add(
              new go.Panel("Horizontal")
                .add(  // the row of status indicators
                  makeIndicator("ind0"),
                  makeIndicator("ind1"),
                  makeIndicator("ind2")
                ),  // end Horizontal Panel
              new go.Picture({ width: 32, height: 32, margin: 4 })
                .bind("source", "icon", makeImagePath),
              new go.TextBlock({
                  stretch: go.Stretch.Horizontal, textAlign: "center"
                })
                .bind("text", "number")
                .bind("background", "color")
            )  // end Vertical Panel
        ),  // end Auto Panel
      new go.TextBlock({ margin: 4 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { key: 1, text: "Device Type A", number: 17, icon: "server switch.jpg", color: "moccasin",
    ind0: "red", ind1: "orange", ind2: "mediumspringgreen" },
  { key: 2, text: "Device Type B", number: 97, icon: "voice atm switch.jpg", color: "mistyrose",
    ind0: "lightgray", ind1: "orange", ind2: "green" }
];
diagram.model.linkDataArray = [
  { from: 1, to: 2 }
];
```

Decorated Content
-----------------

Sometimes you want to have a simple node that may display additional visuals to indicate what state it is in.

One way to implement this is to use a Spot [Panel](https://gojs.net/latest/api/symbols/Panel.html), where the main element is itself a Panel containing the elements that you always want to display, and there are additional objects located at spots around the main element. The basic outline would be:

```
Node, "Spot"
    Panel, "Auto"  // the contents with border
        Shape        // the border
        Panel, ...   // the contents
           . . .
    Shape  // the decoration
```

So the basic body of the node is in a "Vertical" or any kind of Panel, which is surrounded by a border using an "Auto" Panel, which gets decorations using the "Spot" Panel that is also the Node.

The same design of having the Node be a "Spot" Panel can also used for placing ports relative to the body of a node.

```
diagram.nodeTemplate =
  new go.Node("Spot", {
      toolTip:
        new go.Adornment("Auto")
          .add(
            new go.Shape({ fill: "#FFFFCC" })
              .bind("visible", "info", i => i ? true : false),
            new go.TextBlock({ margin: 4 })
              .bind("text", "info")
          )
    })
    .add(
      // the main content:
      new go.Panel("Vertical")
        .add(
          new go.Picture({ maxSize: new go.Size(50, 50) })
            .bind("source", "img"),
          new go.TextBlock({ margin: new go.Margin(3, 0, 0, 0) })
            .bind("text", "text")
            .bind("stroke", "error", err => err ? "red" : "black")
        ),
      // decorations:
      new go.Shape("TriangleUp", {
          alignment: go.Spot.TopLeft,
          fill: "yellow", width: 14, height: 14,
          visible: false
        })
        .bind("visible", "info", i => i ? true : false),
      new go.Shape("StopSign", {
          alignment: go.Spot.TopRight,
          fill: "red", width: 14, height: 14,
          visible: false
        })
        .bind("visible", "error")
    );

diagram.model.nodeDataArray = [
  { text: "Demeter", img: "images/50x40.png", info: "" },
  { text: "Copricat", img: "images/50x40.png", error: true, info: "shredded curtains" }
];
```

As another example of a node decoration, this implements a "ribbon" at the top right corner of the node. The ribbon is implemented by a [Panel](https://gojs.net/latest/api/symbols/Panel.html) that contains both a [Shape](https://gojs.net/latest/api/symbols/Shape.html) and a [TextBlock](https://gojs.net/latest/api/symbols/TextBlock.html), and the panel is positioned by its [GraphObject.alignment](https://gojs.net/latest/api/symbols/GraphObject.html#alignment) and [GraphObject.alignmentFocus](https://gojs.net/latest/api/symbols/GraphObject.html#alignmentFocus) in the Spot Panel that also is the [Node](https://gojs.net/latest/api/symbols/Node.html). The appearance of the ribbon is achieved by using a custom [Geometry](https://gojs.net/latest/api/symbols/Geometry.html) and binding [GraphObject.opacity](https://gojs.net/latest/api/symbols/GraphObject.html#opacity).

```
diagram.nodeTemplate =
  new go.Node("Spot", {
      locationSpot: go.Spot.Center, locationObjectName: "BODY",
      selectionObjectName: "BODY"
    })
    .add(
      new go.Panel("Auto", {
          name: "BODY", width: 150, height: 100, portId: ""
        })
        .add(
          new go.Shape({ fill: "lightgray", stroke: null, strokeWidth: 0 }),
          new go.TextBlock()
            .bind("text")
        ),  // end "Auto" Panel
      new go.Panel("Spot", {
          // note that the opacity defaults to zero (not visible),
          // in case there is no "ribbon" property
          opacity: 0,
          alignment: new go.Spot(1, 0, 2, -2),
          alignmentFocus: go.Spot.TopRight
        })
        .bind("opacity", "ribbon", t => t ? 1 : 0)
        .add(
          new go.Shape({  // the ribbon itself
              geometryString: "F1 M0 0 L30 0 70 40 70 70z",
              fill: "red", stroke: null, strokeWidth: 0
            }),
          new go.TextBlock({
              alignment: new go.Spot(1, 0, -29, 29),
              angle: 45, maxSize: new go.Size(100, NaN),
              stroke: "white", font: "bold 13px sans-serif", textAlign: "center"
            })
            .bind("text", "ribbon")
        )  // end inner "Spot" Panel
    );  // end outer "Spot" Panel

diagram.model = new go.GraphLinksModel([
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta", ribbon: "NEWEST" }
],[
]);
```

Position and Location
---------------------

Nodes are positioned in document coordinates. (For more information, read [Coordinate Systems](https://gojs.net/latest/intro/viewport.html).) The point at which a Node resides, in document coordinates, is normally the top-left corner of the Node's [GraphObject.actualBounds](https://gojs.net/latest/api/symbols/GraphObject.html#actualBounds). If you set the [GraphObject.position](https://gojs.net/latest/api/symbols/GraphObject.html#position) of a Node, you will be modifying the `x` and `y` values of the node's [GraphObject.actualBounds](https://gojs.net/latest/api/symbols/GraphObject.html#actualBounds).

However there are times when it is more natural to think that the "point" of a Node is not at the top-left corner but at some other spot within. This is especially true when you want any variably-sized text labels or occasional decorations to be ignored regarding the node's location. That is why Nodes also have a "location" which refers to a point inside the Node. If you set the [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) of a Node, you will be lining up the location point of the node to be at that point in document coordinates. When you move a Node you are actually changing its [Part.location](https://gojs.net/latest/api/symbols/Part.html#location).

By default the location of a Node is the same as its position. However you can set the [Part.locationSpot](https://gojs.net/latest/api/symbols/Part.html#locationSpot) to cause the location point to be at some spot in the node's actualBounds. Furthermore you can set the [Part.locationObjectName](https://gojs.net/latest/api/symbols/Part.html#locationObjectName) to cause the location point to be at some spot in some element within the node. The position will always be at the top-left corner of the whole node, but the location may be some point at some spot in some object within the node.

```
diagram.grid.visible = true;

diagram.add(
  new go.Node("Vertical", { position: new go.Point(0, 0) })  // set the Node.position
    .add(
      new go.TextBlock("position", { editable: true }),
      new go.Shape({ name: "SHAPE", width: 30, height: 30, fill: "lightgreen" })
    ));

diagram.add(
  new go.Node("Vertical", {
      location: new go.Point(100, 0),  // set the Node.location
      locationObjectName: "SHAPE"  // the location point is on the element named "SHAPE"
    })
    .add(
      new go.TextBlock("location", { editable: true }),
      new go.Shape({ name: "SHAPE", width: 30, height: 30, fill: "lightgreen" })
    ));
```

In this example both nodes have the same Y-coordinate value of zero. Note how in the above example the "position" Node has the top-left corner of the node at the grid point. Yet the "location" Node has the top-left corner of the green square at the grid point. If you edit the text of each node after double-clicking on the text, note how the green square moves relative to the diagram grid for the "position" node, but that it does not move for the "location" node.

It is common to specify the [Part.locationSpot](https://gojs.net/latest/api/symbols/Part.html#locationSpot) to be `go.Spot.Center` so that the location point is at the center of some element in the node, rather than at the top-left corner of that element.

```
diagram.grid.visible = true;

diagram.add(
  new go.Node("Vertical", { position: new go.Point(0, 0) })  // set the Node.position
    .add(
      new go.TextBlock("position", { editable: true }),
      new go.Panel("Auto")
        .add(
          new go.Shape("Circle", { name: "SHAPE", width: 16, height: 16, fill: "lightgreen" }),
          new go.Shape("Circle", { width: 6, height: 6, strokeWidth: 0 })
        )
    ));

diagram.add(
  new go.Node("Vertical", {
      location: new go.Point(100, 0),  // set the Node.location
      locationObjectName: "SHAPE",  // the location point is at the center of "SHAPE"
      locationSpot: go.Spot.Center
    })
    .add(
      new go.TextBlock("location", { editable: true }),
      new go.Panel("Auto")
        .add(
          new go.Shape("Circle", { name: "SHAPE", width: 16, height: 16, fill: "lightgreen" }),
          new go.Shape("Circle", { width: 6, height: 6, strokeWidth: 0 })
        )
    ));
```

If the position or location of a Node is not [Point.isReal](https://gojs.net/latest/api/symbols/Point.html#isReal), it will not be seen, because GoJS will not know where to draw the node. In fact the default value for a node's position or location is `NaN, NaN` and it is the responsibility of either the [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) or data bindings to assign real point values for each node.
