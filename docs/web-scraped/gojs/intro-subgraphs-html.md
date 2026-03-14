# Source: https://gojs.net/intro/subgraphs.html

Title: SubGraphs

URL Source: https://gojs.net/intro/subgraphs.html

Markdown Content:
Groups as SubGraphs
-------------------

There are some common ways of treating the nodes and links that are the members of a group as if it were its own graph. One way to declutter a diagram is to "collapse" a [Group](https://gojs.net/latest/api/symbols/Group.html) to hide the subgraph that it holds.

A [Group](https://gojs.net/latest/api/symbols/Group.html) has its own [Group.layout](https://gojs.net/latest/api/symbols/Group.html#layout) that is responsible for the positioning of member [Node](https://gojs.net/latest/api/symbols/Node.html)s and the routing of member [Link](https://gojs.net/latest/api/symbols/Link.html)s. This is exactly like a [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) having its own [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) that positions top-level Nodes and routes top-level Links.

Keep in mind that subgraphs are not separate Diagrams and that Groups are just one way of organizing Parts. Because subgraphs are collections of Nodes and Links in the same Diagram as the Group itself, it is possible to have Links that connect Nodes that are inside a Group with Nodes that are outside of the group. It is also possible to have links that connect nodes with the group of which they are a member.

Layouts of SubGraphs
--------------------

You can specify a [Layout](https://gojs.net/latest/api/symbols/Layout.html) that applies to a group's subgraph by setting the [Group.layout](https://gojs.net/latest/api/symbols/Group.html#layout) property. This operates on the group's member nodes and links as if it were its own diagram. A diagram layout of nodes that include groups with their own layout will treat those groups as if they were simple nodes, albeit probably larger than normal nodes.

In this example the group has a different layout than the layout for the whole diagram. In this case the only difference is the direction in which the layout works, but you could use a completely different layout algorithm.

For simplicity these examples use the default templates for nodes and links.

```
diagram.groupTemplate =
  new go.Group("Auto", {
      // declare the Group.layout:
      layout: new go.LayeredDigraphLayout({
          direction: 0,
          columnSpacing: 10
        })
    })
    .add(
      new go.Shape("RoundedRectangle", {  // surrounds everything
          parameter1: 10, fill: "rgba(128,128,128,0.33)"  // translucent!
        }),
      new go.Panel("Vertical")  // position header above the subgraph
        .add(
          // group title near top, next to button
          new go.TextBlock({ font: "Bold 12pt Sans-Serif" })
            .bind("text"),
          // represents area for all member parts
          new go.Placeholder({ padding: 5, background: "white" })
        )
    );

// declare the Diagram.layout:
diagram.layout =
  new go.LayeredDigraphLayout({
      direction: 90,
      layerSpacing: 10,
      isRealtime: false
    });

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Omega", isGroup: true },
  { key: 3, text: "Beta", group: 2 },
  { key: 4, text: "Gamma", group: 2 },
  { key: 5, text: "Epsilon", group: 2 },
  { key: 6, text: "Zeta", group: 2 },
  { key: 7, text: "Delta" }
];
const linkDataArray = [
  { from: 1, to: 2 }, // from a Node to the Group
  { from: 3, to: 4 },  // this link is a member of the Group
  { from: 3, to: 5 },  // this link is a member of the Group
  { from: 4, to: 6 },  // this link is a member of the Group
  { from: 5, to: 6 },  // this link is a member of the Group
  { from: 2, to: 7 }  // from the Group to a Node
];

diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

The default layout for a Group is an instance of [Layout](https://gojs.net/latest/api/symbols/Layout.html), just as it is for [Diagram](https://gojs.net/latest/api/symbols/Diagram.html). So if you do not specify a value for [Group.layout](https://gojs.net/latest/api/symbols/Group.html#layout), the default layout for the group will position all member nodes that do not have a real [Part.location](https://gojs.net/latest/api/symbols/Part.html#location).

If you explicitly set [Group.layout](https://gojs.net/latest/api/symbols/Group.html#layout) to null, the Diagram will be responsible for laying out all of Nodes and Links as if the Group did not exist. This is possible because a subgraph is not another [Diagram](https://gojs.net/latest/api/symbols/Diagram.html).

Collapsing and Expanding Groups
-------------------------------

One common technique to visually simplify a diagram is to hide parts of them by "collapsing" them. In the case of [Group](https://gojs.net/latest/api/symbols/Group.html)s, it may make sense to be able to hide the subgraph.

To collapse a group, set [Group.isSubGraphExpanded](https://gojs.net/latest/api/symbols/Group.html#isSubGraphExpanded) to false; to make sure it is expanded, set that property to true.

It is commonplace to provide a button on a group to allow users to collapse and expand groups as they wish. **GoJS** makes this easy to implement by providing a predefined kind of [Panel](https://gojs.net/latest/api/symbols/Panel.html), named "SubGraphExpanderButton", that acts as a button to collapse and expand [Group](https://gojs.net/latest/api/symbols/Group.html)s. This button changes the visibility of the member nodes and links but does not change the visibility of the group itself. When the group's visual tree includes a [Placeholder](https://gojs.net/latest/api/symbols/Placeholder.html), the placeholder will automatically shrink when the member parts become invisible and will inflate when the member parts become visible again.

Click on the expander button to collapse or expand the group. Changing the size of the group also invalidates the layout that is responsible for positioning the group as a single node. Often the size of the group changes greatly, so a layout usually needs to be performed again.

```
diagram.groupTemplate =
  new go.Group("Auto", {
      // declare the Group.layout:
      layout: new go.LayeredDigraphLayout({
          direction: 0,
          columnSpacing: 10
        })
    })
    .add(
      new go.Shape("RoundedRectangle", {  // surrounds everything
          parameter1: 10, fill: "rgba(128,128,128,0.33)"
        }),
      new go.Panel("Vertical",  // position header above the subgraph
            { defaultAlignment: go.Spot.Left })
        .add(
          new go.Panel("Horizontal",  // the header
              { defaultAlignment: go.Spot.Top })
            .add(
              // the button for the user to expand/collapse the group
              go.GraphObject.build("SubGraphExpanderButton"),
              // group title near top, next to button
              new go.TextBlock({ font: "Bold 12pt Sans-Serif" })
                .bind("text")
            ),
          // represents area for all member parts
          new go.Placeholder({ padding: new go.Margin(0, 10), background: "white" })
        )
    );

// declare the Diagram.layout:
diagram.layout =
  new go.LayeredDigraphLayout({
      direction: 90,
      layerSpacing: 10,
      isRealtime: false
    });

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Omega", isGroup: true },
  { key: 3, text: "Beta", group: 2 },
  { key: 4, text: "Gamma", group: 2 },
  { key: 5, text: "Epsilon", group: 2 },
  { key: 6, text: "Zeta", group: 2 },
  { key: 7, text: "Delta" }
];
const linkDataArray = [
  { from: 1, to: 2 }, // from a Node to the Group
  { from: 3, to: 4 },  // this link is a member of the Group
  { from: 3, to: 5 },  // this link is a member of the Group
  { from: 4, to: 6 },  // this link is a member of the Group
  { from: 5, to: 6 },  // this link is a member of the Group
  { from: 2, to: 7 }  // from the Group to a Node
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

If you do not want a layout to be performed again when the group changes size, you can set the [Part.layoutConditions](https://gojs.net/latest/api/symbols/Part.html#layoutConditions) property to control the circumstances under which the layout will be invalidated.

A [Placeholder](https://gojs.net/latest/api/symbols/Placeholder.html) can be a piece within complex panels. The following example demonstrates a different way to have each Group have a header holding a button and some text.

```
diagram.groupTemplate =
  new go.Group("Auto", { layout: new go.TreeLayout() })
    .add(
      new go.Shape("Rectangle", { fill: "orange", stroke: "darkorange" }),
      new go.Panel("Table", { margin: 0.5 })
        // avoid overlapping border with table contents
        .addRowDefinition(0, { background: "white" })  // header is white
        .add(
          go.GraphObject.build("SubGraphExpanderButton", { row: 0, column: 0, margin: 3 }),
          new go.TextBlock({  // title is centered in header
              row: 0, column: 1, font: "bold 14px Sans-Serif", stroke: "darkorange",
              textAlign: "center", stretch: go.Stretch.Horizontal
            })
            .bind("text"),
          new go.Placeholder({  // becomes zero-sized when Group.isSubGraphExpanded is false
              row: 1, columnSpan: 2, padding: 10, alignment: go.Spot.TopLeft
            })
            .bindObject("padding", "isSubGraphExpanded", exp => exp ? 10 : 0)
        )
    );

diagram.layout =
  new go.TreeLayout({ isRealtime: false });

diagram.model = new go.GraphLinksModel([
    { key: 1, text: "Alpha" },
    { key: 2, text: "GROUP", isGroup: true },
    { key: 3, text: "Beta", group: 2 },
    { key: 4, text: "Gamma", group: 2 },
    { key: 5, text: "Delta" }
  ], [
    { from: 1, to: 3 },
    { from: 3, to: 4 },
    { from: 1, to: 5 }
  ]);
```

Note how when collapsing the group, the link from "Alpha" to "Beta" changes to appear to connect with the Group rather than with the now hidden "Beta" Node.
