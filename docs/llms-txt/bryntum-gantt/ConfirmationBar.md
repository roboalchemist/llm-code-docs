# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ConfirmationBar.md

# [ConfirmationBar](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar)

This widget is a `Toolbar` with default buttons for [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) common to system dialogs. Button order is appropriate for the platform. For example, on Windows, OK/Cancel buttons are presented in that order, while on Mac OS X and many flavors of Linux, these buttons are presented in Cancel/OK order.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[defaultButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#config-defaultButton)
The name of the default button. Must match with the defaults in [namedItems](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-namedItems).

[items](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#config-items)
In addition to normal form of [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items), this class supports a comma-delimited string.

For example:

```
 items : 'ok,cancel',
 // or
 items : 'yes,no',
```

These are equivalent to:

```
 items : {
     ok     : true,
     cancel : true
 },
 // or
 items : {
     yes : true,
     no  : true
 },
```

Both forms use the pre-defined buttons: `'cancel'`, `'ok'`, `'no'`, `'yes'`.

[keyMap](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#config-keyMap)
Maps `Enter` and `Escape` to [doDefault](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#function-doDefault) and [doCancel](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#function-doCancel), respectively.

[namedItems](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#config-namedItems)
The default buttons available for use in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) config.

[syncWidthButtons](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#config-syncWidthButtons)
Set to `false` to disable synchronizing button widths. By default, buttons are assigned a `minWidth` based on the longest [text](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-text). The default OK and Cancel buttons (in the en-US locale) will be assigned `minWidth = '6em'`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isConfirmationBar](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-isConfirmationBar)
Identifies an object as an instance of [ConfirmationBar](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar) class, or subclass thereof.

[isConfirmationBar](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-isConfirmationBar-static)
Identifies an object as an instance of [ConfirmationBar](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar) class, or subclass thereof.

[defaultButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-defaultButton)
The name of the default button. Must match with the defaults in [namedItems](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-namedItems).

[syncWidthButtons](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-syncWidthButtons)
Set to `false` to disable synchronizing button widths. By default, buttons are assigned a `minWidth` based on the longest [text](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-text). The default OK and Cancel buttons (in the en-US locale) will be assigned `minWidth = '6em'`.

[cancelButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-cancelButton)
Returns the `cancel` button if present in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) config or `null` if not present.

[noButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-noButton)
Returns the `no` button if present in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) config or `null` if not present.

[okButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-okButton)
Returns the `ok` button if present in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) config or `null` if not present.

[yesButton](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#property-yesButton)
Returns the `yes` button if present in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) config or `null` if not present.

## Functions

Functions are methods available for calling on the class

[doCancel](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#function-doCancel)
Called by the [keyMap](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-keyMap) to process `Escape`. This triggers a click from the first button in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items) config that is present:

* [cancelButton](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#property-cancelButton)
* [noButton](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#property-noButton)
* the first button that is not the [defaultButton](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-defaultButton)

[doDefault](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#function-doDefault)
Called by the [keyMap](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-keyMap) to process `Enter` or `NumpadEnter`. This triggers a click from the [defaultButton](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-defaultButton).

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[choice](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#event-choice)
This event is fired when the user clicks one of the [buttons](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar#config-items).

## Typedefs

Typedefs are type definitions for the class

[ConfirmationBarChoice](https://bryntum.com/docs/gantt/api/Core/widget/ConfirmationBar#typedef-ConfirmationBarChoice)
A description of the chosen button in a [ConfirmationBar](https://bryntum.com/docs/gantt/api/#Core/widget/ConfirmationBar).
