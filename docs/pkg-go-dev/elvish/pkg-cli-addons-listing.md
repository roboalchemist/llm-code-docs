### Overview ¶

Package listing provides the custom listing addon.

### Index ¶

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

      func Start ¶
  
    
  

    
    
      

```
func Start(app cli.App, cfg Config)
```

Start starts the custom listing addon.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Keybinding.
 Binding cli.Handler
 // Caption of the listing. If empty, defaults to " LISTING ".
 Caption string
 // A function that takes the query string and returns a list of Item's and
 // the index of the Item to select. Required.
 GetItems func(query string) (items []Item, selected int)
 // A function to call when the user has accepted the selected item. If the
 // return value is true, the listing will not be closed after accpeting.
 // If unspecified, the Accept function default to a function that does
 // nothing other than returning false.
 Accept func(string) bool
 // Whether to automatically accept when there is only one item.
 AutoAccept bool
}
```

Config is the configuration to start the custom listing addon.

####

      type Item ¶
  
    
  

    
    
      

```
type Item struct {
 // Passed to the Accept callback in Config.
 ToAccept string
 // How the item is shown.
 ToShow ui.Text
}
```

Item is an item to show in the listing.
