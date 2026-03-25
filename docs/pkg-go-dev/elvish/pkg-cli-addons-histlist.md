### Overview ¶

Package histlist implements the history listing addon.

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

Start starts history listing.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Binding provides key binding.
 Binding cli.Handler
 // Store provides the source of all commands.
 Store Store
 // Dedup is called to determine whether deduplication should be done.
 // Defaults to true if unset.
 Dedup func() bool
 // CaseSensitive is called to determine whether the filter should be
 // case-sensitive. Defaults to true if unset.
 CaseSensitive func() bool
}
```

Config contains configurations to start history listing.

####

      type Store ¶
  
    
  

    
    
      

```
type Store interface {
 AllCmds() ([]store.Cmd, error)
}
```

Store wraps the AllCmds method. It is a subset of histutil.Store.
