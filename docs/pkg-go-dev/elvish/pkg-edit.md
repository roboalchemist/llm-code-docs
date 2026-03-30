### Overview ¶

Package edit implements the line editor for Elvish.

The line editor is based on the cli package, which implements a general,
Elvish-agnostic line editor, and multiple "addon" packages. This package
glues them together and provides Elvish bindings for them.

### Index ¶

- Variables

-
          type BindingMap

-

-
            func MakeBindingMap(raw hashmap.Map) (BindingMap, error)

-

-
            func (bt BindingMap) Assoc(k, v interface{}) (interface{}, error)

-
            func (bt BindingMap) Dissoc(k interface{}) interface{}

-
            func (bt BindingMap) GetKey(k ui.Key) eval.Callable

-
            func (bt BindingMap) HasKey(k interface{}) bool

-
            func (bt BindingMap) Index(index interface{}) (interface{}, error)

-
            func (bt BindingMap) Repr(indent int) string

-
          type Editor

-

-
            func NewEditor(tty cli.TTY, ev *eval.Evaler, st store.Store) *Editor

-

-
            func (ed *Editor) Ns() *eval.Ns

-
            func (ed *Editor) ReadCode() (string, error)

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var EmptyBindingMap = BindingMap{vals.EmptyMap}
```

### Functions ¶

This section is empty.

### Types ¶

####

      type BindingMap ¶
  
    
  

    
    
      

```
type BindingMap struct {
 hashmap.Map
}
```

BindingMap is a special Map that converts its key to ui.Key and ensures
that its values satisfy eval.CallableValue.

####

      func MakeBindingMap ¶
  
    
  

    
    
      

```
func MakeBindingMap(raw hashmap.Map) (BindingMap, error)
```
