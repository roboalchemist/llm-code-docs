# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.logger.md.txt

# firebase_functions.logger module

Logger module for Firebase Functions.

## Classes

|                                                                                                                                                                   ### LogEntry *class* firebase_functions.logger.LogEntry                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: TypedDict LogEntry represents a log entry. See [LogEntry](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). message*: NotRequired\[str\]* : severity*: Required\[[LogSeverity](https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.logger#firebase_functions.logger.LogSeverity "firebase_functions.logger.LogSeverity")\]* : |

|                                                                                                                                            ### LogSeverity *class* firebase_functions.logger.LogSeverity(*value* )                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: str, Enum LogSeverity indicates the detailed severity of the log entry. See LogSeverity \<https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity\>. ALERT*= 'ALERT'* : CRITICAL*= 'CRITICAL'* : DEBUG*= 'DEBUG'* : EMERGENCY*= 'EMERGENCY'* : ERROR*= 'ERROR'* : INFO*= 'INFO'* : NOTICE*= 'NOTICE'* : WARNING*= 'WARNING'* : |

## Functions

| ### debug firebase_functions.logger.debug(*\*args* , *\*\*kwargs* ) â None |
|----------------------------------------------------------------------------|
| Logs a debug message.                                                      |

| ### error firebase_functions.logger.error(*\*args* , *\*\*kwargs* ) â None |
|----------------------------------------------------------------------------|
| Logs an error message.                                                     |

| ### info firebase_functions.logger.info(*\*args* , *\*\*kwargs* ) â None |
|--------------------------------------------------------------------------|
| Logs an info message.                                                    |

| ### log firebase_functions.logger.log(*\*args* , *\*\*kwargs* ) â None |
|------------------------------------------------------------------------|
| Logs a log message.                                                    |

| ### warn firebase_functions.logger.warn(*\*args* , *\*\*kwargs* ) â None |
|--------------------------------------------------------------------------|
| Logs a warning message.                                                  |

| ### write firebase_functions.logger.write(*entry: [LogEntry](https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.logger#firebase_functions.logger.LogEntry "firebase_functions.logger.LogEntry")* ) â None |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                               |