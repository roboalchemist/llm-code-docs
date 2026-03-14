### Index ¶

- 
          type MethodInfo

- 
          type Reflection

- 

  - 
            func New() *Reflection

- 

  - 
            func (r *Reflection) GetService(ctx context.Context, s string, reply *string) error

  - 
            func (r *Reflection) GetServices(ctx context.Context, s string, reply *string) error

  - 
            func (r *Reflection) Register(name string, rcvr interface{}, metadata string) error

  - 
            func (r *Reflection) Unregister(name string) error

- 
          type ServiceInfo

- 

  - 
            func (si ServiceInfo) String() string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type MethodInfo ¶
  
    
  

    
    
      

```
type MethodInfo struct {
	Name      string
	ReqName   string
	Req       string
	ReplyName string
	Reply     string
}
```

    
  

MethodInfo method info

  

    
      
  
  
    
#### 
      type Reflection ¶
  
    
  

    
    
      

```
type Reflection struct {
	Services map[string]*ServiceInfo
}
```

    
  

    
  
  
    
#### 
      func New ¶
  
    
  

    
    
      

```
func New() *Reflection
```