### Overview ¶

Package stub implements the stub addon, a general-purpose addon that shows a
modeline and supports pluggable binding.

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

Start starts the stub addon.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Keybinding.
 Binding cli.Handler
 // Name to show in the modeline.
 Name string
 // Whether the addon widget gets the focus.
 Focus bool
}
```

Config keeps the configuration for the stub addon.
