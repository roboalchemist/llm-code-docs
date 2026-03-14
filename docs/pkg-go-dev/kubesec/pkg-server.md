### Index ¶

- 
        func ListenAndServe(addr string, timeout time.Duration, logger *zap.SugaredLogger, ...)

- 
        func SetupSignalHandler() (stopCh <-chan struct{})

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ListenAndServe ¶
  
    
  

    
    
      

```
func ListenAndServe(
	addr string,
	timeout time.Duration,
	logger *zap.SugaredLogger,
	stopCh <-chan struct{},
	keypath string,
	schemaConfig ruler.SchemaConfig,
)
```

    
  

ListenAndServe starts a web server and waits for SIGTERM

  

        
	  
  
  
    
#### 
      func SetupSignalHandler ¶
  
    
  

    
    
      

```
func SetupSignalHandler() (stopCh <-chan struct{})
```