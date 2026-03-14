### Index ¶

- Constants

- 
        func Commands() *cobra.Command

- 
        func Dump(input cli.Input) error

- 
          type DumpSubCommand

### Constants ¶

  
    
      View Source
      

```
const (
	DUMP_ARCHIVE_PREFIX = "fission-dump"
	DEFAULT_OUTPUT_DIR  = "fission-dump"
)
```

    
  

  
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

    
  

Commands returns support commands

  

        
	  
  
  
    
#### 
      func Dump ¶
  
    
  

    
    
      

```
func Dump(input cli.Input) error
```