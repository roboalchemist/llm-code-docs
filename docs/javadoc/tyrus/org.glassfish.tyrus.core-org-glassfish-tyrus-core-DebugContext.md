Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class DebugContext

java.lang.Object
org.glassfish.tyrus.core.DebugContext

---

public class DebugContext
extends Object
A `Logger` wrapper that gives logging records a common formatting and temporarily stores log
 records and postpones their logging until they can be provided with a session ID. After a session ID has been
 provided, messages are logged immediately.

 Log records are provided with a session ID, so that log records from a single upgrade request can be easily linked
 together in a log of a busy server or client.

Author:
Petr Janouch

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum`
`DebugContext.TracingThreshold`

Tracing threshold - used for configuration granularity of information that will be sent in tracing headers.

`static enum`
`DebugContext.TracingType`

Type of tracing - used for tracing configuration.

`static enum`
`DebugContext.Type`

Type of the record - used to graphically distinguish these message types in the log.

-

## Constructor Summary

Constructors

Constructor
Description
`DebugContext()`

Constructor that configures tracing to be OFF.

`DebugContext(DebugContext.TracingThreshold tracingThreshold)`

Constructor that configures tracing to be ON and accepts tracing threshold as a parameter.

-

## Method Summary

Modifier and Type
Method
Description
`void`
`appendLogMessage(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Object... messageParts)`

Append a message to the log, the logging will be postponed until the message can be provided with a session ID.

`void`
`appendLogMessageWithThrowable(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Throwable t,
 Object... messageParts)`

Append a message to the log, the logging will be postponed until the message can be provided with a session ID.

`void`
`appendStandardOutputMessage(DebugContext.Type type,
 String message)`

Write a message to the standard output, the logging will be postponed until the message can be provided with
 a session ID.

`void`
`appendTraceMessage(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Object... messageParts)`

Append a message to the log and to the list of trace messages that are sent in handshake response.

`void`
`appendTraceMessageWithThrowable(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Throwable t,
 Object... messageParts)`

Append a message to the log and to the list of trace messages that are sent in handshake response.

`void`
`flush()`

Write pending messages to the log.

`Map<String,List<String>>`
`getTracingHeaders()`

Get headers containing tracing messages.

`void`
`setSessionId(String sessionId)`

Set a session ID that will be used as a common identifier for logged messages related to the same upgrade
 request.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### DebugContext

public DebugContext(DebugContext.TracingThreshold tracingThreshold)
Constructor that configures tracing to be ON and accepts tracing threshold as a parameter.

Parameters:
`tracingThreshold` - tracing threshold.

-

### DebugContext

public DebugContext()
Constructor that configures tracing to be OFF.

-

## Method Details

-

### appendLogMessage

public void appendLogMessage(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Object... messageParts)
Append a message to the log, the logging will be postponed until the message can be provided with a session ID.
 Randomly generated session ID is used if a session has not been created.

Parameters:
`logger` - logger to be used to log the message.
`loggingLevel` - message level.
`type` - type of the message.
`messageParts` - message parts that will be concatenated to create a log message.

-

### appendTraceMessage

public void appendTraceMessage(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Object... messageParts)
Append a message to the log and to the list of trace messages that are sent in handshake response.
 The logging will be postponed until the message can be provided with a session ID. Randomly generated session ID
 is used if a session has not been created.

Parameters:
`logger` - logger to be used to log the message.
`loggingLevel` - message level.
`type` - type of the message.
`messageParts` - message parts that will be stringified and concatenated to create a log message.

-

### appendLogMessageWithThrowable

public void appendLogMessageWithThrowable(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Throwable t,
 Object... messageParts)
Append a message to the log, the logging will be postponed until the message can be provided with a session ID.
 Randomly generated session ID is used if a session has not been created.

Parameters:
`logger` - logger to be used to log the message.
`loggingLevel` - message level.
`type` - type of the message.
`t` - throwable that has been thrown.
`messageParts` - message parts that will be stringified and concatenated to create a log message.

-

### appendTraceMessageWithThrowable

public void appendTraceMessageWithThrowable(Logger logger,
 Level loggingLevel,
 DebugContext.Type type,
 Throwable t,
 Object... messageParts)
Append a message to the log and to the list of trace messages that are sent in handshake response.
 The logging will be postponed until the message can be provided with a session ID. Randomly generated session ID
 is used if a session has not been created.

Parameters:
`logger` - logger to be used to log the message.
`loggingLevel` - message level.
`type` - type of the message.
`t` - throwable that has been thrown.
`messageParts` - message parts that will be stringified and concatenated to create a log message.

-

### appendStandardOutputMessage

public void appendStandardOutputMessage(DebugContext.Type type,
 String message)
Write a message to the standard output, the logging will be postponed until the message can be provided with
 a session ID. Randomly generated session ID is used if a session has not been created.

Parameters:
`type` - type of the message.
`message` - message to be logged.

-

### setSessionId

public void setSessionId(String sessionId)
Set a session ID that will be used as a common identifier for logged messages related to the same upgrade
 request. Setting the session ID will cause the pending messages to be written into the log.

Parameters:
`sessionId` - session ID.

-

### flush

public void flush()
Write pending messages to the log.

-

### getTracingHeaders

public Map<String,List<String>> getTracingHeaders()
Get headers containing tracing messages.

Returns:
tracing headers.
