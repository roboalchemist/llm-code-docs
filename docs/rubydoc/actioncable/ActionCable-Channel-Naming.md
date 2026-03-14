# Module: ActionCable::Channel::Naming
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/channel/naming.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**channel_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**channel_name**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/action_cable/channel/naming.rb', line 23

def channel_name
  self.class.channel_name
end
```