### Overview ¶

Package lastcmd implements an addon that supports inserting the last command
or words from it.

### Index ¶

-
        func Start(app cli.App, cfg Config)

-
          type Config

-
          type Store

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Start ¶
  
    
  

    
    
      

```
func Start(app cli.App, cfg Config)
```

Start starts lastcmd function.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Binding provides key binding.
 Binding cli.Handler
 // Store provides the source for the last command.
 Store Store
 // Wordifier breaks a command into words.
 Wordifier func(string) []string
}
```

Config is the configuration for starting lastcmd.

####

      type Store ¶
  
    
  

    
    
      

```
type Store interface {
 Cursor(prefix string) histutil.Cursor
}
```

Store wraps the LastCmd method. It is a subset of histutil.Store.
