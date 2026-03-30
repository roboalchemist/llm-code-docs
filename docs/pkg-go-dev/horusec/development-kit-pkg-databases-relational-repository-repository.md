### Index ¶

- 
          type IRepository

- 

  - 
            func NewRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IRepository

- 
          type Mock

- 

  - 
            func (m *Mock) Create(_ *accountEntities.Repository, _ SQL.InterfaceWrite) error

  - 
            func (m *Mock) Delete(_ uuid.UUID) error

  - 
            func (m *Mock) Get(_ uuid.UUID) (*accountEntities.Repository, error)

  - 
            func (m *Mock) GetAccountCompanyRole(_, _ uuid.UUID) (*roles.AccountCompany, error)

  - 
            func (m *Mock) GetAllAccountsInRepository(_ uuid.UUID) (*[]roles.AccountRole, error)

  - 
            func (m *Mock) GetByName(_ uuid.UUID, _ string) (*accountEntities.Repository, error)

  - 
            func (m *Mock) List(_, _ uuid.UUID) (*[]accountEntities.RepositoryResponse, error)

  - 
            func (m *Mock) ListByLdapPermissions(_ uuid.UUID, _ []string) (*[]accountEntities.RepositoryResponse, error)

  - 
            func (m *Mock) Update(_ uuid.UUID, _ *accountEntities.Repository) (*accountEntities.Repository, error)

- 
          type Repository

- 

  - 
            func (r *Repository) Create(repository *accountEntities.Repository, transaction SQL.InterfaceWrite) error

  - 
            func (r *Repository) Delete(repositoryID uuid.UUID) error

  - 
            func (r *Repository) Get(repositoryID uuid.UUID) (*accountEntities.Repository, error)

  - 
            func (r *Repository) GetAccountCompanyRole(accountID, companyID uuid.UUID) (*roles.AccountCompany, error)

  - 
            func (r *Repository) GetAllAccountsInRepository(repositoryID uuid.UUID) (*[]roles.AccountRole, error)

  - 
            func (r *Repository) GetByName(companyID uuid.UUID, name string) (*accountEntities.Repository, error)

  - 
            func (r *Repository) List(accountID, companyID uuid.UUID) (*[]accountEntities.RepositoryResponse, error)

  - 
            func (r *Repository) ListByLdapPermissions(companyID uuid.UUID, permissions []string) (*[]accountEntities.RepositoryResponse, error)

  - 
            func (r *Repository) Update(repositoryID uuid.UUID, repository *accountEntities.Repository) (*accountEntities.Repository, error)

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
	Create(repository *accountEntities.Repository, transaction SQL.InterfaceWrite) error
	Update(repositoryID uuid.UUID, repository *accountEntities.Repository) (*accountEntities.Repository, error)
	Get(repositoryID uuid.UUID) (*accountEntities.Repository, error)
	List(accountID uuid.UUID, companyID uuid.UUID) (*[]accountEntities.RepositoryResponse, error)
	Delete(repositoryID uuid.UUID) error
	GetAllAccountsInRepository(repositoryID uuid.UUID) (*[]roles.AccountRole, error)
	GetByName(companyID uuid.UUID, repositoryName string) (*accountEntities.Repository, error)
	GetAccountCompanyRole(accountID, companyID uuid.UUID) (*roles.AccountCompany, error)
	ListByLdapPermissions(companyID uuid.UUID, permissions []string) (*[]accountEntities.RepositoryResponse, error)
}
```

    
  

    
  
  
    
#### 
      func NewRepository ¶
  
    
  

    
    
      

```
func NewRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IRepository
```