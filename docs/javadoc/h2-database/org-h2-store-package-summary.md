# Package org.h2.store

---

package org.h2.store

Storage abstractions and helper classes.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.store.fs

A file system abstraction.

- 

Class
Description
CountingReaderInputStream

An input stream that reads the data from a reader and limits the number of
 bytes that can be read.

Data

This class represents a byte buffer that contains persistent data of a page.

DataHandler

A data handler contains a number of callback methods, mostly related to CLOB
 and BLOB handling.

DataReader

This class is backed by an input stream and supports reading values and
 variable size data.

FileLister

Utility class to list the files of a database.

FileLock

The file lock is used to lock a database so that only one process can write
 to it.

FileLockMethod
 
FileStore

This class is an abstraction of a random access file.

FileStoreInputStream

An input stream that is backed by a file store.

FileStoreOutputStream

An output stream that is backed by a file store.

InDoubtTransaction

Represents an in-doubt transaction (a transaction in the prepare phase).

LobStorageFrontend

This factory creates in-memory objects and temporary files.

LobStorageInterface

A mechanism to store and retrieve lob data.

LobStorageRemoteInputStream

An input stream used by the client side of a tcp connection to fetch LOB data
 on demand from the server.

RangeInputStream

Input stream that reads only a specified range from the source stream.

RangeReader

Reader that reads only a specified range from the source reader.

RecoverTester

A tool that simulates a crash while writing to the database, and then
 verifies the database doesn't get corrupt.