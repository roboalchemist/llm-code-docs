Package org.jsoup.parser

# Class ParseError

java.lang.Object
org.jsoup.parser.ParseError

---

public class ParseError
extends Object
A Parse Error records an error in the input HTML that occurs in either the tokenisation or the tree building phase.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getCursorPos()`

Get the formatted line:column cursor position where the error occurred.

`String`
`getErrorMessage()`

Retrieve the error message.

`int`
`getPosition()`

Retrieves the offset of the error.

`String`
`toString()`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Method Details

  - 

### getErrorMessage

public String getErrorMessage()
Retrieve the error message.

Returns:
the error message.

  - 

### getPosition

public int getPosition()
Retrieves the offset of the error.

Returns:
error offset within input

  - 

### getCursorPos

public String getCursorPos()
Get the formatted line:column cursor position where the error occurred.

Returns:
line:number cursor position

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`