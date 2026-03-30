# Source: https://gojs.net/intro/transactions.html

Title: Transactions

URL Source: https://gojs.net/intro/transactions.html

Markdown Content:
Transactions and the UndoManager
--------------------------------

**GoJS** models and diagrams make use of an [UndoManager](https://gojs.net/latest/api/symbols/UndoManager.html) that can record all changes and support undoing and redoing those changes. Each state change is recorded in a [ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html), which includes enough information about both before and after to be able to reproduce the state change in either direction, backward (undo) or forward (redo). Such changes are grouped together into [Transaction](https://gojs.net/latest/api/symbols/Transaction.html)s so that a user action, which may result in many changes, can be undone and redone as a single operation.

Not all state changes result in [ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html)s that can be recorded by the UndoManager. Some properties are considered transient, such as [Diagram.position](https://gojs.net/latest/api/symbols/Diagram.html#position), [Diagram.scale](https://gojs.net/latest/api/symbols/Diagram.html#scale), [Diagram.currentTool](https://gojs.net/latest/api/symbols/Diagram.html#currentTool), [Diagram.currentCursor](https://gojs.net/latest/api/symbols/Diagram.html#currentCursor), or [Diagram.isModified](https://gojs.net/latest/api/symbols/Diagram.html#isModified). Some changes are structural or considered unchanging, such as [Diagram.model](https://gojs.net/latest/api/symbols/Diagram.html#model), any property of [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html), or any of the tool or layout properties. But most [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) and model properties do raise a ChangedEvent on the Diagram or Model, respectively, when a property value has been changed.

Whenever you modify a model or its data programmatically in response to some event, you should wrap the code in a transaction. Call [Diagram.startTransaction](https://gojs.net/latest/api/symbols/Diagram.html#startTransaction) or [Model.startTransaction](https://gojs.net/latest/api/symbols/Model.html#startTransaction), make the changes, and then call [Diagram.commitTransaction](https://gojs.net/latest/api/symbols/Diagram.html#commitTransaction) or [Model.commitTransaction](https://gojs.net/latest/api/symbols/Model.html#commitTransaction). Although the primary benefit from using transactions is to group together side-effects for undo/redo, you should use transactions even if your application does not support undo/redo by the user.

As with database transactions, you will want to perform transactions that are short and infrequent. Do not leave transactions ongoing between user actions. Consider whether it would be better to have a single transaction surrounding a loop instead of starting and finishing a transaction repeatedly within a loop. Do not execute transactions within a property setter -- such granularity is too small. Instead execute a transaction where the properties are set in response to some user action or external event.

However, unlike database transactions, you do not need to conduct a transaction in order to access any state. All JavaScript objects are in memory, so you can look at their properties at any time that it would make sense to do so. But when you want to make state changes to a [Diagram](https://gojs.net/latest/api/symbols/Diagram.html) or a [GraphObject](https://gojs.net/latest/api/symbols/GraphObject.html) or a [Model](https://gojs.net/latest/api/symbols/Model.html) or a JavaScript object in a model, do so within a transaction.

The only exception is that transactions are unnecessary when initializing a model or a diagram before assigning the model to the [Diagram.model](https://gojs.net/latest/api/symbols/Diagram.html#model) property. (A Diagram only gets access to an UndoManager via the Model, the [Model.undoManager](https://gojs.net/latest/api/symbols/Model.html#undoManager) property.)

Furthermore many event handlers and listeners are already executed within transactions that are conducted by [Tool](https://gojs.net/latest/api/symbols/Tool.html)s or [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) commands, so you often will not need to start and commit a transaction within such functions. Read the API documentation for details about whether a function is called within a transaction. For example, the [GraphObject.click](https://gojs.net/latest/api/symbols/GraphObject.html#click) event handler to respond to a click on a GraphObject needs to perform a transaction if it wants to modify the model or the diagram. Most custom click event handlers do not change the diagram but instead update some HTML.

But implementing an "ExternalObjectsDropped" [DiagramEvent](https://gojs.net/latest/api/symbols/DiagramEvent.html) listener, which usually does want to modify the just-dropped Parts in the [Diagram.selection](https://gojs.net/latest/api/symbols/Diagram.html#selection), is called within the [DraggingTool](https://gojs.net/latest/api/symbols/DraggingTool.html)'s transaction, so no additional start/commit transaction calls are needed.

Finally, some customizations, such as the [Node.linkValidation](https://gojs.net/latest/api/symbols/Node.html#linkValidation) predicate, should not modify the diagram or model at all.

Both model changes and diagram changes are recorded in the [UndoManager](https://gojs.net/latest/api/symbols/UndoManager.html) only if the model's [UndoManager.isEnabled](https://gojs.net/latest/api/symbols/UndoManager.html#isEnabled) has been set to true. If you do not want the user to be able to perform undo or redo and also prevent the recording of any [Transaction](https://gojs.net/latest/api/symbols/Transaction.html)s, but you still want to get "Transaction"-type [ChangedEvent](https://gojs.net/latest/api/symbols/ChangedEvent.html)s because you want to update a database, you can set [UndoManager.maxHistoryLength](https://gojs.net/latest/api/symbols/UndoManager.html#maxHistoryLength) to zero.

To better understand the relationships between objects and transactions in memory, look at this diagram:

A typical case for using transactions is when some command makes a change to the model.

```
// define a function named "addChild" that is invoked by a button click
addChild = () => {
  const selnode = diagram.selection.first();
  if (!(selnode instanceof go.Node)) return;
  diagram.commit(d => {
    // have the Model add a new node data
    const newnode = { key: "N", text: `New ${d.model.nodeDataArray.length}` };
    d.model.addNodeData(newnode);  // this makes sure the key is unique
    // and then add a link data connecting the original node with the new one
    const newlink = { from: selnode.data.key, to: newnode.key };
    // add the new link to the model
    d.model.addLinkData(newlink);
  }, "add node and link");
};

diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("RoundedRectangle", { fill: "whitesmoke" }),
      new go.TextBlock({ margin: 5 })
        .bind("text")
    );

diagram.layout = new go.TreeLayout();

const nodeDataArray = [
  { key: 1, text: "Alpha" },
  { key: 2, text: "Beta" }
];
const linkDataArray = [
  { from: 1, to: 2 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
diagram.model.undoManager.isEnabled = true;
```

In the following example, select a node and then click the button. The addChild function adds a link connecting the selected node to a new node. When no Node is selected, nothing happens.

Supporting the UndoManager
--------------------------

Changes to JavaScript data properties do not automatically result in any notifications that can be observed. Thus when you want to change the value of a property in a manner that can be undone and redone, you should call [Model.setDataProperty](https://gojs.net/latest/api/symbols/Model.html#setDataProperty) (or [Model.set](https://gojs.net/latest/api/symbols/Model.html#set), which is an abbreviation for that method). This will get the previous value for the property, set the property to the new value, and call [Model.raiseDataChanged](https://gojs.net/latest/api/symbols/Model.html#raiseDataChanged), which will also automatically update any target bindings in the Node corresponding to the data.

```
diagram.nodeTemplate =
  new go.Node("Auto")
    .add(
      new go.Shape("RoundedRectangle", { fill: "whitesmoke" }),
      new go.TextBlock({ margin: 5 })
        .bind("text", "someValue")  // bind to the "someValue" data property
    );

const nodeDataArray = [
  { key: "Alpha", someValue: 1 }
];
diagram.model = new go.GraphLinksModel(nodeDataArray);
diagram.model.undoManager.isEnabled = true;

// define a function named "incrementData" callable by onclick
incrementData = () => {
  diagram.model.commit(m => {
    const data = m.nodeDataArray[0];  // get the first node data
    m.set(data, "someValue", (data.someValue || 0) + 1);
  }, "increment");
};
```

Move the node around. Click on the button to increase the value of the "someValue" property on the first node data. Click to focus in the Diagram and then Ctrl-Z and Ctrl-Y to undo and redo the moves and value changes.
