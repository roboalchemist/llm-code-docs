# Source: https://firebase.google.com/docs/reference/js/performance.performancesettings.md.txt

# PerformanceSettings interface

Defines configuration options for the Performance Monitoring SDK.

**Signature:**  

    export interface PerformanceSettings 

## Properties

|                                                                       Property                                                                       |  Type   |                Description                |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------------------|
| [dataCollectionEnabled](https://firebase.google.com/docs/reference/js/performance.performancesettings.md#performancesettingsdatacollectionenabled)   | boolean | Whether to collect custom events.         |
| [instrumentationEnabled](https://firebase.google.com/docs/reference/js/performance.performancesettings.md#performancesettingsinstrumentationenabled) | boolean | Whether to collect out of the box events. |

## PerformanceSettings.dataCollectionEnabled

Whether to collect custom events.

**Signature:**  

    dataCollectionEnabled?: boolean;

## PerformanceSettings.instrumentationEnabled

Whether to collect out of the box events.

**Signature:**  

    instrumentationEnabled?: boolean;