# Class: WebsocketRails::UserManager::RemoteConnection
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::UserManager::RemoteConnection
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/user_manager.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**user**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute user.

  

    
      
- 
  
    
      #**user_identifier**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute user_identifier.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(identifier, user_hash)  ⇒ RemoteConnection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RemoteConnection.

  

      
        
- 
  
    
      #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(identifier, user_hash)  ⇒ RemoteConnection 
  

  

  

  
    

Returns a new instance of RemoteConnection.

  

  

  
    
      

```

195
196
197
198
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 195

def initialize(identifier, user_hash)
  @user_identifier = identifier.to_s
  @user_hash = user_hash
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**user**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute user.

  

  

  
    
      

```

193
194
195
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 193

def user
  @user
end
```

    
  

    
      
      
      
  
### 
  
    #**user_identifier**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute user_identifier.

  

  

  
    
      

```

193
194
195
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 193

def user_identifier
  @user_identifier
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connected?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 200

def connected?
  true
end
```

    
  

    
      
  
### 
  
    #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
  

  

  

  
    
      

```

208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 208

def send_message(event_name, data = {}, options = {})
  options.merge! :user_id => @user_identifier
  options[:data] = data

  event = Event.new(event_name, options)

  # If the user is connected to this worker, trigger the event
  # immediately as the event will be ignored by the Synchronization
  ## dispatcher since the server_token will match.
  if connection = WebsocketRails.users.users[@user_identifier]
    connection.trigger event
  end

  # Still publish the event in case the user is connected to
  # other workers as well.
  #
  # No need to check for Synchronization being enabled here.
  # If a RemoteConnection has been fetched, Synchronization
  # must be enabled.
  Synchronization.publish event
  true
end
```