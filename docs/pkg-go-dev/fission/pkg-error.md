### Index ¶

- Constants

- 
        func GetHTTPError(err error) (int, string)

- 
        func IsNotFound(err error) bool

- 
        func MakeErrorFromHTTP(resp *http.Response) error

- 
          type Error

- 

  - 
            func MakeError(code int, msg string) Error

- 

  - 
            func (err Error) Description() string

  - 
            func (err Error) Error() string

  - 
            func (err Error) HTTPStatus() int

### Constants ¶

  
    
      View Source
      

```
const (
	ErrorInternal = iota

	ErrorNotAuthorized
	ErrorNotFound
	ErrorNameExists
	ErrorInvalidArgument
	ErrorNoSpace
	ErrorNotImplemented
	ErrorChecksumFail
	ErrorSizeLimitExceeded
	ErrorRequestTimeout
	ErrorTooManyRequests
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GetHTTPError ¶
  
    
  

    
    
      

```
func GetHTTPError(err error) (int, string)
```