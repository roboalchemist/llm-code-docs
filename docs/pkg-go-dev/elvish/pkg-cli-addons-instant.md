### Overview ¶

Package instant implements an addon that executes code whenever it changes
and shows the result.

### Index ¶

-
        func Start(app cli.App, cfg Config)

-
          type Config

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

Start starts the addon.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Keybinding.
 Binding cli.Handler
 // The function to execute code and returns the output.
 Execute func(code string) ([]string, error)
}
```

Config keeps the configuration for the instant addon.
