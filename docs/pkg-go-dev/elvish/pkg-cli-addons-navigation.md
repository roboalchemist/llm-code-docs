### Overview ¶

Package navigation provides the functionality of navigating the filesystem.

### Index ¶

-
        func Ascend(app cli.App)

-
        func Descend(app cli.App)

-
        func MutateFiltering(app cli.App, f func(bool) bool)

-
        func MutateShowHidden(app cli.App, f func(bool) bool)

-
        func ScrollPreview(app cli.App, delta int)

-
        func Select(app cli.App, f func(cli.ListBoxState) int)

-
        func SelectedName(app cli.App) string

-
        func Start(app cli.App, cfg Config)

-
          type Config

-
          type Cursor

-

-
            func NewOSCursor() Cursor

-
          type File

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Ascend ¶
  
    
  

    
    
      

```
func Ascend(app cli.App)
```

Ascend ascends in the navigation addon if it is active.

####

      func Descend ¶
  
    
  

    
    
      

```
func Descend(app cli.App)
```

Descend descends in the navigation addon if it is active.

####

      func MutateFiltering ¶
  
    
  

    
    
      

```
func MutateFiltering(app cli.App, f func(bool) bool)
```

MutateFiltering changes the filtering status of the navigation addon if it is
active.

####

      func MutateShowHidden ¶
  
    
  

    
    
      

```
func MutateShowHidden(app cli.App, f func(bool) bool)
```

MutateShowHidden changes whether the navigation addon should show file
whose names start with ".".

####

      func ScrollPreview ¶
  
    
  

    
    
      

```
func ScrollPreview(app cli.App, delta int)
```

ScrollPreview scrolls the preview if the navigation addon is currently
active.

####

      func Select ¶
  
    
  

    
    
      

```
func Select(app cli.App, f func(cli.ListBoxState) int)
```

Select changes the selection if the navigation addon is currently active.

####

      func SelectedName ¶
  
    
  

    
    
      

```
func SelectedName(app cli.App) string
```

SelectedName returns the currently selected name in the navigation addon. It
returns an empty string if the navigation addon is not active, or if there is
no selected name.

####

      func Start ¶
  
    
  

    
    
      

```
func Start(app cli.App, cfg Config)
```

Start starts the navigation function.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // Key binding.
 Binding cli.Handler
 // Underlying filesystem.
 Cursor Cursor
 // A function that returns the relative weights of the widths of the 3
 // columns. If unspecified, the ratio is 1:3:4.
 WidthRatio func() [3]int
}
```

Config contains the configuration needed for the navigation functionality.

####

      type Cursor ¶
  
    
  

    
    
      

```
type Cursor interface {
 // Current returns a File that represents the current directory.
 Current() (File, error)
 // Parent returns a File that represents the parent directory. It may return
 // nil if the current directory is the root of the filesystem.
 Parent() (File, error)
 // Ascend navigates to the parent directory.
 Ascend() error
 // Descend navigates to the named child directory.
 Descend(name string) error
}
```

Cursor represents a cursor for navigating in a potentially virtual filesystem.

####

      func NewOSCursor ¶
  
    
  

    
    
      

```
func NewOSCursor() Cursor
```

NewOSCursor returns a Cursor backed by the OS.
