### Index ¶

- Constants

- 
          type Config

- 

  - 
            func NewConfig() *Config

### Constants ¶

  
    
      View Source
      

```
const (
	EnvRelationalDialect = "HORUSEC_DATABASE_SQL_DIALECT"
	EnvRelationalURI     = "HORUSEC_DATABASE_SQL_URI"
	EnvRelationalLogMode = "HORUSEC_DATABASE_SQL_LOG_MODE"
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Config ¶
  
    
  

    
    
      

```
type Config struct {
	Dialect string
	URI     string
	LogMode bool
}
```

    
  

    
  
  
    
#### 
      func NewConfig ¶
  
    
  

    
    
      

```
func NewConfig() *Config
```