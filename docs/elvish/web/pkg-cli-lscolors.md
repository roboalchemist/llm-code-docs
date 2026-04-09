### Overview ¶

Package lscolors provides styling of filenames based on file features.

This is a reverse-engineered implementation of the parsing and
interpretation of the LS_COLORS environmental variable used by GNU
coreutils.

### Index ¶

-
        func WithTestLsColors() func()

-
          type Colorist

-

-
            func GetColorist() Colorist

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func WithTestLsColors ¶
  
    
  

    
    
      

```
func WithTestLsColors() func()
```

WithTestLsColors sets LS_COLORS to a value where directories are blue and
.png files are red. It returns a function to restore the old value. This
function is mainly useful in tests.

### Types ¶

####

      type Colorist ¶
  
    
  

    
    
      

```
type Colorist interface {
 // GetStyle returns the style for the named file.
 GetStyle(fname string) string
}
```

Colorist styles filenames based on the features of the file.

####

      func GetColorist ¶
  
    
  

    
    
      

```
func GetColorist() Colorist
```
