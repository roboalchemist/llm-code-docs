Package org.jsoup.parser

# Class Parser

java.lang.Object
org.jsoup.parser.Parser

All Implemented Interfaces:
`Cloneable`

---

public class Parser
extends Object
implements Cloneable
Parses HTML or XML into a `Document`. Generally, it is simpler to use one of the parse methods in
 `Jsoup`.
 

Note that a given Parser instance object is threadsafe, but not concurrent. (Concurrent parse calls will
 synchronize.) To reuse a Parser configuration in a multithreaded environment, use `newInstance()` to make
 copies.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`NamespaceHtml`
 
`static final String`
`NamespaceMathml`
 
`static final String`
`NamespaceSvg`
 
`static final String`
`NamespaceXml`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Parser(org.jsoup.parser.TreeBuilder treeBuilder)`

Create a new Parser, using the specified TreeBuilder

- 

## Method Summary

Modifier and Type
Method
Description
`Parser`
`clone()`
 
`String`
`defaultNamespace()`
 
`ParseErrorList`
`getErrors()`

Retrieve the parse errors, if any, from the last parse.

`int`
`getMaxDepth()`

Get the maximum parser depth (maximum number of open elements).

`org.jsoup.parser.TreeBuilder`
`getTreeBuilder()`

Get the TreeBuilder currently in use.

`static Parser`
`htmlParser()`

Create a new HTML parser.

`boolean`
`isTrackErrors()`

Check if parse error tracking is enabled.

`boolean`
`isTrackPosition()`

Test if position tracking is enabled.

`Parser`
`newInstance()`

Creates a new Parser as a deep copy of this; including initializing a new TreeBuilder.

`static Document`
`parse(String html,
 String baseUri)`

Parse HTML into a Document.

`static Document`
`parseBodyFragment(String bodyHtml,
 String baseUri)`

Parse a fragment of HTML into the `body` of a Document.

`static List<Node>`
`parseFragment(String fragmentHtml,
 Element context,
 String baseUri)`

Parse a fragment of HTML into a list of nodes.

`static List<Node>`
`parseFragment(String fragmentHtml,
 Element context,
 String baseUri,
 ParseErrorList errorList)`

Parse a fragment of HTML into a list of nodes.

`List<Node>`
`parseFragmentInput(Reader fragment,
 @Nullable Element context,
 String baseUri)`

Parse a fragment of HTML into a list of nodes.

`List<Node>`
`parseFragmentInput(String fragment,
 @Nullable Element context,
 String baseUri)`

Parse a fragment of HTML into a list of nodes.

`Document`
`parseInput(Reader inputHtml,
 String baseUri)`

Parse the contents of Reader.

`Document`
`parseInput(String html,
 String baseUri)`

Parse the contents of a String.

`static List<Node>`
`parseXmlFragment(String fragmentXml,
 String baseUri)`

Parse a fragment of XML into a list of nodes.

`Parser`
`setMaxDepth(int maxDepth)`

Set the parser's maximum stack depth (maximum number of open elements).

`ParseSettings`
`settings()`

Gets the current ParseSettings for this Parser

`Parser`
`settings(ParseSettings settings)`

Update the ParseSettings of this Parser, to control the case sensitivity of tags and attributes.

`Parser`
`setTrackErrors(int maxErrors)`

Enable or disable parse error tracking for the next parse.

`Parser`
`setTrackPosition(boolean trackPosition)`

Enable or disable source position tracking.

`TagSet`
`tagSet()`

Get the current TagSet for this Parser, which will be either this parser's default, or one that you have set.

`Parser`
`tagSet(TagSet tagSet)`

Set a custom TagSet to use for this Parser.

`String`
`unescape(String string,
 boolean inAttribute)`

Utility method to unescape HTML entities from a string, using this `Parser`'s configuration (for example, to
     collect errors while unescaping).

`static String`
`unescapeEntities(String string,
 boolean inAttribute)`

Utility method to unescape HTML entities from a string.

`static Parser`
`xmlParser()`

Create a new XML parser.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### NamespaceHtml

public static final String NamespaceHtml

See Also:

    - Constant Field Values

  - 

### NamespaceXml

public static final String NamespaceXml

See Also:

    - Constant Field Values

  - 

### NamespaceMathml

public static final String NamespaceMathml

See Also:

    - Constant Field Values

  - 

### NamespaceSvg

public static final String NamespaceSvg

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### Parser

public Parser(org.jsoup.parser.TreeBuilder treeBuilder)
Create a new Parser, using the specified TreeBuilder

Parameters:
`treeBuilder` - TreeBuilder to use to parse input into Documents.

- 

## Method Details

  - 

### newInstance

public Parser newInstance()
Creates a new Parser as a deep copy of this; including initializing a new TreeBuilder. Allows independent (multi-threaded) use.

Returns:
a copied parser

  - 

### clone

public Parser clone()

Overrides:
`clone` in class `Object`

  - 

### parseInput

public Document parseInput(String html,
 String baseUri)
Parse the contents of a String.

Parameters:
`html` - HTML to parse
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
parsed Document

  - 

### parseInput

public Document parseInput(Reader inputHtml,
 String baseUri)
Parse the contents of Reader.

Parameters:
`inputHtml` - HTML to parse
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
parsed Document
Throws:
`UncheckedIOException` - if an I/O error occurs in the Reader

  - 

### parseFragmentInput

public List<Node> parseFragmentInput(String fragment,
 @Nullable Element context,
 String baseUri)
Parse a fragment of HTML into a list of nodes. The context element, if supplied, supplies parsing context.

Parameters:
`fragment` - the fragment of HTML to parse
`context` - (optional) the element that this HTML fragment is being parsed for (i.e. for inner HTML).
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
list of nodes parsed from the input HTML.

  - 

### parseFragmentInput

public List<Node> parseFragmentInput(Reader fragment,
 @Nullable Element context,
 String baseUri)
Parse a fragment of HTML into a list of nodes. The context element, if supplied, supplies parsing context.

Parameters:
`fragment` - the fragment of HTML to parse
`context` - (optional) the element that this HTML fragment is being parsed for (i.e. for inner HTML).
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
list of nodes parsed from the input HTML.
Throws:
`UncheckedIOException` - if an I/O error occurs in the Reader

  - 

### getTreeBuilder

public org.jsoup.parser.TreeBuilder getTreeBuilder()
Get the TreeBuilder currently in use.

Returns:
current TreeBuilder.

  - 

### isTrackErrors

public boolean isTrackErrors()
Check if parse error tracking is enabled.

Returns:
current track error state.

  - 

### setTrackErrors

public Parser setTrackErrors(int maxErrors)
Enable or disable parse error tracking for the next parse.

Parameters:
`maxErrors` - the maximum number of errors to track. Set to 0 to disable.
Returns:
this, for chaining

  - 

### getErrors

public ParseErrorList getErrors()
Retrieve the parse errors, if any, from the last parse.

Returns:
list of parse errors, up to the size of the maximum errors tracked.
See Also:

    - `setTrackErrors(int)`

  - 

### isTrackPosition

public boolean isTrackPosition()
Test if position tracking is enabled. If it is, Nodes will have a Position to track where in the original input
     source they were created from. By default, tracking is not enabled.

Returns:
current track position setting

  - 

### setTrackPosition

public Parser setTrackPosition(boolean trackPosition)
Enable or disable source position tracking. If enabled, Nodes will have a Position to track where in the original
     input source they were created from.

Parameters:
`trackPosition` - position tracking setting; `true` to enable
Returns:
this Parser, for chaining

  - 

### settings

public Parser settings(ParseSettings settings)
Update the ParseSettings of this Parser, to control the case sensitivity of tags and attributes.

Parameters:
`settings` - the new settings
Returns:
this Parser

  - 

### settings

public ParseSettings settings()
Gets the current ParseSettings for this Parser

Returns:
current ParseSettings

  - 

### setMaxDepth

public Parser setMaxDepth(int maxDepth)
Set the parser's maximum stack depth (maximum number of open elements). When reached, new open elements will be
     removed to prevent excessive nesting. Defaults to 512 for the HTML parser, and unlimited for the XML
     parser.

Parameters:
`maxDepth` - maximum parser depth; must be >= 1
Returns:
this Parser, for chaining

  - 

### getMaxDepth

public int getMaxDepth()
Get the maximum parser depth (maximum number of open elements).

Returns:
the current max parser depth

  - 

### tagSet

public Parser tagSet(TagSet tagSet)
Set a custom TagSet to use for this Parser. This allows you to define your own tags, and control how they are
     parsed. For example, you can set a tag to preserve whitespace, or to be treated as a block tag.
     

You can start with the `TagSet.Html()` defaults and customize, or a new empty TagSet.

Parameters:
`tagSet` - the TagSet to use. This gets copied, so that changes that the parse makes (tags found in the document will be added) do not clobber the original TagSet.
Returns:
this Parser
Since:
1.20.1

  - 

### tagSet

public TagSet tagSet()
Get the current TagSet for this Parser, which will be either this parser's default, or one that you have set.

Returns:
the current TagSet. After the parse, this will contain any new tags that were found in the document.
Since:
1.20.1

  - 

### defaultNamespace

public String defaultNamespace()

  - 

### parse

public static Document parse(String html,
 String baseUri)
Parse HTML into a Document.

Parameters:
`html` - HTML to parse
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
parsed Document

  - 

### parseFragment

public static List<Node> parseFragment(String fragmentHtml,
 Element context,
 String baseUri)
Parse a fragment of HTML into a list of nodes. The context element, if supplied, supplies parsing context.

Parameters:
`fragmentHtml` - the fragment of HTML to parse
`context` - (optional) the element that this HTML fragment is being parsed for (i.e. for inner HTML). This
 provides stack context (for implicit element creation).
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
list of nodes parsed from the input HTML. Note that the context element, if supplied, is not modified.

  - 

### parseFragment

public static List<Node> parseFragment(String fragmentHtml,
 Element context,
 String baseUri,
 ParseErrorList errorList)
Parse a fragment of HTML into a list of nodes. The context element, if supplied, supplies parsing context.

Parameters:
`fragmentHtml` - the fragment of HTML to parse
`context` - (optional) the element that this HTML fragment is being parsed for (i.e. for inner HTML). This
 provides stack context (for implicit element creation).
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
`errorList` - list to add errors to
Returns:
list of nodes parsed from the input HTML. Note that the context element, if supplied, is not modified.

  - 

### parseXmlFragment

public static List<Node> parseXmlFragment(String fragmentXml,
 String baseUri)
Parse a fragment of XML into a list of nodes.

Parameters:
`fragmentXml` - the fragment of XML to parse
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
list of nodes parsed from the input XML.

  - 

### parseBodyFragment

public static Document parseBodyFragment(String bodyHtml,
 String baseUri)
Parse a fragment of HTML into the `body` of a Document.

Parameters:
`bodyHtml` - fragment of HTML
`baseUri` - base URI of document (i.e. original fetch location), for resolving relative URLs.
Returns:
Document, with empty head, and HTML parsed into body

  - 

### unescapeEntities

public static String unescapeEntities(String string,
 boolean inAttribute)
Utility method to unescape HTML entities from a string.
     

To track errors while unescaping, use
     `unescape(String, boolean)` with a Parser instance that has error tracking enabled.

Parameters:
`string` - HTML escaped string
`inAttribute` - if the string is to be escaped in strict mode (as attributes are)
Returns:
an unescaped string
See Also:

    - `unescape(String, boolean)`

  - 

### unescape

public String unescape(String string,
 boolean inAttribute)
Utility method to unescape HTML entities from a string, using this `Parser`'s configuration (for example, to
     collect errors while unescaping).

Parameters:
`string` - HTML escaped string
`inAttribute` - if the string is to be escaped in strict mode (as attributes are)
Returns:
an unescaped string
See Also:

    - `setTrackErrors(int)`

    - `unescapeEntities(String, boolean)`

  - 

### htmlParser

public static Parser htmlParser()
Create a new HTML parser. This parser treats input as HTML5, and enforces the creation of a normalised document,
 based on a knowledge of the semantics of the incoming tags.

Returns:
a new HTML parser.

  - 

### xmlParser

public static Parser xmlParser()
Create a new XML parser. This parser assumes no knowledge of the incoming tags and does not treat it as HTML,
 rather creates a simple tree directly from the input.

Returns:
a new simple XML parser.