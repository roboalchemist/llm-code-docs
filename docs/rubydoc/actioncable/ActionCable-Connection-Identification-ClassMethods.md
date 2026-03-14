# Module: ActionCable::Connection::Identification::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/identification.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**identified_by**(*identifiers)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Mark a key as being a connection identifier index that can then be used to find the specific connection again later.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**identified_by**(*identifiers)  ⇒ Object 
  

  

  

  
    

Mark a key as being a connection identifier index that can then be used to find the specific connection again later. Common identifiers are current_user and current_account, but could be anything, really.

Note that anything marked as an identifier will automatically create a delegate by the same name on any channel instances created off the connection.

  

  

  
    
      

```

21
22
23
24
```

    
    
      

```
# File 'lib/action_cable/connection/identification.rb', line 21

def identified_by(*identifiers)
  Array(identifiers).each { |identifier| attr_accessor identifier }
  self.identifiers += identifiers
end
```