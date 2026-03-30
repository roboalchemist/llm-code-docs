### Index ¶

- 
          type MultiError

- 

  - 
            func NewMultiError(errors []error) *MultiError

- 

  - 
            func (e *MultiError) Append(err error)

  - 
            func (e *MultiError) Error() string

  - 
            func (e *MultiError) ErrorOrNil() error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type MultiError ¶
  
    
  

    
    
      

```
type MultiError struct {
	Errors []error
	// contains filtered or unexported fields
}
```

    
  

MultiError holds multiple errors

    
  
  
    
#### 
      func NewMultiError ¶
  
    
  

    
    
      

```
func NewMultiError(errors []error) *MultiError
```

    
  

NewMultiError creates and returns an Error with error splice

  

  
    
  
  
    
#### 
      func (*MultiError) Append ¶
  
    
      added in
      v1.4.1
    
  

    
    
      

```
func (e *MultiError) Append(err error)
```