### Overview ¶

Package errs declares error types used as exception causes.

### Index ¶

-
          type ArityMismatch

-

-
            func (e ArityMismatch) Error() string

-
          type BadValue

-

-
            func (e BadValue) Error() string

-
          type OutOfRange

-

-
            func (e OutOfRange) Error() string

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

This section is empty.

### Types ¶

####

      type ArityMismatch ¶
  
    
  

    
    
      

```
type ArityMismatch struct {
 What      string
 ValidLow  int
 ValidHigh int
 Actual    int
}
```

ArityMismatch encodes an error where the expected number of values is out of
the valid range.

####

      func (ArityMismatch) Error ¶
  
    
  

    
    
      

```
func (e ArityMismatch) Error() string
```
