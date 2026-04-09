### Index ¶

- 
          type Error

- 

  - 
            func Adapter(err error) *Error

- 

  - 
            func (e Error) Error() string

  - 
            func (e Error) IsConnRefusedError() bool

  - 
            func (e Error) IsDialError() bool

  - 
            func (e Error) IsTimeoutError() bool

  - 
            func (e Error) IsUnsupportedProtoScheme() bool

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Error ¶
  
    
  

    
    
      

```
type Error struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func Adapter ¶
  
    
  

    
    
      

```
func Adapter(err error) *Error
```

    
  

Adapter returns an Error if the pass-in error is a network error;
otherwise, nil will be returned.

  

  
    
  
  
    
#### 
      func (Error) Error ¶
  
    
  

    
    
      

```
func (e Error) Error() string
```