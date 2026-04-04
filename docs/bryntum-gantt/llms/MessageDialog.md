# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/MessageDialog.md

# [MessageDialog](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog)

A singleton class which shows common dialogs, similar to the native browser APIs (though these methods do not block the UI thread):

* [confirm](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#function-confirm) shows a confirmation dialog with Ok / Cancel buttons
* [alert](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#function-alert) shows a dialog with a message
* [prompt](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#function-prompt) shows a dialog with a text input field

## Properties

Properties are getters/setters or publicly accessible variables on this class

[okButton](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog#property-okButton)
The enum value for the OK button

[cancelButton](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog#property-cancelButton)
The enum value for the Cancel button

## Functions

Functions are methods available for calling on the class

[confirm](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog#function-confirm)
Shows a confirm dialog with "Ok" and "Cancel" buttons. The returned promise resolves passing the button identifier of the button that was pressed ([okButton](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#property-okButton) or [cancelButton](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#property-cancelButton)).

[alert](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog#function-alert)
Shows an alert popup with a message. The returned promise resolves when the button is clicked.

[prompt](https://bryntum.com/docs/gantt/api/Core/widget/MessageDialog#function-prompt)
Shows a popup with a basic [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) along with a message. The returned promise resolves when the dialog is closed and yields an Object with a `button` ([okButton](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#property-okButton) or [cancelButton](https://bryntum.com/docs/gantt/api/#Core/widget/MessageDialog#property-cancelButton)) and a `text` property with the text the user provided
