# Source: https://gojs.net/intro/dataBinding.html

Title: Data Binding

URL Source: https://gojs.net/intro/dataBinding.html

Markdown Content:
Data binding is a way to extract a value from a source object and set a property on a target object. The target objects are normally [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s; the source objects are usually JavaScript data objects held in a [Model](https://gojs.net/latest/api/symbols/Model.html).

You could write code that gets a desired value from the model data, searches the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) for the appropriate [Part](https://gojs.net/latest/api/symbols/Part.html), searches for the target [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) within the visual tree of that Part, and then sets one or more properties on that GraphObject with that value, perhaps after modifying or converting the original value in a way appropriate for the individual properties. However data binding offers a declarative way to specify such behavior just by supplying a [Binding](https://gojs.net/latest/api/symbols/Binding.html) that names the properties on the source object and on the target object.

Data bindings are used to keep [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) properties in sync with their [Part](https://gojs.net/latest/api/symbols/Part.html)'s data's properties. They are not used to establish or maintain relationships between Parts. Each kind of [Model](https://gojs.net/latest/api/symbols/Model.html) has its own methods for declaring the relationships between parts.

Trying to bind a non-existent property of a [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) will probably result in a warning or error that you can see in the console log. Always check the console log for any kinds of potential exceptions that are normally suppressed by the binding system.

The Relationships of Parts and Data and Binding
-----------------------------------------------

First, look at a diagram that includes comments about the GraphObjects used to build some example nodes and links:

The two [Node](https://gojs.net/latest/api/symbols/Node.html)s and one [Link](https://gojs.net/latest/api/symbols/Link.html) belong to the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) and are on the left side, with shadows. The [TreeModel](https://gojs.net/latest/api/symbols/TreeModel.html) and the two data objects in its [Model.nodeDataArray](https://gojs.net/latest/api/symbols/Model.html#nodeDataArray) are on the right side, in gray.

Each [Node](https://gojs.net/latest/api/symbols/Node.html) and [Link](https://gojs.net/latest/api/symbols/Link.html) has a [Panel.data](https://gojs.net/latest/api/symbols/Panel.html#data) property that references the data object in the model. Thus it is easy, given a Node, to refer to all of the data properties that you have put on the data in the model. These references are drawn as gray links.

Each [Node](https://gojs.net/latest/api/symbols/Node.html) also has three [Binding](https://gojs.net/latest/api/symbols/Binding.html)s, drawn with dashed green lines from the data to the GraphObject:

*   to the [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) property from the `data.location` property
*   to the [Shape.fill](https://gojs.net/latest/api/symbols/Shape.html#fill) property from the `data.color` property
*   to the [TextBlock.text](https://gojs.net/latest/api/symbols/TextBlock.html#text) property from the `data.text` property

The use of templates and data binding greatly simplify the information that must be stored in model data, and allow great flexibility in representing nodes and links in various manners independent of the model data. But not all data properties need to be used in Bindings in the template.

Note that [Binding](https://gojs.net/latest/api/symbols/Binding.html)s are _not_ references from the data to any [Part](https://gojs.net/latest/api/symbols/Part.html). The whole point of separating models from diagrams is to avoid references from data to Diagrams or Nodes or Links or Tools. The only references from diagram to model are the [Diagram.model](https://gojs.net/latest/api/symbols/Diagram.html#model) property and each node or link's [Panel.data](https://gojs.net/latest/api/symbols/Panel.html#data) property.

### Item Arrays, Model Data, and Panels

Here's another diagram showing the relationships of data Objects in the model with GraphObjects (Node, Panel, TextBlock, Picture) in the Diagram. The Node is data bound to an Object in the [Model.nodeDataArray](https://gojs.net/latest/api/symbols/Model.html#nodeDataArray) that has several properties, including one named "items" which is an Array. One of the Panels in the Node has a data binding of the [Panel.itemArray](https://gojs.net/latest/api/symbols/Panel.html#itemArray) property with the source property name being "items".

That Array has four Objects in it, each Object having "image" and "name" properties. The [Panel.itemTemplate](https://gojs.net/latest/api/symbols/Panel.html#itemTemplate) of the Panel whose [Panel.itemArray](https://gojs.net/latest/api/symbols/Panel.html#itemArray) is bound to that Array is defined so as to show a Panel with a RoundedRectangle Shape surrounding a Vertical Panel showing Picture over a TextBlock.

The green dashed links show how a Binding transfers the property value from the data Object to the Picture or TextBlock in the Node.

Binding string and number properties
------------------------------------

It is easy to data bind [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) properties to data properties. In this example we not only data bind [TextBlock.text](https://gojs.net/latest/api/symbols/TextBlock.html#text) and [Shape.fill](https://gojs.net/latest/api/symbols/Shape.html#fill) in nodes to property values of node data, but for thicker colored lines we also bind [Shape.stroke](https://gojs.net/latest/api/symbols/Shape.html#stroke) and [Shape.strokeWidth](https://gojs.net/latest/api/symbols/Shape.html#strokeWidth) in links to property values of link data.

All you need to do is add to the target [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) a new [Binding](https://gojs.net/latest/api/symbols/Binding.html) that names the target property on the visual object and the source property on the data object. Of course the target property must be a settable property; some GraphObject properties are not settable. If you specify a target property name that does not exist you will get warning messages in the console. If the source property value is undefined, the binding is not evaluated.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("RoundedRectangle", { fill: "white" })
        .bind("fill", "color"),  // shape.fill = data.color
      new go.TextBlock({ margin: 5 })
        .bind("text")  // textblock.text = data.key
    );

diagram.linkTemplate =
  new go.Link()
    .add(
      new go.Shape()
        .bind("stroke", "color")  // shape.stroke = data.color
        .bind("strokeWidth", "thick"),  // shape.strokeWidth = data.thick
      new go.Shape({ toArrow: "OpenTriangle", fill: null })
        .bind("stroke", "color")  // shape.stroke = data.color
        .bind("strokeWidth", "thick")  // shape.strokeWidth = data.thick
    );

const nodeDataArray = [
  { key: 1, text: "Alpha", color: "lightblue" },
  { key: 2, text: "Beta", color: "pink" }
];
const linkDataArray = [
  { from: 1, to: 2, color: "blue", thick: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

Note that the link template uses two bindings of the source "color" property. There is one for each target [Shape](https://gojs.net/latest/api/symbols/Shape.html) in the [Link](https://gojs.net/latest/api/symbols/Link.html) template; each binds the [Shape.stroke](https://gojs.net/latest/api/symbols/Shape.html#stroke) property, although they could target other properties.

Alternatively, using [GraphObject.make](https://gojs.net/latest/api/symbols/GraphObject.html#make):

```
diagram.nodeTemplate =
  $(go.Node, "Auto",
    $(go.Shape, "RoundedRectangle",
      { fill: "white" },
      new go.Binding("fill", "color")),  // shape.fill = data.color
    $(go.TextBlock,
      { margin: 5 },
      new go.Binding("text"))  // textblock.text = data.text
  );

diagram.linkTemplate =
  $(go.Link,
    $(go.Shape,
      new go.Binding("stroke", "color"),  // shape.stroke = data.color
      new go.Binding("strokeWidth", "thick")),  // shape.strokeWidth = data.thick
    $(go.Shape,
      { toArrow: "OpenTriangle", fill: null },
      new go.Binding("stroke", "color"),  // shape.stroke = data.color
      new go.Binding("strokeWidth", "thick"))  // shape.strokeWidth = data.thick
  );
```

Binding object properties such as **Part.location**
---------------------------------------------------

You can also data bind properties that have values that are objects. For example it is common to data bind the [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) property.

The value of [Part.location](https://gojs.net/latest/api/symbols/Part.html#location) is of type [Point](https://gojs.net/latest/api/symbols/Point.html), so in this example the data property value must be an instance of Point.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc")  // get the Node.location from the data.loc value
    .add(
      new go.Shape("RoundedRectangle", { fill: "white" })
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  // for each node specify the location using Point values
  { key: 1, text: "Alpha", color: "lightblue", loc: new go.Point(0, 0) },
  { key: 2, text: "Beta", color: "pink", loc: new go.Point(100, 50) }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

For conciseness the rest of these examples make use of the default [Diagram.linkTemplate](https://gojs.net/latest/api/symbols/Diagram.html#linkTemplate).

Conversion functions
--------------------

But what if you want the data property value for the location to be something other than a [Point](https://gojs.net/latest/api/symbols/Point.html)? You can provide a conversion function that converts the actual data property value to the needed value type or format.

For situations like this example, the [Point](https://gojs.net/latest/api/symbols/Point.html) class includes a static function, [Point.parse](https://gojs.net/latest/api/symbols/Point.html#parse), that you can use to convert a string into a Point object. It expects two numbers to be in the input string, representing the [Point.x](https://gojs.net/latest/api/symbols/Point.html#x) and [Point.y](https://gojs.net/latest/api/symbols/Point.html#y) values. It returns a Point object with those values.

You can pass a conversion function as the third argument to the [Binding](https://gojs.net/latest/api/symbols/Binding.html) constructor. In this case it is [Point.parse](https://gojs.net/latest/api/symbols/Point.html#parse). This allows the location to be specified in the form of a string ("100 50") rather than as an expression that returns a [Point](https://gojs.net/latest/api/symbols/Point.html). For data properties on model objects, you will often want to use strings as the representation of [Point](https://gojs.net/latest/api/symbols/Point.html)s, [Size](https://gojs.net/latest/api/symbols/Size.html)s, [Rect](https://gojs.net/latest/api/symbols/Rect.html)s, [Margin](https://gojs.net/latest/api/symbols/Margin.html)s, and [Spot](https://gojs.net/latest/api/symbols/Spot.html)s, rather than references to objects of those classes. Strings are easily read and written in JSON and XML. Trying to read/write classes of objects would take extra space and would require additional cooperation on the part of both the writer and the reader.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc", go.Point.parse)  // convert string into a Point value
    .add(
      new go.Shape("RoundedRectangle", { fill: "white" })
        .bind("fill", "color"),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  { key: 1, text: "Alpha", color: "lightblue", loc: "0 0" },  // note string values for location
  { key: 2, text: "Beta", color: "pink", loc: "100 50" }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

Conversion functions can be named or anonymous functions. They take a data property value and return a value suitable for the property that is being set. They should not have any side-effects. They may get called any number of times in any order.

Here is an example that has several [Shape](https://gojs.net/latest/api/symbols/Shape.html) properties data-bound to the same boolean data property named "highlight". Each conversion function takes the boolean value and returns the appropriate value for the property that is data-bound. This makes it trivial to control the appearance of each node from the data by setting the "highlight" data property to be either false or true.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .bind("location", "loc", go.Point.parse)
    .add(
      new go.Shape("RoundedRectangle",
          { // default values if the data.highlight is undefined:
            fill: "yellow", stroke: "orange", strokeWidth: 2 })
        .bind("fill", "highlight", v => v ? "pink" : "lightblue")
        .bind("stroke", "highlight", v => v ? "red" : "blue")
        .bind("strokeWidth", "highlight", v => v ? 3 : 1),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  { key: 1, text: "Alpha", loc: "0 0", highlight: false },
  { key: 2, text: "Beta", loc: "100 50", highlight: true },
  { key: 3, text: "Gamma", loc: "0 100" }  // highlight property undefined: use defaults
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
```

Note that a conversion function can only return property values. You cannot return GraphObjects to replace objects in the visual tree of the Part. If you need to show different GraphObjects based on bound data, you can bind the [GraphObject.visible](https://gojs.net/latest/api/symbols/GraphObject.html#visible) or the [GraphObject.opacity](https://gojs.net/latest/api/symbols/GraphObject.html#opacity) property. If you really want different visual structures you can use multiple templates (see [Template Maps](https://gojs.net/latest/intro/templateMaps.html)).

Changing data values
--------------------

The examples above all depend on the data bindings being evaluated when the [Part](https://gojs.net/latest/api/symbols/Part.html) has been created and its [Panel.data](https://gojs.net/latest/api/symbols/Panel.html#data) property is set to refer to the corresponding node or link data. These actions occur automatically when the [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) creates diagram parts for the data in the model upon setting [Diagram.model](https://gojs.net/latest/api/symbols/Diagram.html#model).

However, **GoJS** cannot know when the data property of an arbitrary JavaScript object has been modified. If you want to change some data object in a model and have the diagram be automatically updated, what you should do depends on the nature of the property that you are changing.

For most data properties, ones that the model does not treat specially but are data-bound, you can just call [Model.set](https://gojs.net/latest/api/symbols/Model.html#set). In this example we modify the value of "highlight" on a node data object. For fun, this modification occurs about twice a second.

```
diagram.nodeTemplate =
  new go.Node("Auto", { locationSpot: go.Spot.Center })
    .add(
      new go.Shape("RoundedRectangle",
                   { // default values if the data.highlight is undefined:
                     fill: "yellow", stroke: "orange", strokeWidth: 2 })
        .bind("fill", "highlight", v => v ? "pink" : "lightblue")
        .bind("stroke", "highlight", v => v ? "red" : "blue")
        .bind("strokeWidth", "highlight", v => v ? 3 : 1),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.model.nodeDataArray = [
  { text: "Alpha", highlight: false }  // just one node, and no links
];

function flash() {
  // all model changes should happen in a transaction
  diagram.model.commit(m => {
    const data = m.nodeDataArray[0];  // get the first node data
    m.set(data, "highlight", !data.highlight);
  }, "flash");
}
function loop() {
  setTimeout(() => { flash(); loop(); }, 500);
}
loop();
```

Alternatively, using [GraphObject.make](https://gojs.net/latest/api/symbols/GraphObject.html#make):

```
diagram.nodeTemplate =
  $(go.Node, "Auto",
    { locationSpot: go.Spot.Center },
    $(go.Shape, "RoundedRectangle",
      { // default values if the data.highlight is undefined:
        fill: "yellow", stroke: "orange", strokeWidth: 2 },
      new go.Binding("fill", "highlight", v => v ? "pink" : "lightblue"),
      new go.Binding("stroke", "highlight", v => v ? "red" : "blue"),
      new go.Binding("strokeWidth", "highlight", v => v ? 3 : 1)),
    $(go.TextBlock,
      { margin: 5 },
      new go.Binding("text"))
  );
```

Changing graph structure
------------------------

Data binding is not used to establish relationships between parts. For data properties that a particular model knows about, such as "to" or "from" for link data in a [GraphLinksModel](https://gojs.net/latest/api/symbols/GraphLinksModel.html), you must call the appropriate model methods in order to modify the data property. Modifying a data property directly without calling the appropriate model method may cause inconsistencies or undefined behavior.

For node data, the model methods are [Model.setCategoryForNodeData](https://gojs.net/latest/api/symbols/Model.html#setCategoryForNodeData), [Model.setKeyForNodeData](https://gojs.net/latest/api/symbols/Model.html#setKeyForNodeData), [GraphLinksModel.setGroupKeyForNodeData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setGroupKeyForNodeData), [TreeModel.setParentKeyForNodeData](https://gojs.net/latest/api/symbols/TreeModel.html#setParentKeyForNodeData), and [TreeModel.setParentLinkCategoryForNodeData](https://gojs.net/latest/api/symbols/TreeModel.html#setParentLinkCategoryForNodeData). For link data, the model methods are [GraphLinksModel.setCategoryForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setCategoryForLinkData), [GraphLinksModel.setFromKeyForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setFromKeyForLinkData), [GraphLinksModel.setFromPortIdForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setFromPortIdForLinkData), [GraphLinksModel.setToKeyForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setToKeyForLinkData), [GraphLinksModel.setToPortIdForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setToPortIdForLinkData), and [GraphLinksModel.setLabelKeysForLinkData](https://gojs.net/latest/api/symbols/GraphLinksModel.html#setLabelKeysForLinkData).

This example changes the "to" property of a link data, causing the link to connect to a different node. This example uses the default Link template, which does not have any relevant data bindings. The change in the link relationship is accomplished by calling a model method, not via a data binding.

```
diagram.nodeTemplate =
  new go.Node("Auto", { locationSpot: go.Spot.Center })
    .add(
      new go.Shape("RoundedRectangle",
                   { fill: "yellow", stroke: "orange", strokeWidth: 2 }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta" },
  { key: 3, text: "Gamma" }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);

function switchTo() {
  // all model changes should happen in a transaction
  diagram.model.commit(m => {
    const data = m.linkDataArray[0];  // get the first link data
    if (m.getToKeyForLinkData(data) === 2)
      m.setToKeyForLinkData(data, 3);
    else
      m.setToKeyForLinkData(data, 2);
  }, "reconnect link");
}
function loop() {
  setTimeout(() => { switchTo(); loop(); }, 1000);
}
loop();
```

Binding to **GraphObject** sources
----------------------------------

The binding source object need not be a plain JavaScript data object held in the diagram's model. The source object may instead be the same [Part](https://gojs.net/latest/api/symbols/Part.html) or a named [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) in the same [Part](https://gojs.net/latest/api/symbols/Part.html). The source property must be a settable property of the class. The binding is evaluated when the property is set to a new value.

One common use of such a binding is to change the appearance of a Part when the [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected). Call [Binding.ofObject](https://gojs.net/latest/api/symbols/Binding.html#ofObject) to cause the Binding to use the object whose [GraphObject.name](https://gojs.net/latest/api/symbols/GraphObject.html#name) is the given name. Use the empty string, "", or no argument, to refer to the whole Part itself. This is a convenience so that you do not need to name the whole Part. "ofObject" really means "of the GraphObject named ...", as found by [Panel.findObject](https://gojs.net/latest/api/symbols/Panel.html#findObject) when there is a string argument.

In the example below, the [Shape.fill](https://gojs.net/latest/api/symbols/Shape.html#fill) is bound to the [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) property. When the node is selected or de-selected, the [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected) property changes value, so the binding is evaluated. The conversion function gets a boolean value and returns the desired brush color to be used as the shape's fill. This example also turns off selection adornments, so that the only visual way to tell that a node is selected is by the shape's fill color.

```
diagram.nodeTemplate =
  new go.Node("Auto",
              { selectionAdorned: false })  // no blue selection handle!
    .add(
      new go.Shape("RoundedRectangle")
        // bind Shape.fill to Node.isSelected converted to a color
        // no 5th argument source element name means bind to the whole Part
        .bindObject("fill", "isSelected", sel => sel ? "dodgerblue" : "lightgray"),
      new go.TextBlock({ margin: 5 })
        .bind("text", "descr")
    );

diagram.model.nodeDataArray = [
  { descr: "Select me!" },
  { descr: "I turn blue when selected." }
];
```

Alternatively, using [GraphObject.make](https://gojs.net/latest/api/symbols/GraphObject.html#make):

```
diagram.nodeTemplate =
  $(go.Node, "Auto",
    { selectionAdorned: false },  // no blue selection handle!
    $(go.Shape, "RoundedRectangle",
      // bind Shape.fill to Node.isSelected converted to a color
      new go.Binding("fill", "isSelected", sel => sel ? "dodgerblue" : "lightgray")
        .ofObject()),  // no source element name means bind to the whole Part
    $(go.TextBlock,
      { margin: 5 },
      new go.Binding("text", "descr"))
  );
```

Caution: do not declare cycles of binding dependencies -- that will result in undefined behavior. [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) binding sources also require the [Part](https://gojs.net/latest/api/symbols/Part.html) to be bound to data (i.e. [Part.data](https://gojs.net/latest/api/symbols/Part.html#data) must be non-null). The property on the GraphObject must be settable, so it does not work on read-only properties such as ones that return computed values (e.g. [Part.isTopLevel](https://gojs.net/latest/api/symbols/Part.html#isTopLevel)) or Iterators (e.g. [Node.linksConnected](https://gojs.net/latest/api/symbols/Node.html#linksConnected)).

Binding to the shared **Model.modelData** source
------------------------------------------------

The binding source object may be a third kind of source, besides the [Panel.data](https://gojs.net/latest/api/symbols/Panel.html#data) or some [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) within the panel. It can also be the JavaScript Object that is the shared [Model.modelData](https://gojs.net/latest/api/symbols/Model.html#modelData) object. This permits binding of Node or Link element properties to shared properties in the model that will exist and may be modified even though no nodes or links exist in the model.

In the example below, the [Shape.fill](https://gojs.net/latest/api/symbols/Shape.html#fill) is bound to the "color" property on the [Model.modelData](https://gojs.net/latest/api/symbols/Model.html#modelData) object. As you click the button the `changeColor` function modifies the `modelData` object by calling [Model.setDataProperty](https://gojs.net/latest/api/symbols/Model.html#setDataProperty).

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("RoundedRectangle",
                   { fill: "white" })  // the default value if there is no modelData.color property
        .bindModel("fill", "color"),   // meaning a property of Model.modelData
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

// start all nodes yellow
diagram.model.modelData.color = "yellow";

diagram.model.nodeDataArray = [
  { text: "Alpha" },
  { text: "Beta" }
];

diagram.undoManager.isEnabled = true;

changeColor = () => {  // define a function named "changeColor" callable by button.onclick
  diagram.model.commit(m => {
    // alternate between lightblue and lightgreen colors
    const oldcolor = m.modelData.color;
    const newcolor = (oldcolor === "lightblue" ? "lightgreen" : "lightblue");
    m.set(m.modelData, "color", newcolor);
  }, "changed shared color");
}
```

Alternatively, using [GraphObject.make](https://gojs.net/latest/api/symbols/GraphObject.html#make):

```
diagram.nodeTemplate =
  $(go.Node, "Auto",
    $(go.Shape, "RoundedRectangle",
      { fill: "white" },  // the default value if there is no modelData.color property
      new go.Binding("fill", "color").ofModel()),  // meaning a property of Model.modelData
    $(go.TextBlock,
      { margin: 5 },
      new go.Binding("text"))
  );
```

Two-way data binding
--------------------

All of the bindings above only transfer values from the source data to target properties. But sometimes you would like to be able to transfer values from [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html)s back to the model data, to keep the model data up-to-date with the diagram. This is possible by using a TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html), which can pass values not only from source to target, but also from the target object back to the source data.

```
diagram.nodeTemplate =
  new go.Node("Auto", { locationSpot: go.Spot.Center })
    .bindTwoWay("location", "loc")  // the data value must be an instance of Point
    .add(
      new go.Shape("RoundedRectangle", { fill: "lightblue", stroke: "blue", strokeWidth: 2 }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

const nodeDataArray = [
  { text: "Alpha", loc: new go.Point(0, 0) }
];
diagram.model = new go.GraphLinksModel(nodeDataArray);

window.shiftNode = () => {  // define a function named "shiftNode" callable by button.onclick
  // all model changes should happen in a transaction
  diagram.commit(d => {
    const data = d.model.nodeDataArray[0];  // get the first node data
    const node = d.findNodeForData(data);   // find the corresponding Node
    const p = node.location.copy();  // make a copy of the location, a Point
    p.x += 10;
    if (p.x > 200) p.x = 0;
    // changing the Node.location also changes the data.loc property due to TwoWay binding
    node.location = p;
    // show the updated location held by the "loc" property of the node data
    document.getElementById("bindTwoWayData").textContent = data.loc.toString();
  }, "shift node");
};
window.shiftNode();
```

Click on the button to move the [Node](https://gojs.net/latest/api/symbols/Node.html). The effect is basically what happens when the user drags the node. In this example, the TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html) on [Node.location](https://gojs.net/latest/api/symbols/Node.html#location) will update the "loc" property of the node data that is the Node's [Part.data](https://gojs.net/latest/api/symbols/Part.html#data).

nodedata.loc: `Point(10,0)`

Just as you can use a conversion function when going from source to target, you can supply a conversion function to [Binding.makeTwoWay](https://gojs.net/latest/api/symbols/Binding.html#makeTwoWay) for going from target to source. For example, to represent the location as a string in the model data instead of as a [Point](https://gojs.net/latest/api/symbols/Point.html):

```
// storage representation of Points/Sizes/Rects/Margins/Spots as strings, not objects:
.bindTwoWay("location", "loc", go.Point.parse, go.Point.stringify)
```

Or:

```
// storage representation of Points/Sizes/Rects/Margins/Spots as strings, not objects:
new go.Binding("location", "loc", go.Point.parse).makeTwoWay(go.Point.stringify)
```

However, you must not have a TwoWay binding on the node data property that is the "key" property. (That defaults to the name "key" but is actually the value of [Model.nodeKeyProperty](https://gojs.net/latest/api/symbols/Model.html#nodeKeyProperty).) That property value must always be unique among all node data within the model and is known by the Model. A TwoWay binding might change the value, causing a multitude of problems. Similarly, the [Node.key](https://gojs.net/latest/api/symbols/Node.html#key) property is read-only, to prevent accidental changes of the key value.

Reasons for TwoWay Bindings
---------------------------

The basic reason for using a TwoWay [Binding](https://gojs.net/latest/api/symbols/Binding.html) on a settable property is to make sure that any changes to that property will be copied to the corresponding model data. By making sure that the [Model](https://gojs.net/latest/api/symbols/Model.html) is up-to-date, you can easily "save the diagram" just by saving the model and "loading a diagram" is just a matter of loading a model into memory and setting [Diagram.model](https://gojs.net/latest/api/symbols/Diagram.html#model). If you are careful to only hold JSON-serializable data in the model data, you can just use the [Model.toJson](https://gojs.net/latest/api/symbols/Model.html#toJson) and [Model.fromJson](https://gojs.net/latest/api/symbols/Model.html#fromJson) methods for converting a model to and from a textual representation.

_Most bindings do not need to be TwoWay._ For performance reasons you should not make a Binding be TwoWay unless you actually need to propagate changes back to the data. Most settable properties are only set on initialization and then never change.

Settable properties only change value when some code sets them. That code might be in code that you write as part of your app. Or it might be in a command (see [Commands](https://gojs.net/latest/intro/commands.html)) or a tool (see [Tools](https://gojs.net/latest/intro/tools.html)). Here is a list of properties for which a TwoWay Binding is plausible because one of the predefined commands or tools modify them:

*   [Part.location](https://gojs.net/latest/api/symbols/Part.html#location), by [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html) if it is enabled
*   [Link.points](https://gojs.net/latest/api/symbols/Link.html#points), by [LinkReshapingTool](https://gojs.net/latest/api/symbols/LinkReshapingTool.html) if it is enabled
*   [GraphObject.desiredSize](https://gojs.net/latest/api/symbols/GraphObject.html#desiredSize), by [ResizingTool](https://gojs.net/latest/api/symbols/ResizingTool.html) if it is enabled
*   [GraphObject.angle](https://gojs.net/latest/api/symbols/GraphObject.html#angle), by [RotatingTool](https://gojs.net/latest/api/symbols/RotatingTool.html) if it is enabled
*   [TextBlock.text](https://gojs.net/latest/api/symbols/TextBlock.html#text), by [TextEditingTool](https://gojs.net/latest/api/symbols/TextEditingTool.html) if it is enabled
*   [Part.isSelected](https://gojs.net/latest/api/symbols/Part.html#isSelected), by many tools and commands
*   [Node.isTreeExpanded](https://gojs.net/latest/api/symbols/Node.html#isTreeExpanded) and [Node.wasTreeExpanded](https://gojs.net/latest/api/symbols/Node.html#wasTreeExpanded), by [CommandHandler.collapseTree](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseTree) and [CommandHandler.expandTree](https://gojs.net/latest/api/symbols/CommandHandler.html#expandTree), called by a "TreeExpanderButton" 
*   [Group.isSubGraphExpanded](https://gojs.net/latest/api/symbols/Group.html#isSubGraphExpanded) and [Group.wasSubGraphExpanded](https://gojs.net/latest/api/symbols/Group.html#wasSubGraphExpanded), by [CommandHandler.collapseSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseSubGraph) and [CommandHandler.expandSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#expandSubGraph), called by a "SubGraphExpanderButton" 

You will not need to use a TwoWay binding on a property if the Tool that modifies it cannot run, or if the command that modifies it cannot be invoked. You probably will not need a TwoWay binding on any other properties unless you write code to modify them. And even then it is sometimes better to write the code to modify the model data directly by calling [Model.setDataProperty](https://gojs.net/latest/api/symbols/Model.html#setDataProperty), depending on a OneWay Binding to update the GraphObject property.

It is also possible to use TwoWay Bindings where the source is a GraphObject rather than model data. This is needed less frequently, when you do _not_ want to have the state stored in the model, but you do want to synchronize properties of GraphObjects within the same Part.

_Use TwoWay Bindings sparingly._

Theming
-------

The ability to automatically update properties from [Theme](https://gojs.net/latest/api/symbols/Theme.html) objects is basically provided by data binding using a subclass of [Binding](https://gojs.net/latest/api/symbols/Binding.html). However, theme binding is OneWay only. Read more about theming at [Introduction to Theming](https://gojs.net/latest/intro/theming.html).
