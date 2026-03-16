Package org.jsoup.nodes

# Class Attribute

java.lang.Object
org.jsoup.nodes.Attribute

All Implemented Interfaces:
`Cloneable`, `Map.Entry<String,String>`

---

public class Attribute
extends Object
implements Map.Entry<String,String>, Cloneable
A single key + value attribute. (Only used for presentation.)

- 

## Constructor Summary

Constructors

Constructor
Description
`Attribute(String key,
 @Nullable String value)`

Create a new attribute from unencoded (raw) key and value.

`Attribute(String key,
 @Nullable String val,
 @Nullable Attributes parent)`

Create a new attribute from unencoded (raw) key and value.

- 

## Method Summary

Modifier and Type
Method
Description
`Attribute`
`clone()`
 
`static Attribute`
`createFromEncoded(String unencodedKey,
 String encodedValue)`

Create a new Attribute from an unencoded key and a HTML attribute encoded value.

`boolean`
`equals(@Nullable Object o)`
 
`String`
`getKey()`

Get the attribute's key (aka name).

`static @Nullable String`
`getValidKey(String key,
 Document.OutputSettings.Syntax syntax)`

Get a valid attribute key for the given syntax.

`String`
`getValue()`

Get the attribute value.

`boolean`
`hasDeclaredValue()`

Check if this Attribute has a value.

`int`
`hashCode()`
 
`String`
`html()`

Get the HTML representation of this attribute; e.g.

`protected void`
`html(Appendable accum,
 Document.OutputSettings out)`

Deprecated.
internal method; use `html(String, String, QuietAppendable, Document.OutputSettings)` with `QuietAppendable.wrap(Appendable)` instead.

`protected static void`
`html(String key,
 @Nullable String val,
 Appendable accum,
 Document.OutputSettings out)`

Deprecated.
internal method; use `html(String, String, QuietAppendable, Document.OutputSettings)` with `QuietAppendable.wrap(Appendable)` instead.

`static boolean`
`isBooleanAttribute(String key)`

Checks if this attribute name is defined as a boolean attribute in HTML5

`protected boolean`
`isDataAttribute()`
 
`protected static boolean`
`isDataAttribute(String key)`
 
`String`
`localName()`

Get this attribute's local name.

`String`
`namespace()`

Get this attribute's namespace URI, if the attribute was prefixed with a defined namespace name.

`String`
`prefix()`

Get this attribute's key prefix, if it has one; else the empty string.

`void`
`setKey(String key)`

Set the attribute key; case is preserved.

`String`
`setValue(@Nullable String val)`

Set the attribute value.

`protected static boolean`
`shouldCollapseAttribute(String key,
 @Nullable String val,
 Document.OutputSettings out)`
 
`protected final boolean`
`shouldCollapseAttribute(Document.OutputSettings out)`

Deprecated.
internal method; use `shouldCollapseAttribute(String, String, Document.OutputSettings)` instead.

`Range.AttributeRange`
`sourceRange()`

Get the source ranges (start to end positions) in the original input source from which this attribute's **name**
     and **value** were parsed.

`String`
`toString()`

Get the string representation of this attribute, implemented as `html()`.

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Attribute

public Attribute(String key,
 @Nullable String value)
Create a new attribute from unencoded (raw) key and value.

Parameters:
`key` - attribute key; case is preserved.
`value` - attribute value (may be null)
See Also:

    - `createFromEncoded(java.lang.String, java.lang.String)`

  - 

### Attribute

public Attribute(String key,
 @Nullable String val,
 @Nullable Attributes parent)
Create a new attribute from unencoded (raw) key and value.

Parameters:
`key` - attribute key; case is preserved.
`val` - attribute value (may be null)
`parent` - the containing Attributes (this Attribute is not automatically added to said Attributes)
See Also:

    - `createFromEncoded(java.lang.String, java.lang.String)`

- 

## Method Details

  - 

### getKey

public String getKey()
Get the attribute's key (aka name).

Specified by:
`getKey` in interface `Map.Entry<String,String>`
Returns:
the attribute key

  - 

### setKey

public void setKey(String key)
Set the attribute key; case is preserved.

Parameters:
`key` - the new key; must not be null

  - 

### getValue

public String getValue()
Get the attribute value. Will return an empty string if the value is not set.

Specified by:
`getValue` in interface `Map.Entry<String,String>`
Returns:
the attribute value

  - 

### hasDeclaredValue

public boolean hasDeclaredValue()
Check if this Attribute has a value. Set boolean attributes have no value.

Returns:
if this is a boolean attribute / attribute without a value

  - 

