# Class: ActionCable::Connection::TaggedLoggerProxy
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::TaggedLoggerProxy
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/tagged_logger_proxy.rb
  
  

## Overview

  
    

# Action Cable Connection TaggedLoggerProxy

Allows the use of per-connection tags against the server logger. This wouldn’t work using the traditional ActiveSupport::TaggedLogging enhanced Rails.logger, as that logger will reset the tags between requests. The connection is long-lived, so it needs its own set of tags for its independent duration.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**tags**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute tags.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_tags**(*tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(logger, tags:)  ⇒ TaggedLoggerProxy 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of TaggedLoggerProxy.

  

      
        
- 
  
    
      #**tag**(logger, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(logger, tags:)  ⇒ TaggedLoggerProxy 
  

  

  

  
    

Returns a new instance of TaggedLoggerProxy.

  

  

  
    
      

```

16
17
18
19
```

    
    
      

```
# File 'lib/action_cable/connection/tagged_logger_proxy.rb', line 16

def initialize(logger, tags:)
  @logger = logger
  @tags = tags.flatten
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**tags**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute tags.

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/action_cable/connection/tagged_logger_proxy.rb', line 14

def tags
  @tags
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_tags**(*tags)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
```

    
    
      

```
# File 'lib/action_cable/connection/tagged_logger_proxy.rb', line 21

def add_tags(*tags)
  @tags += tags.flatten
  @tags = @tags.uniq
end
```

    
  

    
      
  
### 
  
    #**tag**(logger, &block)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/action_cable/connection/tagged_logger_proxy.rb', line 26

def tag(logger, &block)
  if logger.respond_to?(:tagged)
    current_tags = tags - logger.formatter.current_tags
    logger.tagged(*current_tags, &block)
  else
    yield
  end
end
```