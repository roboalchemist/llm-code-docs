# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md.txt

# CustomSignalCondition interface

Represents a condition that compares provided signals against a target value.

**Signature:**  

    export interface CustomSignalCondition 

## Properties

|                                                                                       Property                                                                                        |                                                                Type                                                                |                                                    Description                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [customSignalKey](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md#customsignalconditioncustomsignalkey)                   | string                                                                                                                             | The key of the signal set in the EvaluationContext                                                                 |
| [customSignalOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md#customsignalconditioncustomsignaloperator)         | [CustomSignalOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#customsignaloperator) | The choice of custom signal operator to determine how to compare targets to value(s).                              |
| [targetCustomSignalValues](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md#customsignalconditiontargetcustomsignalvalues) | string\[\]                                                                                                                         | A list of at most 100 target custom signal values. For numeric operators, this will have exactly ONE target value. |

## CustomSignalCondition.customSignalKey

The key of the signal set in the EvaluationContext

**Signature:**  

    customSignalKey?: string;

## CustomSignalCondition.customSignalOperator

The choice of custom signal operator to determine how to compare targets to value(s).

**Signature:**  

    customSignalOperator?: CustomSignalOperator;

## CustomSignalCondition.targetCustomSignalValues

A list of at most 100 target custom signal values. For numeric operators, this will have exactly ONE target value.

**Signature:**  

    targetCustomSignalValues?: string[];