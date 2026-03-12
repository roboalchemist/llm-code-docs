### Index ¶

- Constants

- 
          type AuthFeatureConfig

- 
          type CanaryFeatureConfig

- 
          type FeatureConfig

- 

  - 
            func GetFeatureConfig(logger *zap.Logger) (*FeatureConfig, error)

### Constants ¶

  
    
      View Source
      

```
const (
	FeatureConfigFile = "/etc/config/config.yaml"
	CanaryFeature     = "canary"
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type AuthFeatureConfig ¶
  
    
      added in
      v1.16.0
    
  

    
    
      

```
type AuthFeatureConfig struct {
	IsEnabled     bool          `json:"enabled"`
	AuthUriPath   string        `json:"authUriPath"`
	JWTExpiryTime time.Duration `json:"jwtExpiryTime"`
	JWTIssuer     string        `json:"jwtIssuer"`
}
```