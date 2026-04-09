### Overview ¶

Package fsutil provides filesystem utilities.

### Index ¶

- Variables

-
        func ClaimFile(dir, pattern string) (*os.File, error)

-
        func DontSearch(exe string) bool

-
        func EachExternal(f func(string))

-
        func GetHome(uname string) (string, error)

-
        func Getwd() string

-
        func IsExecutable(path string) bool

-
        func TildeAbbr(path string) string

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var CurrentUser func() (*user.User, error) = user.Current
```

CurrentUser allows for unit test error injection.

      View Source
      

```
var ErrClaimFileBadPattern = errors.New("ClaimFile: pattern must contain exactly one asterisk")
```

ErrClaimFileBadPattern is thrown when the pattern argument passed to
ClaimFile does not contain exactly one asterisk.

### Functions ¶

####

      func ClaimFile ¶
  
    
  

    
    
      

```
func ClaimFile(dir, pattern string) (*os.File, error)
```

ClaimFile takes a directory and a pattern string containing exactly one
asterisk (e.g. "a*.log"). It opens a file in that directory, with a filename
matching the template, with "*" replaced by a number. That number is one plus
the largest of all existing files matching the template. If no such file
exists, "*" is replaced by 1. The file is opened for read and write, with
permission 0666 (before umask).

For example, if the directory /tmp/elvish contains a1.log, a2.log and a9.log,
calling ClaimFile("/tmp/elvish", "a*.log") will open a10.log. If the
directory has no files matching the pattern, this same call will open a1.log.

This function is useful for automatically determining unique names for log
files. Unique filenames can also be derived by embedding the PID, but using
this function preserves the chronical order of the files.

This function is concurrency-safe: it always opens a new, unclaimed file and
is not subject to race condition.

####

      func DontSearch ¶
  
    
  

    
    
      

```
func DontSearch(exe string) bool
```

DontSearch determines whether the path to an external command should be
taken literally and not searched.

####

      func EachExternal ¶
  
    
  

    
    
      

```
func EachExternal(f func(string))
```

EachExternal calls f for each name that can resolve to an external command.

BUG: EachExternal may generate the same command multiple command it it
appears in multiple directories in PATH.

BUG: EachExternal doesn't work on Windows since it relies on the execution
permission bit, which doesn't exist on Windows.

####

      func GetHome ¶
  
    
  

    
    
      

```
func GetHome(uname string) (string, error)
```

GetHome finds the home directory of a specified user. When given an empty
string, it finds the home directory of the current user.

####

      func Getwd ¶
  
    
  

    
    
      

```
func Getwd() string
```

Getwd returns path of the working directory in a format suitable as the
prompt.

####

      func IsExecutable ¶
  
    
  

    
    
      

```
func IsExecutable(path string) bool
```

IsExecutable determines whether path refers to an executable file.

####

      func TildeAbbr ¶
  
    
  

    
    
      

```
func TildeAbbr(path string) string
```

TildeAbbr abbreviates the user's home directory to ~.

### Types ¶

This section is empty.
