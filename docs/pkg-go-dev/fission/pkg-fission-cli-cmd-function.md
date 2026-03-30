### Index ¶

- Constants

- 
        func Commands() *cobra.Command

- 
        func Create(input cli.Input) error

- 
        func Delete(input cli.Input) error

- 
        func Get(input cli.Input) error

- 
        func GetMeta(input cli.Input) error

- 
        func List(input cli.Input) error

- 
        func ListPods(input cli.Input) error

- 
        func Log(input cli.Input) error

- 
        func RunContainer(input cli.Input) error

- 
        func Test(input cli.Input) error

- 
        func Update(input cli.Input) error

- 
        func UpdateContainer(input cli.Input) error

- 
          type CreateSubCommand

- 
          type DeleteSubCommand

- 
          type GetMetaSubCommand

- 
          type GetSubCommand

- 
          type ListPodsSubCommand

- 
          type ListSubCommand

- 
          type LogSubCommand

- 
          type RunContainerSubCommand

- 
          type TestSubCommand

- 
          type UpdateContainerSubCommand

- 
          type UpdateSubCommand

### Constants ¶

  
    
      View Source
      

```
const (
	DEFAULT_MIN_SCALE   = 1
	DEFAULT_CONCURRENCY = 500
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Commands ¶
  
    
  

    
    
      

```
func Commands() *cobra.Command
```