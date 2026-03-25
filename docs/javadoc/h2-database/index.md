Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.api

Contains interfaces for user-defined extensions, such as triggers and
 user-defined aggregate functions.

org.h2.bnf

The implementation of the BNF (Backus-Naur form) parser and tool.

org.h2.bnf.context

Classes that provide context for the BNF tool, in order to provide BNF-based
 auto-complete.

org.h2.build

The pure Java build system and implementation.

org.h2.build.indexer

A Javadoc indexing mechanism.

org.h2.command

This package contains the parser and the base classes for prepared SQL
 statements.

org.h2.command.ddl

Contains DDL (data definition language) and related SQL statements.

org.h2.command.dml

Contains DML (data manipulation language) and related SQL statements.

org.h2.command.query

Contains queries.

org.h2.compress

Lossless data compression classes.

org.h2.constraint

Database constraints such as check constraints, unique constraints, and
 referential constraints.

org.h2.dev.cache

A LIRS cache implementation.

org.h2.dev.cluster

A clustering implementation.

org.h2.dev.fs

File system tools.

org.h2.dev.ftp

A simple FTP client.

org.h2.dev.ftp.server

A simple FTP server.

org.h2.dev.hash

A perfect hash function tool.

org.h2.dev.net

A tool to redirect and interpret PostgreSQL network protocol packets.

org.h2.dev.security

Security tools.

org.h2.dev.sort

Sorting utilities.

org.h2.dev.util

Utility classes that are currently not used in the database engine.

org.h2.engine

Contains high level classes of the database and classes that don't fit in
 another sub-package.

org.h2.expression

Expressions include mathematical operations, simple values, and others.

org.h2.expression.aggregate

Aggregate functions.

org.h2.expression.analysis

Base classes for data analysis operations and implementations of window
 functions.

org.h2.expression.condition

Condition expressions.

org.h2.expression.function

Functions.

org.h2.expression.function.table

Table value functions.

org.h2.fulltext

The native full text search implementation, and the wrapper for the Lucene
 full text search implementation.

org.h2.index

Various table index implementations, as well as cursors to navigate in an
 index.

org.h2.jcr

Utility classes related to the JCR API.

org.h2.jdbc

Implementation of the JDBC API (package `java.sql`).

org.h2.jdbc.meta

Implementation of the JDBC database metadata API (package `java.sql`).

org.h2.jdbcx

Implementation of the extended JDBC API (package `javax.sql`).

org.h2.jmx

Implementation of the Java Management Extension (JMX) features.

org.h2.message

Trace (logging facility) and error message tool.

org.h2.mode

Utility classes for compatibility with other database, for example MySQL.

org.h2.mvstore

A persistent storage for tree maps.

org.h2.mvstore.cache

Classes related to caching.

org.h2.mvstore.db

Helper classes to use the MVStore in the H2 database.

org.h2.mvstore.rtree

An R-tree implementation.

org.h2.mvstore.tx

Helper classes to use the MVStore in a transactional manner.

org.h2.mvstore.type

Data types and serialization / deserialization.

org.h2.result

Implementation of row and internal result sets.

org.h2.samples

Standalone sample applications.

org.h2.schema

Schema implementation and objects that are stored in a schema (for example,
 sequences and constants).

org.h2.security

Security classes, such as encryption and cryptographically secure hash
 algorithms.

org.h2.security.auth

Authentication classes.

org.h2.security.auth.impl

Authentication classes.

org.h2.server

A TCP server.

org.h2.server.pg

PostgreSQL server implementation of this database.

org.h2.server.web

The H2 Console tool.

org.h2.store

Storage abstractions and helper classes.

org.h2.store.fs

A file system abstraction.

org.h2.store.fs.async

This file system stores files on disk and uses
 `AsynchronousFileChannel` to access the files.

org.h2.store.fs.disk

This file system stores files on disk.

org.h2.store.fs.encrypt

An encrypted file system abstraction.

org.h2.store.fs.mem

This file system keeps files fully in memory.

org.h2.store.fs.niomapped

This file system stores files on disk and uses `java.nio` to access the
 memory mapped files.

org.h2.store.fs.niomem

This file system keeps files fully in off-java-heap memory.

org.h2.store.fs.rec

A file system that records all write operations and can re-play them.

org.h2.store.fs.retry

A file system that re-opens and re-tries the operation if the file was
 closed, because a thread was interrupted.

org.h2.store.fs.split

A file system that may split files into multiple smaller files (required for
 a FAT32 because it only support files up to 2 GiB).

org.h2.store.fs.zip

A zip-file base file system abstraction.

org.h2.table

Classes related to a table and table meta data.

org.h2.test.ap

An annotation processor used for testing.

org.h2.test.auth

Tests for custom authentication.

org.h2.test.bench

The implementation of the benchmark application.

org.h2.test.coverage

Database tests.

org.h2.test.db

Database tests.

org.h2.test.jdbc

JDBC API tests.

org.h2.test.jdbcx

Tests related to distributed transactions.

org.h2.test.mvcc

Multi version concurrency tests.

org.h2.test.poweroff

Poweroff and recovery tests.

org.h2.test.recover

Recovery tests.

org.h2.test.rowlock

Row level locking tests.

org.h2.test.scripts

Script test files.

org.h2.test.server

This package contains server tests.

org.h2.test.store

This package contains tests for the map store.

org.h2.test.synth

Synthetic tests using random operations or statements.

org.h2.test.synth.sql

A synthetic test using random SQL statements executed against multiple
 databases.

org.h2.test.synth.thread

Synthetic tests using random operations in multiple threads.

org.h2.test.todo

Documentation and tests for open issues.

org.h2.test.trace

A player to interpret and execute Java statements in a trace file.

org.h2.test.unit

Unit tests that don't start the database (in most cases).

org.h2.test.utils

Utility classes used by the tests.

org.h2.tools

Various tools.

org.h2.util

Internal utility classes.

org.h2.util.geometry

Internal utility classes for GEOMETRY data type.

org.h2.util.json

Internal utility classes for JSON data type.

org.h2.value

Data type and value implementations.

org.h2.value.lob

LOB data for values.