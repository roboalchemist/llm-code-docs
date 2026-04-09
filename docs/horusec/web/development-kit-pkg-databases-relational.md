### Index ¶

- 
          type InterfaceRead

- 
          type InterfaceWrite

- 
          type MockRead

- 

  - 
            func (m *MockRead) Connect(_, _ string, _ bool) *response.Response

  - 
            func (m *MockRead) Find(entity interface{}, _ *gorm.DB, _ string) *response.Response

  - 
            func (m *MockRead) First(_ interface{}, _ string, _ ...interface{}) *response.Response

  - 
            func (m *MockRead) GetConnection() *gorm.DB

  - 
            func (m *MockRead) IsAvailable() bool

  - 
            func (m *MockRead) RawSQL(_ string, entity interface{}) *response.Response

  - 
            func (m *MockRead) SetFilter(_ map[string]interface{}) *gorm.DB

  - 
            func (m *MockRead) SetLogMode(_ bool)

- 
          type MockWrite

- 

  - 
            func (m *MockWrite) CommitTransaction() *response.Response

  - 
            func (m *MockWrite) Connect(_, _ string, _ bool) *response.Response

  - 
            func (m *MockWrite) Create(_ interface{}, _ string) *response.Response

  - 
            func (m *MockWrite) CreateOrUpdate(_ interface{}, _ map[string]interface{}, _ string) *response.Response

  - 
            func (m *MockWrite) Delete(_ map[string]interface{}, _ string) *response.Response

  - 
            func (m *MockWrite) DeleteByQuery(query *gorm.DB, tableName string) *response.Response

  - 
            func (m *MockWrite) GetConnection() *gorm.DB

  - 
            func (m *MockWrite) IsAvailable() bool

  - 
            func (m *MockWrite) RollbackTransaction() *response.Response

  - 
            func (m *MockWrite) SetLogMode(logMode bool)

  - 
            func (m *MockWrite) StartTransaction() InterfaceWrite

  - 
            func (m *MockWrite) Update(_ interface{}, _ map[string]interface{}, _ string) *response.Response

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type InterfaceRead ¶
  
    
  

    
    
      

```
type InterfaceRead interface {
	Connect(dialect, uri string, logMode bool) *response.Response
	GetConnection() *gorm.DB
	IsAvailable() bool
	SetLogMode(logMode bool)
	Find(entity interface{}, query *gorm.DB, tableName string) *response.Response
	SetFilter(filter map[string]interface{}) *gorm.DB
	First(out interface{}, tableName string, where ...interface{}) *response.Response
	RawSQL(sql string, entity interface{}) *response.Response
}
```