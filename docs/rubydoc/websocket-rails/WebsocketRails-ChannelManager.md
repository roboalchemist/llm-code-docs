# Class: WebsocketRails::ChannelManager
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::ChannelManager
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/channel_manager.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**channels**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute channels.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**channel_tokens**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ ChannelManager 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ChannelManager.

  

      
        
- 
  
    
      #**unsubscribe**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ChannelManager 
  

  

  

  
    

Returns a new instance of ChannelManager.

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 25

def initialize
  @channels = {}.with_indifferent_access
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**channels**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute channels.

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 23

def channels
  @channels
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(channel)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 39

def [](channel)
  @channels[channel] ||= Channel.new channel
end
```

    
  

    
      
  
### 
  
    #**channel_tokens**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 29

def channel_tokens
  @channel_tokens ||= begin
    if WebsocketRails.synchronize?
      ::Redis::HashKey.new('websocket_rails.channel_tokens', Synchronization.redis)
    else
      {}
    end
  end
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(connection)  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
46
47
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 43

def unsubscribe(connection)
  @channels.each do |channel_name, channel|
    channel.unsubscribe(connection)
  end
end
```