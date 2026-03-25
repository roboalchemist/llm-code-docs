Package org.jsoup.nodes

# Class Range.AttributeRange

java.lang.Object
org.jsoup.nodes.Range.AttributeRange

Enclosing class:
Range

---

public static class Range.AttributeRange
extends Object

- 

## Constructor Summary

Constructors

Constructor
Description
`AttributeRange(Range nameRange,
 Range valueRange)`

Creates a new AttributeRange.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`equals(Object o)`
 
`int`
`hashCode()`
 
`Range`
`nameRange()`

Get the source range for the attribute's name.

`String`
`toString()`

Get a String presentation of this Attribute range, in the form
         `line,column:pos-line,column:pos=line,column:pos-line,column:pos` (name start - name end = val start - val end).
         .

`Range`
`valueRange()`

Get the source range for the attribute's value.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### AttributeRange

public AttributeRange(Range nameRange,
 Range valueRange)
Creates a new AttributeRange. Called during parsing by Token.StartTag.

- 

## Method Details

  - 

### nameRange

public Range nameRange()
Get the source range for the attribute's name.

  - 

### valueRange

public Range valueRange()
Get the source range for the attribute's value.

  - 

### toString

public String toString()
Get a String presentation of this Attribute range, in the form
         `line,column:pos-line,column:pos=line,column:pos-line,column:pos` (name start - name end = val start - val end).
         .

Overrides:
`toString` in class `Object`

  - 

### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`