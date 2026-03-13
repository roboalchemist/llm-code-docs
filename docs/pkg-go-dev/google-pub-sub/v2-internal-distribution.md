### Index ¶

- 
          type D

- 

  - 
            func New(n int) *D

- 

  - 
            func (d *D) Percentile(p float64) int

  - 
            func (d *D) Record(v int)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type D ¶
  
    
  

    
    
      

```
type D struct {
	// contains filtered or unexported fields
}
```

    
  

D is a distribution. Methods of D can be called concurrently by multiple
goroutines.

    
  
  
    
#### 
      func New ¶
  
    
  

    
    
      

```
func New(n int) *D
```

    
  

New creates a new distribution capable of holding values from 0 to n-1.

  

  
    
  
  
    
#### 
      func (*D) Percentile ¶
  
    
  

    
    
      

```
func (d *D) Percentile(p float64) int
```

    
  

Percentile computes the p-th percentile of the distribution where
p is between 0 and 1. This method may be called by multiple goroutines.

  

  
    
  
  
    
#### 
      func (*D) Record ¶
  
    
  

    
    
      

```
func (d *D) Record(v int)
```

    
  

Record records value v to the distribution.
To help with distributions with long tails, if v is larger than the maximum value,
Record records the maximum value instead.
If v is negative, Record panics.