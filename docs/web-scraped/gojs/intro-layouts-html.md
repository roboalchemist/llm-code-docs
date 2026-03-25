# Source: https://gojs.net/intro/layouts.html

Title: Layouts

URL Source: https://gojs.net/intro/layouts.html

Markdown Content:
Diagram Layouts
---------------

In general terms, a "layout" is a way of sizing and positioning a collection of objects. HTML has its own layouts for its HTML elements. In **GoJS** you have already seen many examples of Panel layout, such as Auto or Table, which sizes and positions [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s within a [Panel](https://gojs.net/latest/api/symbols/Panel.html). **GoJS** also provides Diagram layouts, which position [Node](https://gojs.net/latest/api/symbols/Node.html)s and route [Link](https://gojs.net/latest/api/symbols/Link.html)s within a [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) or a [Group](https://gojs.net/latest/api/symbols/Group.html).

Naturally the principal purpose of each diagram [Layout](https://gojs.net/latest/api/symbols/Layout.html) is to position nodes, typically by calling [Part.move](https://gojs.net/latest/api/symbols/Part.html#move). But layouts also may also result in custom routing of the links, by setting properties on each [Link](https://gojs.net/latest/api/symbols/Link.html). For example [TreeLayout](https://gojs.net/latest/api/symbols/TreeLayout.html) also ensures that links are routed in the expected direction by setting [Link.fromSpot](https://gojs.net/latest/api/symbols/Link.html#fromSpot) and [Link.toSpot](https://gojs.net/latest/api/symbols/Link.html#toSpot) depending on the [TreeLayout.angle](https://gojs.net/latest/api/symbols/TreeLayout.html#angle). (However, that behavior can be disabled by setting [TreeLayout.setsPortSpot](https://gojs.net/latest/api/symbols/TreeLayout.html#setsPortSpot) and [TreeLayout.setsChildPortSpot](https://gojs.net/latest/api/symbols/TreeLayout.html#setsChildPortSpot). The same is true for some other layouts.)

Diagram layouts can be accomplished in several manners. Manual layouts occur because the user moves nodes, thereby establishing new positions for those nodes. Such layouts might be saved in some persistent data format and later loaded using data binding or assignments in code. Programmatic layouts happen when some code executes to set the [Part](https://gojs.net/latest/api/symbols/Part.html) position or location. Automatic layouts are programmatic layouts that are implemented by the [Layout](https://gojs.net/latest/api/symbols/Layout.html) class or its subclasses.

Default Layout
--------------

The value of [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) defaults to an instance of [Layout](https://gojs.net/latest/api/symbols/Layout.html). This kind of layout is unlike all of the other layout subclasses, in that it only sets the position of nodes that do not already have a position -- i.e. where the X or Y of the [GraphObject.actualBounds](https://gojs.net/latest/api/symbols/GraphObject.html#actualBounds) is NaN. It leaves unmodified all nodes that do have a defined position, and it ignores all links.

The default layout is used in apps where the user is expected to position each Node, perhaps with the aid of grid-snapping or with a tool. Many of the examples you have seen so far do not set [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) and thus use the default layout. Some of the examples data bind the [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) or [GraphObject.position](https://gojs.net/latest/api/symbols/GraphObject.html#position) to a data property. Those examples are basically using manual layout, but with the node positions coming from the node data rather than from arrangement by the user.

Often such apps are diagram editors, where the user places and adjusts the locations of nodes, and those locations are saved in the server. Such bindings are usually TwoWay, in order to automatically save the node locations to the model data.

However many of the examples just allow the standard behavior of a [Layout](https://gojs.net/latest/api/symbols/Layout.html) class or subclass to assign positions to the nodes in the order in which they are seen by the layout and considering any link relationships between the nodes. Those examples are exhibiting automatic layout behavior.

Automatic Layouts
-----------------

**GoJS** offers several kinds of built-in automatic layouts, including:

*   [GridLayout](https://gojs.net/latest/api/symbols/GridLayout.html)
*   [TreeLayout](https://gojs.net/latest/api/symbols/TreeLayout.html)
*   [ForceDirectedLayout](https://gojs.net/latest/api/symbols/ForceDirectedLayout.html)
*   [LayeredDigraphLayout](https://gojs.net/latest/api/symbols/LayeredDigraphLayout.html)
*   [CircularLayout](https://gojs.net/latest/api/symbols/CircularLayout.html)

There are samples for each of these layouts, demonstrating the effects of setting various detailed layout properties. Many of the properties are very specific to the particular kind of layout that they are trying to affect.

*   [GridLayout Sample](https://gojs.net/latest/samples/gLayout.html)
*   [TreeLayout Sample](https://gojs.net/latest/samples/tLayout.html)
*   [ForceDirectedLayout Sample](https://gojs.net/latest/samples/fdLayout.html)
*   [LayeredDigraphLayout Sample](https://gojs.net/latest/samples/ldLayout.html)
*   [CircularLayout Sample](https://gojs.net/latest/samples/cLayout.html)

In the introduction pages and samples you will see many examples that make use of automatic layout by setting the [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) property.

### Layout Usage

You can set [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) in a JavaScript statement:

`diagram.layout = new go.ForceDirectedLayout();`
or:

```
const diagram =
  new go.Diagram("myDiagramDiv",
    {
      layout: new go.TreeLayout({ angle: 90, nodeSpacing: 10, layerSpacing: 30 })
    });
```

### Grid Layout

A simple layout for placing Nodes in a grid-like arrangement.

See the [GridLayout Sample](https://gojs.net/latest/samples/gLayout.html) for a demonstration of layout options. The [Swim Lanes](https://gojs.net/latest/samples/swimLanes.html) sample demonstrates a customization of [GridLayout](https://gojs.net/latest/api/symbols/GridLayout.html). See more samples that make use of [GridLayout](https://gojs.net/latest/api/symbols/GridLayout.html) in the [samples index](https://gojs.net/latest/samples/index.html#gridlayout).

### Tree Layout

This layout positions nodes of a tree-structured graph in layers, either rows or columns depending on the [TreeLayout.angle](https://gojs.net/latest/api/symbols/TreeLayout.html#angle).

See the [TreeLayout sample](https://gojs.net/latest/samples/tLayout.html) for a demonstration of layout options. The [Org Chart Editor](https://gojs.net/latest/samples/orgChartEditor.html), [Parse Tree](https://gojs.net/latest/samples/parseTree.html), [Layer Bands](https://gojs.net/latest/samples/swimBands.html), and [Virtualized Tree](https://gojs.net/latest/samples/virtualizedTreeLayout.html) samples demonstrate customization of [TreeLayout](https://gojs.net/latest/api/symbols/TreeLayout.html). See more samples that make use of [TreeLayout](https://gojs.net/latest/api/symbols/TreeLayout.html) in the [samples index](https://gojs.net/latest/samples/index.html#treelayout).

### Force-Directed Layout

Force-directed layout treats the graph as if it were a system of physical bodies with forces acting on them and between them.

See the [ForceDirectedLayout sample](https://gojs.net/latest/samples/fdLayout.html) for a demonstration of layout options. That sample also demonstrates a simple customization of [ForceDirectedLayout](https://gojs.net/latest/api/symbols/ForceDirectedLayout.html). The [Virtualized Force Directed](https://gojs.net/latest/samples/virtualizedForceLayout.html) sample demonstrates a more complicated customization of [ForceDirectedLayout](https://gojs.net/latest/api/symbols/ForceDirectedLayout.html). See more samples that make use of [ForceDirectedLayout](https://gojs.net/latest/api/symbols/ForceDirectedLayout.html) in the [samples index](https://gojs.net/latest/samples/index.html#forcedirectedlayout).

### Layered Digraph Layout

This arranges nodes of directed graphs into layers, rows or columns depending on the [LayeredDigraphLayout.direction](https://gojs.net/latest/api/symbols/LayeredDigraphLayout.html#direction). Unlike [TreeLayout](https://gojs.net/latest/api/symbols/TreeLayout.html), this works not only with tree-structured graphs, but with any graph, although it's best with directed acyclic graphs.

See the [LayeredDigraphLayout sample](https://gojs.net/latest/samples/ldLayout.html) for a demonstration of layout options. The [Genogram](https://gojs.net/latest/samples/genogram.html) sample demonstrates a complex customization of [LayeredDigraphLayout](https://gojs.net/latest/api/symbols/LayeredDigraphLayout.html). See more samples that make use of [LayeredDigraphLayout](https://gojs.net/latest/api/symbols/LayeredDigraphLayout.html) in the [samples index](https://gojs.net/latest/samples/index.html#layereddigraphlayout).

### Circular Layout

This layout positions nodes in a circular or elliptical arrangement.

See the [CircularLayout sample](https://gojs.net/latest/samples/cLayout.html) for a demonstration of layout options. The [Friend Wheel](https://gojs.net/latest/samples/friendWheel.html) sample demonstrates a simple customization of [CircularLayout](https://gojs.net/latest/api/symbols/CircularLayout.html). See more samples that make use of [CircularLayout](https://gojs.net/latest/api/symbols/CircularLayout.html) in the [samples index](https://gojs.net/latest/samples/index.html#circularlayout).

### Custom Layouts

GoJS encourages creation of custom layouts. The intro page on [GoJS extensions](https://gojs.net/latest/intro/extensions.html) gives a simple example of a custom layout. See more samples that make use of custom layouts in the [samples index](https://gojs.net/latest/samples/index.html#customlayout).

There are also many layouts that are extensions -- not predefined in the `go.js` or `go-debug.js` library, but available as source code in one of the three extension directories, with some documentation, and with corresponding samples.

*   [ArrangingLayout](https://gojs.net/latest/api/symbols/ArrangingLayout.html): sample at [ArrangingLayout Sample](https://gojs.net/latest/samples/Arranging.html), defined in [ArrangingLayout.js](https://gojs.net/latest/extensions/ArrangingLayout.js)
*   [DoubleTreeLayout](https://gojs.net/latest/api/symbols/DoubleTreeLayout.html): sample at [DoubleTreeLayout Sample](https://gojs.net/latest/samples/doubleTree.html), defined in [DoubleTreeLayout.js](https://gojs.net/latest/extensions/DoubleTreeLayout.js)
*   [FishboneLayout](https://gojs.net/latest/api/symbols/FishboneLayout.html): sample at [FishboneLayout Sample](https://gojs.net/latest/samples/Fishbone.html), defined in [FishboneLayout.js](https://gojs.net/latest/extensions/FishboneLayout.js)
*   [PackedLayout](https://gojs.net/latest/api/symbols/PackedLayout.html): sample at [PackedLayout Sample](https://gojs.net/latest/samples/PackedLayout.html), defined in [PackedLayout.js](https://gojs.net/latest/extensionsJSM/PackedLayout.js)
*   [ParallelLayout](https://gojs.net/latest/api/symbols/ParallelLayout.html): sample at [ParallelLayout Sample](https://gojs.net/latest/samples/Parallel.html), defined in [ParallelLayout.js](https://gojs.net/latest/extensions/ParallelLayout.js)
*   [SerpentineLayout](https://gojs.net/latest/api/symbols/SerpentineLayout.html): sample at [SerpentineLayout Sample](https://gojs.net/latest/samples/Serpentine.html), defined in [SerpentineLayout.js](https://gojs.net/latest/extensions/SerpentineLayout.js)
*   [SpiralLayout](https://gojs.net/latest/api/symbols/SpiralLayout.html): sample at [SpiralLayout Sample](https://gojs.net/latest/samples/Spiral.html), defined in [SpiralLayout.js](https://gojs.net/latest/extensions/SpiralLayout.js)
*   [SwimLaneLayout](https://gojs.net/latest/api/symbols/SwimLaneLayout.html): sample at [SwimLaneLayout Sample](https://gojs.net/latest/samples/SwimLaneLayout.html), defined in [SwimLaneLayout.js](https://gojs.net/latest/extensions/SwimLaneLayout.js)
*   [TableLayout](https://gojs.net/latest/api/symbols/TableLayout.html): sample at [TableLayout Sample](https://gojs.net/latest/samples/Table.html), defined in [TableLayout.js](https://gojs.net/latest/extensions/TableLayout.js)
*   [TreeMapLayout](https://gojs.net/latest/api/symbols/TreeMapLayout.html): sample at [TreeMapLayout Sample](https://gojs.net/latest/samples/TreeMap.html), defined in [TreeMapLayout.js](https://gojs.net/latest/extensions/TreeMapLayout.js)

Layout Invalidation
-------------------

A layout is considered "valid" when it has performed its positioning of its nodes and perhaps routed its links. However some kinds of changes cause a layout to become "invalid", thereby causing it to be performed again in the near future. Because layouts can be computationally expensive, automatic layouts are not performed as soon as a layout is invalidated. Instead they are typically performed at the end of a transaction.

The most common reasons for a layout to be invalidated are because a node or a link has been added or removed from the collection of nodes and links that a layout is responsible for, or because a node or a link has changed visibility, or because a node has changed size. If you do not want an automatic layout to happen when such a change occurs, it may be easiest to set [Layout.isOngoing](https://gojs.net/latest/api/symbols/Layout.html#isOngoing) to false.

Another common situation is where you have set [Diagram.layout](https://gojs.net/latest/api/symbols/Diagram.html#layout) to some kind of layout but you want to load a diagram (model) that contains manually positioned or adjusted node locations. The [Binding](https://gojs.net/latest/api/symbols/Binding.html) of [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) to the model data is effective, but the locations are lost when a layout is performed immediately after loading. This situation can be avoided by setting [Layout.isInitial](https://gojs.net/latest/api/symbols/Layout.html#isInitial) to false. After the initial layout the layout might still be invalidated by adding or removing or changing the visibility of a node or a link or by a change in node size, unless you have also set [Layout.isOngoing](https://gojs.net/latest/api/symbols/Layout.html#isOngoing) to false. When both [Layout.isInitial](https://gojs.net/latest/api/symbols/Layout.html#isInitial) and [Layout.isOngoing](https://gojs.net/latest/api/symbols/Layout.html#isOngoing) are false, you can still explicitly cause a layout to happen by either calling [Layout.invalidateLayout](https://gojs.net/latest/api/symbols/Layout.html#invalidateLayout) or by calling [Diagram.layoutDiagram](https://gojs.net/latest/api/symbols/Diagram.html#layoutDiagram) with a `true` argument.

For example, in diagram editors it is commonplace to have TwoWay Bindings on [Node.location](https://gojs.net/latest/api/symbols/Node.html#location) to save manually adjusted node locations. This means that saved models will have saved locations for all of the nodes. But if you create a new model without all of the node data objects having real locations, you will want a layout to be performed initially when the model is loaded. You can accomplish this by setting [Layout.isInitial](https://gojs.net/latest/api/symbols/Layout.html#isInitial) to false (and optionally [Layout.isOngoing](https://gojs.net/latest/api/symbols/Layout.html#isOngoing) to false, if that is what you want when users add or remove nodes or links) and then implementing an "InitialLayoutCompleted" [DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html) listener that decides whether a layout is needed. The decision could be to look at a flag that you add to the [Model.modelData](https://gojs.net/latest/api/symbols/Model.html#modelData). Or you could look at all of the nodes to make sure their locations have real values:

```
new go.Diagram(. . .,
  {
    . . .,
    layout: new go.TreeLayout({ isInitial: false, isOngoing: false }, . . .),
    "InitialLayoutCompleted": e => {
      // if not all Nodes have real locations, force a layout to happen
      if (!e.diagram.nodes.all(n => n.location.isReal())) {
        e.diagram.layoutDiagram(true);
      }
    }
  })
```

But if you do not want a change to a particular Node or Link to cause an automatic layout, yet you do want that invalidation for other Nodes or Links, you can set the [Part.layoutConditions](https://gojs.net/latest/api/symbols/Part.html#layoutConditions) property to the combination of [Part](https://gojs.net/latest/api/symbols/Part.html) "Layout..." flags that suits your needs. It is most common to not want a layout for the [LayoutConditions.NodeSized](https://gojs.net/latest/api/symbols/LayoutConditions.html#NodeSized) condition:

```
new go.Node(. . ., {
    layoutConditions: go.LayoutConditions.Standard & ~go.LayoutConditions.NodeSized,
    . . .
  })
  . . .
```

Parts that remain not visible or that are in layers that are [Layer.isTemporary](https://gojs.net/latest/api/symbols/Layer.html#isTemporary) also never invalidate any Layout.

Finally, you can set [Part.isLayoutPositioned](https://gojs.net/latest/api/symbols/Part.html#isLayoutPositioned) to false in order for the Layout to completely ignore that Part. But you will have to make sure that that Part does have a real [Part.location](https://gojs.net/latest/api/symbols/Part.html#location), since no layout will set it for you. Without a real location the part will not be visible anywhere in the diagram. Furthermore if a node has **isLayoutPositioned** set to false, Layouts will not only ignore that node but also all links connecting with that node. Because the node will not be moved by the layout, it might overlap with the laid-out nodes and links. You can also set or bind [Part.isLayoutPositioned](https://gojs.net/latest/api/symbols/Part.html#isLayoutPositioned) to false on Links in order to have the layout ignore those links. This is demonstrated in [Org Chart Extras](https://gojs.net/latest/samples/orgChartExtras.html).
