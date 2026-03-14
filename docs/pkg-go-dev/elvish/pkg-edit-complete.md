### Overview ¶

Package complete implements the code completion algorithm for Elvish.

### Index ¶

-
          type ArgGenerator

-
          type CodeBuffer

-
          type ComplexItem

-

-
            func (c ComplexItem) Cook(q parse.PrimaryType) completion.Item

-
            func (c ComplexItem) String() string

-
          type Config

-
          type Filterer

-
          type PlainItem

-

-
            func (p PlainItem) Cook(q parse.PrimaryType) completion.Item

-
            func (p PlainItem) String() string

-
          type PureEvaler

-
          type RawItem

-

-
            func FilterPrefix(ctxName, seed string, items []RawItem) []RawItem

-
            func GenerateFileNames(args []string) ([]RawItem, error)

-
            func GenerateForSudo(cfg Config, args []string) ([]RawItem, error)

-
          type Result

-

-
            func Complete(code CodeBuffer, cfg Config) (*Result, error)

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

This section is empty.

### Types ¶

####

      type ArgGenerator ¶
  
    
  

    
    
      

```
type ArgGenerator func(args []string) ([]RawItem, error)
```

ArgGenerator is the type of functions that generate raw candidates for a
command argument. It takes all the existing arguments, the last being the
argument to complete, and returns raw candidates or an error.

####

      type CodeBuffer ¶
  
    
  

    
    
      

```
type CodeBuffer struct {
 Content string
 Dot     int
}
```

CodeBuffer is the same the type in github.com/elves/elvish/pkg/el/codearea,
replicated here to avoid an unnecessary dependency.

####

      type ComplexItem ¶
  
    
  

    
    
      

```
type ComplexItem struct {
 Stem         string   // Used in the code and the menu.
 CodeSuffix   string   // Appended to the code.
 Display      string   // How the item is displayed. If empty, defaults to Stem.
 DisplayStyle ui.Style // Use for displaying.
}
```

ComplexItem is an implementation of RawItem that offers customization options.

####

      func (ComplexItem) Cook ¶
  
    
  

    
    
      

```
func (c ComplexItem) Cook(q parse.PrimaryType) completion.Item
```
