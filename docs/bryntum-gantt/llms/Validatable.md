# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Validatable.md

# [Validatable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable)

This mixin provides validation functionality to [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field).

Not to be used directly.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isValidatable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#property-isValidatable)
Identifies an object as an instance of [Validatable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Validatable) class, or subclass thereof.

[isValidatable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#property-isValidatable-static)
Identifies an object as an instance of [Validatable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Validatable) class, or subclass thereof.

[errorTip](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#property-errorTip)
A singleton error tooltip which activates on hover of invalid fields. before show, it gets a reference to the field and interrogates its active error list to display as the tip content.

[errorTip](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#property-errorTip-static)
A singleton error tooltip which activates on hover of invalid fields. before show, it gets a reference to the field and interrogates its active error list to display as the tip content.

Please note: Not applicable when using widgets inside a shadow root

## Functions

Functions are methods available for calling on the class

[setError](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#function-setError)
Adds an error message to the list of errors on this field. By default, the field's valid/invalid state is updated; pass `false` as the second parameter to disable that if multiple changes are being made to the error state.

Note, that you need to manually remove the added error with the [clearError](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Validatable#function-clearError) method to "release" the normal data update process (invalid data won't be synced). You can also use the 3rd argument of this method to automatically remove the error upon the next user interaction.

[clearError](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#function-clearError)
Removes an error message from the list of errors on this field.

By default, the field's valid/invalid state is updated; pass `false` as the second parameter to disable that if multiple changes are being made to the error state.

[getErrors](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Validatable#function-getErrors)
Returns an array of error messages as set by [setError](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Validatable#function-setError), or `undefined` if there are currently no errors.
