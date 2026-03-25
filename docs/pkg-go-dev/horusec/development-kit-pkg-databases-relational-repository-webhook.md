### Index ¶

- 
          type IWebhook

- 

  - 
            func NewWebhookRepository(databaseRead relational.InterfaceRead, databaseWrite relational.InterfaceWrite) IWebhook

- 
          type Mock

- 

  - 
            func (m *Mock) Create(_ *webhook.Webhook) error

  - 
            func (m *Mock) GetAllByCompanyID(_ uuid.UUID) (*[]webhook.ResponseWebhook, error)

  - 
            func (m *Mock) GetByRepositoryID(_ uuid.UUID) (*webhook.Webhook, error)

  - 
            func (m *Mock) GetByWebhookID(_ uuid.UUID) (*webhook.Webhook, error)

  - 
            func (m *Mock) Remove(_ uuid.UUID) error

  - 
            func (m *Mock) Update(_ *webhook.Webhook) error

- 
          type Webhook

- 

  - 
            func (w *Webhook) Create(wh *webhook.Webhook) error

  - 
            func (w *Webhook) GetAllByCompanyID(companyID uuid.UUID) (*[]webhook.ResponseWebhook, error)

  - 
            func (w *Webhook) GetByRepositoryID(repositoryID uuid.UUID) (*webhook.Webhook, error)

  - 
            func (w *Webhook) GetByWebhookID(webhookID uuid.UUID) (*webhook.Webhook, error)

  - 
            func (w *Webhook) Remove(webhookID uuid.UUID) error

  - 
            func (w *Webhook) Update(wh *webhook.Webhook) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type IWebhook ¶
  
    
  

    
    
      

```
type IWebhook interface {
	GetByRepositoryID(repositoryID uuid.UUID) (*webhook.Webhook, error)
	GetByWebhookID(webhookID uuid.UUID) (*webhook.Webhook, error)
	GetAllByCompanyID(companyID uuid.UUID) (*[]webhook.ResponseWebhook, error)
	Create(wh *webhook.Webhook) error
	Update(wh *webhook.Webhook) error
	Remove(webhookID uuid.UUID) error
}
```

    
  

    
  
  
    
#### 
      func NewWebhookRepository ¶
  
    
  

    
    
      

```
func NewWebhookRepository(databaseRead relational.InterfaceRead, databaseWrite relational.InterfaceWrite) IWebhook
```