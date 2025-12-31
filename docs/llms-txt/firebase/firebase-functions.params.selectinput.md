# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.selectinput.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectinput.md.txt

# params.SelectInput interface

Specifies that a parameter's value should be determined by having the user select from a list of pre-canned options interactively at deploy time.

**Signature:**  

    export interface SelectInput<T = unknown> 

## Properties

|                                                                   Property                                                                   |                                                                                          Type                                                                                           | Description |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [select](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectinput.md#paramsselectinputselect) | { options: Array\<[SelectOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectoptions.md#paramsselectoptions_interface)\<T\>\>; } |             |

## params.SelectInput.select

**Signature:**  

    select: {
            options: Array<SelectOptions<T>>;
        };