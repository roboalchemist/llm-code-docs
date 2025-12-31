# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.selectoptions.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectoptions.md.txt

# params.SelectOptions interface

One of the options provided to a `SelectInput`, containing a value and optionally a human-readable label to display in the selection interface.

**Signature:**  

    export interface SelectOptions<T = unknown> 

## Properties

|                                                                    Property                                                                    |  Type  | Description |
|------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------|
| [label](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectoptions.md#paramsselectoptionslabel) | string |             |
| [value](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectoptions.md#paramsselectoptionsvalue) | T      |             |

## params.SelectOptions.label

**Signature:**  

    label?: string;

## params.SelectOptions.value

**Signature:**  

    value: T;