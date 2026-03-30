# Module: ActionCable::Channel::Broadcasting::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/broadcasting.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast_to**(broadcastables, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Broadcast a hash to a unique broadcasting for this array of `broadcastables` in this channel.

  

      
        
- 
  
    
      #**broadcasting_for**(broadcastables)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a unique broadcasting identifier for this `model` in this channel:.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast_to**(broadcastables, message)  ⇒ Object 
  

  

  

  
    

Broadcast a hash to a unique broadcasting for this array of `broadcastables` in this channel.

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/action_cable/channel/broadcasting.rb', line 14

def broadcast_to(broadcastables, message)
  ActionCable.server.broadcast(broadcasting_for(broadcastables), message)
end
```

    
  

    
      
  
### 
  
    #**broadcasting_for**(broadcastables)  ⇒ Object 
  

  

  

  
    

Returns a unique broadcasting identifier for this `model` in this channel:

```
CommentsChannel.broadcasting_for("all") # => "comments:all"

```

You can pass an array of objects as a target (e.g. Active Record model), and it would be serialized into a string under the hood.

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/action_cable/channel/broadcasting.rb', line 24

def broadcasting_for(broadcastables)
  serialize_broadcasting([ channel_name ] + Array(broadcastables))
end
```