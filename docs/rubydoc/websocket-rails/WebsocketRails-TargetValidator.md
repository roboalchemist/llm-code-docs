# Class: WebsocketRails::TargetValidator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::TargetValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event_map.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**validate_target**(target)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parses the target and extracts controller/action pair or raises an error if target is invalid.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**validate_target**(target)  ⇒ Object 
  

  

  

  
    

Parses the target and extracts controller/action pair or raises an error if target is invalid

  

  

  
    
      

```

148
149
150
151
152
153
154
155
156
157
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 148

def self.validate_target(target)
  case target
    when Hash
      validate_hash_target target
    when String
      validate_string_target target
  else
    raise('Must specify the event target either as a string product#new_product or as a Hash to: ProductController, with_method: :new_product')
  end
end
```