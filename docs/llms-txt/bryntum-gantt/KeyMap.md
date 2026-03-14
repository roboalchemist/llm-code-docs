# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/KeyMap.md

# [KeyMap](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap)

Mixin for widgets that allows for standardized and customizable keyboard shortcuts functionality. Can be configured on any widget or compatible feature.

```
const grid = new Grid({
    keyMap: {
        // Changing keyboard navigation to respond to WASD keys.
        w : 'navigateUp',
        a : 'navigateLeft',
        s : 'navigateDown',
        d : 'navigateRight',

        // Removes mappings for arrow keys.
        ArrowUp    : null,
        ArrowLeft  : null,
        ArrowDown  : null,
        ArrowRight : null
    },

    // If key was not handled by the keyMap, this function is called.
    // Use this to process keystrokes that are not part of the keyMap *after* the keyMap has been processed.
    defaultKeyHandler(keyEvent) {
        if (keyEvent.target.matches('.my-element-class')) {
            // Do something special when the key is pressed in an element with the class 'my-element-class'
       }
    }
});
```

The invoking `KeyboardEvent` is passed as the first argument into all handlers.

The owning Widget of the KeyMap is injected into the passed `KeyboardEvent` in the `widget` property.

For more information on how to customize keyboard shortcuts, please see our guide (Guides/Customization/Keyboard shortcuts)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[keyMap](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#config-keyMap)
An object whose keys are the [key](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) name and optional modifier prefixes: `'Ctrl+'`, `'Alt+'`, `'Meta+'`, and `'Shift+'` (case-insensitive). The values are the name of the instance method to call when the keystroke is received.

For example:

```
 keyMap : {
     'Ctrl+A': 'onSelectAll',
     'Ctrl+Z': 'onUndo',
     't'     : 'gotoNow',
     [/\d/]  : 'onDigit'
 }
```

If a key is a visible character (as above), and _not_ modified by any modifier keys, and emanates from an editable element (such as an `<input>` or `<textarea>`), the keystroke is ignored. This is to allow the browser to handle typing in editable elements.

In addition to key names, the special key `'delegate'` can be included to specify additional objects that have their own `keyMap`. If a keystroke is not handled by this `keyMap`, the delegates are processed until one has a matching entry in its `keyMap`. The value of the `delegate` key can be a single string, an array of strings or an object whose [truthy keys](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getTruthyKeys-static) are [dot paths](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getPath-static) identifying the delegate(s) related to this instance.

For example:

```
 keyMap : {
     delegate : ['widgetMap.foo', 'widgetMap.bar', 'tbar']
 }
```

An widget with the above `keyMap` will delegate to the child widgets named `foo` and `bar` via the widget's [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap). In addition, the `tbar` property of the widget will also be considered as a delegate.

The following is equivalent to the above `delegate` but using an object. This form can be used to allow removal of entries by derived classes or an overriding instance config.

```
 keyMap : {
     delegate : {
         'widgetMap.foo' : true,
         'widgetMap.bar' : true,
         tbar            : true
     }
 }
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isKeyMap](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#property-isKeyMap)
Identifies an object as an instance of [KeyMap](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/KeyMap) class, or subclass thereof.

[isKeyMap](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#property-isKeyMap-static)
Identifies an object as an instance of [KeyMap](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/KeyMap) class, or subclass thereof.

[keyMap](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#property-keyMap)
An object whose keys are the [key](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) name and optional modifier prefixes: `'Ctrl+'`, `'Alt+'`, `'Meta+'`, and `'Shift+'` (case-insensitive). The values are the name of the instance method to call when the keystroke is received.

For example:

```
 keyMap : {
     'Ctrl+A': 'onSelectAll',
     'Ctrl+Z': 'onUndo',
     't'     : 'gotoNow',
     [/\d/]  : 'onDigit'
 }
```

If a key is a visible character (as above), and _not_ modified by any modifier keys, and emanates from an editable element (such as an `<input>` or `<textarea>`), the keystroke is ignored. This is to allow the browser to handle typing in editable elements.

In addition to key names, the special key `'delegate'` can be included to specify additional objects that have their own `keyMap`. If a keystroke is not handled by this `keyMap`, the delegates are processed until one has a matching entry in its `keyMap`. The value of the `delegate` key can be a single string, an array of strings or an object whose [truthy keys](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getTruthyKeys-static) are [dot paths](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getPath-static) identifying the delegate(s) related to this instance.

For example:

```
 keyMap : {
     delegate : ['widgetMap.foo', 'widgetMap.bar', 'tbar']
 }
```

An widget with the above `keyMap` will delegate to the child widgets named `foo` and `bar` via the widget's [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap). In addition, the `tbar` property of the widget will also be considered as a delegate.

The following is equivalent to the above `delegate` but using an object. This form can be used to allow removal of entries by derived classes or an overriding instance config.

```
 keyMap : {
     delegate : {
         'widgetMap.foo' : true,
         'widgetMap.bar' : true,
         tbar            : true
     }
 }
```

[keyMapElement](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#property-keyMapElement)
Override to attach the keyMap keydown event listener to something else than this.element

[keyMapSubComponents](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#property-keyMapSubComponents)
Override to make keyMap resolve subcomponent actions to something else than this.features.

## Functions

Functions are methods available for calling on the class

[addKeyBinding](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-addKeyBinding)
Add a key binding to this widget's keyMap.

```
// Add a key binding to the widget to call its own onCtrlEnter method when Ctrl+Enter is pressed.
myWidget.addKeyBinding('Ctrl+Enter', 'onCtrlEnter');
```

[removeKeyBinding](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-removeKeyBinding)
Remove a key binding to this widget's keyMap.

```
// Add a key binding to the widget to call its own onCtrlEnter method when Ctrl+Enter is pressed.
myWidget.removeKeyBinding('Ctrl+Enter', 'onCtrlEnter');
```

[matchKeyMapEntry](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-matchKeyMapEntry)
Returns the `keyMap` property name which matches the passed KeyboardEvent if any.

[performKeyMapAction](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-performKeyMapAction)
Called on keyMapElement keyDown

[resolveKeyMapAction](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-resolveKeyMapAction)
Resolves correct `this` and handler function. If subComponent (action includes a dot) it will resolve in keyMapSubComponents (defaults to this.features).

For example, in feature configurable: `keyMap: { ArrowUp: 'navigateUp' }`

Will be translated (by InstancePlugin) to: \`keyMap: { ArrowUp: 'featureName.navigateUp' }

And resolved to correct function path here.

Override to change action function mapping.

[mergeKeyMaps](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#function-mergeKeyMaps)
This function is used for merging two keyMaps with each other. It can be used for example by a Grid's feature to merge the fetature's keyMap into the Grid's with the use of a subPrefix.

## Typedefs

Typedefs are type definitions for the class

[KeyMapConfig](https://bryntum.com/docs/gantt/api/Core/widget/mixin/KeyMap#typedef-KeyMapConfig)
Mapped key configuration
