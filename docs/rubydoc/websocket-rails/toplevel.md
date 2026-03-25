# Top Level Namespace
  
  
  

  

  
  
  
  
  

  

  

## Defined Under Namespace

  
    
      **Modules:** WebsocketRails
    
  
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**create_event**(name, data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**create_event**(name, data)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 32

def create_event(name, data)
  WebsocketRails::SpecHelperEvent.new(name, {data: data})
end
```