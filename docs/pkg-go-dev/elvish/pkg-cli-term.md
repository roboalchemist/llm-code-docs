### Overview ¶

Package term provides functionality for working with terminals.

### Index ¶

- Variables

-
        func BuffersHeight(bufs ...*Buffer) (l int)

-
        func CellsWidth(cs []Cell) int

-
        func CompareCells(r1, r2 []Cell) (bool, int)

-
        func IsReadErrorRecoverable(err error) bool

-
        func Sanitize(in, out *os.File)

-
        func Setup(in, out *os.File) (func() error, error)

-
        func SetupGlobal() func()

-
          type Buffer

-

-
            func NewBuffer(width int) *Buffer

-

-
            func (b *Buffer) Buffer() *Buffer

-
            func (b *Buffer) Col() int

-
            func (b *Buffer) Cursor() Pos

-
            func (b *Buffer) Extend(b2 *Buffer, moveDot bool)

-
            func (b *Buffer) ExtendRight(b2 *Buffer)

-
            func (b *Buffer) TTYString() string

-
            func (b *Buffer) TrimToLines(low, high int)

-
          type BufferBuilder

-

-
            func NewBufferBuilder(width int) *BufferBuilder

-

-
            func (bb *BufferBuilder) Buffer() *Buffer

-
            func (bb *BufferBuilder) Cursor() Pos

-
            func (bb *BufferBuilder) MarkLines(args ...interface{}) *BufferBuilder

-
            func (bb *BufferBuilder) Newline() *BufferBuilder

-
            func (bb *BufferBuilder) SetDotHere() *BufferBuilder

-
            func (bb *BufferBuilder) SetEagerWrap(v bool) *BufferBuilder

-
            func (bb *BufferBuilder) SetIndent(indent int) *BufferBuilder

-
            func (bb *BufferBuilder) Write(text string, ts ...ui.Styling) *BufferBuilder

-
            func (bb *BufferBuilder) WriteRuneSGR(r rune, style string) *BufferBuilder

-
            func (bb *BufferBuilder) WriteSpaces(w int, ts ...ui.Styling) *BufferBuilder

-
            func (bb *BufferBuilder) WriteStringSGR(text, style string) *BufferBuilder

-
            func (bb *BufferBuilder) WriteStyled(t ui.Text) *BufferBuilder

-
          type Cell

-
          type CursorPosition

-
          type Event

-
          type FatalErrorEvent

-
          type KeyEvent

-

-
            func K(r rune, mods ...ui.Mod) KeyEvent

-
          type Line

-
          type Lines

-
          type MouseEvent

-
          type NonfatalErrorEvent

-
          type PasteSetting

-
          type Pos

-
          type Reader

-

-
            func NewReader(f *os.File) Reader

-
          type Writer

-

-
            func NewWriter(f io.Writer) Writer

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var DotHere = struct{ x struct{} }{}
```

DotHere is a special argument to MarkLines to mark the position of the dot.

      View Source
      

```
var ErrStopped = errors.New("stopped")
```

ErrStopped is returned by Reader when Close is called during a ReadEvent or
ReadRawEvent method.

### Functions ¶

####

      func BuffersHeight ¶
  
    
  

    
    
      

```
func BuffersHeight(bufs ...*Buffer) (l int)
```

BuffersHeight computes the combined height of a number of buffers.

####

      func CellsWidth ¶
  
    
  

    
    
      

```
func CellsWidth(cs []Cell) int
```

CellsWidth returns the total width of a Cell slice.

####

      func CompareCells ¶
  
    
  

    
    
      

```
func CompareCells(r1, r2 []Cell) (bool, int)
```

CompareCells returns whether two Cell slices are equal, and when they are
not, the first index at which they differ.

####

      func IsReadErrorRecoverable ¶
  
    
  

    
    
      

```
func IsReadErrorRecoverable(err error) bool
```

IsReadErrorRecoverable returns whether an error returned by Reader is
recoverable.

####

      func Sanitize ¶
  
    
  

    
    
      

```
func Sanitize(in, out *os.File)
```

Sanitize sanitizes the terminal after an external command has executed.

####

      func Setup ¶
  
    
  

    
    
      

```
func Setup(in, out *os.File) (func() error, error)
```

Setup sets up the terminal so that it is suitable for the Reader and
Writer to use. It returns a function that can be used to restore the
original terminal config.

####

      func SetupGlobal ¶
  
    
  

    
    
      

```
func SetupGlobal() func()
```

SetupGlobal sets up the terminal for the entire Elvish session.

### Types ¶

####

      type Buffer ¶
  
    
  

    
    
      

```
type Buffer struct {
 Width int
 // Lines the content of the buffer.
 Lines Lines
 // Dot is what the user perceives as the cursor.
 Dot Pos
}
```

Buffer reflects a continuous range of lines on the terminal.

The Unix terminal API provides only awkward ways of querying the terminal
Buffer, so we keep an internal reflection and do one-way synchronizations
(Buffer -> terminal, and not the other way around). This requires us to
exactly match the terminal's idea of the width of characters (wcwidth) and
where to insert soft carriage returns, so there could be bugs.

####

      func NewBuffer ¶
  
    
  

    
    
      

```
func NewBuffer(width int) *Buffer
```

NewBuffer builds a new buffer, with one empty line.

####

      func (*Buffer) Buffer ¶
  
    
  

    
    
      

```
func (b *Buffer) Buffer() *Buffer
```

Buffer returns itself.

####

      func (*Buffer) Col ¶
  
    
  

    
    
      

```
func (b *Buffer) Col() int
```

Col returns the column the cursor is in.

####

      func (*Buffer) Cursor ¶
  
    
  

    
    
      

```
func (b *Buffer) Cursor() Pos
```

Cursor returns the current position of the cursor.

####

      func (*Buffer) Extend ¶
  
    
  

    
    
      

```
func (b *Buffer) Extend(b2 *Buffer, moveDot bool)
```

Extend adds all lines from b2 to the bottom of this buffer. If moveDot is
true, the dot is updated to match the dot of b2.

####

      func (*Buffer) ExtendRight ¶
  
    
  

    
    
      

```
func (b *Buffer) ExtendRight(b2 *Buffer)
```

ExtendRight extends bb to the right. It pads each line in b to be b.Width and
appends the corresponding line in b2 to it, making new lines when b2 has more
lines than bb.

####

      func (*Buffer) TTYString ¶
  
    
  

    
    
      

```
func (b *Buffer) TTYString() string
```

TTYString returns a string for representing the buffer on the terminal.

####

      func (*Buffer) TrimToLines ¶
  
    
  

    
    
      

```
func (b *Buffer) TrimToLines(low, high int)
```

TrimToLines trims a buffer to the lines [low, high).
