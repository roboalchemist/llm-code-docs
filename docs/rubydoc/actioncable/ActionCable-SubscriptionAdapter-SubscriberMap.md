# Class: ActionCable::SubscriptionAdapter::SubscriberMap
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::SubscriptionAdapter::SubscriberMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/subscriber_map.rb
  
  

  
## Direct Known Subclasses

  

Async::AsyncSubscriberMap, PostgreSQL::Listener, Redis::Listener

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_channel**(channel, on_success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**add_subscriber**(channel, subscriber, on_success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcast**(channel, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ SubscriberMap 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SubscriberMap.

  

      
        
- 
  
    
      #**invoke_callback**(callback, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_channel**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_subscriber**(channel, subscriber)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ SubscriberMap 
  

  

  

  
    

Returns a new instance of SubscriberMap.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 8

def initialize
  @subscribers = Hash.new { |h, k| h[k] = [] }
  @sync = Mutex.new
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_channel**(channel, on_success)  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 49

def add_channel(channel, on_success)
  on_success.call if on_success
end
```

    
  

    
      
  
### 
  
    #**add_subscriber**(channel, subscriber, on_success)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 13

def add_subscriber(channel, subscriber, on_success)
  @sync.synchronize do
    new_channel = !@subscribers.key?(channel)

    @subscribers[channel] << subscriber

    if new_channel
      add_channel channel, on_success
    elsif on_success
      on_success.call
    end
  end
end
```

    
  

    
      
  
### 
  
    #**broadcast**(channel, message)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 38

def broadcast(channel, message)
  list = @sync.synchronize do
    return if !@subscribers.key?(channel)
    @subscribers[channel].dup
  end

  list.each do |subscriber|
    invoke_callback(subscriber, message)
  end
end
```

    
  

    
      
  
### 
  
    #**invoke_callback**(callback, message)  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 56

def invoke_callback(callback, message)
  callback.call message
end
```

    
  

    
      
  
### 
  
    #**remove_channel**(channel)  ⇒ Object 
  

  

  

  
    
      

```

53
54
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 53

def remove_channel(channel)
end
```

    
  

    
      
  
### 
  
    #**remove_subscriber**(channel, subscriber)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/subscriber_map.rb', line 27

def remove_subscriber(channel, subscriber)
  @sync.synchronize do
    @subscribers[channel].delete(subscriber)

    if @subscribers[channel].empty?
      @subscribers.delete channel
      remove_channel channel
    end
  end
end
```