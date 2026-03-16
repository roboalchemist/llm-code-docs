Package org.jsoup.helper

# Class W3CDom

java.lang.Object
org.jsoup.helper.W3CDom

---

public class W3CDom
extends Object
Helper class to transform a `Document` to a `org.w3c.dom.Document`,
 for integration with toolsets that use the W3C DOM.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static class `
`W3CDom.W3CBuilder`

Implements the conversion by walking the input.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected DocumentBuilderFactory`
`factory`
 
`static final String`
`SourceProperty`

For W3C Documents created by this class, this property is set on each node to link back to the original jsoup node.

`static final String`
`XPathFactoryProperty`

To get support for XPath versions > 1, set this property to the classname of an alternate XPathFactory
     implementation.

- 

## Constructor Summary

Constructors

Constructor
Description
`W3CDom()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`asString(Document doc)`

Serialize a W3C document that was created by `fromJsoup(org.jsoup.nodes.Element)` to a String.

`static String`
`asString(Document doc,
 @Nullable Map<String,String> properties)`

Serialize a W3C document to a String.

`Node`
`contextNode(Document wDoc)`

For a Document created by `fromJsoup(org.jsoup.nodes.Element)`, retrieves the W3C context node.

`static Document`
`convert(Document in)`

Converts a jsoup DOM to a W3C DOM.

`void`
`convert(Document in,
 Document out)`

Converts a jsoup document into the provided W3C Document.

`void`
`convert(Element in,
 Document out)`

Converts a jsoup element into the provided W3C Document.

`Document`
`fromJsoup(Document in)`

Convert a jsoup Document to a W3C Document.

`Document`
`fromJsoup(Element in)`

Convert a jsoup DOM to a W3C Document.

`boolean`
`namespaceAware()`

Returns if this W3C DOM is namespace aware.

`W3CDom`
`namespaceAware(boolean namespaceAware)`

Update the namespace aware setting.

`static HashMap<String,String>`
`OutputHtml()`

Canned default for HTML output.

`static HashMap<String,String>`
`OutputXml()`

Canned default for XML output.

`NodeList`
`selectXpath(String xpath,
 Document doc)`

Evaluate an XPath query against the supplied document, and return the results.

`NodeList`
`selectXpath(String xpath,
 Node contextNode)`

Evaluate an XPath query against the supplied context node, and return the results.

`<T extends Node>
List<T>`
`sourceNodes(NodeList nodeList,
 Class<T> nodeType)`

Retrieves the original jsoup DOM nodes from a nodelist created by this convertor.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### SourceProperty

public static final String SourceProperty
For W3C Documents created by this class, this property is set on each node to link back to the original jsoup node.

See Also:

    - Constant Field Values

  - 

### XPathFactoryProperty

public static final String XPathFactoryProperty
To get support for XPath versions > 1, set this property to the classname of an alternate XPathFactory
     implementation. (For e.g. `net.sf.saxon.xpath.XPathFactoryImpl`).

See Also:

    - Constant Field Values

  - 

### factory

protected DocumentBuilderFactory factory

- 

## Constructor Details

  - 

### W3CDom

public W3CDom()

- 

## Method Details

  - 

### namespaceAware

public boolean namespaceAware()
Returns if this W3C DOM is namespace aware. By default, this will be `true`, but is disabled for simplicity
     when using XPath selectors in `Element.selectXpath(String)`.

Returns:
the current namespace aware setting.

  - 

### namespaceAware

public W3CDom namespaceAware(boolean namespaceAware)
Update the namespace aware setting. This impacts the factory that is used to create W3C nodes from jsoup nodes.
     

For HTML documents, controls if the document will be in the default `http://www.w3.org/1999/xhtml`
     namespace if otherwise unset..

Parameters:
`namespaceAware` - the updated setting
Returns:
this W3CDom, for chaining.

  - 

### convert

public static Document convert(Document in)
Converts a jsoup DOM to a W3C DOM.

Parameters:
`in` - jsoup Document
Returns:
W3C Document

  - 

### asString

public static String asString(Document doc,
 @Nullable Map<String,String> properties)
