# Module: ActionCable::Channel::Naming::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/naming.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**channel_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the name of the channel, underscored, without the `Channel` ending.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**channel_name**  ⇒ Object 
  

  

  

  
    

Returns the name of the channel, underscored, without the `Channel` ending. If the channel is in a namespace, then the namespaces are represented by single colon separators in the channel name.

```
ChatChannel.channel_name # => 'chat'
Chats::AppearancesChannel.channel_name # => 'chats:appearances'
FooChats::BarAppearancesChannel.channel_name # => 'foo_chats:bar_appearances'

```

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/action_cable/channel/naming.rb', line 18

def channel_name
  @channel_name ||= name.delete_suffix("Channel").gsub("::", ":").underscore
end
```