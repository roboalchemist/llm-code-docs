### Index ¶

- 
        func Commands() *cobra.Command

- 
        func Create(input cli.Input) error

- 
        func Delete(input cli.Input) error

- 
        func Get(input cli.Input) error

- 
        func GetIngressConfig(annotations []string, rule string, tls string, fallbackRelativeURL string, ...) (*fv1.IngressConfig, error)

- 
        func GetMethod(method string) (string, error)

- 
        func List(input cli.Input) error

- 
        func Update(input cli.Input) error

- 
          type CreateSubCommand

- 
          type DeleteSubCommand

- 
          type GetSubCommand

- 
          type ListSubCommand

- 
          type UpdateSubCommand

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Commands ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func Commands() *cobra.Command
```