# Class: ActionCable::Connection::Subscriptions
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::Subscriptions
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/subscriptions.rb
  
  

## Overview

  
    

# Action Cable Connection Subscriptions

Collection class for all the channel subscriptions established on a given connection. Responsible for routing incoming commands that arrive on the connection to the proper channel.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**execute_command**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**identifiers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(connection)  ⇒ Subscriptions 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**perform_action**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_subscription**(subscription)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe_from_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection)  ⇒ Subscriptions 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

15
16
17
18
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 15

def initialize(connection)
  @connection = connection
  @subscriptions = {}
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add**(data)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
36
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
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 33

def add(data)
  id_key = data["identifier"]
  id_options = ActiveSupport::JSON.decode(id_key).with_indifferent_access

  return if subscriptions.key?(id_key)

  subscription_klass = id_options[:channel].safe_constantize

  if subscription_klass && ActionCable::Channel::Base > subscription_klass
    subscription = subscription_klass.new(connection, id_key, id_options)
    subscriptions[id_key] = subscription
    subscription.subscribe_to_channel
  else
    logger.error "Subscription class not found: #{id_options[:channel].inspect}"
  end
end
```

    
  

    
      
  
### 
  
    #**execute_command**(data)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
25
26
27
28
29
30
31
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 20

def execute_command(data)
  case data["command"]
  when "subscribe"   then add data
  when "unsubscribe" then remove data
  when "message"     then perform_action data
  else
    logger.error "Received unrecognized command in #{data.inspect}"
  end
rescue Exception => e
  @connection.rescue_with_handler(e)
  logger.error "Could not execute command from (#{data.inspect}) [#{e.class} - #{e.message}]: #{e.backtrace.first(5).join(" | ")}"
end
```

    
  

    
      
  
### 
  
    #**identifiers**  ⇒ Object 
  

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 64

def identifiers
  subscriptions.keys
end
```

    
  

    
      
  
### 
  
    #**perform_action**(data)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 60

def perform_action(data)
  find(data).perform_action ActiveSupport::JSON.decode(data["data"])
end
```

    
  

    
      
  
### 
  
    #**remove**(data)  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
53
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 50

def remove(data)
  logger.info "Unsubscribing from channel: #{data['identifier']}"
  remove_subscription find(data)
end
```

    
  

    
      
  
### 
  
    #**remove_subscription**(subscription)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 55

def remove_subscription(subscription)
  subscription.unsubscribe_from_channel
  subscriptions.delete(subscription.identifier)
end
```

    
  

    
      
  
### 
  
    #**unsubscribe_from_all**  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/action_cable/connection/subscriptions.rb', line 68

def unsubscribe_from_all
  subscriptions.each { |id, channel| remove_subscription(channel) }
end
```