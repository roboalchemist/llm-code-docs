### Overview ¶

Do not edit mock_Plugin_Closer.go directly as your changes will be
overwritten. Instead, edit mock_Plugin_Closer.go.src and re-run
"go generate ./" in the root SDK package.

Package sdk contains the low-level interfaces and API for creating Sentinel
plugins. A Sentinel plugin can provide data dynamically to Sentinel policies.

For plugin authors, the subfolder "framework" contains a high-level
framework for easily implementing plugins in Go.

    
### Index ¶

- Variables

- 
          type GetKey

- 

  - 
            func (g *GetKey) Call() bool

- 
          type GetReq

- 

  - 
            func (g *GetReq) GetKeys() []string

- 
          type GetResult

- 
          type GetResultList

- 

  - 
            func (r GetResultList) KeyId(id uint64) *GetResult

- 
          type MockPlugin

- 

  - 
            func NewMockPlugin(t mockConstructorTestingTNewMockPlugin) *MockPlugin

- 

  - 
            func (_m *MockPlugin) Configure(_a0 map[string]interface{}) error

  - 
            func (_m *MockPlugin) Get(reqs []*GetReq) ([]*GetResult, error)

- 
          type MockPluginCloser

- 

  - 
            func (_m *MockPluginCloser) Close() error

- 
          type Plugin

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var (
	// Undefined is a constant value that represents the undefined object in
	// Sentinel. By making this the return value, it'll be converted to
	// Undefined.
	Undefined = &undefined{}

	// Null is a constant value that represents the null object in Sentinel.
	// By making this a return value, it will convert to null.
	Null = &null{}
)
```

    
  

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type GetKey ¶
  
    
  

    
    
      

```
type GetKey struct {
	// The key for this part of the request.
	Key string

	// The list of arguments for a call expression. This is "nil" if
	// this key is not a call. This may be length zero (but non-nil) if
	// this is a call with no arguments.
	Args []interface{}
}
```

    
  

GetKey is an individual key in the larger possible selector of the
specific plugin call, along with any supplied arguments for the
specific key.

    
  
  
    
#### 
      func (*GetKey) Call ¶
  
    
  

    
    
      

```
func (g *GetKey) Call() bool
```

    
  

Call returns true if this request is a call expression.