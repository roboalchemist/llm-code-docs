### Overview ¶

Package cli implements a generic interactive line editor.

### Index ¶

- Constants

- Variables

-
        func CategorizeSmallWord(r rune) int

-
        func IsAlnum(r rune) bool

-
        func Left(s ListBoxState) int

-
        func ModeLine(content string, space bool) ui.Text

-
        func ModePrompt(content string, space bool) func() ui.Text

-
        func Next(s ListBoxState) int

-
        func NextPage(s ListBoxState) int

-
        func NextWrap(s ListBoxState) int

-
        func Prev(s ListBoxState) int

-
        func PrevPage(s ListBoxState) int

-
        func PrevWrap(s ListBoxState) int

-
        func Right(s ListBoxState) int

-
        func SetAddon(a App, addon Widget)

-
        func SetCodeBuffer(a App, buf CodeBuffer)

-
        func TestHandle(t *testing.T, tests []HandleTest)

-
        func TestRender(t *testing.T, tests []RenderTest)

-
        func WriteListing(b *term.BufferBuilder, name, filter string, lines ...string)

-
          type App

-

-
            func NewApp(spec AppSpec) App

-
          type AppSpec

-
          type CodeArea

-

-
            func NewCodeArea(spec CodeAreaSpec) CodeArea

-
          type CodeAreaSpec

-
          type CodeAreaState

-

-
            func (s *CodeAreaState) ApplyPending()

-
          type CodeBuffer

-

-
            func GetCodeBuffer(a App) CodeBuffer

-

-
            func (c *CodeBuffer) InsertAtDot(text string)

-
          type ColView

-

-
            func NewColView(spec ColViewSpec) ColView

-
          type ColViewSpec

-
          type ColViewState

-
          type ComboBox

-

-
            func NewComboBox(spec ComboBoxSpec) ComboBox

-
          type ComboBoxSpec

-
          type DummyHandler

-

-
            func (DummyHandler) Handle(term.Event) bool

-
          type Empty

-

-
            func (Empty) Handle(event term.Event) bool

-
            func (Empty) Render(width, height int) *term.Buffer

-
          type Focuser

-
          type FuncHandler

-

-
            func (f FuncHandler) Handle(event term.Event) bool

-
          type HScrollbar

-

-
            func (h HScrollbar) Render(width, height int) *term.Buffer

-
          type HandleTest

-
          type Handler

-
          type Highlighter

-
          type Items

-
          type Label

-

-
            func (l Label) Handle(event term.Event) bool

-
            func (l Label) Render(width, height int) *term.Buffer

-
          type ListBox

-

-
            func NewListBox(spec ListBoxSpec) ListBox

-
          type ListBoxSpec

-
          type ListBoxState

-
          type MapHandler

-

-
            func (m MapHandler) Handle(event term.Event) bool

-
          type PendingCode

-
          type Prompt

-

-
            func NewConstPrompt(t ui.Text) Prompt

-
          type RenderTest

-
          type Renderer

-
          type State

-
          type TTY

-

-
            func NewTTY(in, out *os.File) TTY

-
          type TestItems

-

-
            func (it TestItems) Len() int

-
            func (it TestItems) Show(i int) ui.Text

-
          type TextView

-

-
            func NewTextView(spec TextViewSpec) TextView

-
          type TextViewSpec

-
          type TextViewState

-
          type VScrollbar

-

-
            func (v VScrollbar) Render(width, height int) *term.Buffer

-
          type VScrollbarContainer

-

-
            func (v VScrollbarContainer) Render(width, height int) *term.Buffer

-
          type Widget

-

-
            func Addon(a App) Widget

### Examples ¶

- Package (Loop)

### Constants ¶

      View Source
      

```
const Selected = "<- selected"
```

Selected is a special value in the argument to WriteListing, signalling that
the argument before it is the selected line.

### Variables ¶

      View Source
      

```
var StdTTY = NewTTY(os.Stdin, os.Stderr)
```

StdTTY is the terminal connected to inputs from stdin and output to stderr.

### Functions ¶

####

      func CategorizeSmallWord ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func CategorizeSmallWord(r rune) int
```

CategorizeSmallWord determines if the rune is whitespace, alphanum, or
something else.

####

      func IsAlnum ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func IsAlnum(r rune) bool
```

IsAlnum determines if the rune is an alphanumeric character.

####

      func Left ¶
  
    
  

    
    
      

```
func Left(s ListBoxState) int
```

