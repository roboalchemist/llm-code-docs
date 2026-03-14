### Overview ¶

Package getopt implements a command-line argument parser.

It tries to cover all common styles of option syntaxes, and provides context
information when given a partial input. It is mainly useful for writing
completion engines and wrapper programs.

If you are looking for an option parser for your go program, consider using
the flag package in the standard library instead.

### Index ¶

-
          type Config

-

-
            func (conf Config) HasAll(flags Config) bool

-
            func (i Config) String() string

-
          type Context

-
          type ContextType

-

-
            func (i ContextType) String() string

-
          type Getopt

-

-
            func (g *Getopt) Parse(elems []string) ([]*ParsedOption, []string, *Context)

-
          type HasArg

-

-
            func (i HasArg) String() string

-
          type Option

-
          type ParsedOption

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

This section is empty.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config uint
```

Config configurates the parsing behavior.

```
const (
 // DoubleDashTerminatesOptions indicates that all elements after an argument
 // "--" are treated as arguments.
 DoubleDashTerminatesOptions Config = 1 << iota
 // FirstArgTerminatesOptions indicates that all elements after the first
 // argument are treated as arguments.
 FirstArgTerminatesOptions
 // LongOnly indicates that long options may be started by either one or two
 // dashes, and short options are not allowed. Should replicate the behavior
 // of getopt_long_only and the
 // flag package of the Go standard library.
 LongOnly
 // GNUGetoptLong is a configuration that should replicate the behavior of
 // GNU getopt_long.
 GNUGetoptLong = DoubleDashTerminatesOptions
 // POSIXGetopt is a configuration that should replicate the behavior of
 // POSIX getopt.
 POSIXGetopt = DoubleDashTerminatesOptions | FirstArgTerminatesOptions
)
```
