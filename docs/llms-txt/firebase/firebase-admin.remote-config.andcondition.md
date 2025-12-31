# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.andcondition.md.txt

# AndCondition interface

Represents a collection of conditions that evaluate to true if all are true.

**Signature:**  

    export interface AndCondition 

## Properties

|                                                                Property                                                                 |                                                                           Type                                                                           |          Description          |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [conditions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.andcondition.md#andconditionconditions) | Array\<[OneOfCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofcondition_interface)\> | The collection of conditions. |

## AndCondition.conditions

The collection of conditions.

**Signature:**  

    conditions?: Array<OneOfCondition>;