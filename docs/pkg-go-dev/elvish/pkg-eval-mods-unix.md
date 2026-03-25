### Overview ¶

Package unix exports an Elvish namespace that contains variables and
functions that deal with features unique to UNIX-like operating systems. On
non-UNIX operating systems it exports an empty namespace.

### Index ¶

- Constants

- Variables

-
          type UmaskVariable

-

-
            func (UmaskVariable) Get() interface{}

-
            func (UmaskVariable) Set(v interface{}) error

### Constants ¶

      View Source
      

```
const ExposeUnixNs = true
```

ExposeUnixNs indicate whether this module should be exposed as a usable
elvish namespace.

### Variables ¶

      View Source
      

```
var Ns = eval.NsBuilder{
 "umask": UmaskVariable{},
}.Ns()
```

Ns is an Elvish namespace that contains variables and functions that deal
with features unique to UNIX-like operating systems. On

### Functions ¶

This section is empty.

### Types ¶

####

      type UmaskVariable ¶
  
    
  

    
    
      

```
type UmaskVariable struct{}
```

UmaskVariable is a variable whose value always reflects the current file
creation permission mask. Setting it changes the current file creation
permission mask for the process (not an individual thread).

####

      func (UmaskVariable) Get ¶
  
    
  

    
    
      

```
func (UmaskVariable) Get() interface{}
```

Get returns the current file creation umask as a string.

####

      func (UmaskVariable) Set ¶
  
    
  

    
    
      

```
func (UmaskVariable) Set(v interface{}) error
```

Set changes the current file creation umask. It can be called with a string
(the usual case) or a float64.
