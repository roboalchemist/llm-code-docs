# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/HintFlow.md

# [HintFlow](https://bryntum.com/docs/gantt/api/Core/util/HintFlow)

A class which shows a user a series of educational [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint) popups in a flow. Each hint in the flow is shown in sequence attached to a target element. The user can navigate through the hints using buttons or keyboard shortcuts (N for next, P for previous, S or ESCAPE to stop).

It must be configured with an array of hint configurations. Each configuration is a config object for a [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint). Each hint in the flow may be configured with [content](https://bryntum.com/docs/gantt/api/#Core/widget/Hint#config-content) or [title](https://bryntum.com/docs/gantt/api/#Core/widget/Hint#config-title) to show contextual information for its `target`:

```
new HintFlow({
    // Default configs to apply to all hints
    defaults : {
        modal : true
    },
    hints : [{
        // CSS selector to find the target element
        target  : '.b-tab-panel-tab[data-item-index="1"]',

        // Action to take when the 'Next' button is clicked
        nextAction : {
            click : '.b-tab-panel-tab[data-item-index="1"]'
        }

        // Config props for the displayed Hint popup
        title   : 'Change tab',
        content : 'Click here to move to the next tab',
        align   : 't-n'
    }, {
        target  : '.b-tabpanel .b-tabpanel-body :nth-child(2) input',
        title   : 'Change name',
        content : 'Enter the new name here',
        nextAction : {
              text : 'New name[Enter]'
        }
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
  * contextmenu: A CSS selector to find the target element to right click.
  * dblclick: A CSS selector to find the target element to double click.
  * type: A string to type into the target element.
  * fn: A function to call when the hint is shown.
  * drag: An object with the following properties:
    * target: The target element to drag, or a CSS selector to find the target element.
    * by: The distance to drag the target element, as an array of `[dx, dy]`.
  * waitFor: A CSS selector to wait for or the number of milliseconds to wait before continuing to the next hint.
  * allowInteraction: Specify as `true` to allow the user to interact with the target element.
* previousAction: The action(s) to take when the 'Previous' button is clicked.

* autoNext: The number of milliseconds to wait before automatically moving to the next hint, or a CSS selector to find the target element to wait for.

* highlightTarget: Specify as `true` to highlight the target element with a bright outline.

* buttons: Overrides for buttons to show in the hint. This is an object which may contain the following properties:

  * next: Override config for the 'Next' button
  * previous: Override config for the 'Previous' button
  * stop: Config to add a 'Stop' button. By default the dialog close, or typing S button is used.

Other properties (eg [modal](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-modal) can be added to the object, and will be passed to the [Hint](https://bryntum.com/docs/gantt/api/#Core/widget/Hint) instance.

Pressing `N` will navigate to the next hint. `P` will navigate to the previous hint. Pressing `S` or `ESCAPE` will stop the tutorial. These defaults can be changed by setting the `keyMap` property in the [defaults](https://bryntum.com/docs/gantt/api/#Core/util/HintFlow#config-defaults) object.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[hints](https://bryntum.com/docs/gantt/api/Core/util/HintFlow#config-hints)
The array of hint configurations to show in the flow.

[defaults](https://bryntum.com/docs/gantt/api/Core/util/HintFlow#config-defaults)
An object containing configuration properties to be applied to all hints in the flow.

An example may be to set the `modal` property to `true` to make all hints modal, or to set up keyboard shortcuts for the flow:

```
new HintFlow({
    defaults : {
        modal  : true,
        keyMap : {
            'A' : 'next',
            'B' : 'previous',
            'C' : 'stop'
        }
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHintFlow](https://bryntum.com/docs/gantt/api/Core/util/HintFlow#property-isHintFlow)
Identifies an object as an instance of [HintFlow](https://bryntum.com/docs/gantt/api/#Core/util/HintFlow) class, or subclass thereof.

[isHintFlow](https://bryntum.com/docs/gantt/api/Core/util/HintFlow#property-isHintFlow-static)
Identifies an object as an instance of [HintFlow](https://bryntum.com/docs/gantt/api/#Core/util/HintFlow) class, or subclass thereof.
