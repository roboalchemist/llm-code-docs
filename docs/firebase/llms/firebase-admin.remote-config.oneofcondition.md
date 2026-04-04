# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md.txt

# OneOfCondition interface

Represents a condition that may be one of several types. Only the first defined field will be processed.

**Signature:**  

    export interface OneOfCondition 

## Properties

|                                                                    Property                                                                     |                                                                                 Type                                                                                 |                   Description                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [andCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditionandcondition) | [AndCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.andcondition.md#andcondition_interface)                            | Makes this condition an AND condition.          |
| [customSignal](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditioncustomsignal) | [CustomSignalCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md#customsignalcondition_interface) | Makes this condition a custom signal condition. |
| [false](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditionfalse)               | Record\<string, never\>                                                                                                                                              | Makes this condition a constant false.          |
| [orCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditionorcondition)   | [OrCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.orcondition.md#orcondition_interface)                               | Makes this condition an OR condition.           |
| [percent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditionpercent)           | [PercentCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentcondition_interface)                | Makes this condition a percent condition.       |
| [true](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofconditiontrue)                 | Record\<string, never\>                                                                                                                                              | Makes this condition a constant true.           |

## OneOfCondition.andCondition

Makes this condition an AND condition.

**Signature:**  

    andCondition?: AndCondition;

## OneOfCondition.customSignal

Makes this condition a custom signal condition.

**Signature:**  

    customSignal?: CustomSignalCondition;

## OneOfCondition.false

Makes this condition a constant false.

**Signature:**  

    false?: Record<string, never>;

## OneOfCondition.orCondition

Makes this condition an OR condition.

**Signature:**  

    orCondition?: OrCondition;

## OneOfCondition.percent

Makes this condition a percent condition.

**Signature:**  

    percent?: PercentCondition;

## OneOfCondition.true

Makes this condition a constant true.

**Signature:**  

    true?: Record<string, never>;