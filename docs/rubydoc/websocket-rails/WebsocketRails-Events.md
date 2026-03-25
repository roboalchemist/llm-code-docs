# Class: WebsocketRails::Events
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Events
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**describe_events**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**describe_events**(&block)  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 105

def self.describe_events(&block)
  raise "This method has been deprecated. Please use WebsocketRails::EventMap.describe instead."
end
```