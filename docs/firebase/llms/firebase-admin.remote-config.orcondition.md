# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.orcondition.md.txt

# OrCondition interface

Represents a collection of conditions that evaluate to true if any are true.

**Signature:**  

    export interface OrCondition 

## Properties

|                                                               Property                                                                |                                                                           Type                                                                           |          Description          |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [conditions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.orcondition.md#orconditionconditions) | Array\<[OneOfCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofcondition_interface)\> | The collection of conditions. |

## OrCondition.conditions

The collection of conditions.

**Signature:**  

    conditions?: Array<OneOfCondition>;