Package org.jsoup.helper

# Class DataUtil

java.lang.Object
org.jsoup.helper.DataUtil

---

public final class DataUtil
extends Object
Internal static utilities for handling data.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final Charset`
`UTF_8`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static Document`
`load(File file,
 @Nullable String charsetName,
 String baseUri)`

Loads and parses a file to a Document, with the HtmlParser.

`static Document`
`load(File file,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Loads and parses a file to a Document.

`static Document`
`load(InputStream in,
 @Nullable String charsetName,
 String baseUri)`

Parses a Document from an input steam.

`static Document`
`load(InputStream in,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Parses a Document from an input steam, using the provided Parser.

`static Document`
`load(Path path,
 @Nullable String charsetName,
 String baseUri)`

Loads and parses a file to a Document, with the HtmlParser.

`static Document`
`load(Path path,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Loads and parses a file to a Document.

`static ByteBuffer`
`readToByteBuffer(InputStream inStream,
 int maxSize)`

Read the input stream into a byte buffer.

`static StreamParser`
`streamParser(Path path,
 @Nullable Charset charset,
 String baseUri,
 Parser parser)`

Returns a `StreamParser` that will parse the supplied file progressively.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### UTF_8

public static final Charset UTF_8

- 

## Method Details

  - 

### load

public static Document load(File file,
 @Nullable String charsetName,
 String baseUri)
                     throws IOException
Loads and parses a file to a Document, with the HtmlParser. Files that are compressed with gzip (and end in `.gz` or `.z`)
 are supported in addition to uncompressed files.

Parameters:
`file` - file to load
`charsetName` - (optional) character set of input; specify `null` to attempt to autodetect. A BOM in
     the file will always override this setting.
`baseUri` - base URI of document, to resolve relative links against
Returns:
Document
Throws:
`IOException` - on IO error

  - 

### load

public static Document load(File file,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                     throws IOException
Loads and parses a file to a Document. Files that are compressed with gzip (and end in `.gz` or `.z`)
 are supported in addition to uncompressed files.

Parameters:
`file` - file to load
`charsetName` - (optional) character set of input; specify `null` to attempt to autodetect. A BOM in
     the file will always override this setting.
`baseUri` - base URI of document, to resolve relative links against
`parser` - alternate `parser` to use.
Returns:
Document
Throws:
`IOException` - on IO error
Since:
1.14.2

  - 

### load

public static Document load(Path path,
 @Nullable String charsetName,
 String baseUri)
                     throws IOException
Loads and parses a file to a Document, with the HtmlParser. Files that are compressed with gzip (and end in `.gz` or `.z`)
 are supported in addition to uncompressed files.

Parameters:
`path` - file to load
`charsetName` - (optional) character set of input; specify `null` to attempt to autodetect. A BOM in
     the file will always override this setting.
`baseUri` - base URI of document, to resolve relative links against
Returns:
Document
Throws:
`IOException` - on IO error

  - 

### load

public static Document load(Path path,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                     throws IOException
Loads and parses a file to a Document. Files that are compressed with gzip (and end in `.gz` or `.z`)
 are supported in addition to uncompressed files.

Parameters:
`path` - file to load
`charsetName` - (optional) character set of input; specify `null` to attempt to autodetect. A BOM in
 the file will always override this setting.
`baseUri` - base URI of document, to resolve relative links against
`parser` - alternate `parser` to use.
Returns:
Document
Throws:
`IOException` - on IO error
Since:
1.17.2

  - 

### streamParser

public static StreamParser streamParser(Path path,
 @Nullable Charset charset,
 String baseUri,
 Parser parser)
                                 throws IOException
Returns a `StreamParser` that will parse the supplied file progressively.
 Files that are compressed with gzip (and end in `.gz` or `.z`)
 are supported in addition to uncompressed files.

Parameters:
`path` - file to load
`charset` - (optional) character set of input; specify `null` to attempt to autodetect from metadata.
 A BOM in the file will always override this setting.
`baseUri` - base URI of document, to resolve relative links against
`parser` - underlying HTML or XML parser to use.
Returns:
Document
Throws:
`IOException` - on IO error
Since:
1.18.2
See Also:

    - `Connection.Response.streamParser()`

  - 

### load

public static Document load(InputStream in,
 @Nullable String charsetName,
 String baseUri)
                     throws IOException
Parses a Document from an input steam.

Parameters:
`in` - input stream to parse. The stream will be closed after reading.
`charsetName` - character set of input (optional)
`baseUri` - base URI of document, to resolve relative links against
Returns:
Document
Throws:
`IOException` - on IO error

  - 

### load

public static Document load(InputStream in,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                     throws IOException
Parses a Document from an input steam, using the provided Parser.

Parameters:
`in` - input stream to parse. The stream will be closed after reading.
`charsetName` - character set of input (optional)
`baseUri` - base URI of document, to resolve relative links against
`parser` - alternate `parser` to use.
Returns:
Document
Throws:
`IOException` - on IO error

  - 

### readToByteBuffer

public static ByteBuffer readToByteBuffer(InputStream inStream,
 int maxSize)
                                   throws IOException
Read the input stream into a byte buffer. To deal with slow input streams, you may interrupt the thread this
 method is executing on. The data read until being interrupted will be available.

Parameters:
`inStream` - the input stream to read from
`maxSize` - the maximum size in bytes to read from the stream. Set to 0 to be unlimited.
Returns:
the filled byte buffer
Throws:
`IOException` - if an exception occurs whilst reading from the input stream.