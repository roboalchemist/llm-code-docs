### Index ¶

- 
          type IRepository

- 

  - 
            func NewTokenRepository(databaseRead relational.InterfaceRead, databaseWrite relational.InterfaceWrite) IRepository

- 
          type Repository

- 

  - 
            func (t *Repository) Create(token *api.Token) (*api.Token, error)

  - 
            func (t *Repository) Delete(tokenID uuid.UUID) error

  - 
            func (t *Repository) GetAllOfCompany(companyID uuid.UUID) (*[]api.Token, error)

  - 
            func (t *Repository) GetAllOfRepository(repositoryID uuid.UUID) (*[]api.Token, error)

  - 
            func (t *Repository) GetByValue(value string) (*api.Token, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type IRepository ¶
  
    
  

    
    
      

```
type IRepository interface {
	Create(token *api.Token) (*api.Token, error)
	Delete(tokenID uuid.UUID) error
	GetByValue(value string) (*api.Token, error)
	GetAllOfRepository(repositoryID uuid.UUID) (*[]api.Token, error)
	GetAllOfCompany(CompanyID uuid.UUID) (*[]api.Token, error)
}
```

    
  

    
  
  
    
#### 
      func NewTokenRepository ¶
  
    
  

    
    
      

```
func NewTokenRepository(databaseRead relational.InterfaceRead, databaseWrite relational.InterfaceWrite) IRepository
```