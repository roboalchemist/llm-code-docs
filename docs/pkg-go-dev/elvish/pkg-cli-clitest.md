### Overview ¶

Package clitest provides utilities for testing cli.App.

### Index ¶

- Constants

- Variables

-
        func StartReadCode(readCode func() (string, error)) (<-chan string, <-chan error)

-
        func WithSpec(f func(*cli.AppSpec)) func(*cli.AppSpec, TTYCtrl)

-
        func WithTTY(f func(TTYCtrl)) func(*cli.AppSpec, TTYCtrl)

-
          type Fixture

-

-
            func Setup(fns ...func(*cli.AppSpec, TTYCtrl)) *Fixture

-

-
            func (f *Fixture) MakeBuffer(args ...interface{}) *term.Buffer

-
            func (f *Fixture) Stop()

-
            func (f *Fixture) TestTTY(t *testing.T, args ...interface{})

-
            func (f *Fixture) TestTTYNotes(t *testing.T, args ...interface{})

-
            func (f *Fixture) Wait() (string, error)

-
          type TTYCtrl

-

-
            func GetTTYCtrl(t cli.TTY) (TTYCtrl, bool)

-
            func NewFakeTTY() (cli.TTY, TTYCtrl)

-

-
            func (t TTYCtrl) Buffer() *term.Buffer

-
            func (t TTYCtrl) BufferHistory() []*term.Buffer

-
            func (t TTYCtrl) EventCh() chan term.Event

-
            func (t TTYCtrl) Inject(events ...term.Event)

-
            func (t TTYCtrl) InjectSignal(sigs ...os.Signal)

-
            func (t TTYCtrl) LastBuffer() *term.Buffer

-
            func (t TTYCtrl) LastNotesBuffer() *term.Buffer

-
            func (t TTYCtrl) NotesBufferHistory() []*term.Buffer

-
            func (t TTYCtrl) NotifySignals() <-chan os.Signal

-
            func (t TTYCtrl) RawInput() int

-
            func (t TTYCtrl) ReadEvent() (term.Event, error)

-
            func (t TTYCtrl) ResetBuffer()

-
            func (t TTYCtrl) SetRawInput(n int)

-
            func (t TTYCtrl) SetSetup(restore func(), err error)

-
            func (t TTYCtrl) SetSize(h, w int)

-
            func (t TTYCtrl) Setup() (func(), error)

-
            func (t TTYCtrl) Size() (h, w int)

-
            func (t TTYCtrl) StopInput()

-
            func (t TTYCtrl) StopSignals()

-
            func (t TTYCtrl) TestBuffer(tt *testing.T, b *term.Buffer)

-
            func (t TTYCtrl) TestNotesBuffer(tt *testing.T, b *term.Buffer)

-
            func (t TTYCtrl) UpdateBuffer(bufNotes, buf *term.Buffer, _ bool) error

### Constants ¶

      View Source
      

```
const (
 FakeTTYHeight = 20
 FakeTTYWidth  = 50
)
```

Initial size of fake TTY.

### Variables ¶

      View Source
      

```
var Styles = ui.RuneStylesheet{
 '_': ui.Underlined,
 'b': ui.Bold,
 '*': ui.Stylings(ui.Bold, ui.FgWhite, ui.BgMagenta),
 '+': ui.Inverse,
 '/': ui.FgBlue,
 '#': ui.Stylings(ui.Inverse, ui.FgBlue),
 '!': ui.FgRed,
 '?': ui.Stylings(ui.FgBrightWhite, ui.BgRed),
 '-': ui.FgMagenta,
 'X': ui.Stylings(ui.Inverse, ui.FgMagenta),
 'v': ui.FgGreen,
 'V': ui.Stylings(ui.Underlined, ui.FgGreen),
 '$': ui.FgMagenta,
}
```

Styles defines a common stylesheet for unit tests.

### Functions ¶

####

      func StartReadCode ¶
  
    
  

    
    
      

```
func StartReadCode(readCode func() (string, error)) (<-chan string, <-chan error)
```

StartReadCode starts the readCode function asynchronously, and returns two
channels that deliver its return values. The two channels are closed after
return values are delivered, so that subsequent reads will return zero values
and not block.

####

      func WithSpec ¶
  
    
  

    
    
      

```
func WithSpec(f func(*cli.AppSpec)) func(*cli.AppSpec, TTYCtrl)
```

WithSpec takes a function that operates on *cli.AppSpec, and wraps it into a
form suitable for passing to Setup.

####

      func WithTTY ¶
  
    
  

    
    
      

```
func WithTTY(f func(TTYCtrl)) func(*cli.AppSpec, TTYCtrl)
```

WithTTY takes a function that operates on TTYCtrl, and wraps it to a form
suitable for passing to Setup.

### Types ¶

####

      type Fixture ¶
  
    
  

    
    
      

```
type Fixture struct {
 App cli.App
 TTY TTYCtrl
 // contains filtered or unexported fields
}
```

Fixture is a test fixture.

####

      func Setup ¶
  
    
  

    
    
      

```
func Setup(fns ...func(*cli.AppSpec, TTYCtrl)) *Fixture
```

Setup sets up a test fixture. It contains an App whose ReadCode method has
been started asynchronously.

####

      func (*Fixture) MakeBuffer ¶
  
    
  

    
    
      

```
func (f *Fixture) MakeBuffer(args ...interface{}) *term.Buffer
```

MakeBuffer is a helper for building a buffer. It is equivalent to
term.NewBufferBuilder(width of terminal).MarkLines(args...).Buffer().

####

      func (*Fixture) Stop ¶
  
    
  

    
    
      

```
func (f *Fixture) Stop()
```

Stop stops ReadCode and waits for it to finish. If ReadCode has already been
stopped, it is a no-op.

####

      func (*Fixture) TestTTY ¶
  
    
  

    
    
      

```
func (f *Fixture) TestTTY(t *testing.T, args ...interface{})
```

TestTTY is equivalent to f.TTY.TestBuffer(f.MakeBuffer(args...)).

####

      func (*Fixture) TestTTYNotes ¶
  
    
  

    
    
      

```
func (f *Fixture) TestTTYNotes(t *testing.T, args ...interface{})
```

TestTTYNotes is equivalent to f.TTY.TestNotesBuffer(f.MakeBuffer(args...)).

####

      func (*Fixture) Wait ¶
  
    
  

    
    
      

```
func (f *Fixture) Wait() (string, error)
```

Wait waits for ReaCode to finish, and returns its return values.
