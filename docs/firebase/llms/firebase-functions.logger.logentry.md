# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.logentry.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.logger.logentry.md.txt

# logger.LogEntry interface

`LogEntry` represents a \[structured Cloud Logging\](https://cloud.google.com/logging/docs/structured-logging) entry. All keys aside from `severity` and `message` are included in the `jsonPayload` of the logged entry.

**Signature:**  

    export interface LogEntry 

## Properties

|                                                           Property                                                            |                                                        Type                                                        | Description |
|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------|
| [message](https://firebase.google.com/docs/reference/functions/firebase-functions.logger.logentry.md#loggerlogentrymessage)   | string                                                                                                             |             |
| [severity](https://firebase.google.com/docs/reference/functions/firebase-functions.logger.logentry.md#loggerlogentryseverity) | [LogSeverity](https://firebase.google.com/docs/reference/functions/firebase-functions.logger.md#loggerlogseverity) |             |

## logger.LogEntry.message

**Signature:**  

    message?: string;

## logger.LogEntry.severity

**Signature:**  

    severity: LogSeverity;