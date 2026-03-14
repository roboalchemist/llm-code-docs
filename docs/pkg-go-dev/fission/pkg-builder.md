### Index ¶

- 
          type Builder

- 

  - 
            func MakeBuilder(logger *zap.Logger, sharedVolumePath string) *Builder

- 

  - 
            func (builder *Builder) Clean(w http.ResponseWriter, r *http.Request)

  - 
            func (builder *Builder) Handler(w http.ResponseWriter, r *http.Request)

  - 
            func (builder *Builder) VersionHandler(w http.ResponseWriter, r *http.Request)

- 
          type PackageBuildRequest

- 
          type PackageBuildResponse

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Builder ¶
  
    
  

    
    
      

```
type Builder struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func MakeBuilder ¶
  
    
  

    
    
      

```
func MakeBuilder(logger *zap.Logger, sharedVolumePath string) *Builder
```