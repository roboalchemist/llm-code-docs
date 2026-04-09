Package org.jsoup.nodes

# Class Range.Position

java.lang.Object
org.jsoup.nodes.Range.Position

Enclosing class:
Range

---

public static class Range.Position
extends Object
A Position object tracks the character position in the original input source where a Node starts or ends. If you want to
     track these positions, tracking must be enabled in the Parser with
     `Parser.setTrackPosition(boolean)`.

See Also:

- `Node.sourceRange()`

- 

## Constructor Summary

Constructors

Constructor
Description
`Position(int pos,
 int lineNumber,
 int columnNumber)`

Create a new Position object.

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`columnNumber()`

Gets the cursor number (1-based) of the original input source that this Position was read at.

`boolean`
`equals(Object o)`
 
`int`
`hashCode()`
 
`boolean`
`isTracked()`

Test if this position was tracked during parsing.

`int`
`lineNumber()`

Gets the line number (1-based) of the original input source that this Position was read at.

`int`
`pos()`

Gets the position index (0-based) of the original input source that this Position was read at.

`String`
`toString()`

Gets a String presentation of this Position, in the format `line,column:pos`.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Position

public Position(int pos,
 int lineNumber,
 int columnNumber)
Create a new Position object. Called by the TreeBuilder if source position tracking is on.

Parameters:
`pos` - position index
`lineNumber` - line number
`columnNumber` - column number

- 

## Method Details

  - 

### pos

public int pos()
Gets the position index (0-based) of the original input source that this Position was read at. This tracks the
         total number of characters read into the source at this position, regardless of the number of preceding lines.

Returns:
the position, or `-1` if untracked.

  - 

### lineNumber

public int lineNumber()
Gets the line number (1-based) of the original input source that this Position was read at.

Returns:
the line number, or `-1` if untracked.

  - 

### columnNumber

public int columnNumber()
Gets the cursor number (1-based) of the original input source that this Position was read at. The cursor number
         resets to 1 on every new line.

Returns:
the cursor number, or `-1` if untracked.

  - 

### isTracked

public boolean isTracked()
Test if this position was tracked during parsing.

Returns:
true if this was tracked during parsing, false otherwise (and all fields will be `-1`).

  - 

### toString

public String toString()
Gets a String presentation of this Position, in the format `line,column:pos`.

Overrides:
`toString` in class `Object`
Returns:
a String

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