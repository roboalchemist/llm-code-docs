Package org.jsoup.nodes

# Class Attributes

java.lang.Object
org.jsoup.nodes.Attributes

All Implemented Interfaces:
`Cloneable`, `Iterable<Attribute>`

---

public class Attributes
extends Object
implements Iterable<Attribute>, Cloneable
The attributes of an Element.
 

 During parsing, attributes in with the same name in an element are deduplicated, according to the configured parser's
 attribute case-sensitive setting. It is possible to have duplicate attributes subsequently if
 `add(String, String)` vs `put(String, String)` is used.
 
 

 Attribute name and value comparisons are generally **case sensitive**. By default for HTML, attribute names are
 normalized to lower-case on parsing. That means you should use lower-case strings when referring to attributes by
 name.
 

Author:
Jonathan Hedley, [email protected]

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected static final String`
`dataPrefix`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Attributes()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`Attributes`
`add(String key,
 @Nullable String value)`

Adds a new attribute.

`void`
`addAll(Attributes incoming)`

Add all the attributes from the incoming set to this set.

`List<Attribute>`
`asList()`

Get the attributes as a List, for iteration.

`@Nullable Attribute`
`attribute(String key)`

Get an Attribute by key.

`Attributes`
`clone()`
 
`Map<String,String>`
`dataset()`

Retrieves a filtered view of attributes that are HTML5 custom data attributes; that is, attributes with keys
 starting with `data-`.

`int`
`deduplicate(ParseSettings settings)`

Internal method.

`boolean`
`equals(@Nullable Object o)`

Checks if these attributes are equal to another set of attributes, by comparing the two sets.

`String`
`get(String key)`

Get an attribute value by key.

`String`
`getIgnoreCase(String key)`

Get an attribute's value by case-insensitive key

`boolean`
`hasDeclaredValueForKey(String key)`

Check if these attributes contain an attribute with a value for this key.

`boolean`
`hasDeclaredValueForKeyIgnoreCase(String key)`

Check if these attributes contain an attribute with a value for this key.

`int`
`hashCode()`

Calculates the hashcode of these attributes, by iterating all attributes and summing their hashcodes.

`boolean`
`hasKey(String key)`

Tests if these attributes contain an attribute with this key.

`boolean`
`hasKeyIgnoreCase(String key)`

Tests if these attributes contain an attribute with this key.

`String`
`html()`

Get the HTML representation of these attributes.

`boolean`
`isEmpty()`

Test if this Attributes list is empty.

`Iterator<Attribute>`
`iterator()`
 
`void`
`normalize()`

Internal method.

`Attributes`
`put(String key,
 boolean value)`

Set a new boolean attribute.

`Attributes`
`put(String key,
 @Nullable String value)`

Set a new attribute, or replace an existing one by key.

`Attributes`
`put(Attribute attribute)`

Set a new attribute, or replace an existing one by key.

`void`
`remove(String key)`

Remove an attribute by key.

`void`
`removeIgnoreCase(String key)`

Remove an attribute by key.

`int`
`size()`

Get the number of attributes in this set, excluding any internal-only attributes (e.g. user data).

`Range.AttributeRange`
`sourceRange(String key)`

Get the source ranges (start to end position) in the original input source from which this attribute's **name**
     and **value** were parsed.

`Attributes`
`sourceRange(String key,
 Range.AttributeRange range)`

Set the source ranges (start to end position) from which this attribute's **name** and **value** were parsed.

`String`
`toString()`
 
`@Nullable Object`
`userData(String key)`

Get an arbitrary user-data object by key.

`Attributes`
`userData(String key,
 @Nullable Object value)`

Set an arbitrary user-data object by key.

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`forEach, spliterator`

- 

## Field Details

  - 

### dataPrefix

protected static final String dataPrefix

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### Attributes

public Attributes()

- 

## Method Details

  - 

### get

public String get(String key)
Get an attribute value by key.

Parameters:
`key` - the (case-sensitive) attribute key
Returns:
the attribute value if set; or empty string if not set (or a boolean attribute).
See Also:

    - `hasKey(String)`

  - 

### attribute

public @Nullable Attribute attribute(String key)
Get an Attribute by key. The Attribute will remain connected to these Attributes, so changes made via
     `Attribute.setKey(String)`, `Attribute.setValue(String)` etc will cascade back to these Attributes and
     their owning Element.

Parameters:
`key` - the (case-sensitive) attribute key
Returns:
the Attribute for this key, or null if not present.
Since:
1.17.2

  - 

### getIgnoreCase

public String getIgnoreCase(String key)
Get an attribute's value by case-insensitive key

Parameters:
`key` - the attribute name
Returns:
the first matching attribute value if set; or empty string if not set (ora boolean attribute).

  - 

### add

public Attributes add(String key,
 @Nullable String value)
Adds a new attribute. Will produce duplicates if the key already exists.

See Also:

    - `put(String, String)`

  - 

### put

public Attributes put(String key,
 @Nullable String value)
Set a new attribute, or replace an existing one by key.

Parameters:
`key` - case sensitive attribute key (not null)
`value` - attribute value (which can be null, to set a true boolean attribute)
Returns:
these attributes, for chaining

  - 

### userData

public @Nullable Object userData(String key)
Get an arbitrary user-data object by key.

Parameters:
`key` - case-sensitive key to the object.
Returns:
the object associated to this key, or `null` if not found.
Since:
1.17.1
See Also:

    - `userData(String key, Object val)`

  - 

### userData

public Attributes userData(String key,
 @Nullable Object value)
Set an arbitrary user-data object by key. Will be treated as an internal attribute, so will not be emitted in HTML.

Parameters:
`key` - case-sensitive key
`value` - object value. Providing a `null` value has the effect of removing the key from the userData map.
Returns:
these attributes
Since:
1.17.1
See Also:

    - `userData(String key)`

  - 

### put

public Attributes put(String key,
 boolean value)
Set a new boolean attribute. Removes the attribute if the value is false.

Parameters:
`key` - case **insensitive** attribute key
`value` - attribute value
Returns:
these attributes, for chaining

  - 

### put

public Attributes put(Attribute attribute)
Set a new attribute, or replace an existing one by key.

Parameters:
`attribute` - attribute with case-sensitive key
Returns:
these attributes, for chaining

  - 

### remove

public void remove(String key)
Remove an attribute by key. **Case sensitive.**

Parameters:
`key` - attribute key to remove

  - 

### removeIgnoreCase

public void removeIgnoreCase(String key)
Remove an attribute by key. **Case insensitive.**

Parameters:
`key` - attribute key to remove

  - 

### hasKey

public boolean hasKey(String key)
Tests if these attributes contain an attribute with this key.

Parameters:
`key` - case-sensitive key to check for
Returns:
true if key exists, false otherwise

  - 

### hasKeyIgnoreCase

public boolean hasKeyIgnoreCase(String key)
Tests if these attributes contain an attribute with this key.

Parameters:
`key` - key to check for
Returns:
true if key exists, false otherwise

  - 

### hasDeclaredValueForKey

public boolean hasDeclaredValueForKey(String key)
Check if these attributes contain an attribute with a value for this key.

Parameters:
`key` - key to check for
Returns:
true if key exists, and it has a value

  - 

### hasDeclaredValueForKeyIgnoreCase

public boolean hasDeclaredValueForKeyIgnoreCase(String key)
Check if these attributes contain an attribute with a value for this key.

Parameters:
`key` - case-insensitive key to check for
Returns:
true if key exists, and it has a value

  - 

### size

public int size()
Get the number of attributes in this set, excluding any internal-only attributes (e.g. user data).
     

Internal attributes are excluded from the `html()`, `asList()`, and `iterator()`
     methods.

Returns:
size

  - 

### isEmpty

public boolean isEmpty()
Test if this Attributes list is empty.
     

This does not include internal attributes, such as user data.

  - 

### addAll

public void addAll(Attributes incoming)
Add all the attributes from the incoming set to this set.

Parameters:
`incoming` - attributes to add to these attributes.

  - 

### sourceRange

public Range.AttributeRange sourceRange(String key)
Get the source ranges (start to end position) in the original input source from which this attribute's **name**
     and **value** were parsed.
     

Position tracking must be enabled prior to parsing the content.

Parameters:
`key` - the attribute name
Returns:
the ranges for the attribute's name and value, or `untracked` if the attribute does not exist or its range
     was not tracked.
Since:
1.17.1
See Also:

    - `Parser.setTrackPosition(boolean)`

    - `Attribute.sourceRange()`

    - `Node.sourceRange()`

    - `Element.endSourceRange()`

  - 

### sourceRange

public Attributes sourceRange(String key,
 Range.AttributeRange range)
Set the source ranges (start to end position) from which this attribute's **name** and **value** were parsed.

Parameters:
`key` - the attribute name
`range` - the range for the attribute's name and value
Returns:
these attributes, for chaining
Since:
1.18.2

  - 

### iterator

public Iterator<Attribute> iterator()

Specified by:
`iterator` in interface `Iterable<Attribute>`

  - 

### asList

public List<Attribute> asList()
Get the attributes as a List, for iteration.

Returns:
a view of the attributes as an unmodifiable List.

  - 

### dataset

public Map<String,String> dataset()
Retrieves a filtered view of attributes that are HTML5 custom data attributes; that is, attributes with keys
 starting with `data-`.

Returns:
map of custom data attributes.

  - 

### html

public String html()
Get the HTML representation of these attributes.

Returns:
HTML

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`

  - 

### equals

public boolean equals(@Nullable Object o)
Checks if these attributes are equal to another set of attributes, by comparing the two sets. Note that the order
 of the attributes does not impact this equality (as per the Map interface equals()).

Overrides:
`equals` in class `Object`
Parameters:
`o` - attributes to compare with
Returns:
if both sets of attributes have the same content

  - 

### hashCode

public int hashCode()
Calculates the hashcode of these attributes, by iterating all attributes and summing their hashcodes.

Overrides:
`hashCode` in class `Object`
Returns:
calculated hashcode

  - 

### clone

public Attributes clone()

Overrides:
`clone` in class `Object`

  - 

### normalize

public void normalize()
Internal method. Lowercases all (non-internal) keys.

  - 

### deduplicate

public int deduplicate(ParseSettings settings)
Internal method. Removes duplicate attribute by name. Settings for case sensitivity of key names.

Parameters:
`settings` - case sensitivity
Returns:
number of removed dupes