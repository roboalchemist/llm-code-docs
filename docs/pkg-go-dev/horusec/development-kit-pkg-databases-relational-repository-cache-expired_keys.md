### Index ¶

- 
          type ExpiredKeys

- 

  - 
            func (e *ExpiredKeys) RemoveKeysExpiredFromDatabase()

- 
          type Interface

- 

  - 
            func NewExpiredKeys(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) Interface

- 
          type Mock

- 

  - 
            func (m *Mock) RemoveKeysExpiredFromDatabase()

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ExpiredKeys ¶
  
    
  

    
    
      

```
type ExpiredKeys struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*ExpiredKeys) RemoveKeysExpiredFromDatabase ¶
  
    
  

    
    
      

```
func (e *ExpiredKeys) RemoveKeysExpiredFromDatabase()
```