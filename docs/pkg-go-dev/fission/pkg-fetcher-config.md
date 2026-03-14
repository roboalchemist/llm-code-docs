### Index ¶

- 
          type Config

- 

  - 
            func MakeFetcherConfig(sharedMountPath string) (*Config, error)

- 

  - 
            func (cfg *Config) AddFetcherToPodSpec(podSpec *apiv1.PodSpec, mainContainerName string) error

  - 
            func (cfg *Config) AddSpecializingFetcherToPodSpec(podSpec *apiv1.PodSpec, mainContainerName string, fn *fv1.Function, ...) error

  - 
            func (cfg *Config) NewSpecializeRequest(fn *fv1.Function, env *fv1.Environment) fetcher.FunctionSpecializeRequest

  - 
            func (cfg *Config) SharedMountPath() string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Config ¶
  
    
  

    
    
      

```
type Config struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func MakeFetcherConfig ¶
  
    
  

    
    
      

```
func MakeFetcherConfig(sharedMountPath string) (*Config, error)
```