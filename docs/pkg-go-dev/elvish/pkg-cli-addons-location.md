### Overview ¶

Package location implements an addon that supports viewing location history
and changing to a selected directory.

### Index ¶

-
        func Start(app cli.App, cfg Config)

-
          type Config

-
          type Store

-
          type WorkspaceIterator

-

-
            func (ws WorkspaceIterator) Parse(path string) (kind, root string)

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

Start starts the directory history feature.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Binding is the key binding.
 Binding cli.Handler
 // Store provides the directory history and the function to change directory.
 Store Store
 // IteratePinned specifies pinned directories by calling the given function
 // with all pinned directories.
 IteratePinned func(func(string))
 // IterateHidden specifies hidden directories by calling the given function
 // with all hidden directories.
 IterateHidden func(func(string))
 // IterateWorksapce specifies workspace configuration.
 IterateWorkspaces WorkspaceIterator
}
```

Config is the configuration to start the location history feature.

####

      type Store ¶
  
    
  

    
    
      

```
type Store interface {
 Dirs(blacklist map[string]struct{}) ([]store.Dir, error)
 Chdir(dir string) error
 Getwd() (string, error)
}
```

Store defines the interface for interacting with the directory history.

####

      type WorkspaceIterator ¶
  
    
  

    
    
      

```
type WorkspaceIterator func(func(kind, pattern string) bool)
```

WorkspaceIterator is a function that iterates all workspaces by calling
the passed function with the name and pattern of each kind of workspace.
Iteration should stop when the called function returns false.

####

      func (WorkspaceIterator) Parse ¶
  
    
  

    
    
      

```
func (ws WorkspaceIterator) Parse(path string) (kind, root string)
```

Parse returns whether the path matches any kind of workspace. If there is
a match, it returns the kind of the workspace and the root. It there is no
match, it returns "", "".
