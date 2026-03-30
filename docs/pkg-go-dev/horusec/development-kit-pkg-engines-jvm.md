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
            func (r *Rules) GetAllRules(rules []engine.Rule) []engine.Rule

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
	GetAllRules(rules []engine.Rule) []engine.Rule
}
```

    
  

    
  
  
    
#### 
      func NewRules ¶
  
    
  

    
    
      

```
func NewRules() Interface
```