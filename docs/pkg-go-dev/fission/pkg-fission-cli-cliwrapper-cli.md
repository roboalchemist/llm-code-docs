### Index ¶

- 
          type Input

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type Input ¶
  
    
  

    
    
      

```
type Input interface {
	Context() context.Context

	// IsSet checks whether a flag has been set by the user
	IsSet(key string) bool

	// Bool returns true if given flag has been set;
	// otherwise, return false.
	Bool(key string) bool

	// String returns string value of given flag.
	String(key string) string

	// StringSlice returns string slice of given flag.
	StringSlice(key string) []string

	// Int returns int value of given flag.
	Int(key string) int

	// IntSlice returns int slice of given flag.
	IntSlice(key string) []int

	// Int64 returns int64 value of given flag.
	Int64(key string) int64

	// Int64Slice returns int64 slice of given flag.
	Int64Slice(key string) []int64

	// GlobalBool returns true if given global flag has been set;
	// otherwise, return false.
	GlobalBool(key string) bool

	// GlobalString returns global string value of given flag.
	GlobalString(key string) string

	// GlobalStringSlice returns global string slice of given flag.
	GlobalStringSlice(key string) []string

	// GlobalInt returns global int value of given flag.
	GlobalInt(key string) int

	// GlobalIntSlice returns global int slice of given flag.
	GlobalIntSlice(key string) []int

	// GlobalInt64 returns global int64 value of given flag.
	GlobalInt64(key string) int64

	// GlobalInt64Slice returns global int64 slice of given flag.
	GlobalInt64Slice(key string) []int64

	// Duration returns time duration of given flag.
	Duration(key string) time.Duration

	// Stdout returns io.Writer for stdout.
	Stdout() io.Writer

	// Stderr returns io.Writer for stderr.
	Stderr() io.Writer
}
```