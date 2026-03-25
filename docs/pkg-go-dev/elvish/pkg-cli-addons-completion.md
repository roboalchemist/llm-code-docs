### Overview ¶

Package completion implements the UI for showing, filtering and inserting
completion candidates.

### Index ¶

-
        func Close(app cli.App)

-
        func Start(app cli.App, cfg Config)

-
          type Config

-
          type Item

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Close ¶
  
    
  

    
    
      

```
func Close(app cli.App)
```

Close closes the completion UI.

####

      func Start ¶
  
    
  

    
    
      

```
func Start(app cli.App, cfg Config)
```

Start starts the completion UI.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 Binding cli.Handler
 Name    string
 Replace diag.Ranging
 Items   []Item
}
```

Config keeps the configuration for the completion UI.

####

      type Item ¶
  
    
  

    
    
      

```
type Item struct {
 // Used in the UI and for filtering.
 ToShow string
 // Style to use in the UI.
 ShowStyle ui.Style
 // Used when inserting a candidate.
 ToInsert string
}
```

Item represents a completion item, also known as a candidate.
