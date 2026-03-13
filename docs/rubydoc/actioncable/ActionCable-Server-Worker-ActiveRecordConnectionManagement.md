# Module: ActionCable::Server::Worker::ActiveRecordConnectionManagement
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  

  
  
    Included in:
    ActionCable::Server::Worker
  
  

  
  
    Defined in:
    lib/action_cable/server/worker/active_record_connection_management.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**with_database_connections**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**with_database_connections**(&block)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/server/worker/active_record_connection_management.rb', line 17

def with_database_connections(&block)
  connection.logger.tag(ActiveRecord::Base.logger, &block)
end
```