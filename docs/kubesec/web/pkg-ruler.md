### Index ¶

- 
        func GenerateInTotoLink(reports []Report, fileBytes []byte) in_toto.Metablock

- 
          type InvalidInputError

- 

  - 
            func (e *InvalidInputError) Error() string

- 
          type NotSupportedError

- 

  - 
            func (e *NotSupportedError) Error() string

- 
          type Report

- 
          type Reports

- 
          type Rule

- 

  - 
            func (r *Rule) Eval(json []byte) (int, error)

- 
          type RuleRef

- 
          type RuleRefCustomOrder

- 

  - 
            func (rr RuleRefCustomOrder) Len() int

  - 
            func (rr RuleRefCustomOrder) Less(i, j int) bool

  - 
            func (rr RuleRefCustomOrder) Swap(i, j int)

- 
          type RuleScoring

- 
          type Ruleset

- 

  - 
            func NewRuleset(logger *zap.SugaredLogger) *Ruleset

- 

  - 
            func (rs *Ruleset) Run(fileName string, fileBytes []byte, schemaConfig SchemaConfig) ([]Report, error)

- 
          type SchemaConfig

- 

  - 
            func NewDefaultSchemaConfig() SchemaConfig

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GenerateInTotoLink ¶
  
    
  

    
    
      

```
func GenerateInTotoLink(reports []Report, fileBytes []byte) in_toto.Metablock
```