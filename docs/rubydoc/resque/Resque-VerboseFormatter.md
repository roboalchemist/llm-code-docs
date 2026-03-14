# Class: Resque::VerboseFormatter
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::VerboseFormatter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/log_formatters/verbose_formatter.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(serverity, datetime, progname, msg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(serverity, datetime, progname, msg)  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/resque/log_formatters/verbose_formatter.rb', line 3

def call(serverity, datetime, progname, msg)
  "*** #{msg}\n"
end

```