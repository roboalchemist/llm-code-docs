# Class: ActionCable::SubscriptionAdapter::PostgreSQL
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- ActionCable::SubscriptionAdapter::PostgreSQL
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ChannelPrefix
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/postgresql.rb
  
  

## Overview

  
    

:nodoc:

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Listener
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#logger, #server

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ PostgreSQL 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PostgreSQL.

  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(channel, callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**with_broadcast_connection**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**with_subscriptions_connection**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#identifier

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ PostgreSQL 
  

  

  

  
    

Returns a new instance of PostgreSQL.

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 14

def initialize(*)
  super
  @listener = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
23
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 19

def broadcast(channel, payload)
  with_broadcast_connection do |pg_conn|
    pg_conn.exec("NOTIFY #{pg_conn.escape_identifier(channel_identifier(channel))}, '#{pg_conn.escape_string(payload)}'")
  end
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 33

def shutdown
  listener.shutdown
end
```

    
  

    
      
  
### 
  
    #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 25

def subscribe(channel, callback, success_callback = nil)
  listener.add_subscriber(channel_identifier(channel), callback, success_callback)
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(channel, callback)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 29

def unsubscribe(channel, callback)
  listener.remove_subscriber(channel_identifier(channel), callback)
end
```

    
  

    
      
  
### 
  
    #**with_broadcast_connection**(&block)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 51

def with_broadcast_connection(&block) # :nodoc:
  ActiveRecord::Base.connection_pool.with_connection do |ar_conn|
    pg_conn = ar_conn.raw_connection
    verify!(pg_conn)
    yield pg_conn
  end
end
```

    
  

    
      
  
### 
  
    #**with_subscriptions_connection**(&block)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
46
47
48
49
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 37

def with_subscriptions_connection(&block) # :nodoc:
  # Action Cable is taking ownership over this database connection, and will
  # perform the necessary cleanup tasks.
  # We purposedly avoid #checkout to not end up with a pinned connection
  ar_conn = ActiveRecord::Base.connection_pool.new_connection
  pg_conn = ar_conn.raw_connection

  verify!(pg_conn)
  pg_conn.exec("SET application_name = #{pg_conn.escape_identifier(identifier)}")
  yield pg_conn
ensure
  ar_conn&.disconnect!
end
```