### Index ¶

- 
          type Version

- 

  - 
            func NewVersion(v string) (*Version, error)

- 

  - 
            func (v *Version) Set(value string) error

  - 
            func (v *Version) String() string

  - 
            func (v *Version) Type() string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Version ¶
  
    
  

    
    
      

```
type Version struct {
	Prefix      string
	Major       uint
	Minor       uint
	Patch       uint
	Phase       phases.Phase
	PatchNumber uint
}
```

    
  

    
  
  
    
#### 
      func NewVersion ¶
  
    
  

    
    
      

```
func NewVersion(v string) (*Version, error)
```