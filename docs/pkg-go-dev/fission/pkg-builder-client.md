### Index ¶

- 
          type ClientInterface

- 

  - 
            func MakeClient(logger *zap.Logger, builderUrl string) ClientInterface

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
	Build(context.Context, *builder.PackageBuildRequest) (*builder.PackageBuildResponse, error)
	Clean(context.Context, string) error
}
```

    
  

    
  
  
    
#### 
      func MakeClient ¶
  
    
  

    
    
      

```
func MakeClient(logger *zap.Logger, builderUrl string) ClientInterface
```