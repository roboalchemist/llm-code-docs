Package org.jsoup

# Class Jsoup

java.lang.Object
org.jsoup.Jsoup

---

public class Jsoup
extends Object
The core public access point to the jsoup functionality.

Author:
Jonathan Hedley

- 

## Method Summary

Modifier and Type
Method
Description
`static String`
`clean(String bodyHtml,
 String baseUri,
 Safelist safelist)`

Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through an allow-list of safe
     tags and attributes.

`static String`
`clean(String bodyHtml,
 String baseUri,
 Safelist safelist,
 Document.OutputSettings outputSettings)`

Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through a safe-list of
 permitted tags and attributes.

`static String`
`clean(String bodyHtml,
 Safelist safelist)`

Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through a safe-list of permitted
     tags and attributes.

`static Connection`
`connect(String url)`

Creates a new `Connection` (session), with the defined request URL.

`static boolean`
`isValid(String bodyHtml,
 Safelist safelist)`

Test if the input body HTML has only tags and attributes allowed by the Safelist.

`static Connection`
`newSession()`

Creates a new `Connection` to use as a session.

`static Document`
`parse(File file)`

Parse the contents of a file as HTML.

`static Document`
`parse(File file,
 @Nullable String charsetName)`

Parse the contents of a file as HTML.

`static Document`
`parse(File file,
 @Nullable String charsetName,
 String baseUri)`

Parse the contents of a file as HTML.

