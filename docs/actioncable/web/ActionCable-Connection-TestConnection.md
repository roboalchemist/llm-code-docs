# Module: ActionCable::Connection::TestConnection
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute logger.

  

    
      
- 
  
    
      #**request**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute request.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(request)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute logger.

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 58

def logger
  @logger
end
```

    
  

    
      
      
      
  
### 
  
    #**request**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute request.

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 58

def request
  @request
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**initialize**(request)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 60

def initialize(request)
  inner_logger = ActiveSupport::Logger.new(StringIO.new)
  tagged_logging = ActiveSupport::TaggedLogging.new(inner_logger)
  @logger = ActionCable::Connection::TaggedLoggerProxy.new(tagged_logging, tags: [])
  @request = request
  @env = request.env
end
```