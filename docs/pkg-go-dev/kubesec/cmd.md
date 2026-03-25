### Index ¶

- 
        func Execute()

- 
        func NewLogger(logLevel string, zapEncoding string) (*zap.SugaredLogger, error)

- 
          type File

- 
          type ScanFailedValidationError

- 

  - 
            func (e *ScanFailedValidationError) Error() string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Execute ¶
  
    
  

    
    
      

```
func Execute()
```

    
  

Execute runs kubesec

  

        
	  
  
  
    
#### 
      func NewLogger ¶
  
    
  

    
    
      

```
func NewLogger(logLevel string, zapEncoding string) (*zap.SugaredLogger, error)
```

    
  

NewLogger creates a logger

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type File ¶
  
    
  

    
    
      

```
type File struct {
	// contains filtered or unexported fields
}
```

    
  

File holds the name and contents

  

    
      
  
  
    
#### 
      type ScanFailedValidationError ¶
  
    
  

    
    
      

```
type ScanFailedValidationError struct {
}
```

    
  

    
  
  
    
#### 
      func (*ScanFailedValidationError) Error ¶
  
    
  

    
    
      

```
func (e *ScanFailedValidationError) Error() string
```