### Overview ¶

Package highlight provides an Elvish syntax highlighter.

### Index ¶

- Variables

-
          type Config

-
          type Highlighter

-

-
            func NewHighlighter(cfg Config) *Highlighter

-

-
            func (hl *Highlighter) Get(code string) (ui.Text, []error)

-
            func (hl *Highlighter) LateUpdates() <-chan struct{}

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var MaxBlockForLate = 10 * time.Millisecond
```

MaxBlockForLate specifies the maximum wait time to block for late results.
It can be changed for test cases.

### Functions ¶

This section is empty.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 Check      func(n parse.Tree) error
 HasCommand func(name string) bool
}
```

Config keeps configuration for highlighting code.

####

      type Highlighter ¶
  
    
  

    
    
      

```
type Highlighter struct {
 // contains filtered or unexported fields
}
```

Highlighter is a code highlighter that can deliver results asynchronously.

####

      func NewHighlighter ¶
  
    
  

    
    
      

```
func NewHighlighter(cfg Config) *Highlighter
```
