### Index ¶

- 
          type AccountRepository

- 

  - 
            func (a *AccountRepository) Create(accountRepository *roles.AccountRepository, transaction SQL.InterfaceWrite) error

  - 
            func (a *AccountRepository) DeleteAccountRepository(accountID, repositoryID uuid.UUID) error

  - 
            func (a *AccountRepository) DeleteFromAllRepositories(accountID, companyID uuid.UUID) error

  - 
            func (a *AccountRepository) GetAccountRepository(accountID, repositoryID uuid.UUID) (*roles.AccountRepository, error)

  - 
            func (a *AccountRepository) GetOfAccount(accountID uuid.UUID) (accountRepository []roles.AccountRepository, err error)

  - 
            func (a *AccountRepository) UpdateAccountRepository(accountRepository *roles.AccountRepository) error

- 
          type IAccountRepository

- 

  - 
            func NewAccountRepositoryRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IAccountRepository

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type AccountRepository ¶
  
    
  

    
    
      

```
type AccountRepository struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*AccountRepository) Create ¶
  
    
  

    
    
      

```
func (a *AccountRepository) Create(accountRepository *roles.AccountRepository, transaction SQL.InterfaceWrite) error
```