Left moves the selection to the item to the left. It is only meaningful in
horizontal layout and suitable as an argument to Widget.Select.

####

      func ModeLine ¶
  
    
  

    
    
      

```
func ModeLine(content string, space bool) ui.Text
```

ModeLine returns a text styled as a modeline.

####

      func ModePrompt ¶
  
    
  

    
    
      

```
func ModePrompt(content string, space bool) func() ui.Text
```

ModePrompt returns a callback suitable as the prompt in the codearea of a

####

      func Next ¶
  
    
  

    
    
      

```
func Next(s ListBoxState) int
```

Next moves the selection to the previous item, or does nothing if the
last item is currently selected. It is a suitable as an argument to
Widget.Select.

####

      func NextPage ¶
  
    
  

    
    
      

```
func NextPage(s ListBoxState) int
```

NextPage moves the selection to the item one page after. It is only
meaningful in vertical layout and suitable as an argument to Widget.Select.

TODO(xiaq): This does not correctly with multi-line items.

####

      func NextWrap ¶
  
    
  

    
    
      

```
func NextWrap(s ListBoxState) int
```

NextWrap moves the selection to the previous item, or to the first item
if the last item is currently selected. It is a suitable as an argument to
Widget.Select.

####

      func Prev ¶
  
    
  

    
    
      

```
func Prev(s ListBoxState) int
```

Prev moves the selection to the previous item, or does nothing if the
first item is currently selected. It is a suitable as an argument to
Widget.Select.

####

      func PrevPage ¶
  
    
  

    
    
      

```
func PrevPage(s ListBoxState) int
```

PrevPage moves the selection to the item one page before. It is only
meaningful in vertical layout and suitable as an argument to Widget.Select.

TODO(xiaq): This does not correctly with multi-line items.

####

      func PrevWrap ¶
  
    
  

    
    
      

```
func PrevWrap(s ListBoxState) int
```

PrevWrap moves the selection to the previous item, or to the last item if
the first item is currently selected. It is a suitable as an argument to
Widget.Select.

####

      func Right ¶
  
    
  

    
    
      

```
func Right(s ListBoxState) int
```

Right moves the selection to the item to the right. It is only meaningful in
horizontal layout and suitable as an argument to Widget.Select.

####

      func SetAddon ¶
  
    
  

    
    
      

```
func SetAddon(a App, addon Widget)
```

SetAddon sets the addon widget of the app.

####

      func SetCodeBuffer ¶
  
    
  

    
    
      

```
func SetCodeBuffer(a App, buf CodeBuffer)
```

SetCodeBuffer sets the code buffer of the main code area widget of the app.

####

      func TestHandle ¶
  
    
  

    
    
      

```
func TestHandle(t *testing.T, tests []HandleTest)
```

TestHandle runs the given Handler tests.

####

      func TestRender ¶
  
    
  

    
    
      

```
func TestRender(t *testing.T, tests []RenderTest)
```

TestRender runs the given Renderer tests.

####

      func WriteListing ¶
  
    
  

    
    
      

```
func WriteListing(b *term.BufferBuilder, name, filter string, lines ...string)
```

WriteListing is a unit test helper that emulates the rendering of a "listing"
type addon. Among the lines arguments, the value "<- selected" is special and
signals that the argument before it is the selected line.

### Types ¶

####

      type App ¶
  
    
  

    
    
      

```
type App interface {
 // MutateState mutates the state of the app.
 MutateState(f func(*State))
 // CopyState returns a copy of the a state.
 CopyState() State
 // CodeArea returns the codearea widget of the app.
 CodeArea() CodeArea
 // ReadCode requests the App to read code from the terminal by running an
 // event loop. This function is not re-entrant.
 ReadCode() (string, error)
 // Redraw requests a redraw. It never blocks and can be called regardless of
 // whether the App is active or not.
 Redraw()
 // RedrawFull requests a full redraw. It never blocks and can be called
 // regardless of whether the App is active or not.
 RedrawFull()
 // CommitEOF causes the main loop to exit with EOF. If this method is called
 // when an event is being handled, the main loop will exit after the handler
 // returns.
 CommitEOF()
 // CommitCode causes the main loop to exit with the current code content. If
 // this method is called when an event is being handled, the main loop will
 // exit after the handler returns.
 CommitCode()
 // Notify adds a note and requests a redraw.
 Notify(note string)
}
```

App represents a CLI app.

####

      func NewApp ¶
  
    
  

    
    
      

```
func NewApp(spec AppSpec) App
```

NewApp creates a new App from the given specification.
