### Index ¶

- 
        func NewTabWriter(w io.Writer) *tabwriter.Writer

- 
        func Print(format string, in interface{}, w io.Writer, fn PrintTable) error

- 
        func SanitizeAddr(addr string) (string, error)

- 
          type PrintTable

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func NewTabWriter ¶
  
    
  

    
    
      

```
func NewTabWriter(w io.Writer) *tabwriter.Writer
```

    
  

NewTabWriter returns a default writer to write tables.

  

        
	  
  
  
    
#### 
      func Print ¶
  
    
  

    
    
      

```
func Print(format string, in interface{}, w io.Writer, fn PrintTable) error
```

    
  

Print prints any object in yaml, json or table format.

  

        
	  
  
  
    
#### 
      func SanitizeAddr ¶
  
    
      added in
      v2.14.0
    
  

    
    
      

```
func SanitizeAddr(addr string) (string, error)
```

    
  

Sanitize and validate HTTP listen address.
It accepts "port", ":port", "ip:port", "[ipv6]:port" as valid addresses
if only "port" is provided, the semi-colon prefix is added

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type PrintTable ¶
  
    
  

    
    
      

```
type PrintTable func(w io.Writer) error
```

    
  

PrintTable defines how to print a table.