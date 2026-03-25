# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventCopyPaste.md

# [EventCopyPaste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste)

Allow using Ctrl/CMD + C/X and Ctrl/CMD + V to copy/cut and paste events.

This feature also adds entries to the [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu) for copying & cutting (see example below for how to configure) and to the [ScheduleMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleMenu) for pasting.

You can configure how a newly pasted record is named using [generateNewName](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-generateNewName).

If you want to highlight the paste location when clicking in the schedule, consider enabling the [ScheduleContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext) feature.

When used with Scheduler Pro, pasting will bypass any constraint set on the event to allow the copy to be assigned the targeted date.

This feature is **enabled** by default.

Customize menu items
--------------------

See [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu) and [ScheduleMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleMenu) for more info on customizing the menu items supplied by the feature. This snippet illustrates the concept:

```
// Custom copy text + remove cut option from event menu:
const scheduler = new Scheduler({
    features : {
        eventMenu : {
            items : {
                copyEvent : {
                    text : 'Copy booking'
                },
                cutEvent  : false
            }
        }
    }
});
```

Keyboard shortcuts
------------------

The feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Ctrl`+`C`

_copy_

Copies selected event(s) into the clipboard.

`Ctrl`+`X`

_cut_

Cuts out selected event(s) into the clipboard.

`Ctrl`+`V`

_paste_

Insert copied or cut event(s) from the clipboard.

Please note that Ctrl is the equivalent to Command and Alt is the equivalent to Option for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Scheduler/guides/customization/keymap.md).

Multi assigned events
---------------------

In a Scheduler that uses single assignment, copying and then pasting creates a clone of the event and assigns it to the target resource. Cutting and pasting moves the original event to the target resource.

In a Scheduler using multi assignment, the behaviour is slightly more complex. Cutting and pasting reassigns the event to the target, keeping other assignments of the same event intact. The behaviour for copying and pasting is configurable using the [copyPasteAction](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-copyPasteAction) config. It accepts two values:

* `'clone'` - The default, the event is cloned and the clone is assigned to the target resource. Very similar to the behaviour with single assignment (event count goes up by 1).
* `'assign'` - The original event is assigned to the target resource (event count is unaffected).

This snippet shows how to reconfigure it:

```
const scheduler = new Scheduler({
    features : {
        eventCopyPaste : {
            copyPasteAction : 'assign'
        }
    }
});
```

Copying multiple assignments of the same event will always result in all but the first assignment being removed on paste, since paste targets a single resource and an event can only be assigned to a resource once.

Native/shared clipboard
-----------------------

If you have multiple Schedulers (or other Bryntum products) on the same page, they will share clipboard. This makes it possible to copy and paste between different Scheduler instances. It is also possible to use the native Clipboard API if it is available and if you set [useNativeClipboard](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-useNativeClipboard) to `true`.

Regardless of native clipboard availability, copy-pasting "outside" of the current Scheduler instance will convert the copied events to a string. When pasting, the string will then be parsed back into events. In case of usage of the native Clipboard API, this means it is possible to copy and paste events between completely different applications.

To configure the fields that is converted and parsed from the copied string value, please see the [eventToStringFields](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-eventToStringFields) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nameField](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#config-nameField)
The field to use as the name field when updating the name of copied records

[copyPasteAction](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#config-copyPasteAction)
How to handle a copy paste operation when the host uses multi assignment. Either:

* `'clone'` - The default, clone the copied event, assigning the clone to the target resource.
* `'assign'` - Add an assignment for the existing event to the target resource.

For single assignment mode, it always uses the `'clone'` behaviour.

[eventToStringFields](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#config-eventToStringFields)
When copying events (or assignments), data will be sent to the clipboard as a tab (`\t`) and new-line (`\n`) separated string with field values for fields present in this config (in specified order). The default included fields are (in this order):

* name
* startDate
* endDate
* duration
* durationUnit
* allDay To override, provide your own array of fields:

```
new Scheduler({
    features : {
        eventCopyPaste : {
            eventToStringFields : [
               'name',
               'startDate',
               'endDate',
               'percentDone'
            ]
        }
    }
});
```

Please note that this config is both used for \*\*converting\*\* events to a string value and is also used to \*\*parse\*\* a string value to events.

[unifiedPaste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#config-unifiedPaste)
By default, pasting of multiple events will spread out according to the pattern it was copied. Set to `false` to paste into the same resource and same date.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventCopyPaste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#property-isEventCopyPaste)
Identifies an object as an instance of [EventCopyPaste](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste) class, or subclass thereof.

[isEventCopyPaste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#property-isEventCopyPaste-static)
Identifies an object as an instance of [EventCopyPaste](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[copyEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#function-copyEvents)
Copy events (when using single assignment mode) or assignments (when using multi assignment mode) to clipboard to paste later

[stringConverter](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#function-stringConverter)
Called from Clipboardable after writing a non-string value to the clipboard

[pasteEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#function-pasteEvents)
Paste events or assignments to specified date and resource

[stringParser](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#function-stringParser)
Called from Clipboardable after reading from clipboard, and it is determined that the clipboard data is "external"

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[copy](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#event-copy)
Fires on the owning Scheduler after a copy action is performed. Depending on if the EventStore is using [singleAssignment](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore#config-singleAssignment) or the configuration of [copyPasteAction](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-copyPasteAction), either the `eventRecords` or the `assignmentRecords` param will be populated with record copies.

[beforeCopy](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#event-beforeCopy)
Fires on the owning Scheduler before a copy action is performed, return `false` to prevent the action

[paste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#event-paste)
Fires on the owning Scheduler after a paste action is performed.

[pasteNotAllowed](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#event-pasteNotAllowed)
Fires on the owning Scheduler if a paste action is not allowed. Depending on if the EventStore is using [singleAssignment](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore#config-singleAssignment) or the configuration of [copyPasteAction](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-copyPasteAction), either the `eventRecords` or the `assignmentRecords` param will be populated with record copies.

[beforePaste](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventCopyPaste#event-beforePaste)
Fires on the owning Scheduler before a paste action is performed, return `false` to prevent the action. Depending on if the EventStore is using [singleAssignment](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore#config-singleAssignment) or the configuration of [copyPasteAction](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventCopyPaste#config-copyPasteAction), either the `eventRecords` or the `assignmentRecords` param will be populated with record copies.
