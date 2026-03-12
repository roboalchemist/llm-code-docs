### Index ¶

- Constants

- 
          type Cache

- 

  - 
            func MakeCache[K comparable, V any](ctimeExpiry, atimeExpiry time.Duration) *Cache[K, V]

- 

  - 
            func (c *Cache[K, V]) Copy() map[K]V

  - 
            func (c *Cache[K, V]) Delete(key K) error

  - 
            func (c *Cache[K, V]) Get(key K) (V, error)

  - 
            func (c *Cache[K, V]) IsOld(v *Value[V]) bool

  - 
            func (c *Cache[K, V]) Set(key K, value V) (V, error)

- 
          type Value

### Constants ¶

  
    
      View Source
      

```
const (
	GET requestType = iota
	SET
	DELETE
	EXPIRE
	COPY
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Cache ¶
  
    
  

    
    
      

```
type Cache[K comparable, V any] struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func MakeCache ¶
  
    
  

    
    
      

```
func MakeCache[K comparable, V any](ctimeExpiry, atimeExpiry time.Duration) *Cache[K, V]
```