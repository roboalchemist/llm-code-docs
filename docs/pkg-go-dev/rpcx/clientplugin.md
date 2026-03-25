### Index ¶

- 
          type RedisRateLimitingPlugin

- 

  - 
            func NewRedisRateLimitingPlugin(addrs []string, rate int, burst int, period time.Duration) *RedisRateLimitingPlugin

- 

  - 
            func (plugin *RedisRateLimitingPlugin) PreCall(ctx context.Context, servicePath, serviceMethod string, args interface{}) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type RedisRateLimitingPlugin ¶
  
    
  

    
    
      

```
type RedisRateLimitingPlugin struct {
	// contains filtered or unexported fields
}
```

    
  

RedisRateLimitingPlugin can limit requests per unit time

    
  
  
    
#### 
      func NewRedisRateLimitingPlugin ¶
  
    
  

    
    
      

```
func NewRedisRateLimitingPlugin(addrs []string, rate int, burst int, period time.Duration) *RedisRateLimitingPlugin
```

    
  

NewRedisRateLimitingPlugin creates a new RateLimitingPlugin

  

  
    
  
  
    
#### 
      func (*RedisRateLimitingPlugin) PreCall ¶
  
    
  

    
    
      

```
func (plugin *RedisRateLimitingPlugin) PreCall(ctx context.Context, servicePath, serviceMethod string, args interface{}) error
```

    
  

PreCall can limit request processing.