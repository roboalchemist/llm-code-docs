# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup.md

# [RecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup)

A confirmation dialog shown when modifying a recurring event or some of its occurrences. For recurring events, the dialog informs the user that the change will be applied to all occurrences.

For occurrences, the dialog lets the user choose if the change should affect all future occurrences, or this occurrence only.

Built-in widgets and buttons
----------------------------

The Popup does not contain any built-in widgets, but it has built-in buttons in the toolbar that you can customize:

Widget ref

Type

Weight

Description

`changeSingleButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Change a single event in a recurring sequence

`changeMultipleButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Change all future events in a recurring sequence

`cancelButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Cancel

Usage example:

```
const confirmation = new RecurrenceConfirmationPopup({
    bbar        : {
        items : {
            // Disable button
            changeSingleButton : {
                disabled : true
            }
        }
    }
});

confirmation.confirm({
    eventRecord : recurringEvent,
    actionType  : "delete",
    changerFn   : () => recurringEvent.remove(event)
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-isRecurrenceConfirmationPopup)
Identifies an object as an instance of [RecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup) class, or subclass thereof.

[isRecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-isRecurrenceConfirmationPopup-static)
Identifies an object as an instance of [RecurrenceConfirmationPopup](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup) class, or subclass thereof.

[changeMultipleButton](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeMultipleButton)
Reference to the "Apply changes to multiple occurrences" button, if used

[changeSingleButton](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeSingleButton)
Reference to the button that causes changing of the event itself only, if used

[cancelButton](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-cancelButton)
Reference to the cancel button, if used

## Functions

Functions are methods available for calling on the class

[onChangeMultipleButtonClick](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-onChangeMultipleButtonClick)
Handler for "Apply changes to multiple occurrences" [button](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeMultipleButton). It calls [processMultipleRecords](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-processMultipleRecords) and then hides the dialog.

[onChangeSingleButtonClick](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-onChangeSingleButtonClick)
Handler for the [button](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeSingleButton) that causes changing of the event itself only. It calls [processSingleRecord](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-processSingleRecord) and then hides the dialog.

[onCancelButtonClick](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-onCancelButtonClick)
Handler for [cancel button](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-cancelButton). It calls `cancelFn` provided to [confirm](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-confirm) call and then hides the dialog.

[confirm](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-confirm)
Displays the confirmation.

This function is async, and awaitable, resolving only when the process has been either completed or canceled Usage example:

```
const popup = new RecurrenceConfirmationPopup();

await popup.confirm({
    eventRecord,
    actionType : "delete",
    changerFn  : () => eventStore.remove(record)
});

Toast.show('Event deleted');
```

[processMultipleRecords](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-processMultipleRecords)
Applies changes to multiple occurrences as reaction on "Apply changes to multiple occurrences" [button](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeMultipleButton) click.

[processSingleRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/recurrence/RecurrenceConfirmationPopup#function-processSingleRecord)
Applies changes to a single record by making it a "real" event and adding an exception to the recurrence. The method is called as reaction on clicking the [button](https://bryntum.com/docs/gantt/api/#Scheduler/view/recurrence/RecurrenceConfirmationPopup#property-changeSingleButton) that causes changing of the event itself only.