`static Document`
`parse(File file,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Parse the contents of a file as HTML.

`static Document`
`parse(InputStream in,
 @Nullable String charsetName,
 String baseUri)`

Read an input stream, and parse it to a Document.

`static Document`
`parse(InputStream in,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Read an input stream, and parse it to a Document.

`static Document`
`parse(String html)`

Parse HTML into a Document.

`static Document`
`parse(String html,
 String baseUri)`

Parse HTML into a Document.

`static Document`
`parse(String html,
 String baseUri,
 Parser parser)`

Parse HTML into a Document, using the provided Parser.

`static Document`
`parse(String html,
 Parser parser)`

Parse HTML into a Document, using the provided Parser.

`static Document`
`parse(URL url,
 int timeoutMillis)`

Fetch a URL, and parse it as HTML.

`static Document`
`parse(Path path)`

Parse the contents of a file as HTML.

`static Document`
`parse(Path path,
 @Nullable String charsetName)`

Parse the contents of a file as HTML.

`static Document`
`parse(Path path,
 @Nullable String charsetName,
 String baseUri)`

Parse the contents of a file as HTML.

`static Document`
`parse(Path path,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)`

Parse the contents of a file as HTML.

`static Document`
`parseBodyFragment(String bodyHtml)`

Parse a fragment of HTML, with the assumption that it forms the `body` of the HTML.

`static Document`
`parseBodyFragment(String bodyHtml,
 String baseUri)`

Parse a fragment of HTML, with the assumption that it forms the `body` of the HTML.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### parse

public static Document parse(String html,
 String baseUri)
Parse HTML into a Document. The parser will make a sensible, balanced document tree out of any HTML.

Parameters:
`html` - HTML to parse
`baseUri` - The URL where the HTML was retrieved from. Used to resolve relative URLs to absolute URLs, that occur
     before the HTML declares a `<base href>` tag.
Returns:
sane HTML

  - 

### parse

public static Document parse(String html,
 String baseUri,
 Parser parser)
Parse HTML into a Document, using the provided Parser. You can provide an alternate parser, such as a simple XML
     (non-HTML) parser.

Parameters:
`html` - HTML to parse
`baseUri` - The URL where the HTML was retrieved from. Used to resolve relative URLs to absolute URLs, that occur
     before the HTML declares a `<base href>` tag.
`parser` - alternate `parser` to use.
Returns:
sane HTML

  - 

### parse

public static Document parse(String html,
 Parser parser)
Parse HTML into a Document, using the provided Parser. You can provide an alternate parser, such as a simple XML
     (non-HTML) parser.  As no base URI is specified, absolute URL resolution, if required, relies on the HTML including
     a `<base href>` tag.

Parameters:
`html` - HTML to parse
     before the HTML declares a `<base href>` tag.
`parser` - alternate `parser` to use.
Returns:
sane HTML

  - 

### parse

public static Document parse(String html)
Parse HTML into a Document. As no base URI is specified, absolute URL resolution, if required, relies on the HTML
     including a `<base href>` tag.

Parameters:
`html` - HTML to parse
Returns:
sane HTML
See Also:

    - `parse(String, String)`

  - 

### connect

public static Connection connect(String url)
Creates a new `Connection` (session), with the defined request URL. Use to fetch and parse a HTML page.
 

 Use examples:
 

  
    - `Document doc = Jsoup.connect("http://example.com").userAgent("Mozilla").data("name", "jsoup").get();`
  
    - `Document doc = Jsoup.connect("http://example.com").cookie("auth", "token").post();`
 

Parameters:
`url` - URL to connect to. The protocol must be `http` or `https`.
Returns:
the connection. You can add data, cookies, and headers; set the user-agent, referrer, method; and then execute.
See Also:

    - `newSession()`

    - `Connection.newRequest()`

  - 

### newSession

public static Connection newSession()
Creates a new `Connection` to use as a session. Connection settings (user-agent, timeouts, URL, etc), and
     cookies will be maintained for the session. Use examples:

```

Connection session = Jsoup.newSession()
     .timeout(20 * 1000)
     .userAgent("FooBar 2000");

Document doc1 = session.newRequest()
     .url("https://jsoup.org/").data("ref", "example")
     .get();
Document doc2 = session.newRequest()
     .url("https://en.wikipedia.org/wiki/Main_Page")
     .get();
Connection con3 = session.newRequest();

```

     

For multi-threaded requests, it is safe to use this session between threads, but take care to call `Connection.newRequest()` per request and not share that instance between threads when executing or parsing.

Returns:
a connection
Since:
1.14.1

  - 

### parse

public static Document parse(File file,
 @Nullable String charsetName,
 String baseUri)
                      throws IOException
Parse the contents of a file as HTML.

Parameters:
`file` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.

  - 

### parse

public static Document parse(File file,
 @Nullable String charsetName)
                      throws IOException
Parse the contents of a file as HTML. The location of the file is used as the base URI to qualify relative URLs.

Parameters:
`file` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.
See Also:

    - `parse(file, charset, baseUri)`

  - 

### parse

public static Document parse(File file)
                      throws IOException
Parse the contents of a file as HTML. The location of the file is used as the base URI to qualify relative URLs.
     The charset used to read the file will be determined by the byte-order-mark (BOM), or a `<meta charset>` tag,
     or if neither is present, will be `UTF-8`.

     

This is the equivalent of calling `parse(file, null)`

Parameters:
`file` - the file to load HTML from. Supports gzipped files (ending in .z or .gz).
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found or read.
Since:
1.15.1
See Also:

    - `parse(file, charset, baseUri)`

  - 

### parse

public static Document parse(File file,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                      throws IOException
Parse the contents of a file as HTML.

Parameters:
`file` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
`parser` - alternate `parser` to use.
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.
Since:
1.14.2

  - 

### parse

public static Document parse(Path path,
 @Nullable String charsetName,
 String baseUri)
                      throws IOException
Parse the contents of a file as HTML.

Parameters:
`path` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.
Since:
1.18.1

  - 

### parse

public static Document parse(Path path,
 @Nullable String charsetName)
                      throws IOException
Parse the contents of a file as HTML. The location of the file is used as the base URI to qualify relative URLs.

Parameters:
`path` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.
Since:
1.18.1
See Also:

    - `parse(file, charset, baseUri)`

  - 

### parse

public static Document parse(Path path)
                      throws IOException
Parse the contents of a file as HTML. The location of the file is used as the base URI to qualify relative URLs.
     The charset used to read the file will be determined by the byte-order-mark (BOM), or a `<meta charset>` tag,
     or if neither is present, will be `UTF-8`.

     

This is the equivalent of calling `parse(file, null)`

Parameters:
`path` - the file to load HTML from. Supports gzipped files (ending in .z or .gz).
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found or read.
Since:
1.18.1
See Also:

    - `parse(file, charset, baseUri)`

  - 

### parse

public static Document parse(Path path,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                      throws IOException
Parse the contents of a file as HTML.

Parameters:
`path` - file to load HTML from. Supports gzipped files (ending in .z or .gz).
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
`parser` - alternate `parser` to use.
Returns:
sane HTML
Throws:
`IOException` - if the file could not be found, or read, or if the charsetName is invalid.
Since:
1.18.1

  - 

### parse

public static Document parse(InputStream in,
 @Nullable String charsetName,
 String baseUri)
                      throws IOException
Read an input stream, and parse it to a Document.

Parameters:
`in` - input stream to read. The stream will be closed after reading.
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
Returns:
sane HTML
Throws:
`IOException` - if the stream could not be read, or if the charsetName is invalid.

  - 

### parse

public static Document parse(InputStream in,
 @Nullable String charsetName,
 String baseUri,
 Parser parser)
                      throws IOException
Read an input stream, and parse it to a Document. You can provide an alternate parser, such as a simple XML
     (non-HTML) parser.

Parameters:
`in` - input stream to read. Make sure to close it after parsing.
`charsetName` - (optional) character set of file contents. Set to `null` to determine from `http-equiv` meta tag, if
     present, or fall back to `UTF-8` (which is often safe to do).
`baseUri` - The URL where the HTML was retrieved from, to resolve relative links against.
`parser` - alternate `parser` to use.
Returns:
sane HTML
Throws:
`IOException` - if the stream could not be read, or if the charsetName is invalid.

  - 

### parseBodyFragment

public static Document parseBodyFragment(String bodyHtml,
 String baseUri)
Parse a fragment of HTML, with the assumption that it forms the `body` of the HTML.

Parameters:
`bodyHtml` - body HTML fragment
`baseUri` - URL to resolve relative URLs against.
Returns:
sane HTML document
See Also:

    - `Document.body()`

  - 

### parseBodyFragment

public static Document parseBodyFragment(String bodyHtml)
Parse a fragment of HTML, with the assumption that it forms the `body` of the HTML.

Parameters:
`bodyHtml` - body HTML fragment
Returns:
sane HTML document
See Also:

    - `Document.body()`

  - 

### parse

public static Document parse(URL url,
 int timeoutMillis)
                      throws IOException
Fetch a URL, and parse it as HTML. Provided for compatibility; in most cases use `connect(String)` instead.
     

     The encoding character set is determined by the content-type header or http-equiv meta tag, or falls back to `UTF-8`.

Parameters:
`url` - URL to fetch (with a GET). The protocol must be `http` or `https`.
`timeoutMillis` - Connection and read timeout, in milliseconds. If exceeded, IOException is thrown.
Returns:
The parsed HTML.
Throws:
`MalformedURLException` - if the request URL is not a HTTP or HTTPS URL, or is otherwise malformed
`HttpStatusException` - if the response is not OK and HTTP response errors are not ignored
`UnsupportedMimeTypeException` - if the response mime type is not supported and those errors are not ignored
`SocketTimeoutException` - if the connection times out
`IOException` - if a connection or read error occurs
See Also:

    - `connect(String)`

  - 

### clean

public static String clean(String bodyHtml,
 String baseUri,
 Safelist safelist)
Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through an allow-list of safe
     tags and attributes.

Parameters:
`bodyHtml` - input untrusted HTML (body fragment)
`baseUri` - URL to resolve relative URLs against
`safelist` - list of permitted HTML elements
Returns:
safe HTML (body fragment)
See Also:

    - `Cleaner.clean(Document)`

  - 

### clean

public static String clean(String bodyHtml,
 Safelist safelist)
Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through a safe-list of permitted
     tags and attributes.

     

Note that as this method does not take a base href URL to resolve attributes with relative URLs against, those
     URLs will be removed, unless the input HTML contains a `<base href> tag`. If you wish to preserve those, use
     the `clean(String html, String baseHref, Safelist)` method instead, and enable
     `Safelist.preserveRelativeLinks(boolean)`.

     

Note that the output of this method is still **HTML** even when using the TextNode only
     `Safelist.none()`, and so any HTML entities in the output will be appropriately escaped.
     If you want plain text, not HTML, you should use a text method such as `Element.text()` instead, after
     cleaning the document.
     

Example:
     

```

     String sourceBodyHtml = "<p>5 is < 6.</p>";
     String html = Jsoup.clean(sourceBodyHtml, Safelist.none());

     Cleaner cleaner = new Cleaner(Safelist.none());
     String text = cleaner.clean(Jsoup.parse(sourceBodyHtml)).text();

     // html is: 5 is < 6.
     // text is: 5 is < 6.
     
```

Parameters:
`bodyHtml` - input untrusted HTML (body fragment)
`safelist` - list of permitted HTML elements
Returns:
safe HTML (body fragment)
See Also:

    - `Cleaner.clean(Document)`

  - 

### clean

public static String clean(String bodyHtml,
 String baseUri,
 Safelist safelist,
 Document.OutputSettings outputSettings)
Get safe HTML from untrusted input HTML, by parsing input HTML and filtering it through a safe-list of
 permitted tags and attributes.
 

The HTML is treated as a body fragment; it's expected the cleaned HTML will be used within the body of an
 existing document. If you want to clean full documents, use `Cleaner.clean(Document)` instead, and add
 structural tags (`html, head, body` etc) to the safelist.

Parameters:
`bodyHtml` - input untrusted HTML (body fragment)
`baseUri` - URL to resolve relative URLs against
`safelist` - list of permitted HTML elements
`outputSettings` - document output settings; use to control pretty-printing and entity escape modes
Returns:
safe HTML (body fragment)
See Also:

    - `Cleaner.clean(Document)`

  - 

### isValid

public static boolean isValid(String bodyHtml,
 Safelist safelist)
Test if the input body HTML has only tags and attributes allowed by the Safelist. Useful for form validation.
     

     This method is intended to be used in a user interface as a validator for user input. Note that regardless of the
     output of this method, the input document **must always** be normalized using a method such as
     `clean(String, String, Safelist)`, and the result of that method used to store or serialize the document
     before later reuse such as presentation to end users. This ensures that enforced attributes are set correctly, and
     that any differences between how a given browser and how jsoup parses the input HTML are normalized.
     
     

Example:
     

```

     Safelist safelist = Safelist.relaxed();
     boolean isValid = Jsoup.isValid(sourceBodyHtml, safelist);
     String normalizedHtml = Jsoup.clean(sourceBodyHtml, "https://example.com/", safelist);
     
```

     

Assumes the HTML is a body fragment (i.e. will be used in an existing HTML document body.)

Parameters:
`bodyHtml` - HTML to test
`safelist` - safelist to test against
Returns:
true if no tags or attributes were removed; false otherwise
See Also:

    - `clean(String, Safelist)`