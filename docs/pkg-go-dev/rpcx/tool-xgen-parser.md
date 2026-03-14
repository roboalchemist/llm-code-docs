### Overview ¶

Package parser parses Go code and keeps track of all the types defined
and provides access to all the constants defined for an int type.

    
### Index ¶

- 
          type Parser

- 

  - 
            func (p *Parser) Parse(fname string, isDir bool) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Parser ¶
  
    
  

    
    
      

```
type Parser struct {
	PkgPath     string
	PkgName     string
	PkgFullName string
	StructNames map[string]bool
}
```

    
  

    
  
  
    
#### 
      func (*Parser) Parse ¶
  
    
  

    
    
      

```
func (p *Parser) Parse(fname string, isDir bool) error
```