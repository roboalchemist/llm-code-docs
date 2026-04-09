### Overview ¶

Package prog provides the entry point to Elvish. Its subpackages correspond
to subprograms of Elvish.

### Index ¶

- Variables

-
        func BadUsage(msg string) error

-
        func Exit(exit int) error

-
        func Run(fds [3]*os.File, args []string, programs ...Program) int

-
        func SetDeprecationLevel(level int) func()

-
          type Flags

-
          type Program

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var DeprecationLevel = 15
```

DeprecationLevel is a global flag that controls which deprecations to show.
If its value is X, Elvish shows deprecations that should be shown for version
0.X.

### Functions ¶

####

      func BadUsage ¶
  
    
  

    
    
      

```
func BadUsage(msg string) error
```

BadUsage returns an error that may be returned by Program.Main, which
requests the main program to print out a message, the usage information and
exit with 2.

####

      func Exit ¶
  
    
  

    
    
      

```
func Exit(exit int) error
```

Exit returns an error that may be returned by Program.Main, which requests the
main program to exit with the given code. If the exit code is 0, it returns nil.

####

      func Run ¶
  
    
  

    
    
      

```
func Run(fds [3]*os.File, args []string, programs ...Program) int
```

Run parses command-line flags and runs the first applicable subprogram. It
returns the exit status of the program.

####

      func SetDeprecationLevel ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func SetDeprecationLevel(level int) func()
```

SetDeprecationLevel sets ShowDeprecations to the given value, and returns a
function to restore the old value.

### Types ¶

####

      type Flags ¶
  
    
  

    
    
      

```
type Flags struct {
 Log, CPUProfile string

 Help, Version, BuildInfo, JSON bool

 CodeInArg, CompileOnly, NoRc bool

 Web  bool
 Port int

 Daemon bool
 Forked int

 Bin, DB, Sock string
}
```

Flags keeps command-line flags.

####

      type Program ¶
  
    
  

    
    
      

```
type Program interface {
 // ShouldRun returns whether the subprogram should run.
 ShouldRun(f *Flags) bool
 // Run runs the subprogram.
 Run(fds [3]*os.File, f *Flags, args []string) error
}
```

Program represents a subprogram.
