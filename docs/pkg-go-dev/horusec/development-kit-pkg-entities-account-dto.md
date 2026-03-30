### Index ¶

- 
          type ClaimsJWT

- 

  - 
            func (c *ClaimsJWT) Valid() error

- 
          type InviteUser

- 

  - 
            func (i *InviteUser) SetInviteUserCompanyID(companyID uuid.UUID) *InviteUser

  - 
            func (i *InviteUser) SetInviteUserRepositoryAndCompanyID(companyID, repositoryID uuid.UUID) *InviteUser

  - 
            func (i *InviteUser) ToAccountRepository(accountID uuid.UUID) *roles.AccountRepository

  - 
            func (i *InviteUser) ToBytes() []byte

  - 
            func (i *InviteUser) Validate() error

- 
          type RemoveUser

- 

  - 
            func (r *RemoveUser) SetAccountAndCompanyID(accountID, companyID uuid.UUID) *RemoveUser

  - 
            func (r *RemoveUser) SetAccountAndRepositoryID(accountID, repositoryID uuid.UUID) *RemoveUser

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ClaimsJWT ¶
  
    
  

    
    
      

```
type ClaimsJWT struct {
	Email       string   `json:"email"`
	Username    string   `json:"username"`
	Permissions []string `json:"permissions"`
	jwt.StandardClaims
}
```

    
  

    
  
  
    
#### 
      func (*ClaimsJWT) Valid ¶
  
    
  

    
    
      

```
func (c *ClaimsJWT) Valid() error
```