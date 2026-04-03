# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.namedcondition.md.txt

# NamedCondition interface

Represents a Remote Config condition in the dataplane. A condition targets a specific group of users. A list of these conditions comprise part of a Remote Config template.

**Signature:**  

    export interface NamedCondition 

## Properties

|                                                                 Property                                                                  |                                                                      Type                                                                       |                                                                                       Description                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [condition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.namedcondition.md#namedconditioncondition) | [OneOfCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofcondition_interface) | The logic of this condition. See the documentation on [condition expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field. |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.namedcondition.md#namedconditionname)           | string                                                                                                                                          | A non-empty and unique name of this condition.                                                                                                                                           |

## NamedCondition.condition

The logic of this condition. See the documentation on [condition expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field.

**Signature:**  

    condition: OneOfCondition;

## NamedCondition.name

A non-empty and unique name of this condition.

**Signature:**  

    name: string;