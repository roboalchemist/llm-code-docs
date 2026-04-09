### Index ¶

- 
          type AnalysisData

- 

  - 
            func (a *AnalysisData) ToBytes() []byte

- 
          type Token

- 

  - 
            func (t *Token) GetID() uuid.UUID

  - 
            func (t *Token) GetKey() uuid.UUID

  - 
            func (t *Token) GetTable() string

  - 
            func (t *Token) Map() map[string]interface{}

  - 
            func (t *Token) SetCreateData() *Token

  - 
            func (t *Token) SetExpiresAtTimeDefault() *Token

  - 
            func (t *Token) SetKey(value uuid.UUID) *Token

  - 
            func (t *Token) TableName() string

  - 
            func (t *Token) ToBytes() []byte

  - 
            func (t *Token) ToString() string

  - 
            func (t *Token) Validate(isRequiredRepositoryID bool) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type AnalysisData ¶
  
    
  

    
    
      

```
type AnalysisData struct {
	Analysis       *horusec.Analysis `json:"analysis"`
	RepositoryName string            `json:"repositoryName"`
}
```

    
  

    
  
  
    
#### 
      func (*AnalysisData) ToBytes ¶
  
    
  

    
    
      

```
func (a *AnalysisData) ToBytes() []byte
```