### Overview ¶

Package vars contains basic types for manipulating Elvish variables.

### Index ¶

- Variables

-
        func DelElement(variable Var, indices []interface{}) error

-
        func ElementErrorLevel(err error) int

-
        func IsBlackhole(v Var) bool

-
          type PtrVar

-

-
            func FromPtr(p interface{}) PtrVar

-
            func FromPtrWithMutex(p interface{}, m *sync.RWMutex) PtrVar

-

-
            func (v PtrVar) Get() interface{}

-
            func (v PtrVar) GetRaw() interface{}

-
            func (v PtrVar) Set(val interface{}) error

-
          type Var

-

-
            func FromEnv(name string) Var

-
            func FromGet(get func() interface{}) Var

-
            func FromInit(v interface{}) Var

-
            func FromSetGet(set func(interface{}) error, get func() interface{}) Var

-
            func HeadOfElement(v Var) Var

-
            func MakeElement(v Var, indices []interface{}) (Var, error)

-
            func NewBlackhole() Var

-
            func NewEnvListVar(name string) Var

-
            func NewReadOnly(v interface{}) Var

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var (
 ErrPathMustBeString           = errors.New("path must be string")
 ErrPathCannotContainColonZero = errors.New(`path cannot contain colon or \0`)
)
```

Errors

      View Source
      

```
var ErrSetReadOnlyVar = errors.New("read-only variable; cannot be set")
```

ErrSetReadOnlyVar is returned by the Set method of a read-only variable.

### Functions ¶

####

      func DelElement ¶
  
    
  

    
    
      

```
func DelElement(variable Var, indices []interface{}) error
```

DelElement deletes an element. It uses a similar process to MakeElement,
except that the last level of container needs to be Dissoc-able instead of
Assoc-able.

####

      func ElementErrorLevel ¶
  
    
  

    
    
      

```
func ElementErrorLevel(err error) int
```

ElementErrorLevel returns the level of an error returned by MakeElement or
DelElement. Level 0 represents that the error is about the variable itself.
If the argument was not returned from MakeVariable, -1 is returned.

####

      func IsBlackhole ¶
  
    
  

    
    
      

```
func IsBlackhole(v Var) bool
```

IsBlackhole returns whether the variable is a blackhole variable.

### Types ¶

####

      type PtrVar ¶
  
    
  

    
    
      

```
type PtrVar struct {
 // contains filtered or unexported fields
}
```

####

      func FromPtr ¶
  
    
  

    
    
      

```
func FromPtr(p interface{}) PtrVar
```

FromPtr creates a variable from a pointer. The variable is kept in sync with
the value the pointer points to, converting with vals.ScanToGo and
vals.FromGo when Get and Set. Its access is guarded by a new mutex.

####

      func FromPtrWithMutex ¶
  
    
  

    
    
      

```
func FromPtrWithMutex(p interface{}, m *sync.RWMutex) PtrVar
```

FromPtrWithMutex creates a variable from a pointer. The variable is kept in
sync with the value the pointer points to, converting with vals.ScanToGo and
vals.FromGo when Get and Set. Its access is guarded by the supplied mutex.

####

      func (PtrVar) Get ¶
  
    
  

    
    
      

```
func (v PtrVar) Get() interface{}
```

Get returns the value pointed by the pointer, after conversion using FromGo.

####

      func (PtrVar) GetRaw ¶
  
    
  

    
    
      

```
func (v PtrVar) GetRaw() interface{}
```

GetRaw returns the value pointed by the pointer without any conversion.

####

      func (PtrVar) Set ¶
  
    
  

    
    
      

```
func (v PtrVar) Set(val interface{}) error
```

Set sets the value pointed by the pointer, after conversion using ScanToGo.
