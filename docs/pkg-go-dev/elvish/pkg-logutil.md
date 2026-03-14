### Overview ¶

Package logutil provides logging utilities.

### Index ¶

-
        func GetLogger(prefix string) *log.Logger

-
        func SetOutput(newout io.Writer)

-
        func SetOutputFile(fname string) error

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func GetLogger ¶
  
    
  

    
    
      

```
func GetLogger(prefix string) *log.Logger
```

GetLogger gets a logger with a prefix.

####

      func SetOutput ¶
  
    
  

    
    
      

```
func SetOutput(newout io.Writer)
```

SetOutput redirects the output of all loggers obtained with GetLogger to the
new io.Writer. If the old output was a file opened by SetOutputFile, it is
closed.

####

      func SetOutputFile ¶
  
    
  

    
    
      

```
func SetOutputFile(fname string) error
```

SetOutputFile redirects the output of all loggers obtained with GetLogger to
the named file. If the old output was a file opened by SetOutputFile, it is
closed. The new file is truncated. SetOutFile("") is equivalent to
SetOutput(ioutil.Discard).

### Types ¶

This section is empty.
