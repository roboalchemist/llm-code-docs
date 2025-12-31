# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.logger.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md.txt

# logger namespace

## Functions

|                                                          Function                                                          |                                                                  Description                                                                   |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [debug(args)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerdebug)  | Writes a `DEBUG` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.   |
| [error(args)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggererror)  | Writes an `ERROR` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.  |
| [info(args)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerinfo)    | Writes an `INFO` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.   |
| [log(args)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerlog)      | Writes an `INFO` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.   |
| [warn(args)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerwarn)    | Writes a `WARNING` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry. |
| [write(entry)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerwrite) | Writes a `LogEntry` to `stdout`/`stderr` (depending on severity).                                                                              |

## Interfaces

|                                                                  Interface                                                                   |                                                                                                        Description                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LogEntry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.logentry.md#loggerlogentry_interface) | `LogEntry` represents a \[structured Cloud Logging\](https://cloud.google.com/logging/docs/structured-logging) entry. All keys aside from `severity` and `message` are included in the `jsonPayload` of the logged entry. |

## Type Aliases

|                                                           Type Alias                                                            |                                                                              Description                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LogSeverity](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.md#loggerlogseverity) | `LogSeverity` indicates the detailed severity of the log entry. See \[LogSeverity\](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). |

## logger.debug()

Writes a `DEBUG` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.

**Signature:**  

    export declare function debug(...args: any[]): void;

### Parameters

| Parameter |  Type   |                             Description                             |
|-----------|---------|---------------------------------------------------------------------|
| args      | any\[\] | Arguments, concatenated into the log message with space separators. |

**Returns:**

void

## logger.error()

Writes an `ERROR` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.

**Signature:**  

    export declare function error(...args: any[]): void;

### Parameters

| Parameter |  Type   |                             Description                             |
|-----------|---------|---------------------------------------------------------------------|
| args      | any\[\] | Arguments, concatenated into the log message with space separators. |

**Returns:**

void

## logger.info()

Writes an `INFO` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.

**Signature:**  

    export declare function info(...args: any[]): void;

### Parameters

| Parameter |  Type   |                             Description                             |
|-----------|---------|---------------------------------------------------------------------|
| args      | any\[\] | Arguments, concatenated into the log message with space separators. |

**Returns:**

void

## logger.log()

Writes an `INFO` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.

**Signature:**  

    export declare function log(...args: any[]): void;

### Parameters

| Parameter |  Type   |                             Description                             |
|-----------|---------|---------------------------------------------------------------------|
| args      | any\[\] | Arguments, concatenated into the log message with space separators. |

**Returns:**

void

## logger.warn()

Writes a `WARNING` severity log. If the last argument provided is a plain object, it is added to the `jsonPayload` in the Cloud Logging entry.

**Signature:**  

    export declare function warn(...args: any[]): void;

### Parameters

| Parameter |  Type   |                             Description                             |
|-----------|---------|---------------------------------------------------------------------|
| args      | any\[\] | Arguments, concatenated into the log message with space separators. |

**Returns:**

void

## logger.write()

Writes a `LogEntry` to `stdout`/`stderr` (depending on severity).

**Signature:**  

    export declare function write(entry: LogEntry): void;

### Parameters

| Parameter |                                                                     Type                                                                     |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| entry     | [LogEntry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger.logentry.md#loggerlogentry_interface) | The `LogEntry` including severity, message, and any additional structured metadata. |

**Returns:**

void

## logger.LogSeverity

`LogSeverity` indicates the detailed severity of the log entry. See \[LogSeverity\](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).

**Signature:**  

    export type LogSeverity = "DEBUG" | "INFO" | "NOTICE" | "WARNING" | "ERROR" | "CRITICAL" | "ALERT" | "EMERGENCY";