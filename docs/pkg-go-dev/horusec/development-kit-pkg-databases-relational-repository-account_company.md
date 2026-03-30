### Index ¶

- 
          type AccountCompany

- 

  - 
            func (a *AccountCompany) CreateAccountCompany(companyID, accountID uuid.UUID, role accountEnums.Role, tx SQL.InterfaceWrite) error

  - 
            func (a *AccountCompany) DeleteAccountCompany(accountID, companyID uuid.UUID) error

  - 
            func (a *AccountCompany) GetAccountCompany(accountID, companyID uuid.UUID) (*roles.AccountCompany, error)

  - 
            func (a *AccountCompany) UpdateAccountCompany(accountCompany *roles.AccountCompany) error

- 
          type IAccountCompany

- 

  - 
            func NewAccountCompanyRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IAccountCompany

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type AccountCompany ¶
  
    
  

    
    
      

```
type AccountCompany struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*AccountCompany) CreateAccountCompany ¶
  
    
  

    
    
      

```
func (a *AccountCompany) CreateAccountCompany(companyID, accountID uuid.UUID,
	role accountEnums.Role, tx SQL.InterfaceWrite) error
```