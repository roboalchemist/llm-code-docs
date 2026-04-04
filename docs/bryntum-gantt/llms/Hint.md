# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Hint.md

# [Hint](https://bryntum.com/docs/gantt/api/Core/widget/Hint)

A popup designed to show the user instruction on how to use a specific feature, for onboarding purposes.

This class is not intended to be instantiated directly, but rather to be used by the [HintFlow](https://bryntum.com/docs/gantt/api/#Core/util/HintFlow) class.

The `HintFlow` class must be configured with an array of hint configurations like this:

```
new HintFlow({
    // Default configs to apply to all hints
    defaults : {
        modal : true
    },
    hints : [{
        // CSS selector to find the target element
        target  : '.b-tabpanel-tab[data-item-index="1"]',

        // Action to take when the 'Next' button is clicked
        nextAction : {
            click : '.b-tabpanel-tab[data-item-index="1"]'
        }

        // Config props for the displayed Hint popup
        title   : 'Change tab',
        content : 'Click here to move to the next tab',
        align   : 't-n'
    }, {
        target  : '.b-button:contains(Save)',
        title   : 'Save',
        content : 'Click here to save the changes',
        nextAction : {
           click : '.b-button:contains(Save)'
        }
   }]
});
```

Each entry in the `hints` array of the [HintFlow](https://bryntum.com/docs/gantt/api/#Core/util/HintFlow) class should be an object with the following properties:

* target: Required The target element to highlight, or a CSS selector to find the target element. If the target selector ends with a `?`, the hint will be skipped if the target is not found. By default, the hint will be aligned to this element.

* title: The title to display in the hint.

* content: Required. The content to display in the hint.

* align: The alignment of the hint relative to the target element. If this is specified as an [AlignSpec](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#typedef-AlignSpec) object, the hint will be aligned to the `target` property of this object if present.

  * target: The element to align to, or a CSS selector to find the element to align to.
* nextAction: The action(s) to take when the 'Next' button is clicked. Properties may be:

  * click: A CSS selector to find the target element to click.
  * type: A string to type into the target element.
  * dblclick: A CSS selector to find the target element to double click.
  * contextmenu: A CSS selector to find the target element to right click.
  * fn: A function to call when the hint is shown.
  * drag: An object with the following properties:
    * target: The target element to drag, or a CSS selector to find the target element.
    * by: The distance to drag the target element, as an array of `[dx, dy]`.
  * waitFor: A CSS selector to wait for or the number of milliseconds to wait before continuing to the next hint.
* previousAction: The action(s) to take when the 'Previous' button is clicked.

* autoNext: The number of milliseconds to wait before automatically moving to the next hint, or a CSS selector to find the target element to wait for.

* highlightTarget: Specify as `true` to highlight the target element with a bright outline.

* buttons: Overrides for buttons to show in the hint. This is an object which may contain the following properties:

  * next: Override config for the 'Next' button
  * previous: Override config for the 'Previous' button
  * stop: Config to add a 'Stop' button. By default the dialog close, or typing S button is used.

Other properties (eg [modal](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-modal) can be added to the object, and will be passed to the [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint) instance.

When using a HintFlow tutorial, pressing `N` will navigate to the next hint, `P` will navigate to the previous hint. Pressing `S` or `ESCAPE` will stop the tutorial.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[previousAction](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-previousAction)
The actions to take when the 'Previous' button is clicked.

By default, user interaction during these actions is disabled.

The property names are the actions to take, and the values are the configuration for that action.

[nextAction](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-nextAction)
The actions to take when the 'Next' button is clicked.

By default, user interaction during these actions is disabled.

The property names are the actions to take, and the values are the configuration for that action.

[keyMap](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-keyMap)
The mapping of key names to hint actions. The actions are `previous`, `next`, and `stop`. By default, the following key mappings are used:

* `P` for `previous`
* `N` for `next`
* `S` for `stop` The key mappings can be overridden by providing a `keyMap` config object.

[buttons](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-buttons)
Overrides for buttons to show in the hint.

By default, hints show a 'Next' button.

The last hint will show a 'Previous' button instead of 'Next'.

These buttons can be overridden by providing a `buttons` config object for the listed properties

[maxWait](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-maxWait)
How long in milliseconds to wait for a target to become available before giving up.

[highlightTarget](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-highlightTarget)
Specify as a truthy value to highlight the target element with a bright outline.

[autoNext](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-autoNext)
Either the number of milliseconds to wait before automatically moving to the next hint, or a CSS selector to wait for before moving to the next hint.

[target](https://bryntum.com/docs/gantt/api/Core/widget/Hint#config-target)
The target element to highlight, or a CSS selector to find the target element.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHint](https://bryntum.com/docs/gantt/api/Core/widget/Hint#property-isHint)
Identifies an object as an instance of [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint) class, or subclass thereof.

[isHint](https://bryntum.com/docs/gantt/api/Core/widget/Hint#property-isHint-static)
Identifies an object as an instance of [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint) class, or subclass thereof.

## Typedefs

Typedefs are type definitions for the class

[HintActions](https://bryntum.com/docs/gantt/api/Core/widget/Hint#typedef-HintActions)
An object which describes actions to take when navigating between hints.
