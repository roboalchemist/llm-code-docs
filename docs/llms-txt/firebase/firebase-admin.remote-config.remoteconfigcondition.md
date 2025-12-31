# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md.txt

# RemoteConfigCondition interface

Interface representing a Remote Config condition. A condition targets a specific group of users. A list of these conditions make up part of a Remote Config template.

**Signature:**  

    export interface RemoteConfigCondition 

## Properties

|                                                                         Property                                                                          |                                                    Type                                                    |                                                                                             Description                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [expression](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md#remoteconfigconditionexpression) | string                                                                                                     | The logic of this condition. See the documentation on [condition expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field.            |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md#remoteconfigconditionname)             | string                                                                                                     | A non-empty and unique name of this condition.                                                                                                                                                      |
| [tagColor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md#remoteconfigconditiontagcolor)     | [TagColor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#tagcolor) | The color associated with this condition for display purposes in the Firebase Console. Not specifying this value results in the console picking an arbitrary color to associate with the condition. |

## RemoteConfigCondition.expression

The logic of this condition. See the documentation on [condition expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field.

**Signature:**  

    expression: string;

## RemoteConfigCondition.name

A non-empty and unique name of this condition.

**Signature:**  

    name: string;

## RemoteConfigCondition.tagColor

The color associated with this condition for display purposes in the Firebase Console. Not specifying this value results in the console picking an arbitrary color to associate with the condition.

**Signature:**  

    tagColor?: TagColor;