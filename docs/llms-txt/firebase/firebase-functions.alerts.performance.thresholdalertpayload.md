# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md.txt

# alerts.performance.ThresholdAlertPayload interface

The internal payload object for a performance threshold alert. Payload is wrapped inside a object.

**Signature:**  

    export interface ThresholdAlertPayload 

## Properties

|                                                                                                     Property                                                                                                      |  Type  |                                                                                                     Description                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [appVersion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadappversion)                   | string | The app version this alert was triggered for, can be omitted if the alert is for a network request (because the alert was checked against data from all versions of app) or a web app (where the app is versionless) |
| [conditionPercentile](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadconditionpercentile) | number | The percentile of the alert condition, can be 0 if percentile is not applicable to the alert condition and omitted; range: \[1, 100\]                                                                                |
| [eventName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadeventname)                     | string | Name of the trace or network request this alert is for (e.g. my_custom_trace, firebase.com/api/123)                                                                                                                  |
| [eventType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadeventtype)                     | string | The resource type this alert is for (i.e. trace, network request, screen rendering, etc.)                                                                                                                            |
| [investigateUri](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadinvestigateuri)           | string | The link to Fireconsole to investigate more into this alert                                                                                                                                                          |
| [metricType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadmetrictype)                   | string | The metric type this alert is for (i.e. success rate, response time, duration, etc.)                                                                                                                                 |
| [numSamples](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadnumsamples)                   | number | The number of events checked for this alert condition                                                                                                                                                                |
| [thresholdUnit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadthresholdunit)             | string | The unit for the alert threshold (e.g. "percent", "seconds")                                                                                                                                                         |
| [thresholdValue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadthresholdvalue)           | number | The threshold value of the alert condition without units (e.g. "75", "2.1")                                                                                                                                          |
| [violationUnit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadviolationunit)             | string | The unit for the violation value (e.g. "percent", "seconds")                                                                                                                                                         |
| [violationValue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayloadviolationvalue)           | number | The value that violated the alert condition (e.g. "76.5", "3")                                                                                                                                                       |

## alerts.performance.ThresholdAlertPayload.appVersion

The app version this alert was triggered for, can be omitted if the alert is for a network request (because the alert was checked against data from all versions of app) or a web app (where the app is versionless)

**Signature:**  

    appVersion?: string;

## alerts.performance.ThresholdAlertPayload.conditionPercentile

The percentile of the alert condition, can be 0 if percentile is not applicable to the alert condition and omitted; range: \[1, 100\]

**Signature:**  

    conditionPercentile?: number;

## alerts.performance.ThresholdAlertPayload.eventName

Name of the trace or network request this alert is for (e.g. my_custom_trace, firebase.com/api/123)

**Signature:**  

    eventName: string;

## alerts.performance.ThresholdAlertPayload.eventType

The resource type this alert is for (i.e. trace, network request, screen rendering, etc.)

**Signature:**  

    eventType: string;

## alerts.performance.ThresholdAlertPayload.investigateUri

The link to Fireconsole to investigate more into this alert

**Signature:**  

    investigateUri: string;

## alerts.performance.ThresholdAlertPayload.metricType

The metric type this alert is for (i.e. success rate, response time, duration, etc.)

**Signature:**  

    metricType: string;

## alerts.performance.ThresholdAlertPayload.numSamples

The number of events checked for this alert condition

**Signature:**  

    numSamples: number;

## alerts.performance.ThresholdAlertPayload.thresholdUnit

The unit for the alert threshold (e.g. "percent", "seconds")

**Signature:**  

    thresholdUnit: string;

## alerts.performance.ThresholdAlertPayload.thresholdValue

The threshold value of the alert condition without units (e.g. "75", "2.1")

**Signature:**  

    thresholdValue: number;

## alerts.performance.ThresholdAlertPayload.violationUnit

The unit for the violation value (e.g. "percent", "seconds")

**Signature:**  

    violationUnit: string;

## alerts.performance.ThresholdAlertPayload.violationValue

The value that violated the alert condition (e.g. "76.5", "3")

**Signature:**  

    violationValue: number;