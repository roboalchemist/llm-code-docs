# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/base/EditBase.md

# [EditBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase)

Base class for EventEdit. Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[continueEditingOnEventClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-continueEditingOnEventClick)
By default, while editing, _all_ clicks outside the editor will cancel the edit.

Set to `true` to begin editing a new event when an event bar is clicked.

This is normally used in combination with a docked editor, allowing interaction with the scheduler/calendar while editing.

[saveAndCloseOnEnter](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-saveAndCloseOnEnter)
True to save and close this panel if ENTER is pressed in one of the input fields inside the panel.

[dateFormat](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-dateFormat)
This config parameter is passed to the `startDateField` and `endDateField` constructor.

[timeFormat](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-timeFormat)
This config parameter is passed to the `startTimeField` and `endTimeField` constructor.

[editorConfig](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-editorConfig)
Default editor configuration, which widgets it shows etc.

This is the entry point into configuring any aspect of the editor.

The [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) configuration of a Container is _deeply merged_ with its default `items` value. This means that you can specify an `editorConfig` object which configures the editor, or widgets inside the editor:

```
const scheduler = new Scheduler({
    features : {
        eventEdit  : {
            editorConfig : {
                autoClose : false,
                modal     : true,
                cls       : 'editor-widget-cls',
                items : {
                    resourceField : {
                        hidden : true
                    },
                    // Add our own event owner field at the top of the form.
                    // Weight -100 will make it sort top the top.
                    ownerField : {
                        weight : -100,
                        type   : 'usercombo',
                        name   : 'owner',
                        label  : 'Owner'
                    }
                },
                bbar : {
                    items : {
                        deleteButton : false
                    }
                }
            }
        }
    }
});
```

To configure the editor Panel to be docked, use the [drawer](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-drawer) config as shown below:

```
const scheduler = new Scheduler({
    features : {
        eventEdit  : {
            // Dock the editor to the inline-end side of the viewport
            editorConfig : {
                drawer : true
            }
        }
    }
});
```

[items](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-items)
An object to merge with the provided items config of the editor to override the configuration of provided fields, or add new fields.

To remove existing items, set corresponding keys to `null`:

```
const scheduler = new Scheduler({
    features : {
        eventEdit  : {
            items : {
                // Merged with provided config of the resource field
                resourceField : {
                    label : 'Calendar'
                },
                recurrenceCombo : null,
                owner : {
                    weight : -100, // Will sort above system-supplied fields which are weight 0
                    type   : 'usercombo',
                    name   : 'owner',
                    label  : 'Owner'
                }
            }
        }
    }
});
```

The provided fields are called

* `nameField`
* `resourceField`
* `startDateField`
* `startTimeField`
* `endDateField`
* `endTimeField`
* `recurrenceCombo`
* `editRecurrenceButton`

[weekStartDay](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#config-weekStartDay)
The week start day used in all date fields of the feature editor form by default. 0 means Sunday, 6 means Saturday. Defaults to the locale's week start day.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEditBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#property-isEditBase)
Identifies an object as an instance of [EditBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase) class, or subclass thereof.

[isEditBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#property-isEditBase-static)
Identifies an object as an instance of [EditBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onBeforeSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#function-onBeforeSave)
Template method, intended to be overridden. Called before the event record has been updated.

[onAfterSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#function-onAfterSave)
Template method, intended to be overridden. Called after the event record has been updated.

[updateRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#function-updateRecord)
Updates record being edited with values from the editor

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[afterEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/EditBase#event-afterEventEdit)
Fires on the owning Scheduler after editor is closed by any action - save, delete or cancel