### setValue

public String setValue(@Nullable String val)
Set the attribute value.

Specified by:
`setValue` in interface `Map.Entry<String,String>`
Parameters:
`val` - the new attribute value; may be null (to set an enabled boolean attribute)
Returns:
the previous value (if was null; an empty string)

  - 

### prefix

public String prefix()
Get this attribute's key prefix, if it has one; else the empty string.
     

For example, the attribute `og:title` has prefix `og`, and local `title`.

Returns:
the tag's prefix
Since:
1.20.1

  - 

### localName

public String localName()
Get this attribute's local name. The local name is the name without the prefix (if any).
     

For example, the attribute key `og:title` has local name `title`.

Returns:
the tag's local name
Since:
1.20.1

  - 

### namespace

public String namespace()
Get this attribute's namespace URI, if the attribute was prefixed with a defined namespace name. Otherwise, returns
     the empty string. These will only be defined if using the XML parser.

Returns:
the tag's namespace URI, or empty string if not defined
Since:
1.20.1

  - 

### html

public String html()
Get the HTML representation of this attribute; e.g. `href="index.html"`.

Returns:
HTML

  - 

### sourceRange

public Range.AttributeRange sourceRange()
Get the source ranges (start to end positions) in the original input source from which this attribute's **name**
     and **value** were parsed.
     

Position tracking must be enabled prior to parsing the content.

Returns:
the ranges for the attribute's name and value, or `untracked` if the attribute does not exist or its range
     was not tracked.
Since:
1.17.1
See Also:

    - `Parser.setTrackPosition(boolean)`

    - `Attributes.sourceRange(String)`

    - `Node.sourceRange()`

    - `Element.endSourceRange()`

  - 

### html

@Deprecated
protected void html(Appendable accum,
 Document.OutputSettings out)
             throws IOException
Deprecated.
internal method; use `html(String, String, QuietAppendable, Document.OutputSettings)` with `QuietAppendable.wrap(Appendable)` instead. Will be removed in jsoup 1.24.1.

Throws:
`IOException`

  - 

### html

@Deprecated
protected static void html(String key,
 @Nullable String val,
 Appendable accum,
 Document.OutputSettings out)
                    throws IOException
Deprecated.
internal method; use `html(String, String, QuietAppendable, Document.OutputSettings)` with `QuietAppendable.wrap(Appendable)` instead. Will be removed in jsoup 1.24.1.

Throws:
`IOException`

  - 

### getValidKey

public static @Nullable String getValidKey(String key,
 Document.OutputSettings.Syntax syntax)
Get a valid attribute key for the given syntax. If the key is not valid, it will be coerced into a valid key.

Parameters:
`key` - the original attribute key
`syntax` - HTML or XML
Returns:
the original key if it's valid; a key with invalid characters replaced with "_" otherwise; or null if a valid key could not be created.

  - 

### toString

public String toString()
Get the string representation of this attribute, implemented as `html()`.

Overrides:
`toString` in class `Object`
Returns:
string

  - 

### createFromEncoded

public static Attribute createFromEncoded(String unencodedKey,
 String encodedValue)
Create a new Attribute from an unencoded key and a HTML attribute encoded value.

Parameters:
`unencodedKey` - assumes the key is not encoded, as can be only run of simple \w chars.
`encodedValue` - HTML attribute encoded value
Returns:
attribute

  - 

### isDataAttribute

protected boolean isDataAttribute()

  - 

### isDataAttribute

protected static boolean isDataAttribute(String key)

  - 

### shouldCollapseAttribute

@Deprecated
protected final boolean shouldCollapseAttribute(Document.OutputSettings out)
Deprecated.
internal method; use `shouldCollapseAttribute(String, String, Document.OutputSettings)` instead. Will be removed in jsoup 1.24.1.

Collapsible if it's a boolean attribute and value is empty or same as name

Parameters:
`out` - output settings
Returns:
Returns whether collapsible or not

  - 

### shouldCollapseAttribute

protected static boolean shouldCollapseAttribute(String key,
 @Nullable String val,
 Document.OutputSettings out)

  - 

### isBooleanAttribute

public static boolean isBooleanAttribute(String key)
Checks if this attribute name is defined as a boolean attribute in HTML5

  - 

### equals

public boolean equals(@Nullable Object o)

Specified by:
`equals` in interface `Map.Entry<String,String>`
Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Specified by:
`hashCode` in interface `Map.Entry<String,String>`
Overrides:
`hashCode` in class `Object`

  - 

### clone

public Attribute clone()

Overrides:
`clone` in class `Object`