# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.micropercentrange.md.txt

# MicroPercentRange interface

Represents the limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\]

**Signature:**  

    export interface MicroPercentRange 

## Properties

|                                                                                 Property                                                                                  |  Type  |                                                   Description                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------|
| [microPercentLowerBound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.micropercentrange.md#micropercentrangemicropercentlowerbound) | number | The lower limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\]. |
| [microPercentUpperBound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.micropercentrange.md#micropercentrangemicropercentupperbound) | number | The upper limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\]. |

## MicroPercentRange.microPercentLowerBound

The lower limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\].

**Signature:**  

    microPercentLowerBound?: number;

## MicroPercentRange.microPercentUpperBound

The upper limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\].

**Signature:**  

    microPercentUpperBound?: number;