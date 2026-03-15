### Index ¶

- 
          type ICompanyRepository

- 

  - 
            func NewCompanyRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) ICompanyRepository

- 
          type Mock

- 

  - 
            func (m *Mock) Create(_ *accountEntities.Company, _ SQL.InterfaceWrite) (*accountEntities.Company, error)

  - 
            func (m *Mock) Delete(_ uuid.UUID) error

  - 
            func (m *Mock) GetAllAccountsInCompany(_ uuid.UUID) (*[]roles.AccountRole, error)

  - 
            func (m *Mock) GetAllOfAccount(_ uuid.UUID) (*[]accountEntities.CompanyResponse, error)

  - 
            func (m *Mock) GetByID(_ uuid.UUID) (*accountEntities.Company, error)

  - 
            func (m *Mock) ListByLdapPermissions(_ []string) (*[]accountEntities.CompanyResponse, error)

  - 
            func (m *Mock) Update(_ uuid.UUID, _ *accountEntities.Company) (*accountEntities.Company, error)

- 
          type Repository

- 

  - 
            func (r *Repository) Create(company *accountEntities.Company, tx SQL.InterfaceWrite) (*accountEntities.Company, error)

  - 
            func (r *Repository) Delete(companyID uuid.UUID) error

  - 
            func (r *Repository) GetAllAccountsInCompany(companyID uuid.UUID) (*[]roles.AccountRole, error)

  - 
            func (r *Repository) GetAllOfAccount(accountID uuid.UUID) (*[]accountEntities.CompanyResponse, error)

  - 
            func (r *Repository) GetByID(companyID uuid.UUID) (*accountEntities.Company, error)

  - 
            func (r *Repository) ListByLdapPermissions(permissions []string) (*[]accountEntities.CompanyResponse, error)

  - 
            func (r *Repository) Update(companyID uuid.UUID, data *accountEntities.Company) (*accountEntities.Company, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ICompanyRepository ¶
  
    
  

    
    
      

```
type ICompanyRepository interface {
	Create(company *accountEntities.Company, tx SQL.InterfaceWrite) (*accountEntities.Company, error)
	Update(companyID uuid.UUID, data *accountEntities.Company) (*accountEntities.Company, error)
	GetByID(companyID uuid.UUID) (*accountEntities.Company, error)
	GetAllOfAccount(accountID uuid.UUID) (*[]accountEntities.CompanyResponse, error)
	Delete(companyID uuid.UUID) error
	GetAllAccountsInCompany(companyID uuid.UUID) (*[]roles.AccountRole, error)
	ListByLdapPermissions(permissions []string) (*[]accountEntities.CompanyResponse, error)
}
```

    
  

    
  
  
    
#### 
      func NewCompanyRepository ¶
  
    
  

    
    
      

```
func NewCompanyRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) ICompanyRepository
```