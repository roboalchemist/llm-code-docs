# Package org.h2.engine

---

package org.h2.engine

Contains high level classes of the database and classes that don't fit in
 another sub-package.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
CastDataProvider

Provides information for type casts and comparison operations.

Comment

Represents a database object comment.

ConnectionInfo

Encapsulates the connection settings, including user name and password.

Constants

Constants are fixed values that are used in the whole database code.

Database

There is one database object per open database.

DbObject

A database object such as a table, an index, or a user.

DbSettings

This class contains various database-level settings.

Engine

The engine contains a map of all open databases.

GeneratedKeysMode

Modes of generated keys' gathering.

IsolationLevel

Level of isolation.

MetaRecord

A record in the system table of the database.

Mode

The compatibility modes.

Mode.CharPadding

When CHAR values are right-padded with spaces.

Mode.ExpressionNames

Generation of column names for expressions.

Mode.ModeEnum
 
Mode.ViewExpressionNames

Generation of column names for expressions to be used in a view.

NullsDistinct

Determines how rows with `NULL` values in indexed columns are handled
 in unique indexes, unique constraints, or by unique predicate.

Procedure

Represents a procedure.

QueryStatisticsData

Maintains query statistics.

QueryStatisticsData.QueryEntry

The collected statistics for one query.

Right

An access right.

RightOwner

A right owner (sometimes called principal).

Role

Represents a role.

Session

A local or remote session.

Session.DynamicSettings

Dynamic settings.

Session.StaticSettings

Static settings.

SessionLocal

A session represents an embedded database connection.

SessionLocal.Savepoint

Represents a savepoint (a position in a transaction to where one can roll
 back to).

SessionLocal.State
 
SessionLocal.TimeoutValue

An LOB object with a timeout.

SessionRemote

The client side part of a session when using the server mode.

Setting

A persistent database setting.

SettingsBase

The base class for settings.

SysProperties

The constants defined in this class are initialized from system properties.

User

Represents a user object.

UserBuilder