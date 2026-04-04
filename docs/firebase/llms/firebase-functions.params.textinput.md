# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.textinput.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.textinput.md.txt

# params.TextInput interface

Specifies that a parameter's value should be determined by prompting the user to type it in interactively at deploy time. Input that does not match the provided validationRegex, if present, will be retried.

**Signature:**  

    export interface TextInput<T = unknown> 

## Properties

|                                                        Property                                                         |                                            Type                                            | Description |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-------------|
| [text](https://firebase.google.com/docs/reference/functions/firebase-functions.params.textinput.md#paramstextinputtext) | { example?: string; validationRegex?: string \| RegExp; validationErrorMessage?: string; } |             |

## params.TextInput.text

**Signature:**  

    text: {
            example?: string;
            validationRegex?: string | RegExp;
            validationErrorMessage?: string;
        };