# Module: ActionCable::Channel::Broadcasting
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/channel/broadcasting.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast_to**(model, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcasting_for**(model)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast_to**(model, message)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/action_cable/channel/broadcasting.rb', line 45

def broadcast_to(model, message)
  self.class.broadcast_to(model, message)
end
```

    
  

    
      
  
### 
  
    #**broadcasting_for**(model)  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/action_cable/channel/broadcasting.rb', line 41

def broadcasting_for(model)
  self.class.broadcasting_for(model)
end
```