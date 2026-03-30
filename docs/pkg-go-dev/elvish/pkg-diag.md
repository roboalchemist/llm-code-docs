### Overview ¶

Package diag contains building blocks for formatting and processing
diagnostic information.

### Index ¶

-
        func Complain(w io.Writer, msg string)

-
        func Complainf(w io.Writer, format string, args ...interface{})

-
        func Errors(errs ...error) error

-
        func ShowError(w io.Writer, err error)

-
          type Context

-

-
            func NewContext(name, source string, r Ranger) *Context

-

-
            func (c *Context) Show(sourceIndent string) string

-
            func (c *Context) ShowCompact(sourceIndent string) string

-
          type Error

-

-
            func (e *Error) Error() string

-
            func (e *Error) Range() Ranging

-
            func (e *Error) Show(indent string) string

-
          type MultiError

-

-
            func (es MultiError) Error() string

-
          type Ranger

-
          type Ranging

-

-
            func MixedRanging(a, b Ranger) Ranging

-
            func PointRanging(p int) Ranging

-

-
            func (r Ranging) Range() Ranging

-
          type Shower

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Complain ¶
  
    
  

    
    
      

```
func Complain(w io.Writer, msg string)
```

Complain prints a message to w in bold and red, adding a trailing newline.

####

      func Complainf ¶
  
    
  

    
    
      

```
func Complainf(w io.Writer, format string, args ...interface{})
```

Complainf is like Complain, but accepts a format string and arguments.

####

      func Errors ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func Errors(errs ...error) error
```

Errors concatenate multiple errors into one. If all errors are nil, it
returns nil. If there is one non-nil error, it is returned. Otherwise the
return value is a MultiError containing all the non-nil arguments. Arguments
of the type MultiError are flattened.

####

      func ShowError ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func ShowError(w io.Writer, err error)
```

ShowError shows an error. It uses the Show method if the error
implements Shower, and uses Complain to print the error message otherwise.

### Types ¶

####

      type Context ¶
  
    
  

    
    
      

```
type Context struct {
 Name   string
 Source string
 Ranging
 // contains filtered or unexported fields
}
```

Context is a range of text in a source code. It is typically used for
errors that can be associated with a part of the source code, like parse
errors and a traceback entry.

####

      func NewContext ¶
  
    
  

    
    
      

```
func NewContext(name, source string, r Ranger) *Context
```

NewContext creates a new Context.

####

      func (*Context) Show ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func (c *Context) Show(sourceIndent string) string
```

Show shows a SourceContext.

####

      func (*Context) ShowCompact ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func (c *Context) ShowCompact(sourceIndent string) string
```

ShowCompact shows a SourceContext, with no line break between the
source position range description and relevant source excerpt.
