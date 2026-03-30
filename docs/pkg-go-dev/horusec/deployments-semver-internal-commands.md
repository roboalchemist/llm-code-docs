### Index ¶

- 
          type GetCommand

- 

  - 
            func (g *GetCommand) Cmd() *cobra.Command

  - 
            func (g *GetCommand) Execute(cmd *cobra.Command, args []string) error

  - 
            func (g *GetCommand) Handle(version *entities.Version, phase string) error

  - 
            func (g *GetCommand) Init()

- 
          type GetCommandI

- 

  - 
            func NewGetCommand() GetCommandI

- 
          type InitCommand

- 

  - 
            func (i *InitCommand) Cmd() *cobra.Command

  - 
            func (i *InitCommand) Execute(cmd *cobra.Command, args []string) error

  - 
            func (i *InitCommand) Handle() error

  - 
            func (i *InitCommand) Init()

- 
          type InitCommandI

- 

  - 
            func NewInitCommand() InitCommandI

- 
          type UpVersionCommand

- 

  - 
            func (u *UpVersionCommand) Cmd() *cobra.Command

  - 
            func (u *UpVersionCommand) Execute(cmd *cobra.Command, args []string) error

  - 
            func (u *UpVersionCommand) Handle(release *entities.Version, phase string) error

  - 
            func (u *UpVersionCommand) Init()

- 
          type UpVersionCommandI

- 

  - 
            func NewUpVersionCommand() UpVersionCommandI

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type GetCommand ¶
  
    
  

    
    
      

```
type GetCommand struct {
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func (*GetCommand) Cmd ¶
  
    
  

    
    
      

```
func (g *GetCommand) Cmd() *cobra.Command
```