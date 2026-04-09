# Class: WebsocketRails::UserManager::LocalConnection
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::UserManager::LocalConnection
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/user_manager.rb
  
  

## Overview

  
    

The UserManager::LocalConnection Class serves as a proxy object for storing multiple connections that belong to the same user. It implements the same basic interface as a Connection. This allows you to work with the object as though it is a single connection, but still trigger the events on all active connections belonging to the user.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**connections**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute connections.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**connected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**delete**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ LocalConnection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LocalConnection.

  

      
        
- 
  
    
      #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ LocalConnection 
  

  

  

  
    

Returns a new instance of LocalConnection.

  

  

  
    
      

```

136
137
138
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 136

def initialize
  @connections = []
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**connections**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute connections.

  

  

  
    
      

```

134
135
136
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 134

def connections
  @connections
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(connection)  ⇒ Object 
  

  

  

  
    
      

```

140
141
142
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 140

def <<(connection)
  @connections << connection
end
```

    
  

    
      
  
### 
  
    #**connected?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

148
149
150
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 148

def connected?
  true
end
```

    
  

    
      
  
### 
  
    #**delete**(connection)  ⇒ Object 
  

  

  

  
    
      

```

144
145
146
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 144

def delete(connection)
  @connections.delete(connection)
end
```

    
  

    
      
  
### 
  
    #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
  

  

  

  
    
      

```

166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 166

def send_message(event_name, data = {}, options = {})
  options.merge! :user_id => user_identifier
  options[:data] = data

  event = Event.new(event_name, options)

  # Trigger the event on all active connections for this user.
  connections.each do |connection|
    connection.trigger event
  end

  # Still publish the event in case the user is connected to
  # other workers as well.
  Synchronization.publish event if WebsocketRails.synchronize?
  true
end
```

    
  

    
      
  
### 
  
    #**trigger**(event)  ⇒ Object 
  

  

  

  
    
      

```

160
161
162
163
164
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 160

def trigger(event)
  connections.each do |connection|
    connection.trigger event
  end
end
```

    
  

    
      
  
### 
  
    #**user**  ⇒ Object 
  

  

  

  
    
      

```

156
157
158
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 156

def user
  latest_connection.user
end
```

    
  

    
      
  
### 
  
    #**user_identifier**  ⇒ Object 
  

  

  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 152

def user_identifier
  latest_connection.user_identifier
end
```