# Exception: WebsocketRails::ConfigDeprecationError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- WebsocketRails::ConfigDeprecationError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

87
88
89
90
91
92
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 87

def to_s
  out = "Deprecation Error:\n\n\t"
  out << "config/initializers/events.rb has been moved to config/events.rb\n\t"
  out << "Make sure events.rb is in the proper location and the old one has been removed.\n\t"
  out << "More information can be found in the wiki.\n\n"
end
```