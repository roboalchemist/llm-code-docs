Package org.jsoup.parser

# Class CharacterReader

java.lang.Object
org.jsoup.parser.CharacterReader

All Implemented Interfaces:
`AutoCloseable`

---

public final class CharacterReader
extends Object
implements AutoCloseable
CharacterReader consumes tokens off a string. Used internally by jsoup. API subject to changes.
 

If the underlying reader throws an IOException during any operation, the CharacterReader will throw an
 `UncheckedIOException`. That won't happen with String / StringReader inputs.

- 

## Constructor Summary

Constructors

Constructor
Description
`CharacterReader(Reader input)`
 
`CharacterReader(Reader input,
 int sz)`
 
`CharacterReader(String input)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`advance()`

Moves the current position by one.

`void`
`close()`
 
`int`
`columnNumber()`

Get the current column number (that the reader has consumed to).

`char`
`consume()`

Consume one character off the queue.

`String`
`consumeTo(char c)`

Reads characters up to the specific char.

`String`
`consumeTo(String seq)`

Reads the characters up to (but not including) the specified case-sensitive string.

`String`
`consumeToAny(char... chars)`

Read characters until the first of any delimiters is found.

`char`
`current()`

Get the char at the current position.

`boolean`
`isEmpty()`

Tests if all the content has been read.

`boolean`
`isTrackNewlines()`

Check if the tracking of newlines is enabled.

`int`
`lineNumber()`

Get the current line number (that the reader has consumed to).

`int`
`pos()`

Gets the position currently read to in the content.

`String`
`toString()`
 
`void`
`trackNewlines(boolean track)`

Enables or disables line number tracking.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### CharacterReader

public CharacterReader(Reader input,
 int sz)

  - 

### CharacterReader

public CharacterReader(Reader input)

  - 

### CharacterReader

public CharacterReader(String input)

- 

## Method Details

  - 

### close

public void close()

Specified by:
`close` in interface `AutoCloseable`

  - 

### pos

public int pos()
Gets the position currently read to in the content. Starts at 0.

Returns:
current position

  - 

### trackNewlines

public void trackNewlines(boolean track)
Enables or disables line number tracking. By default, will be **off**.Tracking line numbers improves the
     legibility of parser error messages, for example. Tracking should be enabled before any content is read to be of
     use.

Parameters:
`track` - set tracking on|off
Since:
1.14.3

  - 

### isTrackNewlines

public boolean isTrackNewlines()
Check if the tracking of newlines is enabled.

Returns:
the current newline tracking state
Since:
1.14.3

  - 

### lineNumber

public int lineNumber()
Get the current line number (that the reader has consumed to). Starts at line #1.

Returns:
the current line number, or 1 if line tracking is not enabled.
Since:
1.14.3
See Also:

    - `trackNewlines(boolean)`

  - 

### columnNumber

public int columnNumber()
Get the current column number (that the reader has consumed to). Starts at column #1.

Returns:
the current column number
Since:
1.14.3
See Also:

    - `trackNewlines(boolean)`

  - 

### isEmpty

public boolean isEmpty()
Tests if all the content has been read.

Returns:
true if nothing left to read.

  - 

### current

public char current()
Get the char at the current position.

Returns:
char

  - 

### consume

public char consume()
Consume one character off the queue.

Returns:
first character on queue, or EOF if the queue is empty.

  - 

### advance

public void advance()
Moves the current position by one.

  - 

### consumeTo

public String consumeTo(char c)
Reads characters up to the specific char.

Parameters:
`c` - the delimiter
Returns:
the chars read

  - 

### consumeTo

public String consumeTo(String seq)
Reads the characters up to (but not including) the specified case-sensitive string.
     

If the sequence is not found in the buffer, will return the remainder of the current buffered amount, less the
     length of the sequence, such that this call may be repeated.

Parameters:
`seq` - the delimiter
Returns:
the chars read

  - 

### consumeToAny

public String consumeToAny(char... chars)
Read characters until the first of any delimiters is found.

Parameters:
`chars` - delimiters to scan for
Returns:
characters read up to the matched delimiter.

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`