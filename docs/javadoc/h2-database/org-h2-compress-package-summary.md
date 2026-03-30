# Package org.h2.compress

---

package org.h2.compress

Lossless data compression classes.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
CompressDeflate

This is a wrapper class for the Deflater class.

CompressLZF

 This class implements the LZF lossless data compression algorithm.

CompressNo

This class implements a data compression algorithm that does in fact not
 compress.

Compressor

Each data compression algorithm must implement this interface.

LZFInputStream

An input stream to read from an LZF stream.

LZFOutputStream

An output stream to write an LZF stream.