Package org.jsoup.nodes

# Class Range

java.lang.Object
org.jsoup.nodes.Range

---

public class Range
extends Object
A Range object tracks the character positions in the original input source where a Node starts or ends. If you want to
 track these positions, tracking must be enabled in the Parser with
 `Parser.setTrackPosition(boolean)`.

Since:
1.15.2
See Also:

- `Node.sourceRange()`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`Range.AttributeRange`
 
`static class `
`Range.Position`

A Position object tracks the character position in the original input source where a Node starts or ends.

- 

## Constructor Summary

Constructors

Constructor
Description
`Range(Range.Position start,
 Range.Position end)`

Creates a new Range with start and end Positions.

- 

## Method Summary

Modifier and Type
Method
Description
`Range.Position`
`end()`

Get the end position of this node.

`int`
`endPos()`

Get the ending cursor position of this range.

`boolean`
`equals(Object o)`
 
`int`
`hashCode()`
 
`boolean`
`isImplicit()`

Checks if the range represents a node that was implicitly created / closed.

`boolean`
`isTracked()`

Test if this source range was tracked during parsing.

`Range.Position`
`start()`

Get the start position of this node.

`int`
`startPos()`

Get the starting cursor position of this range.

`String`
`toString()`

Gets a String presentation of this Range, in the format `line,column:pos-line,column:pos`.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Range

public Range(Range.Position start,
 Range.Position end)
Creates a new Range with start and end Positions. Called by TreeBuilder when position tracking is on.

Parameters:
`start` - the start position
`end` - the end position

- 

## Method Details

  - 

### start

public Range.Position start()
Get the start position of this node.

Returns:
the start position

  - 

### startPos

public int startPos()
Get the starting cursor position of this range.

Returns:
the 0-based start cursor position.
Since:
1.17.1

  - 

### end

public Range.Position end()
Get the end position of this node.

Returns:
the end position

  - 

### endPos

public int endPos()
Get the ending cursor position of this range.

Returns:
the 0-based ending cursor position.
Since:
1.17.1

  - 

### isTracked

public boolean isTracked()
Test if this source range was tracked during parsing.

Returns:
true if this was tracked during parsing, false otherwise (and all fields will be `-1`).

  - 

### isImplicit

public boolean isImplicit()
Checks if the range represents a node that was implicitly created / closed.
     

For example, with HTML of `<p>One<p>Two`, both `p` elements will have an explicit
     `Node.sourceRange()` but an implicit `Element.endSourceRange()` marking the end position, as neither
     have closing `</p>` tags. The TextNodes will have explicit sourceRanges.
     

A range is considered implicit if its start and end positions are the same.

Returns:
true if the range is tracked and its start and end positions are the same, false otherwise.
Since:
1.17.1

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

  - 

### toString

public String toString()
Gets a String presentation of this Range, in the format `line,column:pos-line,column:pos`.

Overrides:
`toString` in class `Object`
Returns:
a String