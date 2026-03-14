# Class: Resque::VeryVerboseFormatter
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::VeryVerboseFormatter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/log_formatters/very_verbose_formatter.rb
  
  

  
    
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
6
```

    
    
      

```
# File 'lib/resque/log_formatters/very_verbose_formatter.rb', line 3

def call(serverity, datetime, progname, msg)
  time = Time.now.strftime('%H:%M:%S %Y-%m-%d')
  "** [#{time}] #$$: #{msg}\n"
end
```