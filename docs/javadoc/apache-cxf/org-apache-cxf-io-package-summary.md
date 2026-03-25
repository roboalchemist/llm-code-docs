# Package org.apache.cxf.io

---

package org.apache.cxf.io

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
AbstractThresholdOutputStream

Outputstream that will buffer a certain amount before writing anything to the underlying
 stream.

AbstractWrappedOutputStream

Provides a convenient hook onFirstWrite() for those needing
 to wrap an output stream.

CacheAndWriteOutputStream

This outputstream implementation will both write to the outputstream
 that is specified and cache the data at the same time.

CachedConstants
 
CachedOutputStream
 
CachedOutputStreamCallback
 
CachedOutputStreamCleaner

The 

 extension to clean up unclosed `CachedOutputStream` instances (and alike) backed by
 temporary files (leading to disk fill, see https://issues.apache.org/jira/browse/CXF-7396.

CachedWriter
 
CachedWriterCallback
 
CacheSizeExceededException
 
CipherPair

A class to hold a pair of encryption and decryption ciphers.

CopyingOutputStream

Marker interface for OutputStreams that can directly support
 copying from an input stream.

DelayedCachedOutputStreamCleaner
 
DelegatingInputStream
 
ReaderInputStream

`InputStream` implementation that reads a character stream from a `Reader`
 and transforms it to a byte stream using a specified charset encoding.

Transferable

Implementing classes support transfer of their data to a file.

WriteOnCloseOutputStream

This outputstream implementation will cache the message until close()
 is called, at which point it will write the message to the OutputStream
 supplied via the constructor.