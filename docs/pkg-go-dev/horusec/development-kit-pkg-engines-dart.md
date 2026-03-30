### Index ¶

- 
          type Interface

- 

  - 
            func NewRules() Interface

- 
          type Rules

- 

  - 
            func (r *Rules) GetAllRules() (rules []engine.Rule)

  - 
            func (r *Rules) GetTextUnitByRulesExt(projectPath string) ([]engine.Unit, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Interface ¶
  
    
  

    
    
      

```
type Interface interface {
	GetAllRules() []engine.Rule
	GetTextUnitByRulesExt(projectPath string) ([]engine.Unit, error)
}
```

    
  

    
  
  
    
#### 
      func NewRules ¶
  
    
  

    
    
      

```
func NewRules() Interface
```