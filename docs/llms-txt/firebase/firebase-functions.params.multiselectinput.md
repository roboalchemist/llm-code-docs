# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.multiselectinput.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.multiselectinput.md.txt

# params.MultiSelectInput interface

Specifies that a parameter's value should be determined by having the user select a subset from a list of pre-canned options interactively at deploy time. Will result in errors if used on parameters of type other than `string[]`.

**Signature:**  

    export interface MultiSelectInput 

## Properties

|                                                                      Property                                                                       |                                                                                      Type                                                                                       | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [multiSelect](https://firebase.google.com/docs/reference/functions/firebase-functions.params.multiselectinput.md#paramsmultiselectinputmultiselect) | { options: Array\<[SelectOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.params.selectoptions.md#paramsselectoptions_interface)\<string\>\>; } |             |

## params.MultiSelectInput.multiSelect

**Signature:**  

    multiSelect: {
            options: Array<SelectOptions<string>>;
        };