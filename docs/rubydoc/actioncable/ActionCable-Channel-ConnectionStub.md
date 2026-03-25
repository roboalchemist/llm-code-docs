# Class: ActionCable::Channel::ConnectionStub
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Channel::ConnectionStub
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**identifiers**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute identifiers.

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute logger.

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute server.

  

    
      
- 
  
    
      #**subscriptions**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute subscriptions.

  

    
      
- 
  
    
      #**transmissions**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute transmissions.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connection_identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(identifiers = {})  ⇒ ConnectionStub 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ConnectionStub.

  

      
        
- 
  
    
      #**transmit**(cable_message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(identifiers = {})  ⇒ ConnectionStub 
  

  

  

  
    

Returns a new instance of ConnectionStub.

  

  

  
    
      

```

55
56
57
58
59
60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 55

def initialize(identifiers = {})
  @server = ActionCable.server
  @transmissions = []

  identifiers.each do |identifier, val|
    define_singleton_method(identifier) { val }
  end

  @subscriptions = ActionCable::Connection::Subscriptions.new(self)
  @identifiers = identifiers.keys
  @logger = ActiveSupport::TaggedLogging.new ActiveSupport::Logger.new(StringIO.new)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**identifiers**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute identifiers.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 51

def identifiers
  @identifiers
end
```

    
  

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute logger.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 51

def logger
  @logger
end
```

    
  

    
      
      
      
  
### 
  
    #**server**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute server.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 51

def server
  @server
end
```

    
  

    
      
      
      
  
### 
  
    #**subscriptions**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute subscriptions.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 51

def subscriptions
  @subscriptions
end
```

    
  

    
      
      
      
  
### 
  
    #**transmissions**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute transmissions.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 51

def transmissions
  @transmissions
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connection_identifier**  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 72

def connection_identifier
  @connection_identifier ||= connection_gid(identifiers.filter_map { |id| send(id.to_sym) if id })
end
```

    
  

    
      
  
### 
  
    #**transmit**(cable_message)  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 68

def transmit(cable_message)
  transmissions << cable_message.with_indifferent_access
end
```