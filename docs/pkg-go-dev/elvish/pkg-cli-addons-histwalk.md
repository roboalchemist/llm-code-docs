### Overview ¶

Package histwalk implements the history walking addon.

### Index ¶

- Variables

-
        func Accept(app cli.App)

-
        func Close(app cli.App)

-
        func Next(app cli.App) error

-
        func Prev(app cli.App) error

-
        func Start(app cli.App, cfg Config)

-
          type Config

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var ErrHistWalkInactive = errors.New("the histwalk addon is not active")
```

### Functions ¶

####

      func Accept ¶
  
    
  

    
    
      

```
func Accept(app cli.App)
```

Accept closes the histwalk addon, accepting the current shown command. It does
nothing if the histwalk addon is not active.

####

      func Close ¶
  
    
  

    
    
      

```
func Close(app cli.App)
```

Close closes the histwalk addon. It does nothing if the histwalk addon is not
active.

####

      func Next ¶
  
    
  

    
    
      

```
func Next(app cli.App) error
```

Next walks to the next entry in history. It returns ErrHistWalkInactive if
the histwalk addon is not active, and histutil.ErrEndOfHistory if it would go
over the end.

####

      func Prev ¶
  
    
  

    
    
      

```
func Prev(app cli.App) error
```

Prev walks to the previous entry in history. It returns ErrHistWalkInactive
if the histwalk addon is not active, and histutil.ErrEndOfHistory if it would
go over the end.

####

      func Start ¶
  
    
  

    
    
      

```
func Start(app cli.App, cfg Config)
```

Start starts the histwalk addon.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Keybinding.
 Binding cli.Handler
 // History store to walk.
 Store histutil.Store
 // Only walk through items with this prefix.
 Prefix string
}
```

Config keeps the configuration for the histwalk addon.
