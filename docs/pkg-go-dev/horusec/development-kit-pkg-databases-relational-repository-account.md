### Index ¶

- 
          type Account

- 

  - 
            func (a *Account) Create(account *authEntities.Account) error

  - 
            func (a *Account) DeleteAccount(accountID uuid.UUID) error

  - 
            func (a *Account) GetByAccountID(accountID uuid.UUID) (*authEntities.Account, error)

  - 
            func (a *Account) GetByEmail(email string) (*authEntities.Account, error)

  - 
            func (a *Account) GetByUsername(username string) (*authEntities.Account, error)

  - 
            func (a *Account) Update(account *authEntities.Account) error

  - 
            func (a *Account) UpdatePassword(account *authEntities.Account) error

- 
          type IAccount

- 

  - 
            func NewAccountRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IAccount

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Account ¶
  
    
  

    
    
      

```
type Account struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*Account) Create ¶
  
    
  

    
    
      

```
func (a *Account) Create(account *authEntities.Account) error
```