Serialize a W3C document to a String. Provide Properties to define output settings including if HTML or XML. If
 you don't provide the properties (`null`), the output will be auto-detected based on the content of the
 document.

Parameters:
`doc` - Document
`properties` - (optional/nullable) the output properties to use. See `Transformer.setOutputProperties(Properties)` and `OutputKeys`
Returns:
Document as string
See Also:

    - `OutputHtml()`

    - `OutputXml()`

    - `OutputKeys.ENCODING`

    - `OutputKeys.OMIT_XML_DECLARATION`

    - `OutputKeys.STANDALONE`

    - `OutputKeys.DOCTYPE_PUBLIC`

    - `OutputKeys.CDATA_SECTION_ELEMENTS`

    - `OutputKeys.INDENT`

    - `OutputKeys.MEDIA_TYPE`

  - 

### OutputHtml

public static HashMap<String,String> OutputHtml()
Canned default for HTML output.

  - 

### OutputXml

public static HashMap<String,String> OutputXml()
Canned default for XML output.

  - 

### fromJsoup

public Document fromJsoup(Document in)
Convert a jsoup Document to a W3C Document. The created nodes will link back to the original
 jsoup nodes in the user property `SourceProperty` (but after conversion, changes on one side will not
 flow to the other).

Parameters:
`in` - jsoup doc
Returns:
a W3C DOM Document representing the jsoup Document or Element contents.

  - 

### fromJsoup

public Document fromJsoup(Element in)
Convert a jsoup DOM to a W3C Document. The created nodes will link back to the original
 jsoup nodes in the user property `SourceProperty` (but after conversion, changes on one side will not
 flow to the other). The input Element is used as a context node, but the whole surrounding jsoup Document is
 converted. (If you just want a subtree converted, use `convert(org.jsoup.nodes.Element, Document)`.)

Parameters:
`in` - jsoup element or doc
Returns:
a W3C DOM Document representing the jsoup Document or Element contents.
See Also:

    - `sourceNodes(NodeList, Class)`

    - `contextNode(Document)`

  - 

### convert

public void convert(Document in,
 Document out)
Converts a jsoup document into the provided W3C Document. If required, you can set options on the output
 document before converting.

Parameters:
`in` - jsoup doc
`out` - w3c doc
See Also:

    - `fromJsoup(org.jsoup.nodes.Element)`

  - 

### convert

public void convert(Element in,
 Document out)
Converts a jsoup element into the provided W3C Document. If required, you can set options on the output
 document before converting.

Parameters:
`in` - jsoup element
`out` - w3c doc
See Also:

    - `fromJsoup(org.jsoup.nodes.Element)`

  - 

### selectXpath

public NodeList selectXpath(String xpath,
 Document doc)
Evaluate an XPath query against the supplied document, and return the results.

Parameters:
`xpath` - an XPath query
`doc` - the document to evaluate against
Returns:
the matches nodes

  - 

### selectXpath

public NodeList selectXpath(String xpath,
 Node contextNode)
Evaluate an XPath query against the supplied context node, and return the results.

Parameters:
`xpath` - an XPath query
`contextNode` - the context node to evaluate against
Returns:
the matches nodes

  - 

### sourceNodes

public <T extends Node> List<T> sourceNodes(NodeList nodeList,
 Class<T> nodeType)
Retrieves the original jsoup DOM nodes from a nodelist created by this convertor.

Type Parameters:
`T` - node type
Parameters:
`nodeList` - the W3C nodes to get the original jsoup nodes from
`nodeType` - the jsoup node type to retrieve (e.g. Element, DataNode, etc)
Returns:
a list of the original nodes

  - 

### contextNode

public Node contextNode(Document wDoc)
For a Document created by `fromJsoup(org.jsoup.nodes.Element)`, retrieves the W3C context node.

Parameters:
`wDoc` - Document created by this class
Returns:
the corresponding W3C Node to the jsoup Element that was used as the creating context.

  - 

### asString

public String asString(Document doc)
Serialize a W3C document that was created by `fromJsoup(org.jsoup.nodes.Element)` to a String.
 The output format will be XML or HTML depending on the content of the doc.

Parameters:
`doc` - Document
Returns:
Document as string
See Also:

    - `asString(Document, Map)`