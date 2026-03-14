# Package org.h2.store.fs

---

package org.h2.store.fs

A file system abstraction.

- 

Related Packages

Package
Description
org.h2.store

Storage abstractions and helper classes.

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

- 

Class
Description
FakeFileChannel

Fake file channel to use by in-memory and ZIP file systems.

FileBase

The base class for file implementations.

FileBaseDefault

Default implementation of the slow operations that need synchronization because they
 involve the file position.

FilePath

A path to a file.

FilePathWrapper

The base class for wrapping / delegating file systems such as
 the split file system.

FileUtils

This utility class contains utility functions that use the file system
 abstraction.

Recorder

A recorder for the recording file system.