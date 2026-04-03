# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md.txt

# PercentCondition interface

Represents a condition that compares the instance pseudo-random percentile to a given limit.

**Signature:**  

    export interface PercentCondition 

## Properties

|                                                                           Property                                                                            |                                                                           Type                                                                           |                                                                                                            Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [microPercent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentconditionmicropercent)           | number                                                                                                                                                   | The limit of percentiles to target in micro-percents when using the LESS_OR_EQUAL and GREATER_THAN operators. The value must be in the range \[0 and 100000000\].                                                                  |
| [microPercentRange](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentconditionmicropercentrange) | [MicroPercentRange](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.micropercentrange.md#micropercentrange_interface) | The micro-percent interval to be used with the BETWEEN operator.                                                                                                                                                                   |
| [percentOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentconditionpercentoperator)     | [PercentConditionOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#percentconditionoperator)               | The choice of percent operator to determine how to compare targets to percent(s).                                                                                                                                                  |
| [seed](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentconditionseed)                           | string                                                                                                                                                   | The seed used when evaluating the hash function to map an instance to a value in the hash space. This is a string which can have 0 - 32 characters and can contain ASCII characters \[-_.0-9a-zA-Z\].The string is case-sensitive. |

## PercentCondition.microPercent

The limit of percentiles to target in micro-percents when using the LESS_OR_EQUAL and GREATER_THAN operators. The value must be in the range \[0 and 100000000\].

**Signature:**  

    microPercent?: number;

## PercentCondition.microPercentRange

The micro-percent interval to be used with the BETWEEN operator.

**Signature:**  

    microPercentRange?: MicroPercentRange;

## PercentCondition.percentOperator

The choice of percent operator to determine how to compare targets to percent(s).

**Signature:**  

    percentOperator?: PercentConditionOperator;

## PercentCondition.seed

The seed used when evaluating the hash function to map an instance to a value in the hash space. This is a string which can have 0 - 32 characters and can contain ASCII characters \[-_.0-9a-zA-Z\].The string is case-sensitive.

**Signature:**  

    seed?: string;