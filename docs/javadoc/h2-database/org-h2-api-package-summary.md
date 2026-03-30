# Package org.h2.api

---

package org.h2.api

Contains interfaces for user-defined extensions, such as triggers and
 user-defined aggregate functions.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
Aggregate

A user-defined aggregate function needs to implement this interface.

AggregateFunction

A user-defined aggregate function needs to implement this interface.

CredentialsValidator

A class that implement this interface can be used to validate credentials
 provided by client.

DatabaseEventListener

A class that implements this interface can get notified about exceptions
 and other events.

ErrorCode

This class defines the error codes used for SQL exceptions.

H2Type

Data types of H2.

Interval

INTERVAL representation for result sets.

IntervalQualifier

Interval qualifier.

JavaObjectSerializer

Custom serialization mechanism for java objects being stored in column of
 type OTHER.

TableEngine

A class that implements this interface can create custom table
 implementations.

Trigger

A class that implements this interface can be used as a trigger.

UserToRolesMapper

A class that implement this interface can be used during authentication to
 map external users to database roles.