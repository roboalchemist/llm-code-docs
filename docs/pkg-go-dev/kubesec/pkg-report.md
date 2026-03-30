### Index ¶

- Variables

- 
        func PrettyJSON(jsonBytes []byte) ([]byte, error)

- 
        func WriteReports(format string, output io.Writer, reports reports, outputTemplate string) error

- 
          type JSONWriter

- 

  - 
            func (jw JSONWriter) Write(reports reports) error

- 
          type TemplateWriter

- 

  - 
            func NewTemplateWriter(output io.Writer, outputTemplate string) (*TemplateWriter, error)

- 

  - 
            func (tw TemplateWriter) Write(reports reports) error

- 
          type Writer

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var Now = time.Now
```

    
  

Now returns the current time

  
### Functions ¶

  
	  
  
  
    
#### 
      func PrettyJSON ¶
  
    
  

    
    
      

```
func PrettyJSON(jsonBytes []byte) ([]byte, error)
```

    
  

PrettyJSON will indent JSON to be pretty

  

        
	  
  
  
    
#### 
      func WriteReports ¶
  
    
  

    
    
      

```
func WriteReports(format string, output io.Writer, reports reports, outputTemplate string) error
```

    
  

WriteReports writes the result to output, format as passed in argument

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type JSONWriter ¶
  
    
  

    
    
      

```
type JSONWriter struct {
	Output io.Writer
}
```

    
  

JSONWriter implements result Writer

    
  
  
    
#### 
      func (JSONWriter) Write ¶
  
    
  

    
    
      

```
func (jw JSONWriter) Write(reports reports) error
```

    
  

Write writes the reports in JSON format