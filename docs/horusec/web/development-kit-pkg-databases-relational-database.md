### Index ¶

- Variables

- 
        func NewRelationalRead(dialect, uri string, logMode bool) relational.InterfaceRead

- 
        func NewRelationalWrite(dialect, uri string, logMode bool) relational.InterfaceWrite

- 
          type Relational

- 

  - 
            func (r *Relational) CommitTransaction() *response.Response

  - 
            func (r *Relational) Connect(dialect, uri string, logMode bool) *response.Response

  - 
            func (r *Relational) Create(entity interface{}, tableName string) *response.Response

  - 
            func (r *Relational) CreateOrUpdate(entity interface{}, conditions map[string]interface{}, tableName string) *response.Response

  - 
            func (r *Relational) Delete(conditions map[string]interface{}, tableName string) *response.Response

  - 
            func (r *Relational) DeleteByQuery(query *gorm.DB, tableName string) *response.Response

  - 
            func (r *Relational) Find(entity interface{}, query *gorm.DB, tableName string) *response.Response

  - 
            func (r *Relational) First(out interface{}, tableName string, where ...interface{}) *response.Response

  - 
            func (r *Relational) GetConnection() *gorm.DB

  - 
            func (r *Relational) IsAvailable() bool

  - 
            func (r *Relational) RawSQL(sql string, entity interface{}) *response.Response

  - 
            func (r *Relational) RollbackTransaction() *response.Response

  - 
            func (r *Relational) SetFilter(filter map[string]interface{}) *gorm.DB

  - 
            func (r *Relational) SetLogMode(logMode bool)

  - 
            func (r *Relational) StartTransaction() relational.InterfaceWrite

  - 
            func (r *Relational) Update(entity interface{}, conditions map[string]interface{}, tableName string) *response.Response

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var (
	ErrDialectNotFound = errors.New("error on create connection with database dialect not found")
)
```

    
  

  
### Functions ¶

  
	  
  
  
    
#### 
      func NewRelationalRead ¶
  
    
  

    
    
      

```
func NewRelationalRead(dialect, uri string, logMode bool) relational.InterfaceRead
```