### Index ¶

- 
          type Cache

- 

  - 
            func (c *Cache) Del(key string) error

  - 
            func (c *Cache) Exists(key string) bool

  - 
            func (c *Cache) Get(key string) (*cache.Cache, error)

  - 
            func (c *Cache) Set(entity *cache.Cache, expiration time.Duration) error

- 
          type Interface

- 

  - 
            func NewCacheRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) Interface

- 
          type Mock

- 

  - 
            func (m *Mock) Del(_ string) error

  - 
            func (m *Mock) Exists(_ string) bool

  - 
            func (m *Mock) Get(_ string) (*cache.Cache, error)

  - 
            func (m *Mock) Set(_ *cache.Cache, _ time.Duration) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Cache ¶
  
    
  

    
    
      

```
type Cache struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*Cache) Del ¶
  
    
  

    
    
      

```
func (c *Cache) Del(key string) error
```