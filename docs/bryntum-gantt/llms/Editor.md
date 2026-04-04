# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Editor.md

# [Editor](https://bryntum.com/docs/gantt/api/Core/widget/Editor)

Displays an input field, optionally editing a field of a record at a particular position.

Offers events to signal edit completion upon `ENTER` or focus loss (if configured to do so), or edit cancellation on `ESC`, or focus loss if configured that way.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[align](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-align)
The alignment config for how this editor aligns to a target when asked to [startEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-startEdit)

[hideTarget](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-hideTarget)
Controls whether to hide the target element when asked to [startEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-startEdit)

[appendToTargetParent](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-appendToTargetParent)
Set to `true` to automatically append the Editor's element to the parent element of the element being edited.

[matchSize](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-matchSize)
By default, an Editor matches both dimensions, width and height of the element it is targeted at in the [startEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-startEdit) function.

Configure this as false to allow the editor's configured dimensions, or its CSS-imposed dimensions size it.

This may also operate with more granularity by specifying both dimensions in an object:

```
    // Editor can exceed its target's height
    matchSize : {
        width  : true,
        height : false
    }
```

[matchFont](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-matchFont)
Controls whether the editor should match target element's font when asked to [startEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-startEdit)

[fitTargetContent](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-fitTargetContent)
Controls whether the editor should expand its width if the input field has overflow [startEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-startEdit)

[inputField](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-inputField)
A config object, or the `type` string of the widget (usually a [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) subclass, i.e. [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)) which this editor will encapsulate.

[blurAction](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-blurAction)
What action should be taken when focus moves out of the editor, either by `TAB` or clicking outside. May be `'complete'` or `'cancel`'. Any other value results in no action being taken upon focus leaving the editor leaving the application to listen for the [focusOut](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#event-focusOut) event.

[completeKey](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-completeKey)
The name of the `key` which completes the edit.

See https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key\_Values for key names.

[cancelKey](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-cancelKey)
The name of the `key` which cancels the edit.

See https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key\_Values for key names.

[invalidAction](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-invalidAction)
How to handle a request to complete the edit if the field is invalid. There are three choices:

* `block` The default. The edit is not exited, the field remains focused.
* `allow` Allow the edit to be completed.
* `revert` The field value is reverted and the edit is completed.

[completeOnChange](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-completeOnChange)
Configure as `true` to have editing complete as soon as the field fires its `change` event.

[floating](https://bryntum.com/docs/gantt/api/Core/widget/Editor#config-floating)
Set to `true` to render the editor field outside the cell element in the browser viewport space, aligned to bottom of the cell. This will also default [scrollAction](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#config-scrollAction) to `realign` and [matchSize](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#config-matchSize) to `false`. It is also recommended to set a `minHeight` and/or `minWidth` property on the [align](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#config-align) config.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEditor](https://bryntum.com/docs/gantt/api/Core/widget/Editor#property-isEditor)
Identifies an object as an instance of [Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor) class, or subclass thereof.

[isEditor](https://bryntum.com/docs/gantt/api/Core/widget/Editor#property-isEditor-static)
Identifies an object as an instance of [Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor) class, or subclass thereof.

[inputField](https://bryntum.com/docs/gantt/api/Core/widget/Editor#property-inputField)
A config object, or the `type` string of the widget (usually a [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) subclass, i.e. [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)) which this editor will encapsulate.

## Functions

Functions are methods available for calling on the class

[startEdit](https://bryntum.com/docs/gantt/api/Core/widget/Editor#function-startEdit)
Start editing

[completeEdit](https://bryntum.com/docs/gantt/api/Core/widget/Editor#function-completeEdit)
Complete the edit, and, if associated with a record, update the record if possible. If editing is completed, the editor is hidden.

If the field is invalid, the `[invalidAction](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#config-invalidAction)` config is used to decide upon the course of action.

If a [beforeComplete](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#event-beforeComplete) handler returns `false` then editing is not completed.

If the field's values has not been changed, then editing is terminated through [cancelEdit](https://bryntum.com/docs/gantt/api/#Core/widget/Editor#function-cancelEdit).

[cancelEdit](https://bryntum.com/docs/gantt/api/Core/widget/Editor#function-cancelEdit)
Cancel the edit and hide the editor.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStart](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-beforeStart)
Fired before the editor is shown to start an edit operation. Returning `false` from a handler vetoes the edit operation.

[start](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-start)
Fired when an edit operation has begun.

[beforeComplete](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-beforeComplete)
Fired when an edit completion has been requested, either by `ENTER`, or focus loss (if configured to complete on blur). The completion may be vetoed, in which case, focus is moved back into the editor.

[complete](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-complete)
Edit has been completed, and any associated record or element has been updated.

[beforeCancel](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-beforeCancel)
Fired when cancellation has been requested, either by `ESC`, or focus loss (if configured to cancel on blur). The cancellation may be vetoed, in which case, focus is moved back into the editor.

[cancel](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-cancel)
Edit has been canceled without updating the associated record or element.

[keyDown](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-keyDown)
Fire to relay a `keydown` event from the field.

[afterEdit](https://bryntum.com/docs/gantt/api/Core/widget/Editor#event-afterEdit)
Fired after the editor is finalized and hidden, regardless whether it was completed or aborted.
