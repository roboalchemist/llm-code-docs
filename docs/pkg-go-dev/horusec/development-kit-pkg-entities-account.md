### Index ¶

- 
          type Company

- 

  - 
            func (c *Company) GetAuthzAdmin() []string

  - 
            func (c *Company) GetAuthzMember() []string

  - 
            func (c *Company) GetAuthzSupervisor() []string

  - 
            func (c *Company) GetTable() string

  - 
            func (c *Company) MapToUpdate() map[string]interface{}

  - 
            func (c *Company) SetCreateData() *Company

  - 
            func (c *Company) SetUpdateData() *Company

  - 
            func (c *Company) ToBytes() []byte

  - 
            func (c *Company) ToCompanyResponse(role rolesEnum.Role) *CompanyResponse

  - 
            func (c *Company) Validate() error

- 
          type CompanyApplicationAdmin

- 

  - 
            func (c *CompanyApplicationAdmin) ToCompany() *Company

  - 
            func (c *CompanyApplicationAdmin) Validate() error

- 
          type CompanyResponse

- 
          type Repository

- 

  - 
            func (r *Repository) GetAuthzAdmin() []string

  - 
            func (r *Repository) GetAuthzMember() []string

  - 
            func (r *Repository) GetAuthzSupervisor() []string

  - 
            func (r *Repository) GetTable() string

  - 
            func (r *Repository) SetCreateData(companyID uuid.UUID) *Repository

  - 
            func (r *Repository) SetUpdateData(name, description string, authzAdmin, authzMember, authzSupervisor []string) *Repository

  - 
            func (r *Repository) ToAccountRepository(role accountEnum.Role, accountID uuid.UUID) *roles.AccountRepository

  - 
            func (r *Repository) ToRepositoryResponse(role accountEnum.Role) *RepositoryResponse

  - 
            func (r *Repository) Validate() error

- 
          type RepositoryResponse

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Company ¶
  
    
  

    
    
      

```
type Company struct {
	CompanyID   uuid.UUID      `json:"companyID" gorm:"primary_key" swaggerignore:"true"`
	Name        string         `json:"name"`
	Description string         `json:"description"`
	AuthzMember pq.StringArray `json:"authzMember" gorm:"type:text[]"`
	AuthzAdmin  pq.StringArray `json:"authzAdmin" gorm:"type:text[]"`
	CreatedAt   time.Time      `json:"createdAt" swaggerignore:"true"`
	UpdatedAt   time.Time      `json:"updatedAt" swaggerignore:"true"`
}
```

    
  

    
  
  
    
#### 
      func (*Company) GetAuthzAdmin ¶
  
    
      added in
      v1.2.0
    
  

    
    
      

```
func (c *Company) GetAuthzAdmin() []string
```