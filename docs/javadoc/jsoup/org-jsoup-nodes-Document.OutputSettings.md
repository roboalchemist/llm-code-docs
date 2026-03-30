Package org.jsoup.nodes

# Class Document.OutputSettings

java.lang.Object
org.jsoup.nodes.Document.OutputSettings

All Implemented Interfaces:
`Cloneable`

Enclosing class:
Document

---

public static class Document.OutputSettings
extends Object
implements Cloneable
A Document's output settings control the form of the text() and html() methods.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`Document.OutputSettings.Syntax`

The output serialization syntax.

- 

## Constructor Summary

Constructors

Constructor
Description
`OutputSettings()`

Create a new OutputSettings object, with the default settings (UTF-8, HTML, EscapeMode.base, pretty-printing,
         indent amount of 1).

- 

## Method Summary

Modifier and Type
Method
Description
`Charset`
`charset()`

Get the document's current output charset, which is used to control which characters are escaped when
 generating HTML (via the `html()` methods), and which are kept intact.

`Document.OutputSettings`
`charset(String charset)`

Update the document's output charset.

`Document.OutputSettings`
`charset(Charset charset)`

Update the document's output charset.

`Document.OutputSettings`
`clone()`
 
`Entities.EscapeMode`
`escapeMode()`

Get the document's current entity escape mode:
         
         `xhtml`, the minimal named entities in XHTML / XML
         `base`, which provides a limited set of named HTML
         entities and escapes other characters as numbered entities for maximum compatibility
         `extended`,
         which uses the complete set of HTML named entities.
         

`Document.OutputSettings`
`escapeMode(Entities.EscapeMode escapeMode)`

Set the document's escape mode, which determines how characters are escaped when the output character set
 does not support a given character:- using either a named or a numbered escape.

`int`
`indentAmount()`

Get the current tag indent amount, used when pretty printing.

`Document.OutputSettings`
`indentAmount(int indentAmount)`

Set the indent amount for pretty printing

`int`
`maxPaddingWidth()`

Get the current max padding amount, used when pretty printing
 so very deeply nested nodes don't get insane padding amounts.

`Document.OutputSettings`
`maxPaddingWidth(int maxPaddingWidth)`

Set the max padding amount for pretty printing so very deeply nested nodes don't get insane padding amounts.

`boolean`
`outline()`

Get if outline mode is enabled.

`Document.OutputSettings`
`outline(boolean outlineMode)`

Enable or disable HTML outline mode.

`boolean`
`prettyPrint()`

Get if pretty printing is enabled.

`Document.OutputSettings`
`prettyPrint(boolean pretty)`

Enable or disable pretty printing.

`Document.OutputSettings.Syntax`
`syntax()`

Get the document's current output syntax.

`Document.OutputSettings`
`syntax(Document.OutputSettings.Syntax syntax)`

Set the document's output syntax.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### OutputSettings

public OutputSettings()
Create a new OutputSettings object, with the default settings (UTF-8, HTML, EscapeMode.base, pretty-printing,
         indent amount of 1).

- 

## Method Details

  - 

### escapeMode

public Entities.EscapeMode escapeMode()
Get the document's current entity escape mode:
         

         
    - `xhtml`, the minimal named entities in XHTML / XML
         
    - `base`, which provides a limited set of named HTML
         entities and escapes other characters as numbered entities for maximum compatibility
         
    - `extended`,
         which uses the complete set of HTML named entities.
         

         

The default escape mode is `base`.

Returns:
the document's current escape mode

  - 

### escapeMode

public Document.OutputSettings escapeMode(Entities.EscapeMode escapeMode)
Set the document's escape mode, which determines how characters are escaped when the output character set
 does not support a given character:- using either a named or a numbered escape.

Parameters:
`escapeMode` - the new escape mode to use
Returns:
the document's output settings, for chaining

  - 

### charset

public Charset charset()
Get the document's current output charset, which is used to control which characters are escaped when
 generating HTML (via the `html()` methods), and which are kept intact.
 

 Where possible (when parsing from a URL or File), the document's output charset is automatically set to the
 input charset. Otherwise, it defaults to UTF-8.

Returns:
the document's current charset.

  - 

### charset

public Document.OutputSettings charset(Charset charset)
Update the document's output charset.

Parameters:
`charset` - the new charset to use.
Returns:
the document's output settings, for chaining

  - 

### charset

public Document.OutputSettings charset(String charset)
Update the document's output charset.

Parameters:
`charset` - the new charset (by name) to use.
Returns:
the document's output settings, for chaining

  - 

### syntax

public Document.OutputSettings.Syntax syntax()
Get the document's current output syntax.

Returns:
current syntax

  - 

### syntax

public Document.OutputSettings syntax(Document.OutputSettings.Syntax syntax)
Set the document's output syntax. Either `html`, with empty tags and boolean attributes (etc), or
 `xml`, with self-closing tags.
 

When set to `xml`, the `escapeMode` is
 automatically set to `Entities.EscapeMode.xhtml`, but may be subsequently changed if desired.

Parameters:
`syntax` - serialization syntax
Returns:
the document's output settings, for chaining

  - 

### prettyPrint

public boolean prettyPrint()
Get if pretty printing is enabled. Default is true. If disabled, the HTML output methods will not re-format
 the output, and the output will generally look like the input.

Returns:
if pretty printing is enabled.

  - 

### prettyPrint

public Document.OutputSettings prettyPrint(boolean pretty)
Enable or disable pretty printing.

Parameters:
`pretty` - new pretty print setting
Returns:
this, for chaining

  - 

### outline

public boolean outline()
Get if outline mode is enabled. Default is false. If enabled, the HTML output methods will consider
 all tags as block.

Returns:
if outline mode is enabled.

  - 

### outline

public Document.OutputSettings outline(boolean outlineMode)
Enable or disable HTML outline mode.

Parameters:
`outlineMode` - new outline setting
Returns:
this, for chaining

  - 

### indentAmount

public int indentAmount()
Get the current tag indent amount, used when pretty printing.

Returns:
the current indent amount

  - 

### indentAmount

public Document.OutputSettings indentAmount(int indentAmount)
Set the indent amount for pretty printing

Parameters:
`indentAmount` - number of spaces to use for indenting each level. Must be >= 0.
Returns:
this, for chaining

  - 

### maxPaddingWidth

public int maxPaddingWidth()
Get the current max padding amount, used when pretty printing
 so very deeply nested nodes don't get insane padding amounts.

Returns:
the current indent amount

  - 

### maxPaddingWidth

public Document.OutputSettings maxPaddingWidth(int maxPaddingWidth)
Set the max padding amount for pretty printing so very deeply nested nodes don't get insane padding amounts.

Parameters:
`maxPaddingWidth` - number of spaces to use for indenting each level of nested nodes. Must be >= -1.
        Default is 30 and -1 means unlimited.
Returns:
this, for chaining

  - 

### clone

public Document.OutputSettings clone()

Overrides:
`clone` in class `Object`