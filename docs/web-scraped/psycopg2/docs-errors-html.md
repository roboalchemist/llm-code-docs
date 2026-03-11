# Source: https://www.psycopg.org/docs/errors.html

Title: psycopg2.errors – Exception classes mapping PostgreSQL errors — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/errors.html

Published Time: Sun, 08 Mar 2026 18:42:13 GMT

Markdown Content:
psycopg2.errors – Exception classes mapping PostgreSQL errors — Psycopg 2.9.11 documentation
===============

[Psycopg 2.9.11 documentation](https://www.psycopg.org/docs/index.html)
=======================================================================

* ← [`psycopg2.extras` – Miscellaneous goodies for Psycopg 2](https://www.psycopg.org/docs/extras.html "Previous document")
* [`psycopg2.sql` – SQL string composition](https://www.psycopg.org/docs/sql.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

[`psycopg2.errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") – Exception classes mapping PostgreSQL errors[¶](https://www.psycopg.org/docs/errors.html#psycopg2-errors-exception-classes-mapping-postgresql-errors "Link to this heading")
====================================================================================================================================================================================================================================================================================

Added in version 2.8.

Changed in version 2.8.4: added errors introduced in PostgreSQL 12

Changed in version 2.8.6: added errors introduced in PostgreSQL 13

Changed in version 2.9.2: added errors introduced in PostgreSQL 14

Changed in version 2.9.4: added errors introduced in PostgreSQL 15

Changed in version 2.9.10: added errors introduced in PostgreSQL 17

This module exposes the classes psycopg raises upon receiving an error from the database with a `SQLSTATE` value attached (available in the [`pgcode`](https://www.psycopg.org/docs/module.html#psycopg2.Error.pgcode "psycopg2.Error.pgcode") attribute). The content of the module is generated from the PostgreSQL source code and includes classes for every error defined by PostgreSQL in versions between 9.1 and 15.

Every class in the module is named after what referred as “condition name” [in the documentation](https://www.postgresql.org/docs/current/static/errcodes-appendix.html#ERRCODES-TABLE), converted to CamelCase: e.g. the error 22012, `division_by_zero` is exposed by this module as the class `DivisionByZero`.

Every exception class is a subclass of one of the [standard DB-API exception](https://www.psycopg.org/docs/module.html#dbapi-exceptions) and expose the [`Error`](https://www.psycopg.org/docs/module.html#psycopg2.Error "psycopg2.Error") interface. Each class’ superclass is what used to be raised by psycopg in versions before the introduction of this module, so everything should be compatible with previously written code catching one the DB-API class: if your code used to catch `IntegrityError` to detect a duplicate entry, it will keep on working even if a more specialised subclass such as `UniqueViolation` is raised.

The new classes allow a more idiomatic way to check and process a specific error among the many the database may return. For instance, in order to check that a table is locked, the following code could have been used previously:

try:
    cur.execute("LOCK TABLE mytable IN ACCESS EXCLUSIVE MODE NOWAIT")
except psycopg2.OperationalError as e:
    if e.pgcode == psycopg2.errorcodes.LOCK_NOT_AVAILABLE:
        locked = True
    else:
        raise

While this method is still available, the specialised class allows for a more idiomatic error handler:

try:
    cur.execute("LOCK TABLE mytable IN ACCESS EXCLUSIVE MODE NOWAIT")
except psycopg2.errors.LockNotAvailable:
    locked = True

psycopg2.errors.lookup(_code_)[¶](https://www.psycopg.org/docs/errors.html#psycopg2.errors.lookup "Link to this definition")
Lookup an error code and return its exception class.

Raise `KeyError` if the code is not found.

try:
    cur.execute("LOCK TABLE mytable IN ACCESS EXCLUSIVE MODE NOWAIT")
except psycopg2.errors.lookup("55P03"):
    locked = True

SQLSTATE exception classes[¶](https://www.psycopg.org/docs/errors.html#sqlstate-exception-classes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

The following table contains the list of all the SQLSTATE classes exposed by the module.

Note that, for completeness, the module also exposes all the [DB-API-defined exceptions](https://www.psycopg.org/docs/module.html#dbapi-exceptions) and [a few psycopg-specific ones](https://www.psycopg.org/docs/extensions.html#extension-exceptions) exposed by the `extensions` module, which are not listed here.

| SQLSTATE | Exception | Base exception |
| --- | --- | --- |
| **Class 02**: No Data (this is also a warning class per the SQL standard) |
| `02000` | `NoData` | `DatabaseError` |
| `02001` | `NoAdditionalDynamicResultSetsReturned` | `DatabaseError` |
| **Class 03**: SQL Statement Not Yet Complete |
| `03000` | `SqlStatementNotYetComplete` | `DatabaseError` |
| **Class 08**: Connection Exception |
| `08000` | `ConnectionException` | `OperationalError` |
| `08001` | `SqlclientUnableToEstablishSqlconnection` | `OperationalError` |
| `08003` | `ConnectionDoesNotExist` | `OperationalError` |
| `08004` | `SqlserverRejectedEstablishmentOfSqlconnection` | `OperationalError` |
| `08006` | `ConnectionFailure` | `OperationalError` |
| `08007` | `TransactionResolutionUnknown` | `OperationalError` |
| `08P01` | `ProtocolViolation` | `OperationalError` |
| **Class 09**: Triggered Action Exception |
| `09000` | `TriggeredActionException` | `DatabaseError` |
| **Class 0A**: Feature Not Supported |
| `0A000` | `FeatureNotSupported` | `NotSupportedError` |
| **Class 0B**: Invalid Transaction Initiation |
| `0B000` | `InvalidTransactionInitiation` | `DatabaseError` |
| **Class 0F**: Locator Exception |
| `0F000` | `LocatorException` | `DatabaseError` |
| `0F001` | `InvalidLocatorSpecification` | `DatabaseError` |
| **Class 0L**: Invalid Grantor |
| `0L000` | `InvalidGrantor` | `DatabaseError` |
| `0LP01` | `InvalidGrantOperation` | `DatabaseError` |
| **Class 0P**: Invalid Role Specification |
| `0P000` | `InvalidRoleSpecification` | `DatabaseError` |
| **Class 0Z**: Diagnostics Exception |
| `0Z000` | `DiagnosticsException` | `DatabaseError` |
| `0Z002` | `StackedDiagnosticsAccessedWithoutActiveHandler` | `DatabaseError` |
| **Class 20**: Case Not Found |
| `20000` | `CaseNotFound` | `ProgrammingError` |
| **Class 21**: Cardinality Violation |
| `21000` | `CardinalityViolation` | `ProgrammingError` |
| **Class 22**: Data Exception |
| `22000` | `DataException` | `DataError` |
| `22001` | `StringDataRightTruncation` | `DataError` |
| `22002` | `NullValueNoIndicatorParameter` | `DataError` |
| `22003` | `NumericValueOutOfRange` | `DataError` |
| `22004` | `NullValueNotAllowed` | `DataError` |
| `22005` | `ErrorInAssignment` | `DataError` |
| `22007` | `InvalidDatetimeFormat` | `DataError` |
| `22008` | `DatetimeFieldOverflow` | `DataError` |
| `22009` | `InvalidTimeZoneDisplacementValue` | `DataError` |
| `2200B` | `EscapeCharacterConflict` | `DataError` |
| `2200C` | `InvalidUseOfEscapeCharacter` | `DataError` |
| `2200D` | `InvalidEscapeOctet` | `DataError` |
| `2200F` | `ZeroLengthCharacterString` | `DataError` |
| `2200G` | `MostSpecificTypeMismatch` | `DataError` |
| `2200H` | `SequenceGeneratorLimitExceeded` | `DataError` |
| `2200L` | `NotAnXmlDocument` | `DataError` |
| `2200M` | `InvalidXmlDocument` | `DataError` |
| `2200N` | `InvalidXmlContent` | `DataError` |
| `2200S` | `InvalidXmlComment` | `DataError` |
| `2200T` | `InvalidXmlProcessingInstruction` | `DataError` |
| `22010` | `InvalidIndicatorParameterValue` | `DataError` |
| `22011` | `SubstringError` | `DataError` |
| `22012` | `DivisionByZero` | `DataError` |
| `22013` | `InvalidPrecedingOrFollowingSize` | `DataError` |
| `22014` | `InvalidArgumentForNtileFunction` | `DataError` |
| `22015` | `IntervalFieldOverflow` | `DataError` |
| `22016` | `InvalidArgumentForNthValueFunction` | `DataError` |
| `22018` | `InvalidCharacterValueForCast` | `DataError` |
| `22019` | `InvalidEscapeCharacter` | `DataError` |
| `2201B` | `InvalidRegularExpression` | `DataError` |
| `2201E` | `InvalidArgumentForLogarithm` | `DataError` |
| `2201F` | `InvalidArgumentForPowerFunction` | `DataError` |
| `2201G` | `InvalidArgumentForWidthBucketFunction` | `DataError` |
| `2201W` | `InvalidRowCountInLimitClause` | `DataError` |
| `2201X` | `InvalidRowCountInResultOffsetClause` | `DataError` |
| `22021` | `CharacterNotInRepertoire` | `DataError` |
| `22022` | `IndicatorOverflow` | `DataError` |
| `22023` | `InvalidParameterValue` | `DataError` |
| `22024` | `UnterminatedCString` | `DataError` |
| `22025` | `InvalidEscapeSequence` | `DataError` |
| `22026` | `StringDataLengthMismatch` | `DataError` |
| `22027` | `TrimError` | `DataError` |
| `2202E` | `ArraySubscriptError` | `DataError` |
| `2202G` | `InvalidTablesampleRepeat` | `DataError` |
| `2202H` | `InvalidTablesampleArgument` | `DataError` |
| `22030` | `DuplicateJsonObjectKeyValue` | `DataError` |
| `22031` | `InvalidArgumentForSqlJsonDatetimeFunction` | `DataError` |
| `22032` | `InvalidJsonText` | `DataError` |
| `22033` | `InvalidSqlJsonSubscript` | `DataError` |
| `22034` | `MoreThanOneSqlJsonItem` | `DataError` |
| `22035` | `NoSqlJsonItem` | `DataError` |
| `22036` | `NonNumericSqlJsonItem` | `DataError` |
| `22037` | `NonUniqueKeysInAJsonObject` | `DataError` |
| `22038` | `SingletonSqlJsonItemRequired` | `DataError` |
| `22039` | `SqlJsonArrayNotFound` | `DataError` |
| `2203A` | `SqlJsonMemberNotFound` | `DataError` |
| `2203B` | `SqlJsonNumberNotFound` | `DataError` |
| `2203C` | `SqlJsonObjectNotFound` | `DataError` |
| `2203D` | `TooManyJsonArrayElements` | `DataError` |
| `2203E` | `TooManyJsonObjectMembers` | `DataError` |
| `2203F` | `SqlJsonScalarRequired` | `DataError` |
| `2203G` | `SqlJsonItemCannotBeCastToTargetType` | `DataError` |
| `22P01` | `FloatingPointException` | `DataError` |
| `22P02` | `InvalidTextRepresentation` | `DataError` |
| `22P03` | `InvalidBinaryRepresentation` | `DataError` |
| `22P04` | `BadCopyFileFormat` | `DataError` |
| `22P05` | `UntranslatableCharacter` | `DataError` |
| `22P06` | `NonstandardUseOfEscapeCharacter` | `DataError` |
| **Class 23**: Integrity Constraint Violation |
| `23000` | `IntegrityConstraintViolation` | `IntegrityError` |
| `23001` | `RestrictViolation` | `IntegrityError` |
| `23502` | `NotNullViolation` | `IntegrityError` |
| `23503` | `ForeignKeyViolation` | `IntegrityError` |
| `23505` | `UniqueViolation` | `IntegrityError` |
| `23514` | `CheckViolation` | `IntegrityError` |
| `23P01` | `ExclusionViolation` | `IntegrityError` |
| **Class 24**: Invalid Cursor State |
| `24000` | `InvalidCursorState` | `InternalError` |
| **Class 25**: Invalid Transaction State |
| `25000` | `InvalidTransactionState` | `InternalError` |
| `25001` | `ActiveSqlTransaction` | `InternalError` |
| `25002` | `BranchTransactionAlreadyActive` | `InternalError` |
| `25003` | `InappropriateAccessModeForBranchTransaction` | `InternalError` |
| `25004` | `InappropriateIsolationLevelForBranchTransaction` | `InternalError` |
| `25005` | `NoActiveSqlTransactionForBranchTransaction` | `InternalError` |
| `25006` | `ReadOnlySqlTransaction` | `InternalError` |
| `25007` | `SchemaAndDataStatementMixingNotSupported` | `InternalError` |
| `25008` | `HeldCursorRequiresSameIsolationLevel` | `InternalError` |
| `25P01` | `NoActiveSqlTransaction` | `InternalError` |
| `25P02` | `InFailedSqlTransaction` | `InternalError` |
| `25P03` | `IdleInTransactionSessionTimeout` | `InternalError` |
| `25P04` | `TransactionTimeout` | `InternalError` |
| **Class 26**: Invalid SQL Statement Name |
| `26000` | `InvalidSqlStatementName` | `OperationalError` |
| **Class 27**: Triggered Data Change Violation |
| `27000` | `TriggeredDataChangeViolation` | `OperationalError` |
| **Class 28**: Invalid Authorization Specification |
| `28000` | `InvalidAuthorizationSpecification` | `OperationalError` |
| `28P01` | `InvalidPassword` | `OperationalError` |
| **Class 2B**: Dependent Privilege Descriptors Still Exist |
| `2B000` | `DependentPrivilegeDescriptorsStillExist` | `InternalError` |
| `2BP01` | `DependentObjectsStillExist` | `InternalError` |
| **Class 2D**: Invalid Transaction Termination |
| `2D000` | `InvalidTransactionTermination` | `InternalError` |
| **Class 2F**: SQL Routine Exception |
| `2F000` | `SqlRoutineException` | `InternalError` |
| `2F002` | `ModifyingSqlDataNotPermitted` | `InternalError` |
| `2F003` | `ProhibitedSqlStatementAttempted` | `InternalError` |
| `2F004` | `ReadingSqlDataNotPermitted` | `InternalError` |
| `2F005` | `FunctionExecutedNoReturnStatement` | `InternalError` |
| **Class 34**: Invalid Cursor Name |
| `34000` | `InvalidCursorName` | `OperationalError` |
| **Class 38**: External Routine Exception |
| `38000` | `ExternalRoutineException` | `InternalError` |
| `38001` | `ContainingSqlNotPermitted` | `InternalError` |
| `38002` | `ModifyingSqlDataNotPermittedExt` | `InternalError` |
| `38003` | `ProhibitedSqlStatementAttemptedExt` | `InternalError` |
| `38004` | `ReadingSqlDataNotPermittedExt` | `InternalError` |
| **Class 39**: External Routine Invocation Exception |
| `39000` | `ExternalRoutineInvocationException` | `InternalError` |
| `39001` | `InvalidSqlstateReturned` | `InternalError` |
| `39004` | `NullValueNotAllowedExt` | `InternalError` |
| `39P01` | `TriggerProtocolViolated` | `InternalError` |
| `39P02` | `SrfProtocolViolated` | `InternalError` |
| `39P03` | `EventTriggerProtocolViolated` | `InternalError` |
| **Class 3B**: Savepoint Exception |
| `3B000` | `SavepointException` | `InternalError` |
| `3B001` | `InvalidSavepointSpecification` | `InternalError` |
| **Class 3D**: Invalid Catalog Name |
| `3D000` | `InvalidCatalogName` | `ProgrammingError` |
| **Class 3F**: Invalid Schema Name |
| `3F000` | `InvalidSchemaName` | `ProgrammingError` |
| **Class 40**: Transaction Rollback |
| `40000` | `TransactionRollback` | `OperationalError` |
| `40001` | `SerializationFailure` | `OperationalError` |
| `40002` | `TransactionIntegrityConstraintViolation` | `OperationalError` |
| `40003` | `StatementCompletionUnknown` | `OperationalError` |
| `40P01` | `DeadlockDetected` | `OperationalError` |
| **Class 42**: Syntax Error or Access Rule Violation |
| `42000` | `SyntaxErrorOrAccessRuleViolation` | `ProgrammingError` |
| `42501` | `InsufficientPrivilege` | `ProgrammingError` |
| `42601` | `SyntaxError` | `ProgrammingError` |
| `42602` | `InvalidName` | `ProgrammingError` |
| `42611` | `InvalidColumnDefinition` | `ProgrammingError` |
| `42622` | `NameTooLong` | `ProgrammingError` |
| `42701` | `DuplicateColumn` | `ProgrammingError` |
| `42702` | `AmbiguousColumn` | `ProgrammingError` |
| `42703` | `UndefinedColumn` | `ProgrammingError` |
| `42704` | `UndefinedObject` | `ProgrammingError` |
| `42710` | `DuplicateObject` | `ProgrammingError` |
| `42712` | `DuplicateAlias` | `ProgrammingError` |
| `42723` | `DuplicateFunction` | `ProgrammingError` |
| `42725` | `AmbiguousFunction` | `ProgrammingError` |
| `42803` | `GroupingError` | `ProgrammingError` |
| `42804` | `DatatypeMismatch` | `ProgrammingError` |
| `42809` | `WrongObjectType` | `ProgrammingError` |
| `42830` | `InvalidForeignKey` | `ProgrammingError` |
| `42846` | `CannotCoerce` | `ProgrammingError` |
| `42883` | `UndefinedFunction` | `ProgrammingError` |
| `428C9` | `GeneratedAlways` | `ProgrammingError` |
| `42939` | `ReservedName` | `ProgrammingError` |
| `42P01` | `UndefinedTable` | `ProgrammingError` |
| `42P02` | `UndefinedParameter` | `ProgrammingError` |
| `42P03` | `DuplicateCursor` | `ProgrammingError` |
| `42P04` | `DuplicateDatabase` | `ProgrammingError` |
| `42P05` | `DuplicatePreparedStatement` | `ProgrammingError` |
| `42P06` | `DuplicateSchema` | `ProgrammingError` |
| `42P07` | `DuplicateTable` | `ProgrammingError` |
| `42P08` | `AmbiguousParameter` | `ProgrammingError` |
| `42P09` | `AmbiguousAlias` | `ProgrammingError` |
| `42P10` | `InvalidColumnReference` | `ProgrammingError` |
| `42P11` | `InvalidCursorDefinition` | `ProgrammingError` |
| `42P12` | `InvalidDatabaseDefinition` | `ProgrammingError` |
| `42P13` | `InvalidFunctionDefinition` | `ProgrammingError` |
| `42P14` | `InvalidPreparedStatementDefinition` | `ProgrammingError` |
| `42P15` | `InvalidSchemaDefinition` | `ProgrammingError` |
| `42P16` | `InvalidTableDefinition` | `ProgrammingError` |
| `42P17` | `InvalidObjectDefinition` | `ProgrammingError` |
| `42P18` | `IndeterminateDatatype` | `ProgrammingError` |
| `42P19` | `InvalidRecursion` | `ProgrammingError` |
| `42P20` | `WindowingError` | `ProgrammingError` |
| `42P21` | `CollationMismatch` | `ProgrammingError` |
| `42P22` | `IndeterminateCollation` | `ProgrammingError` |
| **Class 44**: WITH CHECK OPTION Violation |
| `44000` | `WithCheckOptionViolation` | `ProgrammingError` |
| **Class 53**: Insufficient Resources |
| `53000` | `InsufficientResources` | `OperationalError` |
| `53100` | `DiskFull` | `OperationalError` |
| `53200` | `OutOfMemory` | `OperationalError` |
| `53300` | `TooManyConnections` | `OperationalError` |
| `53400` | `ConfigurationLimitExceeded` | `OperationalError` |
| **Class 54**: Program Limit Exceeded |
| `54000` | `ProgramLimitExceeded` | `OperationalError` |
| `54001` | `StatementTooComplex` | `OperationalError` |
| `54011` | `TooManyColumns` | `OperationalError` |
| `54023` | `TooManyArguments` | `OperationalError` |
| **Class 55**: Object Not In Prerequisite State |
| `55000` | `ObjectNotInPrerequisiteState` | `OperationalError` |
| `55006` | `ObjectInUse` | `OperationalError` |
| `55P02` | `CantChangeRuntimeParam` | `OperationalError` |
| `55P03` | `LockNotAvailable` | `OperationalError` |
| `55P04` | `UnsafeNewEnumValueUsage` | `OperationalError` |
| **Class 57**: Operator Intervention |
| `57000` | `OperatorIntervention` | `OperationalError` |
| `57014` | `QueryCanceled` | `OperationalError` |
| `57P01` | `AdminShutdown` | `OperationalError` |
| `57P02` | `CrashShutdown` | `OperationalError` |
| `57P03` | `CannotConnectNow` | `OperationalError` |
| `57P04` | `DatabaseDropped` | `OperationalError` |
| `57P05` | `IdleSessionTimeout` | `OperationalError` |
| **Class 58**: System Error (errors external to PostgreSQL itself) |
| `58000` | `SystemError` | `OperationalError` |
| `58030` | `IoError` | `OperationalError` |
| `58P01` | `UndefinedFile` | `OperationalError` |
| `58P02` | `DuplicateFile` | `OperationalError` |
| **Class 72**: Snapshot Failure |
| `72000` | `SnapshotTooOld` | `DatabaseError` |
| **Class F0**: Configuration File Error |
| `F0000` | `ConfigFileError` | `InternalError` |
| `F0001` | `LockFileExists` | `InternalError` |
| **Class HV**: Foreign Data Wrapper Error (SQL/MED) |
| `HV000` | `FdwError` | `OperationalError` |
| `HV001` | `FdwOutOfMemory` | `OperationalError` |
| `HV002` | `FdwDynamicParameterValueNeeded` | `OperationalError` |
| `HV004` | `FdwInvalidDataType` | `OperationalError` |
| `HV005` | `FdwColumnNameNotFound` | `OperationalError` |
| `HV006` | `FdwInvalidDataTypeDescriptors` | `OperationalError` |
| `HV007` | `FdwInvalidColumnName` | `OperationalError` |
| `HV008` | `FdwInvalidColumnNumber` | `OperationalError` |
| `HV009` | `FdwInvalidUseOfNullPointer` | `OperationalError` |
| `HV00A` | `FdwInvalidStringFormat` | `OperationalError` |
| `HV00B` | `FdwInvalidHandle` | `OperationalError` |
| `HV00C` | `FdwInvalidOptionIndex` | `OperationalError` |
| `HV00D` | `FdwInvalidOptionName` | `OperationalError` |
| `HV00J` | `FdwOptionNameNotFound` | `OperationalError` |
| `HV00K` | `FdwReplyHandle` | `OperationalError` |
| `HV00L` | `FdwUnableToCreateExecution` | `OperationalError` |
| `HV00M` | `FdwUnableToCreateReply` | `OperationalError` |
| `HV00N` | `FdwUnableToEstablishConnection` | `OperationalError` |
| `HV00P` | `FdwNoSchemas` | `OperationalError` |
| `HV00Q` | `FdwSchemaNotFound` | `OperationalError` |
| `HV00R` | `FdwTableNotFound` | `OperationalError` |
| `HV010` | `FdwFunctionSequenceError` | `OperationalError` |
| `HV014` | `FdwTooManyHandles` | `OperationalError` |
| `HV021` | `FdwInconsistentDescriptorInformation` | `OperationalError` |
| `HV024` | `FdwInvalidAttributeValue` | `OperationalError` |
| `HV090` | `FdwInvalidStringLengthOrBufferLength` | `OperationalError` |
| `HV091` | `FdwInvalidDescriptorFieldIdentifier` | `OperationalError` |
| **Class P0**: PL/pgSQL Error |
| `P0000` | `PlpgsqlError` | `InternalError` |
| `P0001` | `RaiseException` | `InternalError` |
| `P0002` | `NoDataFound` | `InternalError` |
| `P0003` | `TooManyRows` | `InternalError` |
| `P0004` | `AssertFailure` | `InternalError` |
| **Class XX**: Internal Error |
| `XX000` | `InternalError_` | `InternalError` |
| `XX001` | `DataCorrupted` | `InternalError` |
| `XX002` | `IndexCorrupted` | `InternalError` |

### [Table of Contents](https://www.psycopg.org/docs/index.html)

* [`psycopg2.errors` – Exception classes mapping PostgreSQL errors](https://www.psycopg.org/docs/errors.html#)
  * [SQLSTATE exception classes](https://www.psycopg.org/docs/errors.html#sqlstate-exception-classes)

### Quick search

* ← [`psycopg2.extras` – Miscellaneous goodies for Psycopg 2](https://www.psycopg.org/docs/extras.html "Previous document")
* [`psycopg2.sql` – SQL string composition](https://www.psycopg.org/docs/sql.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

© 2001-2021, Federico Di Gregorio, Daniele Varrazzo, The Psycopg Team.
