### Index ¶

- 
        func Parse(cmd *cobra.Command, args []string) wCli.Input

- 
        func SetFlags(cmd *cobra.Command, flagSet flag.FlagSet)

- 
        func Wrapper(action cmd.CommandAction) func(*cobra.Command, []string) error

- 
        func WrapperChain(actions ...cmd.CommandAction) func(*cobra.Command, []string) error

- 
          type Cli

- 

  - 
            func (u Cli) Bool(key string) bool

  - 
            func (u Cli) Context() context.Context

  - 
            func (u Cli) Duration(key string) time.Duration

  - 
            func (u Cli) GlobalBool(key string) bool

  - 
            func (u Cli) GlobalInt(key string) int

  - 
            func (u Cli) GlobalInt64(key string) int64

  - 
            func (u Cli) GlobalInt64Slice(key string) []int64

  - 
            func (u Cli) GlobalIntSlice(key string) []int

  - 
            func (u Cli) GlobalString(key string) string

  - 
            func (u Cli) GlobalStringSlice(key string) []string

  - 
            func (u Cli) Int(key string) int

  - 
            func (u Cli) Int64(key string) int64

  - 
            func (u Cli) Int64Slice(key string) []int64

  - 
            func (u Cli) IntSlice(key string) []int

  - 
            func (u Cli) IsSet(key string) bool

  - 
            func (u Cli) Stderr() io.Writer

  - 
            func (u Cli) Stdout() io.Writer

  - 
            func (u Cli) String(key string) string

  - 
            func (u Cli) StringSlice(key string) []string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Parse ¶
  
    
  

    
    
      

```
func Parse(cmd *cobra.Command, args []string) wCli.Input
```

    
  

Parse is only for converting urfave *cli.Context to Input and will be removed in future.

  

        
	  
  
  
    
#### 
      func SetFlags ¶
  
    
  

    
    
      

```
func SetFlags(cmd *cobra.Command, flagSet flag.FlagSet)
```