### Index ¶

- 
          type ClientInterface

- 

  - 
            func MakeClient(logger *zap.Logger, fetcherUrl string) ClientInterface

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ClientInterface ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
type ClientInterface interface {
	Specialize(context.Context, *fetcher.FunctionSpecializeRequest) error
	Fetch(context.Context, *fetcher.FunctionFetchRequest) error
	Upload(context.Context, *fetcher.ArchiveUploadRequest) (*fetcher.ArchiveUploadResponse, error)
}
```

    
  

    
  
  
    
#### 
      func MakeClient ¶
  
    
  

    
    
      

```
func MakeClient(logger *zap.Logger, fetcherUrl string) ClientInterface
```