### Index ¶

- 
          type Computer

- 
          type ComputersLanguages

- 
          type CreditCard

- 
          type Language

- 
          type Pet

- 
          type Test

- 

  - 
            func (t *Test) TableName() string

  - 
            func (t *Test) ToBytes() []byte

- 
          type User

- 
          type Zoo

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Computer ¶
  
    
  

    
    
      

```
type Computer struct {
	ID                 uuid.UUID `gorm:"type:uuid;primary_key;"`
	Name               string
	ComputersLanguages []ComputersLanguages `gorm:"foreignKey:ComputerID;references:ID"`
}
```