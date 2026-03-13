### Index ¶

- 
        func Debug(v ...interface{})

- 
        func Debugf(format string, v ...interface{})

- 
        func Error(v ...interface{})

- 
        func Errorf(format string, v ...interface{})

- 
        func Fatal(v ...interface{})

- 
        func Fatalf(format string, v ...interface{})

- 
        func Info(v ...interface{})

- 
        func Infof(format string, v ...interface{})

- 
        func NewDefaultLogger(out io.Writer, prefix string, flag int, lv Level) *defaultLogger

- 
        func Panic(v ...interface{})

- 
        func Panicf(format string, v ...interface{})

- 
        func SetDummyLogger()

- 
        func SetLogger(logger Logger)

- 
        func Warn(v ...interface{})

- 
        func Warnf(format string, v ...interface{})

- 
          type Level

- 
          type Logger

- 

  - 
            func GetLogger() Logger

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Debug ¶
  
    
  

    
    
      

```
func Debug(v ...interface{})
```