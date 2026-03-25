# Module: ActionCable::Connection::Identification
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  
  
    Included in:
    Base, RemoteConnections::RemoteConnection
  
  

  
  
    Defined in:
    lib/action_cable/connection/identification.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connection_identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a single connection identifier that combines the value of all the registered identifiers into a single gid.

  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connection_identifier**  ⇒ Object 
  

  

  

  
    

Return a single connection identifier that combines the value of all the registered identifiers into a single gid.

  

  

  
    
      

```

29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/action_cable/connection/identification.rb', line 29

def connection_identifier
  unless defined? @connection_identifier
    @connection_identifier = connection_gid identifiers.filter_map { |id| instance_variable_get("@#{id}") }
  end

  @connection_identifier
end
```