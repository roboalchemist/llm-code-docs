# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventEdit.md

# [EventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit)

Feature that displays a popup containing widgets for editing event data.

To customize its contents you can:

* Reconfigure built-in widgets by providing override configs in the [items](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase#config-items) config.
* Change the date format of the date & time fields: [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase#config-dateFormat) and [timeFormat](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase#config-timeFormat)
* Configure provided widgets in the editor and add your own in the [items](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/EditBase#config-items) config.
* Remove fields related to recurring events configuration (such as `recurrenceCombo`) by setting [showRecurringUI](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/RecurringEventEdit#config-showRecurringUI) config to `false`.
* Advanced: Reconfigure the whole editor widget using [editorConfig](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit#config-editorConfig)

Built-in widgets
----------------

The built-in widgets are:

Widget ref

Type

Weight

Description

`nameField`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

100

Edit name

`resourceField`

[ResourceCombo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceCombo)

200

Pick resource(s)

`startDateField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

300

Edit startDate (date part)

`startTimeField`

[TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)

400

Edit startDate (time part)

`endDateField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

500

Edit endDate (date part)

`endTimeField`

[TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)

600

Edit endDate (time part)

`recurrenceCombo`

[RecurrenceCombo](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/field/RecurrenceCombo)

700

Select recurrence rule (only visible if recurrence UI is enabled)

`editRecurrenceButton`

[RecurrenceLegendButton](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceLegendButton)

800

Edit the recurrence rule (only visible if recurrence is used)

`colorField` ¹

[EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField)

700

Choose background color for the event bar

**¹** Set the [showEventColorPickers](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-showEventColorPickers) config to `true` to enable this field

Date and time fields
--------------------

The date and time fields both keep the full date and time value of the event's start and end instant.

The date and time fields are [partner](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-partner) linked pairs. Changing one will update the other to keep the full date/time value.

The start and end instants of the event are kept consistent while editing. Changing the start date/time will adjust the end date/time to keep the same duration.

The [min](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-min) of the end fields is kept in sync to be no earlier than the start instant.

The built-in buttons are:

Widget ref

Type

Weight

Description

`saveButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Save event button on the bbar

`deleteButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Delete event button on the bbar

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel event editing button on the bbar

Removing a built-in item
------------------------

To remove a built-in widget, specify its `ref` as `null` in the `items` config:

```
const scheduler = new Scheduler({
    features : {
        eventEdit : {
            items : {
                // Remove the start time field
                startTimeField : null
            }
        }
    }
})
```

Bottom buttons may be hidden using the `bbar` config passed to `editorConfig`:

```
const scheduler = new Scheduler({
    features : {
        eventEdit : {
            editorConfig : {
                bbar : {
                    items : {
                        deleteButton : null
                    }
                }
            }
        }
    }
})
```

To remove fields related to recurring events configuration (such as `recurrenceCombo`), set [showRecurringUI](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/RecurringEventEdit#config-showRecurringUI) config to `false`.

Customizing a built-in widget
-----------------------------

To customize a built-in widget, use its `ref` as the key in the `items` config and specify the configs you want to change (they will merge with the widgets default configs):

```
const scheduler = new Scheduler({
    features : {
        eventEdit : {
            items : {
                // ref for an existing field
                nameField : {
                    // Change its label
                    label : 'Description'
                }
            }
        }
    }
})
```

Adding custom widgets
---------------------

To add a custom widget, add an entry to the `items` config. The `name` property links the input field to a field in the loaded event record:

```
const scheduler = new Scheduler({
    features : {
        eventEdit : {
            items : {
                // Key to use as fields ref (for easier retrieval later)
                color : {
                    type  : 'combo',
                    label : 'Color',
                    items : ['red', 'green', 'blue'],
                    // name will be used to link to a field in the event record when loading and saving in the editor
                    name  : 'eventColor'
                }
            }
        }
    }
})
```

Video guides
------------

[@youtube](https://bryntum.com/docs/gantt/api/https://youtube.com/embed/a0ikJn1tCmw)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/ghWLmifpO_4)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/o7xQ6B_Y04w)

[@youtube](https://bryntum.com/docs/gantt/api/https://www.youtube.com/embed/OuSH7YFndPE)

For more info on customizing the event editor, please see "Customize event editor" guide.

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[triggerEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-triggerEvent)
The event that shall trigger showing the editor. Defaults to `eventdblclick`, set to `''` or null to disable editing of existing events.

[ignoreSelector](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-ignoreSelector)
A CSS selector targeting elements that should not trigger the editor when clicked.

[typeField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-typeField)
The data field in the model that defines the eventType. Applied as class (b-event-type-xx) to the editors element, to allow showing/hiding fields depending on eventType. Dynamic toggling of fields in the editor is activated by adding an `eventTypeField` field to your widget:

```
const scheduler = new Scheduler({
   features : {
      eventEdit : {
          items : {
              eventTypeField : {
                 type  : 'combo',
                 name  : 'eventType',
                 label : 'Type',
                 items : ['Appointment', 'Internal', 'Meeting']
              }
          }
       }
    }
});
```

Note, your event model class also must declare this field:

```
 class MyEvent extends EventModel {
     static get fields() {
         return [
             { name : 'eventType' }
         ];
     }
 }
```

[readOnly](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-readOnly)
Specify `true` to put the editor in read only mode.

It will also be in read only mode if the Scheduler / Calendar is so, or if the event record is read only.

[editorConfig](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-editorConfig)
The configuration for the internal editor widget. With this config you can control the _type_ of editor (defaults to `Popup`) and which widgets to show, change the items in the `bbar`, or change whether the popup should be modal etc.

```
const scheduler = new Scheduler({
    features : {
        eventEdit  : {
            editorConfig : {
                modal  : true,
                cls    : 'my-editor' // A CSS class,
                items  : {
                    owner : {
                        weight : -100, // Will sort above system-supplied fields which are weight 100 to 800
                        type   : 'usercombo',
                        name   : 'owner',
                        label  : 'Owner'
                    },
                    agreement : {
                        weight : 1000, // Will sort below system-supplied fields which are weight 100 to 800
                        type   : 'checkbox',
                        name   : 'agreement',
                        label  : 'Agree to terms'
                    },
                    resourceField : {
                        // Apply a special filter to limit the Combo's access
                        // to resources.
                        store  {
                            filters : [{
                                filterBy(resource) {
                                    return shouldShowResource(record);
                                }
                            }]
                        }
                    }
                },
                bbar : {
                    items : {
                        deleteButton : {
                            hidden : true
                        }
                    }
                }
            }
        }
    }
});
```

Or to use your own custom editor:

```
const scheduler = new Scheduler({
    features : {
        eventEdit  : {
            editorConfig : {
                type : 'myCustomEditorType'
            }
        }
    }
});
```

[minEditSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#config-minEditSize)
How much of a long event bar which is clipped by scrolling must be brought into view to facilitate editing.

In a horizontal Scheduler, this will bring 100 pixels of width into view.

In a vertical Scheduler, this will bring 100 pixels of height into view.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-isEventEdit)
Identifies an object as an instance of [EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit) class, or subclass thereof.

[isEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-isEventEdit-static)
Identifies an object as an instance of [EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit) class, or subclass thereof.

[eventRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-eventRecord)
The current [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) record, which is being edited by the event editor.

[readOnly](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-readOnly)
Specify `true` to put the editor in read only mode.

It will also be in read only mode if the Scheduler / Calendar is so, or if the event record is read only.

[nameField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-nameField)
Reference to the name field, if used

[resourceField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-resourceField)
Reference to the resource field, if used

[startDateField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-startDateField)
Reference to the start date field, if used

[startTimeField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-startTimeField)
Reference to the start time field, if used

[endDateField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-endDateField)
Reference to the end date field, if used

[endTimeField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-endTimeField)
Reference to the end time field, if used

[saveButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-saveButton)
Reference to the save button, if used

[deleteButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-deleteButton)
Reference to the delete button, if used

[cancelButton](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-cancelButton)
Reference to the cancel button, if used

[minEditSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-minEditSize)
How much of a long event bar which is clipped by scrolling must be brought into view to facilitate editing.

In a horizontal Scheduler, this will bring 100 pixels of width into view.

In a vertical Scheduler, this will bring 100 pixels of height into view.

[editor](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-editor)
Returns the editor widget representing this feature

[isEditing](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#property-isEditing)
Returns true if the editor is currently active

## Functions

Functions are methods available for calling on the class

[editEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#function-editEvent)
Opens an editor for the passed event. This function is exposed on Scheduler and can be called as `scheduler.editEvent()`.

[loadRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#function-loadRecord)
Sets fields values from record being edited

[save](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#function-save)
Saves the changes (applies them to record if valid, if invalid editor stays open)

[deleteEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#function-deleteEvent)
Delete event being edited

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[eventEditBeforeSetRecord](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#event-eventEditBeforeSetRecord)
Fired before the editor will load the event record data into its input fields. This is useful if you want to modify the fields before data is loaded (e.g. set some input field to be readonly)

[beforeEventEditShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#event-beforeEventEditShow)
Fires on the owning Scheduler when the editor for an event is available but before it is populated with data and shown. Allows manipulating fields etc.

[beforeEventEdit](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#event-beforeEventEdit)
Fires on the owning Scheduler before an event is displayed in an editor. This may be listened for to allow an application to take over event editing duties. Returning `false` stops the default editing UI from being shown.

Be aware of that when returning `false`, your app must take care of the `eventRecord` lifecycle - for example by commiting it or removing it from the store.

[afterEventSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#event-afterEventSave)
Fires on the owning Scheduler after an event is successfully saved

[beforeEventSave](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventEdit#event-beforeEventSave)
Fires on the owning Scheduler before an event is saved. Return `false` to immediately prevent saving

```
 scheduler.on({
     beforeEventSave() {
         // prevent saving if some custom variable hasn't 123 value
         return myCustomValue === 123;
     }
 });
```

or a `Promise` yielding `true` or `false` for async vetoing.

```
 scheduler.on({
     beforeEventSave() {
         const
             // send ajax request
             response = await fetch('http://my-server/check-parameters.php'),
             data     = await response.json();

         // decide whether it's ok to save based on response "okToSave" property
         return data.okToSave;
     }
 });
```
