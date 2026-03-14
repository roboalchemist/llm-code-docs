# Source: https://gojs.net/intro/commands.html

Title: Commands

URL Source: https://gojs.net/intro/commands.html

Markdown Content:
Commands such as **Delete** or **Paste** or **Undo** are implemented by the [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) class.

Keyboard events, like mouse and touch events, always go to the [Diagram.currentTool](https://gojs.net/latest/api/symbols/Diagram.html#currentTool). The current tool, when the user is not performing some gesture, is the same as the [Diagram.defaultTool](https://gojs.net/latest/api/symbols/Diagram.html#defaultTool), which normally is the [Diagram.toolManager](https://gojs.net/latest/api/symbols/Diagram.html#toolManager). The [ToolManager](https://gojs.net/latest/api/symbols/ToolManager.html) handles keyboard events by delegating them to the [Diagram.commandHandler](https://gojs.net/latest/api/symbols/Diagram.html#commandHandler).

Basically, the diagram handles a keyboard event, creates an [InputEvent](https://gojs.net/latest/api/symbols/InputEvent.html) describing it, and then calls [ToolManager.doKeyDown](https://gojs.net/latest/api/symbols/ToolManager.html#doKeyDown). That in turn just calls [CommandHandler.doKeyDown](https://gojs.net/latest/api/symbols/CommandHandler.html#doKeyDown). The same sequence happens for key-up events.

Please note that the handling of keyboard commands depends on the diagram getting focus and then getting keyboard events. Do not apply any styling such as

`canvas:focus { display: none; } /* DO NOT DO THIS! */`
Keyboard command bindings
-------------------------

The [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) implements the following commands for keyboard input. On a Mac the Command key may be used as the modifier instead of the Control key.

*   Del or Backspace invokes [CommandHandler.deleteSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#deleteSelection)
*   Ctrl-X or Shift-Del invokes [CommandHandler.cutSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#cutSelection)
*   Ctrl-C or Ctrl-Insert invokes [CommandHandler.copySelection](https://gojs.net/latest/api/symbols/CommandHandler.html#copySelection)
*   Ctrl-V or Shift-Insert invokes [CommandHandler.pasteSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#pasteSelection)
*   Ctrl-A invokes [CommandHandler.selectAll](https://gojs.net/latest/api/symbols/CommandHandler.html#selectAll)
*   Ctrl-Z or Alt-Backspace invokes [CommandHandler.undo](https://gojs.net/latest/api/symbols/CommandHandler.html#undo)
*   Ctrl-Y or Ctrl-Shift-Z or Alt-Shift-Backspace invokes [CommandHandler.redo](https://gojs.net/latest/api/symbols/CommandHandler.html#redo)
*   Up or Down or Left or Right (arrow key) calls [Diagram.scroll](https://gojs.net/latest/api/symbols/Diagram.html#scroll)
*   PageUp or PageDown calls [Diagram.scroll](https://gojs.net/latest/api/symbols/Diagram.html#scroll)
*   Home or End calls [Diagram.scroll](https://gojs.net/latest/api/symbols/Diagram.html#scroll)
*   Space invokes [CommandHandler.scrollToPart](https://gojs.net/latest/api/symbols/CommandHandler.html#scrollToPart)
*   Ctrl-- (minus) or Numpad-- invokes [CommandHandler.decreaseZoom](https://gojs.net/latest/api/symbols/CommandHandler.html#decreaseZoom)
*   Ctrl-+ (plus) or Numpad-+ invokes [CommandHandler.increaseZoom](https://gojs.net/latest/api/symbols/CommandHandler.html#increaseZoom)
*   Ctrl-0 invokes [CommandHandler.resetZoom](https://gojs.net/latest/api/symbols/CommandHandler.html#resetZoom)
*   Shift-Z invokes [CommandHandler.zoomToFit](https://gojs.net/latest/api/symbols/CommandHandler.html#zoomToFit); repeat to return to the original scale and position if [CommandHandler.isZoomToFitRestoreEnabled](https://gojs.net/latest/api/symbols/CommandHandler.html#isZoomToFitRestoreEnabled) is true
*   Ctrl-G invokes [CommandHandler.groupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#groupSelection)
*   Ctrl-Shift-G invokes [CommandHandler.ungroupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#ungroupSelection)
*   F2 invokes [CommandHandler.editTextBlock](https://gojs.net/latest/api/symbols/CommandHandler.html#editTextBlock)
*   Menu Key or Shift-F10 or Ctrl-Shift-\ invokes [CommandHandler.showContextMenu](https://gojs.net/latest/api/symbols/CommandHandler.html#showContextMenu)
*   Escape invokes [CommandHandler.stopCommand](https://gojs.net/latest/api/symbols/CommandHandler.html#stopCommand)
*   Ctrl-Alt-Enter switches to [Keyboard Control Mode](https://gojs.net/latest/intro/accessibility.html)

For the keyboard command bindings when in keyboard control mode, see [Keyboard Control Commands](https://gojs.net/latest/intro/accessibility.html#KeyboardCommandTable).

At the current time there are no keyboard bindings for commands such as [CommandHandler.collapseSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseSubGraph), [CommandHandler.collapseTree](https://gojs.net/latest/api/symbols/CommandHandler.html#collapseTree), [CommandHandler.expandSubGraph](https://gojs.net/latest/api/symbols/CommandHandler.html#expandSubGraph), or [CommandHandler.expandTree](https://gojs.net/latest/api/symbols/CommandHandler.html#expandTree). Such Nodes or Groups usually have buttons such as "TreeExpanderButton" or "SubGraphExpanderButton" in them or provide expand/collapse ability via other means.

If you want to have a different behavior for the arrow keys, consider using the sample class extended from [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html): [DrawCommandHandler](https://gojs.net/latest/extensions/DrawCommandHandler.js), which implements options for having the arrow keys move the selection or change the selection.

That DrawCommandHandler extension also demonstrates a customization of the **Copy** and **Paste** commands to automatically shift the location of pasted copies.

CommandHandler
--------------

The [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) class implements pairs of methods: a method to execute a command and a predicate that is true when the command may be executed. For example, for the **Copy** command, there is a [CommandHandler.copySelection](https://gojs.net/latest/api/symbols/CommandHandler.html#copySelection) method and a [CommandHandler.canCopySelection](https://gojs.net/latest/api/symbols/CommandHandler.html#canCopySelection) method.

Keyboard event handling always calls the "can..." predicate first. Only if that returns true does it actually call the method to execute the command.

There are a number of properties that you can set to affect the CommandHandler's standard behavior. For example, if you want to allow the user to group selected parts together with the [CommandHandler.groupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#groupSelection), you will need to set [CommandHandler.archetypeGroupData](https://gojs.net/latest/api/symbols/CommandHandler.html#archetypeGroupData) to a group node data object:

```
diagram.commandHandler.archetypeGroupData =
  { key: "Group", isGroup: true, color: "blue" };
```

That data object is copied and added to the model as the new group data object by [CommandHandler.groupSelection](https://gojs.net/latest/api/symbols/CommandHandler.html#groupSelection).

If you want to add your own keyboard bindings, you can override the [CommandHandler.doKeyDown](https://gojs.net/latest/api/symbols/CommandHandler.html#doKeyDown) method. For example, to support using the "T" key to collapse or expand the currently selected [Group](https://gojs.net/latest/api/symbols/Group.html):

```
myDiagram.commandHandler.doKeyDown = function() { // must be a function, not an arrow =>
  const e = this.diagram.lastInput;
  if (e.code === "KeyT") {  // could also check for e.control or e.shift
    if (this.canCollapseSubGraph()) {
      this.collapseSubGraph();
    } else if (this.canExpandSubGraph()) {
      this.expandSubGraph();
    }
  } else {
    // call base method with no arguments
    go.CommandHandler.prototype.doKeyDown.call(this);
  }
};
```

Do not forget to call the base method in order to handle all of the keys that your method does not handle.

Note that calling the base method involves getting the base class's prototype's method. If the base method takes arguments, be sure to pass arguments to the call to the base method.

Updating command UI
-------------------

It is common to have HTML elements outside of the diagram that invoke commands. You can use the [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html)'s "can..." predicates to enable or disable UI that would invoke the command.

```
// allow the group command to execute
diagram.commandHandler.archetypeGroupData =
  { key: "Group", isGroup: true, color: "blue" };
// modify the default group template to allow ungrouping
diagram.groupTemplate.ungroupable = true;

const nodeDataArray = [
  { key: "Alpha" },
  { key: "Beta" },
  { key: "Delta", group: "Epsilon" },
  { key: "Gamma", group: "Epsilon" },
  { key: "Epsilon", isGroup: true }
];
const linkDataArray = [
  { from: "Alpha", to: "Beta" },
  { from: "Beta", to: "Beta" },
  { from: "Gamma", to: "Delta" },
  { from: "Delta", to: "Alpha" }
];
diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);

// enable or disable a particular button
function enable(name, ok) {
  const button = document.getElementById(name);
  if (button) button.disabled = !ok;
}
// enable or disable all command buttons
function enableAll() {
  const cmd = diagram.commandHandler;
  enable("SelectAll", cmd.canSelectAll());
  enable("Cut", cmd.canCutSelection());
  enable("Copy", cmd.canCopySelection());
  enable("Paste", cmd.canPasteSelection());
  enable("Delete", cmd.canDeleteSelection());
  enable("Group", cmd.canGroupSelection());
  enable("Ungroup", cmd.canUngroupSelection());
  enable("Undo", cmd.canUndo());
  enable("Redo", cmd.canRedo());
}
// notice whenever the selection may have changed
diagram.addDiagramListener("ChangedSelection", e => enableAll());
// notice when the Paste command may need to be reenabled
diagram.addDiagramListener("ClipboardChanged", e => enableAll());
// notice whenever a transaction or undo/redo has occurred
diagram.addModelChangedListener(e => {
  if (e.isTransactionFinished) enableAll();
});
// perform initial enablements after everything has settled down
setTimeout(enableAll, 100);
// make the diagram accessible to button onclick handlers
myDiagram = diagram;
// calls enableAll() due to Model Changed listener
myDiagram.undoManager.isEnabled = true;
```

Each button is implemented in the following fashion:

```
<input id="SelectAll" type="button"
       onclick="myDiagram.commandHandler.selectAll()" value="Select All" />
```

Whenever the selection changes or whenever a transaction or undo or redo occurs, the enableAll function is called to update the `disabled` property of each of the buttons.

Accessibility
-------------

Although much of the predefined functionality of the [CommandHandler](https://gojs.net/latest/api/symbols/CommandHandler.html) is accessible with keyboard commands or the default context menu, not all of it is, and the functionality of the [Tool](https://gojs.net/latest/api/symbols/Tool.html)s mostly depends on mouse or touch events. Your users can use [Keyboard Control Mode](https://gojs.net/latest/intro/accessibility.html) if they cannot use a mouse or finger or if they prefer to use a keyboard.

That mode also supports updating through screen readers. Since for efficiency and flexibility reasons **GoJS** is designed not to use regular HTML DOM elements, making an app that is accessible to screen readers or other accessibility devices is a matter of producing the appropriate application-specific information in an HTML element and implementing a [CommandHandler.focusChanged](https://gojs.net/latest/api/symbols/CommandHandler.html#focusChanged) event handler that updates that element. Read more at [Customizing for Screen Readers](https://gojs.net/latest/intro/accessibility.html#CustomizingforScreenReaders).

More CommandHandler override examples
-------------------------------------

Stop CTRL+Z/CTRL+Y from doing an undo/redo, but still allow [CommandHandler.undo](https://gojs.net/latest/api/symbols/CommandHandler.html#undo) and [CommandHandler.redo](https://gojs.net/latest/api/symbols/CommandHandler.html#redo) to be called programmatically:

```
myDiagram.commandHandler.doKeyDown = function() { // must be a function, not an arrow =>
  const e = this.diagram.lastInput;
  // The meta (Command) key substitutes for "control" for Mac commands
  const control = e.control || e.meta;
  const code = e.code;
  const key = e.key.toLowerCase();
  // Quit on any undo/redo key combination:
  if (control && (code === 'KeyZ' || key === 'z' || code === 'KeyY' || key === 'y')) return;

  // call base method with no arguments (default functionality)
  go.CommandHandler.prototype.doKeyDown.call(this);
};
```
